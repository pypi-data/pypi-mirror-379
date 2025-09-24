from __future__ import annotations

import os
import sys
import json
from pathlib import Path
from typing import Iterable, Optional, Dict, Tuple, List
import tempfile
import hashlib
import platform
from rich.console import Console
from .utils import run, run_capture, is_windows, ensure_dir
from .config import PyPackage

console = Console()


DEF_VENV_DIR = ".venv"

# Global dependencies override (None means use project setting)
GLOBAL_DEPS_OVERRIDE: Optional[bool] = None


def set_global_deps_override(flag: Optional[bool]) -> None:
    global GLOBAL_DEPS_OVERRIDE
    GLOBAL_DEPS_OVERRIDE = flag


def _use_global_deps(cwd: Optional[str]) -> bool:
    if GLOBAL_DEPS_OVERRIDE is not None:
        return bool(GLOBAL_DEPS_OVERRIDE)
    try:
        pkg = PyPackage.load(cwd)
        return bool(getattr(pkg, "useGlobalDeps", False))
    except Exception:
        return False


def venv_dir(cwd: Optional[str] = None) -> Path:
    return Path(cwd or os.getcwd()) / DEF_VENV_DIR


def venv_python(cwd: Optional[str] = None) -> Path:
    vdir = venv_dir(cwd)
    if is_windows():
        return vdir / "Scripts" / "python.exe"
    return vdir / "bin" / "python"


def ensure_venv(cwd: Optional[str] = None, python: Optional[str] = None) -> Path:
    # If project is configured to use global dependencies, return system python
    if _use_global_deps(cwd):
        return Path(sys.executable)
    vdir = venv_dir(cwd)
    if not vdir.exists():
        console.print(f"[cyan]Creating virtual environment at {vdir}...")
        cmd = [python or sys.executable, "-m", "venv", str(vdir)]
        code = run(cmd)
        if code != 0:
            raise RuntimeError("Failed to create virtual environment")
    return venv_python(cwd)


def pip(cmd_args: list[str], cwd: Optional[str] = None) -> int:
    py = ensure_venv(cwd)
    return run([str(py), "-m", "pip", *cmd_args], cwd=cwd)


def get_installed_version(package: str, cwd: Optional[str] = None) -> Optional[str]:
    """Return installed version for package in the managed venv, or None if not found."""
    py = ensure_venv(cwd)
    code, out = run_capture([str(py), "-m", "pip", "show", package], cwd=cwd)
    if code != 0 or not out:
        return None
    for line in out.splitlines():
        if line.lower().startswith("version:"):
            return line.split(":", 1)[1].strip()
    return None


def global_cache_dir() -> Path:
    """Return path to the global cache directory used by PyDM."""
    home = Path.home()
    base = home / ".pydm" / "cache"
    base.mkdir(parents=True, exist_ok=True)
    return base


def pip_download(packages: Iterable[str], dest: Path, cwd: Optional[str] = None) -> int:
    """Download distributions for given package requirements into dest (no deps).

    Note: 'packages' must be requirement specifiers only (no pip options).
    """
    py = ensure_venv(cwd)
    args = [str(py), "-m", "pip", "download", "--no-deps", "-d", str(dest), *list(packages)]
    return run(args, cwd=cwd)


def compute_hashes_for_package(name: str, version: str, cwd: Optional[str] = None) -> List[str]:
    """Download the package wheel/sdist for exact version and compute sha256 hashes.

    Returns list of strings like 'sha256:<hex>'. For simplicity, we hash the downloaded
    artifact(s) for the current platform.
    """
    req = f"{name}=={version}"
    hashes: List[str] = []
    # Primero intenta usar el caché global para evitar descargas
    cache = global_cache_dir()
    candidates = list(cache.glob(f"{name.replace('-', '_')}*-{version}*.whl")) + list(cache.glob(f"{name}*-{version}*.whl"))
    if candidates:
        for file in candidates:
            if file.is_file():
                h = hashlib.sha256()
                with file.open("rb") as f:
                    for chunk in iter(lambda: f.read(8192), b""):
                        h.update(chunk)
                hashes.append(f"sha256:{h.hexdigest()}")
        return hashes

    # Si no está en caché, descarga temporalmente y calcula hash
    with tempfile.TemporaryDirectory() as td:
        tmpdir = Path(td)
        rc = pip_download([req], dest=tmpdir, cwd=cwd)
        if rc != 0:
            return hashes
        for file in tmpdir.iterdir():
            if file.is_file():
                h = hashlib.sha256()
                with file.open("rb") as f:
                    for chunk in iter(lambda: f.read(8192), b""):
                        h.update(chunk)
                hashes.append(f"sha256:{h.hexdigest()}")
    return hashes


