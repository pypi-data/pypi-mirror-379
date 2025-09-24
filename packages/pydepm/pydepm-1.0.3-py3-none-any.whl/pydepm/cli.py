from __future__ import annotations

import os
import json
from pathlib import Path
import sys
import subprocess
from typing import Optional, List
import typer
from rich.console import Console
from rich.table import Table

from .config import PyPackage, init_pypackage
from .installer import (
    install_all,
    install_packages,
    remove_packages,
    ensure_venv,
    get_installed_version,
    ensure_tool,
    run_module,
    set_global_deps_override,
)
from .utils import run as sh_run, ensure_dir, set_verbose

app = typer.Typer(
    help="PyDep (pydep) — Python Dependency Manager",
    add_help_option=True,  # Habilita la opción de ayuda por defecto
    no_args_is_help=True,  # Muestra ayuda si no se proporcionan argumentos
    context_settings={
        'help_option_names': ['-h', '--help']  # Permite tanto -h como --help
    }
)
console = Console()

# Global options
@app.callback()
def _global_options(
    logs: bool = typer.Option(False, "--logs", help="Show detailed command output (verbose)"),
    global_deps: Optional[bool] = typer.Option(None, "--globaldeps", help="Use global Python site (no venv) for this command")
):
    """Global options for PyDM."""
    set_verbose(logs)
    # Allow overriding per-invocation whether to use global dependencies instead of the project's venv
    set_global_deps_override(global_deps)


# ----------------------------
# Helpers
# ----------------------------

def _normalize_name(name: str) -> str:
    return name.replace("-", "_")


def _parse_add_args(pkgs: List[str]) -> list[tuple[str, str]]:
    """Return list of (name, spec) where spec includes leading comparator if any."""
    results: list[tuple[str, str]] = []
    for p in pkgs:
        s = p.strip()
        # Accept formats: name, name==x.y, name>=x, name^x.y.z
        for sep in ["==", ">=", "<=", "~=", ">", "<", "^"]:
            if sep in s:
                name, version = s.split(sep, 1)
                results.append((name.strip(), f"{sep}{version.strip()}"))
                break
        else:
            results.append((s, ""))
    return results


# ----------------------------
# Commands
# ----------------------------

@app.command()
def version():
    """Show PyDM version."""
    from . import __version__
    console.print(f"PyDM {__version__}")


@app.command()
def init(
    name: Optional[str] = typer.Argument(None, help="Project name (optional, uses current directory if not provided)"),
    type: str = typer.Option("app", "--type", help="Project type: app or module"),
    globaldeps: bool = typer.Option(False, "--global-deps", "--globaldeps", help="Use global Python site (no venv) for this project"),
    pyproject: Optional[bool] = typer.Option(
        None, 
        "--pyproject/--no-pyproject", 
        help="For app type: enable/disable pyproject.toml generation (default: disabled). For module type, this flag is ignored as pyproject.toml is always generated."
    )
):
    """Initialize a new project or existing directory.
    
    If a name is provided, creates a new directory with that name.
    If no name is provided, initializes the current directory.
    
    For module type projects, pyproject.toml is always generated with CLI entry points.
    For app type projects, use --pyproject to enable pyproject.toml generation.
    """
    if type == "module" and pyproject is not None:
        console.print("[yellow]Note: --pyproject flag is ignored for module type as pyproject.toml is always generated.")
    
    # If no name provided and it's a module, prompt for name
    if name is None and type == "module":
        name = typer.prompt("Enter project name")
    
    if name:
        # Create new directory structure
        target = Path(os.getcwd()) / name
        if target.exists():
            console.print(f"[red]Directory already exists: {target}")
            raise typer.Exit(1)
            
        console.print(f"[green]Creating project at {target}")
        target.mkdir(parents=True, exist_ok=False)
        cwd = str(target)
        
        # Only create README for module projects without a name (current directory init)
        if type == "module" and not name:
            (target / "README.md").write_text(f"# {name or 'My Project'}\n\nProject created with PyDM.\n", encoding="utf-8")
        
        # Create type-specific structure
        if type == "module":
            pkg_name = _normalize_name(name)
            # Create module directory directly in the project root
            module_dir = target / pkg_name
            ensure_dir(str(module_dir))
            
            # Create __init__.py
            (module_dir / "__init__.py").write_text(
                f'"""{name} module."""\n'
                f'__version__ = "0.1.0"\n',
                encoding="utf-8"
            )
            
            # Create main.py with a simple hello world
            main_content = '''"""Main entry point for the module."""

def hello():
    """Print a hello message."""
    print("Hello from PyDM!")

if __name__ == "__main__":
    hello()
'''
            (module_dir / "main.py").write_text(main_content, encoding="utf-8")
            
            # For module type, we don't create pyproject.toml by default anymore
            # It will be created when running pydep convert --to toml if needed
            
        else:
            # app by default
            main_content = '''
from rich import print

def main():
    """Main entry point for the application."""
    print("[bold green]Hello from your PyDM app![/bold green]")

if __name__ == "__main__":
    main()
'''
            (target / "main.py").write_text(main_content.lstrip(), encoding="utf-8")
    else:
        # Initialize current directory
        cwd = None
        console.print("[green]Initializing project in current directory...")
    
    # Initialize the package
    with console.status("Configuring project..."):
        init_pypackage(cwd=cwd, pkg_type=type, name=name, globaldeps=globaldeps, pyproject_use=pyproject)
    
    if name:
        console.print(f"[green]Project created at {target}")
    else:
        console.print("[green]Project initialized in current directory")
        
    console.print("\nNext steps:")
    console.print(f"1. {'cd ' + str(target) + ' && ' if name else ''}pydep install")
    console.print(f"2. {'cd ' + str(target) + ' && ' if name else ''}pydep run dev")


