# frida.py

import re
from pathlib import Path
from typing import Optional, Dict, Tuple, List
import xml.etree.ElementTree as ET

from ..exceptions import FridaPatchError, NetworkError, ValidationError
from ..utils.core import run_command as runcommand, get_apk_patchx_home as getapkpatchxhome, download_file as downloadfile
from ..utils.versions import get_latest_github_release as getlatestgithubrelease

from .apktool import ApktoolService
from .signing import SigningService
from .patch_smali import SmaliPatcher
from .patch_dex import DexPatcher
from ..utils import manifest as manifest_utils  # uses ManifestUtils

class FridaService:
    """
    Service for Frida gadget operations with robust manifest parsing.
    - Prefers Application class if defined.
    - Falls back to resolved MAIN/LAUNCHER activity (handles activity-alias).
    - Resolves class names relative to manifest package.
    - Searches all smali and smali_classesN for exact class.
    """
    ARCH_MAPPING = {
        "arm": ["armeabi-v7a", "android-arm"],
        "arm64": ["arm64-v8a", "android-arm64"],
        "x86": ["x86", "android-x86"],
        "x86_64": ["x86_64", "android-x86_64"],
    }

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.apktool_service = ApktoolService(verbose=verbose)
        self.signing_service = SigningService(verbose=verbose)
        self.dex_patcher = DexPatcher(verbose=verbose)

    def patch_apk(
        self,
        apk_path: Path,
        arch: str,
        gadget_config: Optional[Path] = None,
        add_network_config: bool = False,
        no_sources: bool = False,
        only_main_classes: bool = False,
        frida_version: Optional[str] = None,
        decode_args: Optional[str] = None,
        build_args: Optional[str] = None,
        prefer_application: bool = True,
        prefer_dex_patch: bool = False,
    ) -> Path:
        if arch not in self.ARCH_MAPPING:
            raise ValidationError(f"Unsupported arch '{arch}'. Supported: {list(self.ARCH_MAPPING)}")

        # Decode APK
        workdir = self.apktool_service.decode(
            apk_path=apk_path,
            no_sources=no_sources,
            decode_args=decode_args or "",
        )

        manifest_path = workdir / "AndroidManifest.xml"
        if not manifest_path.exists():
            raise FridaPatchError("Decoded manifest not found after apktool decode")

        # Manifest edits
        try:
            manifest_utils.ManifestUtils.add_internet_permission(manifest_path)
            manifest_utils.ManifestUtils.set_extract_native_libs(manifest_path, True)
            if add_network_config:
                manifest_utils.ManifestUtils.ensure_network_security_config(manifest_path, workdir)
        except Exception as e:
            raise FridaPatchError(f"Failed manifest edits: {e}")

        # Determine target class
        package_name = self._get_manifest_package(manifest_path)
        app_class = self._get_application_class(manifest_path, package_name)
        main_activity = self._get_main_activity(manifest_path, package_name)

        target_class = None
        if prefer_application and app_class:
            target_class = app_class
        elif main_activity:
            target_class = main_activity
        elif app_class:
            target_class = app_class

        if not target_class:
            raise FridaPatchError("Unable to resolve Application or MAIN/LAUNCHER activity from manifest")

        # Copy gadget .so and optional config
        abi_dir = self._ensure_gadget(workdir, arch, frida_version, gadget_config)

        # Inject loadLibrary into target class
        if prefer_dex_patch:
            # Try dex-level patch first; fallback to smali
            patched = self._try_dex_injection(workdir, target_class)
            if not patched:
                self._inject_smali(workdir, target_class)
        else:
            # Smali first; fallback to dex
            success = self._inject_smali(workdir, target_class)
            if not success:
                if not self._try_dex_injection(workdir, target_class):
                    raise FridaPatchError("Failed to patch either smali or dex for target class")

        # Build and sign
        built_apk = self.apktool_service.build(workdir, build_args=build_args or "")
        signed_apk = self.signing_service.sign_apk(built_apk)
        return signed_apk

    # ---------------------------
    # Gadget retrieval and copy
    # ---------------------------

    def _ensure_gadget(self, workdir: Path, arch: str, frida_version: Optional[str], gadget_config: Optional[Path]) -> Path:
        libs_dir = workdir / "lib"
        libs_dir.mkdir(parents=True, exist_ok=True)

        abi_variants = self.ARCH_MAPPING[arch]
        # Put gadget in all present ABI folders to maximize compatibility
        present_abis = self._discover_present_abis(workdir)
        target_abis: List[str] = [abi for abi in abi_variants if abi in present_abis] or [abi_variants[0]]

        gadget_name = "libfrida-gadget.so"
        config_name_candidates = ["frida-gadget.config", "libfrida-gadget.config.so"]

        # Download gadget
        gadget_path = self._download_frida_gadget(arch, frida_version)

        for abi in set(target_abis):
            abi_dir = libs_dir / abi
            abi_dir.mkdir(parents=True, exist_ok=True)
            (abi_dir / gadget_name).write_bytes(gadget_path.read_bytes())

            if gadget_config and gadget_config.exists():
                # Write both common config names for compatibility
                (abi_dir / "frida-gadget.config").write_bytes(gadget_config.read_bytes())
                (abi_dir / "libfrida-gadget.config.so").write_bytes(gadget_config.read_bytes())

        return libs_dir

    def _download_frida_gadget(self, arch: str, frida_version: Optional[str]) -> Path:
        tools_dir = getapkpatchxhome() / "tools"
        tools_dir.mkdir(parents=True, exist_ok=True)

        # Resolve frida version
        if frida_version:
            version = frida_version
        else:
            try:
                version = getlatestgithubrelease("frida/frida", tag_prefix="")  # e.g. 16.3.3
            except Exception as e:
                raise NetworkError(f"Failed to fetch latest Frida version: {e}")

        # Arch map to frida naming
        frida_arch = {
            "arm": "android-arm",
            "arm64": "android-arm64",
            "x86": "android-x86",
            "x86_64": "android-x86_64",
        }[arch]

        # Download URL
        # Official gadget assets are bundled in frida-gadget-{arch}.so.xz under releases
        url = f"https://github.com/frida/frida/releases/download/{version}/frida-gadget-{frida_arch}.so.xz"
        xz_path = tools_dir / f"frida-gadget-{frida_arch}-{version}.so.xz"
        so_path = tools_dir / f"frida-gadget-{frida_arch}-{version}.so"

        if not so_path.exists():
            if self.verbose:
                print(f"Downloading Frida gadget {version} for {frida_arch} ...")
            downloadfile(url, xz_path)
            # Decompress xz
            runcommand(["unxz", "-f", str(xz_path)], check=True)
            # After unxz, file will be without .xz
            if not so_path.exists():
                # Some environments name output differently; fallback to Python lzma
                import lzma
                data = lzma.open(str(xz_path.with_suffix("")), "rb").read() if xz_path.with_suffix("").exists() else lzma.open(str(xz_path), "rb").read()
                so_path.write_bytes(data)
                if xz_path.exists():
                    xz_path.unlink(missing_ok=True)
            if self.verbose:
                print(f"Downloaded gadget to {so_path}")

        return so_path

    def _discover_present_abis(self, workdir: Path) -> List[str]:
        lib = workdir / "lib"
        if not lib.exists():
            return []
        return [p.name for p in lib.iterdir() if p.is_dir()]

    # ---------------------------
    # Injection logic
    # ---------------------------

    def _inject_smali(self, workdir: Path, fqcn: str) -> bool:
        smali_file = self._find_smali_class(workdir, fqcn)
        if not smali_file:
            return False
        # Avoid double injection
        try:
            content = smali_file.read_text(encoding="utf-8", errors="ignore")
            if "System.loadLibrary(\"frida-gadget\")" in content or "System.loadLibrary(\"frida_gadget\")" in content:
                if self.verbose:
                    print(f"Class already patched: {fqcn}")
                return True
        except Exception:
            pass

        ok = SmaliPatcher.inject_loadlibrary(smali_file, "frida-gadget")
        if not ok:
            raise FridaPatchError(f"Smali injection failed for {fqcn} at {smali_file}")
        return True

    def _try_dex_injection(self, workdir: Path, fqcn: str) -> bool:
        try:
            dex_path = self.dex_patcher.find_dex_with_class(workdir, fqcn)
            if not dex_path:
                return False
            self.dex_patcher.patch_dex(dex_path, fqcn, "frida-gadget")
            return True
        except Exception:
            return False

    def _find_smali_class(self, workdir: Path, fqcn: str) -> Optional[Path]:
        rel_path = Path(*fqcn.split("."))  # com/example/App
        smali_dirs = [workdir / "smali"] + sorted(workdir.glob("smali_classes*"), key=lambda p: p.name)
        for sd in smali_dirs:
            candidate = sd / f"{rel_path}.smali"
            if candidate.exists():
                return candidate
        return None

    # ---------------------------
    # Manifest parsing
    # ---------------------------

    def _get_manifest_package(self, manifest_path: Path) -> Optional[str]:
        try:
            tree = ET.parse(manifest_path)
            root = tree.getroot()
            return root.get("package")
        except Exception as e:
            if self.verbose:
                print(f"Manifest package parse error: {e}")
            # Fallback to regex if necessary
            try:
                m = re.search(r'package="([^"]+)"', manifest_path.read_text())
                return m.group(1) if m else None
            except Exception:
                return None

    def _get_application_class(self, manifest_path: Path, pkg: Optional[str]) -> Optional[str]:
        try:
            ns = {"android": "http://schemas.android.com/apk/res/android"}
            tree = ET.parse(manifest_path)
            root = tree.getroot()
            app = root.find("application")
            if app is None:
                return None
            name = app.get("{http://schemas.android.com/apk/res/android}name")
            if not name:
                return None
            return self._resolve_class_name(name, pkg)
        except Exception:
            # Regex fallback
            try:
                text = manifest_path.read_text()
                m = re.search(r'android:name="([^"]+)"', text)
                return self._resolve_class_name(m.group(1), pkg) if m else None
            except Exception:
                return None

    def _get_main_activity(self, manifest_path: Path, pkg: Optional[str]) -> Optional[str]:
        """
        Resolve true launcher component:
        - Prefer <activity> with action MAIN + category LAUNCHER.
        - Else check <activity-alias> targets that have MAIN/LAUNCHER.
        - Return fully qualified class name.
        """
        ns = {"android": "http://schemas.android.com/apk/res/android"}
        try:
            tree = ET.parse(manifest_path)
            root = tree.getroot()
            # Collect candidates
            activities = list(root.iter("activity"))
            aliases = list(root.iter("activity-alias"))

            def is_launcher(node) -> bool:
                for intent in node.findall("intent-filter"):
                    has_main = any(a.get("{http://schemas.android.com/apk/res/android}name") == "android.intent.action.MAIN" for a in intent.findall("action"))
                    has_launcher = any(c.get("{http://schemas.android.com/apk/res/android}name") == "android.intent.category.LAUNCHER" for c in intent.findall("category"))
                    if has_main and has_launcher:
                        return True
                return False

            # Direct activity
            for act in activities:
                if is_launcher(act):
                    name = act.get("{http://schemas.android.com/apk/res/android}name")
                    if name:
                        return self._resolve_class_name(name, pkg)

            # Activity alias pointing to targetActivity
            for alias in aliases:
                if is_launcher(alias):
                    target = alias.get("{http://schemas.android.com/apk/res/android}targetActivity")
                    if target:
                        return self._resolve_class_name(target, pkg)

            # Some apps use CATEGORY_LEANBACK_LAUNCHER (TV); fallback
            for act in activities:
                for intent in act.findall("intent-filter"):
                    has_main = any(a.get("{http://schemas.android.com/apk/res/android}name") == "android.intent.action.MAIN" for a in intent.findall("action"))
                    has_tv = any(c.get("{http://schemas.android.com/apk/res/android}name") in (
                        "android.intent.category.LEANBACK_LAUNCHER", "android.intent.category.HOME") for c in intent.findall("category"))
                    if has_main and has_tv:
                        name = act.get("{http://schemas.android.com/apk/res/android}name")
                        if name:
                            return self._resolve_class_name(name, pkg)

            return None
        except Exception as e:
            if self.verbose:
                print(f"Manifest parse error (main activity): {e}")
            # Regex fallback (last resort)
            try:
                text = manifest_path.read_text()
                # crude but safer fallback; still resolve with package
                m = re.search(
                    r'<activity[^>]*android:name="([^"]+)"[^>]*>.*?'
                    r'<intent-filter>.*?'
                    r'<action[^>]*android:name="android.intent.action.MAIN"[^>]*/>.*?'
                    r'<category[^>]*android:name="android.intent.category.(?:LAUNCHER|LEANBACK_LAUNCHER|HOME)"[^>]*/>.*?'
                    r'</intent-filter>.*?</activity>',
                    text, flags=re.DOTALL
                )
                return self._resolve_class_name(m.group(1), pkg) if m else None
            except Exception:
                return None

    def _resolve_class_name(self, name: str, pkg: Optional[str]) -> str:
        """
        Resolve Android-style class names:
        - Fully qualified com.example.Main stays as-is.
        - .Main -> pkg + .Main
        - Main -> pkg + .Main
        """
        if not name:
            raise ValidationError("Empty class name")
        if name.startswith("."):
            if not pkg:
                raise ValidationError(f"Relative class '{name}' with unknown package")
            return f"{pkg}{name}"
        if "." not in name:
            if not pkg:
                raise ValidationError(f"Unqualified class '{name}' with unknown package")
            return f"{pkg}.{name}"
        return name