def freeze_versions(cwd: Optional[str] = None) -> Dict[str, str]:
    """Return mapping name -> exact version from pip freeze in the managed venv."""
    py = ensure_venv(cwd)
    code, out = run_capture([str(py), "-m", "pip", "freeze"], cwd=cwd)
    result: Dict[str, str] = {}
    if code != 0 or not out:
        return result
    for line in out.splitlines():
        line = line.strip()
        if not line or line.startswith("-") or "==" not in line:
            continue
        name, ver = line.split("==", 1)
        result[name.lower()] = ver
    return result


def get_requires(package: str, cwd: Optional[str] = None) -> List[str]:
    """Return list of required package names (lowercased) for the given package using pip show."""
    py = ensure_venv(cwd)
    code, out = run_capture([str(py), "-m", "pip", "show", package], cwd=cwd)
    if code != 0 or not out:
        return []
    for line in out.splitlines():
        if line.startswith("Requires:"):
            reqs = line.split(":", 1)[1].strip()
            if not reqs:
                return []
            # Split by comma and take the name part (strip extras and version if present)
            names = []
            for item in reqs.split(","):
                nm = item.strip()
                if not nm:
                    continue
                # drop extras marker like pkg[extra]
                nm = nm.split("[")[0].strip()
                names.append(nm.lower())
            return names
    return []


def dependency_closure(top_level: List[str], versions: Dict[str, str], cwd: Optional[str] = None) -> List[str]:
    """Compute dependency closure starting from top-level package names, using pip show Requires field.

    Only includes packages present in 'versions'. Returns a list of lowercased names.
    """
    seen: set[str] = set()
    queue: List[str] = [n.lower() for n in top_level]
    while queue:
        name = queue.pop(0)
        if name in seen:
            continue
        if name not in versions:
            # Not installed or not part of this environment
            seen.add(name)
            continue
        seen.add(name)
        for child in get_requires(name, cwd=cwd):
            if child not in seen:
                queue.append(child)
    # Filter to those with versions (installed)
    return [n for n in seen if n in versions]


def pip_list_outdated(cwd: Optional[str] = None) -> List[dict]:
    """Return list of outdated packages using pip list --outdated --format=json."""
    py = ensure_venv(cwd)
    code, out = run_capture([str(py), "-m", "pip", "list", "--outdated", "--format", "json"], cwd=cwd)
    if code != 0 or not out:
        return []
    try:
        data = json.loads(out)
        if isinstance(data, list):
            return data
    except Exception:
        return []
    return []


def pip_show(package: str, cwd: Optional[str] = None) -> Dict[str, str]:
    """Return parsed fields from pip show output as a dict."""
    py = ensure_venv(cwd)
    code, out = run_capture([str(py), "-m", "pip", "show", package], cwd=cwd)
    result: Dict[str, str] = {}
    if code != 0 or not out:
        return result
    for line in out.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            result[k.strip()] = v.strip()
    return result


def generate_lockfile(cwd: Optional[str] = None, fast: bool = False, quiet: bool = False, output_file: Optional[Path] = None) -> Path:
    """Generate a lockfile with exact versions and hashes for project dependencies only.

    We compute the dependency closure starting from pypackage.json dependencies.
    
    Args:
        cwd: Working directory (default: current directory)
        fast: If True, skip computing hashes for faster generation
        quiet: If True, suppress output messages
        output_file: Optional path to the output lockfile. If None, uses pypackage-lock.json in cwd.
    
    Returns:
        Path to the generated lockfile
    """
    versions = freeze_versions(cwd)
    try:
        pkg = PyPackage.load(cwd)
        top = list((pkg.dependencies or {}).keys())
    except Exception:
        top = []
    closure = dependency_closure(top, versions, cwd=cwd) if top else list(versions.keys())
    lock: Dict[str, Dict[str, object]] = {}
    if not quiet:
        console.print("[cyan]Computing hashes for lockfile...")
    for name_lower in sorted(closure):
        ver = versions.get(name_lower)
        if not ver:
            continue
        hashes: List[str] = []
        if not fast:
            hashes = compute_hashes_for_package(name_lower, ver, cwd=cwd)
        lock[name_lower] = {
            "version": f"=={ver}",
            "hashes": hashes,
        }
    meta = {
        "python": platform.python_version(),
        "platform": platform.platform(),
    }
    lock_data = {
        "lockfileVersion": 1,
        "metadata": meta,
        "packages": lock,
    }
    
    # Use the provided output file or default to pypackage-lock.json in cwd
    if output_file is None:
        path = PyPackage.lockfile_path(cwd)
    else:
        path = output_file
    
    # Ensure the parent directory exists
    path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write the lockfile
    path.write_text(json.dumps(lock_data, indent=2), encoding="utf-8")
    
    if not quiet:
        console.print(f"[green]Lockfile written to {path}")
    
    return path