@app.command()
def install(
    editable: bool = typer.Option(False, "-e", "--editable", help="Install the current project in editable mode"),
    g: bool = typer.Option(False, "-g", "--global", help="Install into global Python site (no venv) for this command")
):
    """Install the current project or its dependencies.
    
    Without --editable, installs dependencies from pypackage.json.
    With --editable, installs the current project in development mode.
    """
    try:
        pkg = PyPackage.load()
    except FileNotFoundError as e:
        console.print("[red]Error: Could not find pypackage.json in the current directory.")
        console.print("[yellow]To create a new project, run one of these commands:")
        console.print("  pydep init --type app     # For an application")
        console.print("  pydep init --type module  # For a module")
        console.print("\nIf you already have a project, make sure you're in the right directory.")
        raise typer.Exit(1) from e
    
    if editable:
        project_dir = pkg.path().parent
        pyproject_path = project_dir / "pyproject.toml"
        
        # Generate pyproject.toml in the project root
        try:
            # Generate the pyproject.toml
            pkg.to_pyproject(pyproject_path)
            
            # Install in editable mode
            cmd = [sys.executable, "-m", "pip", "install", "-e", "."]
            if g:
                cmd.insert(1, "--user")
            
            # Debug: Show the command and working directory
            console.print(f"[yellow]Running: {' '.join(cmd)} in {project_dir}")
            
            # Run the command
            result = subprocess.run(
                cmd,
                cwd=project_dir,
                check=False,
                capture_output=True,
                text=True
            )
            
            # Show command output for debugging
            if result.stdout:
                console.print(result.stdout)
            if result.stderr:
                console.print(f"[yellow]{result.stderr}")
            
            if result.returncode == 0:
                console.print("[green]✓ Successfully installed in editable mode")
            else:
                console.print(f"[red]✗ Failed to install in editable mode (code: {result.returncode})")
                if result.stderr:
                    console.print(f"[red]Error: {result.stderr}")
                raise typer.Exit(1)
                
        except Exception as e:
            console.print(f"[red]Error during editable install: {str(e)}")
            import traceback
            console.print(traceback.format_exc())
            raise typer.Exit(1)
            
        finally:
            # Clean up the pyproject.toml if it was created by us
            if pyproject_path.exists() and not (project_dir / ".pydmconf" / "pyproject.toml").exists():
                try:
                    pyproject_path.unlink()
                except Exception as e:
                    console.print(f"[yellow]Warning: Could not remove temporary pyproject.toml: {e}")
    else:
        # Normal dependency installation
        install_all(str(pkg.path().parent), use_global=g)


@app.command()
def add(
    packages: List[str] = typer.Argument(..., help="Packages to add (e.g., requests==2.32.0 or typer^0.12.3)"),
    g: bool = typer.Option(False, "-g", "--global", help="Install package(s) globally (no venv) for this command"),
    no_deps: bool = typer.Option(False, "--no-deps", help="Install packages without their dependencies")
):
    """Add one or more dependencies to pypackage.json and install them.
    
    By default, all dependencies will be installed. Use --no-deps to install only
    the specified packages without their dependencies.
    """
    if g:
        set_global_deps_override(True)
    try:
        pkg = PyPackage.load()
    except FileNotFoundError:
        console.print("[red]pypackage.json not found. Run 'pydep init'.")
        raise typer.Exit(1)

    parsed = _parse_add_args(packages)
    # Track packages without a specifier to pin exact version afterwards
    no_spec = {name for name, spec in parsed if not (spec or "").strip()}
    for name, spec in parsed:
        pkg.dependencies[name] = spec or ""
    pkg.save()

    # Normalize requirements for pip
    reqs: list[str] = []
    for name, spec in parsed:
        s = spec.strip()
        if s.startswith("^"):
            base = s[1:]
            parts = base.split(".")
            try:
                major = int(parts[0])
                upper = f"<{major+1}.0.0"
                reqs.append(f"{name}>={base},{upper}")
            except Exception:
                reqs.append(f"{name}{s}")
        else:
            # Si no se especifica versión, usamos >= para permitir actualizaciones de parche
            reqs.append(f"{name}{s}" if s else name)

    # Preparar argumentos para pip
    pip_args = ["--upgrade"]
    if no_deps:
        pip_args.append("--no-deps")
    
    # Primero intentamos instalar sin restricciones de versión para permitir que pip resuelva los conflictos
    with console.status("[cyan]Resolving dependencies..."):
        if no_deps:
            # Si --no-deps está activado, instalamos directamente las versiones especificadas
            code = install_packages(pip_args + reqs)
        else:
            # Intento 1: Instalar sin restricciones de versión
            temp_reqs = [req.split("==")[0].split("<")[0].split(">")[0].split("~")[0].split("^")[0] for req in reqs]
            code = install_packages(pip_args + temp_reqs)
            
            if code != 0:
                # Intento 2: Si falla, intentamos con las restricciones originales
                console.print("[yellow]Warning: Could not resolve dependencies with flexible versions. Trying with exact versions...")
                code = install_packages(pip_args + reqs)
                if code != 0:
                    console.print("[red]Error: Could not resolve package dependencies. Try one of these solutions:")
                    console.print("1. Use --no-deps to install without dependencies")
                    console.print("2. Specify version constraints manually, e.g.: pydep add 'requests>=2.25.0,<3.0.0'")
                    raise typer.Exit(code)

    # Pin exact versions for those without specifier
    modified = False
    with console.status("[cyan]Pinning exact versions..."):
        for name in no_spec:
            ver = get_installed_version(name)
            if ver:
                pkg.dependencies[name] = f"=={ver}"
                modified = True
    if modified:
        pkg.save()
        console.print("[green]Dependencies updated with exact versions in pypackage.json")
    raise typer.Exit(0)


@app.command()
def remove(packages: List[str] = typer.Argument(..., help="Packages to remove"), g: bool = typer.Option(False, "-g", "--global", help="Remove from global site-packages for this command")):
    """Remove one or more dependencies from pypackage.json and uninstall from the environment."""
    if g:
        set_global_deps_override(True)
    try:
        pkg = PyPackage.load()
    except FileNotFoundError:
        console.print("[red]pypackage.json not found in the current directory")
        raise typer.Exit(1)

    for name in packages:
        if name in pkg.dependencies:
            del pkg.dependencies[name]
    pkg.save()

    with console.status("[cyan]Uninstalling packages..."):
        code = remove_packages(packages)
    raise typer.Exit(code)


@app.command("run")
def run_cmd(script: str = typer.Argument(..., help="Script name defined in pypackage.json")):
    """Run a script defined in pypackage.json (equivalent to npm run)."""
    try:
        pkg = PyPackage.load()
    except FileNotFoundError:
        console.print("[red]pypackage.json not found in the current directory")
        raise typer.Exit(1)

    cmd = pkg.scripts.get(script)
    if not cmd:
        console.print(f"[red]Script '{script}' not found in pypackage.json")
        raise typer.Exit(1)

    # Asegura venv para comandos python si se desea
    ensure_venv()

    console.print(f"[cyan]Running: {cmd}")
    
    # Usar subprocess.Popen directamente para mejor manejo de E/S
    import subprocess
    import sys
    
    process = None
    try:
        process = subprocess.Popen(
            cmd,
            shell=True,
            bufsize=0,  # Sin buffer
            text=True,
            stdin=sys.stdin,
            stdout=sys.stdout,
            stderr=sys.stderr
        )
        process.communicate()  # Esperar a que termine el proceso
        exit_code = process.returncode
    except Exception as e:
        console.print(f"[red]Error running script: {e}")
        exit_code = 1
    
    # Si llegamos aquí, el proceso terminó (bien o mal)
    raise typer.Exit(exit_code)