def install_with_cache(packages: Iterable[str], cwd: Optional[str] = None) -> int:
    """Install given package requirements using the global cache to avoid re-downloads.

    Accepts pip options mixed with requirements (e.g., ["--upgrade", "requests"]).
    """
    cache = global_cache_dir()
    args = list(packages)
    opts = [a for a in args if isinstance(a, str) and a.startswith("-")]
    reqs = [a for a in args if not (isinstance(a, str) and a.startswith("-"))]
    # If using global deps, prefer --user installs to avoid admin
    if _use_global_deps(cwd) and "--user" not in opts:
        opts = ["--user", *opts]
    if reqs:
        # Pre-download artifacts for requirements only
        pip_download(reqs, dest=cache, cwd=cwd)
    # Try install from cache first
    base = ["install", *opts, "--no-index", "--find-links", str(cache), *reqs]
    rc = pip(base, cwd=cwd)
    if rc != 0:
        # Fallback to network with cache as find-links
        base = ["install", *opts, "--find-links", str(cache), *reqs]
        rc = pip(base, cwd=cwd)
    return rc


def install_packages(packages: Iterable[str], cwd: Optional[str] = None) -> int:
    if not packages:
        return 0
    # Hide pip options in the display list
    display = [p for p in packages if not (isinstance(p, str) and p.startswith("-"))]
    console.print("[green]Installing packages:", ", ".join(display))
    return install_with_cache(packages, cwd=cwd)


def remove_packages(packages: Iterable[str], cwd: Optional[str] = None) -> int:
    if not packages:
        return 0
    console.print("[yellow]Uninstalling packages:", ", ".join(packages))
    return pip(["uninstall", "-y", *packages], cwd=cwd)


def install_all(cwd: Optional[str] = None, use_global: bool = False) -> int:
    try:
        pkg = PyPackage.load(cwd)
    except FileNotFoundError:
        console.print("[red]pypackage.json not found in the current directory")
        return 1
    
    # Configurar el uso de dependencias globales si se solicita
    if use_global:
        set_global_deps_override(True)
        
    # Si hay lockfile, instalar exactamente desde lockfile
    lock_path = PyPackage.lockfile_path(cwd)
    if lock_path.exists():
        try:
            lock = json.loads(lock_path.read_text(encoding="utf-8"))
            packages = [f"{name}{entry.get('version','')}" for name, entry in lock.get("packages", {}).items()]
            if packages:
                console.print("[cyan]Installing from lockfile...")
                return install_with_cache(packages, cwd=cwd)
        except Exception as e:
            console.print(f"[yellow]Invalid lockfile. Ignoring and resolving from pypackage.json. Error: {e}")

    reqs = [f"{name}{spec}" if any(c in spec for c in "><=~^*") else f"{name}=={spec}" for name, spec in pkg.dependencies.items()]
    # Interpret ^x.y.z como >=x.y.z,<x+1.0.0 de forma simple
    norm_reqs: list[str] = []
    for name, spec in pkg.dependencies.items():
        s = spec.strip()
        if s.startswith("^"):
            base = s[1:]
            parts = base.split(".")
            try:
                major = int(parts[0])
                upper = f"<{major+1}.0.0"
                norm_reqs.append(f"{name}>={base},{upper}")
            except Exception:
                norm_reqs.append(f"{name}{s}")
        else:
            norm_reqs.append(f"{name}{s}")
    if not norm_reqs:
        console.print("[yellow]No dependencies to install.")
        ensure_venv(cwd)
        return 0
    code = install_packages(norm_reqs, cwd=cwd)
    if code == 0:
        console.print("[green]Dependencies installed.")
    return code


def ensure_tool(package: str, cwd: Optional[str] = None) -> int:
    """Ensure a tool is installed inside the managed venv (e.g., 'build', 'twine', 'pip-audit')."""
    return pip(["install", package], cwd=cwd)


def run_module(module: str, args: list[str] | tuple[str, ...] = (), cwd: Optional[str] = None, force_stream: bool = False) -> int:
    """Run a Python module inside the managed venv (e.g., python -m build)."""
    py = ensure_venv(cwd)
    return run([str(py), "-m", module, *list(args)], cwd=cwd, force_stream=force_stream)


def run_module_capture(module: str, args: list[str] | tuple[str, ...] = (), cwd: Optional[str] = None) -> tuple[int, str]:
    """Run a Python module inside the managed venv and capture its combined output."""
    py = ensure_venv(cwd)
    return run_capture([str(py), "-m", module, *list(args)], cwd=cwd)