@app.command()
def build():
    """Build the project (wheel/sdist or executable for app type)."""
    try:
        pkg = PyPackage.load()
    except FileNotFoundError:
        console.print("[red]pypackage.json not found in the current directory")
        raise typer.Exit(1)
    
    # Ensure .pydepconf directory exists
    config_dir = Path(".pydepconf")
    config_dir.mkdir(exist_ok=True)
    
    # Generate pyproject.toml in .pydmconf only if needed
    pyproject_path = None
    if pkg.type == "module" or (pkg.type == "app" and getattr(pkg, 'pyprojectUse', False)):
        pyproject_path = config_dir / "pyproject.toml"
        console.print("[cyan]Generating pyproject.toml in .pydepconf directory...")
        pkg.to_pyproject(pyproject_path)
    
    # Handle module type with build
    if pkg.type == "module":
        console.print("[cyan]Building Python module...")
        ensure_tool("build")
        
        # Create a temporary directory for the build
        import tempfile
        import shutil
        
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            
            # Copy all files to the temporary directory
            for item in Path(".").iterdir():
                if item.name in [".pydepconf", ".venv", "venv", "__pycache__", ".git", ".gitignore", ".pytest_cache"]:
                    continue
                if item.is_file():
                    shutil.copy2(item, tmp_path / item.name)
                elif item.is_dir():
                    shutil.copytree(item, tmp_path / item.name, dirs_exist_ok=True)
            
            # Copy the generated pyproject.toml to the temporary directory if it exists
            if pyproject_path and pyproject_path.exists():
                shutil.copy2(pyproject_path, tmp_path / "pyproject.toml")
            
            # Create README.md if it doesn't exist
            if not (tmp_path / "README.md").exists() and pkg.description:
                (tmp_path / "README.md").write_text(f"# {pkg.name}\n\n{pkg.description}")
            
            # Run build in the temporary directory
            with console.status("[cyan]Building package..."):
                result = subprocess.run(
                    [sys.executable, "-m", "build", "--outdir", "dist"],
                    cwd=tmp_path,
                    capture_output=True,
                    text=True
                )
                
                # Show build output
                if result.stdout:
                    console.print(result.stdout)
                if result.stderr:
                    console.print(f"[yellow]{result.stderr}")
                
                if result.returncode != 0:
                    console.print("[red]Build failed")
                    raise typer.Exit(1)
                
                # Copy the built packages to the current directory
                dist_dir = Path("dist")
                dist_dir.mkdir(exist_ok=True)
                
                for pkg_file in (tmp_path / "dist").glob("*"):
                    shutil.copy2(pkg_file, dist_dir / pkg_file.name)
                
                console.print(f"[green]Package built in: {dist_dir.absolute()}")
                
                # If there are CLI scripts, show installation instructions
                if pkg.cli:
                    console.print("\n[bold]CLI tools available after installation:[/]")
                    for script_name, script_config in pkg.cli.items():
                        if isinstance(script_config, dict):
                            name = script_config.get('name', script_name)
                            console.print(f"  • {name}")
                    
                    console.print("\nTo install the package with CLI tools:")
                    console.print("  pip install .  # Install in development mode")
                    console.print("  # or")
                    console.print(f"  pip install {dist_dir}/*.whl  # Install from built wheel")
    
    # Handle app type with PyInstaller
    elif pkg.type == "app" and hasattr(pkg, 'executable') and pkg.executable and 'target' in pkg.executable:
        console.print("[cyan]Building executable with PyInstaller...")
        ensure_tool("pyinstaller")
        
        # Get executable config or use defaults
        target = pkg.executable.get('target', 'main.py')
        parameters = pkg.executable.get('parameters', ['--onefile'])
        output_dir = pkg.executable.get('output', 'dist/executable')
        
        # Ensure target file exists
        if not Path(target).exists():
            console.print(f"[red]Target file not found: {target}")
            raise typer.Exit(1)
            
        # Prepare PyInstaller command
        cmd = ["pyinstaller"]
        
        # Add parameters if any
        if parameters:
            cmd.extend(parameters)
            
        # Add output directory if specified
        if output_dir:
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)
            cmd.extend(["--distpath", str(output_path)])
            
        # Add target file
        cmd.append(target)
        
        # Run PyInstaller
        console.print(f"[cyan]Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, check=True)
        
        if result.returncode == 0:
            console.print(f"[green]Executable created in: {output_dir}")
        else:
            console.print("[red]Failed to build executable with PyInstaller")
            raise typer.Exit(1)
    else:
        # Standard build for module type or app without executable config
        ensure_tool("build")
        
        # Create a temporary directory for the build
        import tempfile
        import shutil
        
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            
            # Copy all files to the temporary directory
            for item in Path(".").iterdir():
                if item.name in [".pydepconf", ".venv", "venv", "__pycache__", ".git", ".gitignore"]:
                    continue
                if item.is_file():
                    shutil.copy2(item, tmp_path / item.name)
                elif item.is_dir():
                    shutil.copytree(item, tmp_path / item.name, dirs_exist_ok=True)
            
            # Copy the generated pyproject.toml to the temporary directory if it exists
            if pyproject_path and pyproject_path.exists():
                shutil.copy2(pyproject_path, tmp_path / "pyproject.toml")
            
            # Run build in the temporary directory
            with console.status("[cyan]Building package..."):
                result = subprocess.run(
                    [sys.executable, "-m", "build", "--outdir", "dist"],
                    cwd=tmp_path,
                    capture_output=True,
                    text=True
                )
                
                # Show build output
                if result.stdout:
                    console.print(result.stdout)
                if result.stderr:
                    console.print(f"[yellow]{result.stderr}")
                
                if result.returncode != 0:
                    console.print("[red]Build failed")
                    raise typer.Exit(1)
                
                # Copy the built packages to the current directory
                dist_dir = Path("dist")
                dist_dir.mkdir(exist_ok=True)
                
                for pkg_file in (tmp_path / "dist").glob("*"):
                    shutil.copy2(pkg_file, dist_dir / pkg_file.name)
                
                console.print("[green]✓ Python package built in ./dist")
                console.print("\nNext steps:")
                console.print("  • Install in development mode: [cyan]pydep install -e[/cyan]")


@app.command()
def convert(
    to: str = typer.Option("toml", "--to", help="Conversion type: toml or lock"),
    hashes: bool = typer.Option(False, "--hashes/--no-hashes", help="Include sha256 hashes in the lockfile (disabled by default for speed)"),
    outdir: Optional[Path] = typer.Option(None, "--outdir", "-o", help="Output directory for the generated file (default: current directory for lock, .pydepconf for toml)"),
):
    """Convert pypackage.json to other formats.
    
    By default, pyproject.toml is generated in the .pydmconf directory,
    while pypackage-lock.json is generated in the current directory.
    """
    try:
        pkg = PyPackage.load()
    except FileNotFoundError:
        console.print("[red]pypackage.json not found in the current directory")
        raise typer.Exit(1)
    
    if to == "lock":
        # For lock files, use the specified output directory or current directory
        output_file = Path(outdir or ".") / "pypackage-lock.json"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        from .installer import generate_lockfile
        console.print("[cyan]Generating pypackage-lock.json (may take a while when including hashes)...")
        with console.status("[cyan]Resolving and writing lockfile..."):
            generate_lockfile(fast=not hashes, quiet=True, output_file=output_file)
        console.print(f"[green]Lockfile generated at: {output_file.absolute()}")
        return
    
    # For TOML, use the specified output directory or .pydepconf
    if to == "toml":
        if outdir is None:
            # Default to current directory for backward compatibility
            output_file = Path.cwd() / "pyproject.toml"
        else:
            output_file = outdir / "pyproject.toml"
            output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with console.status("[cyan]Generating pyproject.toml..."):
            pkg.to_pyproject(output_file)
        
        if outdir is None:
            console.print("[green]pyproject.toml generated in the current directory.")
        else:
            console.print(f"[green]pyproject.toml generated at: {output_file.absolute()}")
        return
    
    console.print(f"[red]Unsupported conversion target: {to}")
    raise typer.Exit(1)


@app.command()
def audit(
    json_output: bool = typer.Option(False, "--json", help="Show raw JSON output from pip-audit"),
    extended: bool = typer.Option(False, "--extended", help="Also show packages with no known vulnerabilities")
):
    """Audit dependencies using pip-audit and show a concise summary (no --logs required)."""
    ensure_venv()
    ensure_tool("pip-audit")

    if json_output:
        code = run_module("pip_audit", args=["--format", "json"])
        raise typer.Exit(code)

    # Capture JSON and render pretty tables
    from .installer import run_module_capture
    rc, out = run_module_capture("pip_audit", args=["--format", "json"])
    text = out.strip()
    if not text:
        console.print("[yellow]pip-audit produced no output.")
        raise typer.Exit(rc)

    # Some pip-audit versions print a human line before JSON; extract JSON payload
    json_start = text.find("{")
    if json_start == -1:
        json_start = text.find("[")
    payload = text[json_start:] if json_start != -1 else text

    try:
        data = json.loads(payload)
    except Exception:
        console.print(text)
        raise typer.Exit(rc)

    # Normalize data to a list of package dicts
    if isinstance(data, dict) and isinstance(data.get("dependencies"), list):
        pkgs = data["dependencies"]
    elif isinstance(data, list):
        pkgs = data
    else:
        console.print("[red]Unexpected pip-audit JSON format.")
        raise typer.Exit(1)

    total_pkgs = len(pkgs)
    vulns_rows = []
    ok_rows = []
    for pkg in pkgs:
        name = pkg.get("name", "")
        ver = pkg.get("version", "")
        vulns = pkg.get("vulns") or []
        if vulns:
            for v in vulns:
                vid = v.get("id", "")
                fixes = v.get("fix_versions") or []
                fix_str = ", ".join(fixes) if fixes else "(no fix available)"
                vulns_rows.append((name, ver, vid, fix_str))
        else:
            ok_rows.append((name, ver))

    if not vulns_rows:
        console.print("[green]✔ No known vulnerabilities were found in audited dependencies.")
        if extended and ok_rows:
            t2 = Table(show_header=True, header_style="bold")
            t2.add_column("Package")
            t2.add_column("Version")
            for n, v in sorted(set(ok_rows)):
                t2.add_row(n, v)
            console.print(t2)
        raise typer.Exit(0)

    console.print(f"[red]✖ Found {len(vulns_rows)} vulnerabilities affecting {len(set(n for n,_,_,_ in vulns_rows))} packages (audited {total_pkgs}).")
    t = Table(show_header=True, header_style="bold")
    t.add_column("Package")
    t.add_column("Version")
    t.add_column("Advisory ID")
    t.add_column("Fix Versions")
    for row in vulns_rows:
        t.add_row(*row)
    console.print(t)

    if extended and ok_rows:
        t2 = Table(show_header=True, header_style="bold")
        t2.add_column("Package (no known vulns)")
        t2.add_column("Version")
        for n, v in sorted(set(ok_rows)):
            t2.add_row(n, v)
        console.print(t2)

    console.print("Tip: try 'pip install --upgrade <package>' or adjust versions in pypackage.json and regenerate the lock.")
    raise typer.Exit(1)


@app.command()
def outdated():
    """Show outdated packages in the managed venv."""
    from .installer import pip_list_outdated
    with console.status("[cyan]Checking for outdated packages..."):
        rows = pip_list_outdated()
    if not rows:
        console.print("[green]All packages are up to date.")
        return
    t = Table(show_header=True, header_style="bold")
    t.add_column("Package")
    t.add_column("Current")
    t.add_column("Latest")
    t.add_column("Type")
    for r in rows:
        t.add_row(r.get("name",""), r.get("version",""), r.get("latest_version",""), r.get("latest_filetype",""))
    console.print(t)


@app.command("list")
def list_cmd():
    """List installed packages and versions.
    
    If a virtual environment exists in the current directory, lists packages from there.
    Otherwise, lists globally installed packages.
    """
    from .installer import freeze_versions, venv_exists, get_global_packages
    
    # Check if a virtual environment exists
    has_venv = venv_exists()
    
    # Don't create a venv if one doesn't exist
    with console.status("[cyan]Checking for installed packages..."):
        packages = freeze_versions(ensure_venv_exists=False)
    
    if not packages and has_venv:
        console.print("[yellow]No packages installed in the virtual environment.")
        return
    
    if not packages:
        # No venv exists, list global packages
        console.print("[yellow]No virtual environment found. Listing globally installed packages...")
        with console.status("[cyan]Checking global packages..."):
            packages = get_global_packages()
        
        if not packages:
            console.print("[yellow]No packages found in global Python environment.")
            return
    
    # Create and display the table
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Package", style="cyan")
    table.add_column("Version", style="green")
    
    # Add environment info to the table title
    env_type = "Virtual Environment" if has_venv else "Global Environment"
    table.title = f"Installed Packages ({env_type})"
    
    for name, ver in sorted(packages.items()):
        table.add_row(name, ver)
    
    console.print(table)
    
    if not has_venv:
        console.print("\n[yellow]Note:[/] No virtual environment found. To create one, run: [cyan]pydep install[/]")


@app.command()
def why(package: str = typer.Argument(..., help="Package name to explain")):
    """Explain why a package is installed by showing a path from a top-level dependency."""
    from .installer import freeze_versions, get_requires, dependency_closure
    with console.status("[cyan]Analyzing dependency graph..."):
        versions = freeze_versions()
    if package.lower() not in versions:
        console.print(f"[red]{package} is not installed in the managed venv.")
        raise typer.Exit(1)
    # Build reverse dependency graph
    # Determine top-levels
    try:
        p = PyPackage.load()
        tops = set(k.lower() for k in (p.dependencies or {}).keys())
    except Exception:
        tops = set()
    # Fast path: target is a top-level dependency
    target = package.lower()
    if target in tops:
        console.print("Dependency paths:")
        console.print(f"  - {target} (top-level)")
        raise typer.Exit(0)

    # Limit graph to project's dependency closure for speed
    closure = set(dependency_closure(list(tops), versions)) if tops else set(versions.keys())
    # Build reverse edges within closure only, with a small cache for requires()
    rev: dict[str, set[str]] = {}
    requires_cache: dict[str, list[str]] = {}
    for pkg in closure:
        deps = requires_cache.get(pkg)
        if deps is None:
            deps = get_requires(pkg)
            requires_cache[pkg] = deps
        for dep in deps:
            if dep in closure or dep in tops:
                rev.setdefault(dep, set()).add(pkg)
    # BFS from target towards tops using reverse edges
    from collections import deque
    q = deque([(target, [target])])
    seen = {target}
    found_paths = []
    with console.status("[cyan]Tracing dependency path..."):
        while q and len(found_paths) < 3:
            node, path = q.popleft()
            if node in tops:
                found_paths.append(list(reversed(path)))
                continue
            for parent in sorted(rev.get(node, [])):
                if parent not in seen:
                    seen.add(parent)
                    q.append((parent, [parent] + path))
    if not found_paths:
        console.print("[yellow]No path from a top-level dependency was found (may be indirect or environment-installed).")
        raise typer.Exit(0)
    console.print("Dependency paths:")
    for path in found_paths:
        console.print("  - " + " -> ".join(path))


@app.command()
def update(
    packages: List[str] = typer.Argument(None, help="Specific packages to update (default: all declared dependencies)"),
    g: bool = typer.Option(False, "-g", "--global", help="Update in global site-packages for this command"),
):
    """Update dependencies to their latest compatible versions and refresh pypackage.json and the lockfile."""
    if g:
        set_global_deps_override(True)
    try:
        pkg = PyPackage.load()
    except FileNotFoundError:
        console.print("[red]pypackage.json not found in the current directory")
        raise typer.Exit(1)

    deps_dict = pkg.dependencies or {}
    targets: List[str] = packages or [k for k in deps_dict.keys()]
    if not targets:
        console.print("[yellow]No dependencies to update.")
        raise typer.Exit(0)

    # Upgrade using pip, then write exact versions back
    reqs = [name for name in targets]
    with console.status("[cyan]Updating dependencies..."):
        code = install_packages(["--upgrade", *reqs])
    if code != 0:
        raise typer.Exit(code)
    # Persist exact versions
    from .installer import get_installed_version
    modified = False
    with console.status("[cyan]Pinning exact versions..."):
        for name in targets:
            ver = get_installed_version(name)
            if ver:
                pkg.dependencies[name] = f"=={ver}"
                modified = True
    if modified:
        pkg.save()
    # Regenerate lock (fast by default)
    from .installer import generate_lockfile
    with console.status("[cyan]Regenerating lockfile..."):
        generate_lockfile(fast=True, quiet=True)
    console.print("[green]Dependencies updated and lockfile regenerated.")
