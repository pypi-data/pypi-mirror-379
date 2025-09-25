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

from .installer import cleanup_old_cache, global_cache_dir

def clear_cache_command(max_age_days: Optional[int] = None):
    """Clear the package cache."""
    cache_dir = global_cache_dir()
    try:
        if max_age_days is not None:
            console.print(f"[yellow]Cleaning cache older than {max_age_days} days...[/]")
            cleanup_old_cache(max_age_days)
            console.print("[green]✓ Cache cleanup completed")
        else:
            if cache_dir.exists():
                import shutil
                shutil.rmtree(cache_dir)
                cache_dir.mkdir(parents=True)
                console.print(f"[green]✓ Successfully cleared package cache at: {cache_dir}")
            else:
                console.print("[yellow]ℹ️  Package cache is already empty")
    except Exception as e:
        console.print(f"[red]Error clearing cache: {e}")
        raise typer.Exit(1)

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
@app.command(name="clear-cache")
def clear_cache_cmd(
    max_age: Optional[int] = typer.Option(
        None,
        "--max-age",
        help="Clear cache older than X days (default: clear all)"
    )
):
    """Clear the package cache.
    
    Examples:
        pydep clear-cache          # Clear entire cache
        pydep clear-cache --max-age 30  # Clear cache older than 30 days
    """
    clear_cache_command(max_age)
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
    """Show PyDepM version."""
    from . import __version__
    console.print(f"PyDepM {__version__}")


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
    
    # Always ask for project name if not provided
    if name is None:
        name = typer.prompt("Enter project name")
        if not name.strip():
            console.print("[red]Project name cannot be empty!")
            raise typer.Exit(1)
    
    # Ask for project type if not provided via command line
    if type == "app":  # If using default value, ask for confirmation/choice
        console.print("\n[bold]Project type:[/bold]")
        console.print("1. app - Simple application with main.py")
        console.print("2. module - Python package with CLI entry points")
        
        type_choice = typer.prompt(
            "Choose project type (1 or 2)", 
            type=str, 
            default="1"
        ).strip()
        
        if type_choice == "1":
            type = "app"
        elif type_choice == "2":
            type = "module"
        else:
            console.print("[red]Invalid choice. Using 'app' as default.")
            type = "app"
    
    console.print(f"[green]Selected project type: {type}")
    # ← FIN DE LA PARTE NUEVA ↑
    
    # Ask if user wants full project structure (esta parte ya existe)
    create_full_structure = typer.confirm(
        "Do you want to create the full project structure?",
        default=True,
    )
    
    target = None
    cwd = None
    
    if create_full_structure:
        # Create full directory structure (existing logic)
        target = Path(os.getcwd()) / name
        if target.exists():
            console.print(f"[red]Directory already exists: {target}")
            raise typer.Exit(1)
            
        console.print(f"[green]Creating project structure at {target}")
        target.mkdir(parents=True, exist_ok=False)
        cwd = str(target)
        
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
            
            # Create README for module projects
            (target / "README.md").write_text(f"# {name}\n\nModule project created with PyDM.\n", encoding="utf-8")
            
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
            (target / "README.md").write_text(f"# {name}\n\nApp project created with PyDM.\n", encoding="utf-8")
    else:
        # Minimal structure - ONLY pypackage.json in current directory
        # NO directories, NO module folders, NO additional files
        console.print(f"[green]Creating minimal project '{name}' in current directory...")
        cwd = os.getcwd()
    
    # Initialize the package (creates pypackage.json)
    with console.status("Configuring project..."):
        # Pasar create_module_structure=False cuando no se quiere estructura completa
        init_pypackage(
            cwd=cwd, 
            pkg_type=type, 
            name=name, 
            globaldeps=globaldeps, 
            pyproject_use=pyproject,
            create_module_structure=create_full_structure  # ← Nuevo parámetro
        )
    
    if create_full_structure:
        console.print(f"[green]Project created at {target}")
        console.print("\nNext steps:")
        console.print(f"1. cd {name} && pydep install")
        console.print(f"2. cd {name} && pydep run dev")
    else:
        console.print(f"[green]Minimal project '{name}' initialized in current directory")
        console.print("[yellow]Note: Only pypackage.json was created. No additional files or folders were generated.")
        console.print("\nNext steps:")
        console.print("1. pydep install")
        console.print("2. pydep run dev")

@app.command()
def install(
    editable: bool = typer.Option(False, "-e", "--editable", help="Install the current project in editable mode"),
    g: bool = typer.Option(False, "-g", "--global", help="Install into global Python site (no venv) for this command")
):
    """Install the current project or its dependencies."""
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
        temp_pyproject_created = False
        
        try:
            # Generate pyproject.toml in the project root
            if not pyproject_path.exists():
                pkg.to_pyproject(pyproject_path)
                temp_pyproject_created = True
            
            # Install in editable mode
            cmd = [sys.executable, "-m", "pip", "install", "-e", "."]
            if g:
                cmd.insert(1, "--user")
            
            console.print(f"[yellow]Running: {' '.join(cmd)} in {project_dir}")
            
            result = subprocess.run(
                cmd,
                cwd=project_dir,
                check=False,
                capture_output=True,
                text=True
            )
            
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
            # Mantener pyproject.toml para depuración en caso de error
            console.print("[yellow]pyproject.toml kept for debugging purposes")
            raise typer.Exit(1)
            
        finally:
            # Solo eliminar si fue creado por nosotros y la instalación fue exitosa
            if temp_pyproject_created and pyproject_path.exists():
                try:
                    # Verificar que no existe una versión en el directorio de configuración
                    config_pyproject = project_dir / ".pydep" / "pyproject.toml"
                    if not config_pyproject.exists():
                        pyproject_path.unlink()
                        console.print("[green]✓ Temporary pyproject.toml cleaned up")
                except Exception as e:
                    console.print(f"[yellow]Warning: Could not remove temporary pyproject.toml: {e}")
    else:
        # Normal dependency installation
        install_all(str(pkg.path().parent), use_global=g)
        
        # Update versions in pypackage.json
        modified = False
        with console.status("[cyan]Updating package versions in pypackage.json..."):
            # Check main dependencies
            for name, version in pkg.dependencies.items():
                if not version:  # If no version specified
                    ver = get_installed_version(name)
                    if ver:
                        pkg.dependencies[name] = f"=={ver}"
                        modified = True
            
            # Check optional dependencies
            for group, deps in pkg.optionalDependencies.items():
                for name, version in deps.items():
                    if not version:  # If no version specified
                        ver = get_installed_version(name)
                        if ver:
                            deps[name] = f"=={ver}"
                            modified = True
        
        if modified:
            pkg.save()
            console.print("[green]✓ Updated package versions in pypackage.json")
        else:
            console.print("[green]✓ All dependencies are up to date")


@app.command()
def add(
    packages: List[str] = typer.Argument(..., help="Packages to add"),
    g: bool = typer.Option(False, "-g", "--global", help="Install package(s) globally"),
    no_deps: bool = typer.Option(False, "--no-deps", help="Install packages without their dependencies")
):
    """Add one or more dependencies to pypackage.json and install them."""
    if g:
        set_global_deps_override(True)
    try:
        pkg = PyPackage.load()
    except FileNotFoundError:
        console.print("[red]pypackage.json not found. Run 'pydep init'.")
        raise typer.Exit(1)

    parsed = _parse_add_args(packages)
    no_spec = {name for name, spec in parsed if not (spec or "").strip()}
    
    # Update pypackage.json first
    for name, spec in parsed:
        pkg.dependencies[name] = spec or ""
    pkg.save()

    # Prepare requirements for pip
    reqs: list[str] = []
    for name, spec in parsed:
        s = spec.strip()
        if s.startswith("^"):
            # Convert caret to pip compatible
            base = s[1:]
            parts = base.split(".")
            try:
                major = int(parts[0])
                reqs.append(f"{name}>={base},<{major+1}.0.0")
            except (ValueError, IndexError):
                reqs.append(f"{name}{s}")
        else:
            reqs.append(f"{name}{s}" if s else name)

    # Install with pip
    pip_args = ["--upgrade"]
    if no_deps:
        pip_args.append("--no-deps")
    
    with console.status("[cyan]Installing packages..."):
        code = install_packages(pip_args + reqs)
        if code != 0:
            console.print("[red]Error: Could not install packages.")
            console.print("Try one of these solutions:")
            console.print("1. Use --no-deps to install without dependencies")
            console.print("2. Check package names and versions")
            raise typer.Exit(code)

    # Set exact versions for packages without specifier
    modified = False
    if not no_deps:  # Only if installing dependencies
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
def run_cmd(
    script: str = typer.Argument(..., help="Script name defined in pypackage.json"),
    interactive: bool = typer.Option(True, "--interactive/--non-interactive", help="Ask before creating virtual environment")
):
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

    # Asegura venv para comandos python - AÑADIR interactive
    try:
        venv_python = ensure_venv(interactive=interactive)
        if venv_python is None:
            console.print("[yellow]Using system Python instead of virtual environment.")
    except RuntimeError as e:
        console.print(f"[red]Error: {e}")
        raise typer.Exit(1)

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
    
    raise typer.Exit(exit_code)

@app.command()
def build():
    """Build the project (wheel/sdist or executable for app type)."""
    try:
        pkg = PyPackage.load()
    except FileNotFoundError:
        console.print("[red]pypackage.json not found in the current directory")
        raise typer.Exit(1)
    
    # Ensure .pydep directory exists
    config_dir = Path(".pydep")
    config_dir.mkdir(exist_ok=True)
    
    # Generate pyproject.toml in .pydep only if needed
    pyproject_path = None
    if pkg.type == "module" or (pkg.type == "app" and getattr(pkg, 'pyprojectUse', False)):
        pyproject_path = config_dir / "pyproject.toml"
        console.print("[cyan]Generating pyproject.toml in .pydep directory...")
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
    to: str = typer.Option(None, "--to", help="Conversion type: toml or lock"),
    from_format: Optional[str] = typer.Option(
        None, 
        "--from", 
        help="Source format to convert from (toml)"
    ),
    hashes: bool = typer.Option(False, "--hashes/--no-hashes", help="Include sha256 hashes in the lockfile (disabled by default for speed)"),
    outdir: Optional[Path] = typer.Option(None, "--outdir", "-o", help="Output directory for the generated file (default: current directory for lock, .pydepconf for toml)"),
):
    """Convert between different package configuration formats.
    
    By default, converts pypackage.json to pyproject.toml in the current directory.
    Use --from toml to convert from pyproject.toml to pypackage.json.
    """
    # Validate formats
    if from_format and from_format not in ["toml"]:
        console.print("[red]Error: Only 'toml' is supported as source format[/]")
        raise typer.Exit(1)

    if to and to not in ["toml", "lock"]:
        console.print("[red]Error: Only 'toml' or 'lock' are supported as target formats[/]")
        raise typer.Exit(1)

    if from_format == "toml":
        if to == "lock":
            console.print("[red]Error: Cannot convert directly from toml to lock. Please convert to pypackage.json first.[/]")
            raise typer.Exit(1)
        convert_from_toml(outdir)
    elif to:
        convert_to_format(to, hashes, outdir)
    else:
        # Default behavior if no --to or --from is specified
        convert_to_format("toml", hashes, outdir)

def convert_from_toml(outdir: Optional[Path] = None):
    """Convert from pyproject.toml to pypackage.json."""
    import toml
    from datetime import datetime
    import re
    
    console.print("[cyan]Converting from pyproject.toml to pypackage.json...[/]")
    
    # Check if pyproject.toml exists
    toml_path = Path("pyproject.toml")
    if not toml_path.exists():
        console.print("[red]Error: pyproject.toml not found in current directory[/]")
        raise typer.Exit(1)
    
    # Load the TOML content
    try:
        with open(toml_path, "r", encoding="utf-8") as f:
            toml_content = toml.load(f)
    except Exception as e:
        console.print(f"[red]Error reading pyproject.toml: {e}[/]")
        raise typer.Exit(1)
    
    # Create basic pypackage structure
    project = toml_content.get("project", {})
    pkg = {
        "type": "module",  # Default to module type when converting from pyproject.toml
        "name": project.get("name", "my-module"),
        "version": project.get("version", "0.1.0"),
        "description": project.get("description", ""),
        "authors": project.get("authors", [{"name": "PyDepM User"}]),
        "license": project.get("license", "MIT"),
        "dependencies": {},
        "optionalDependencies": {},
        "cli": project.get("scripts", {}),
        "pyproject": {
            "_raw": toml.dumps(toml_content)  # Store original TOML content
        }
    }
    
    def parse_dependency(dep):
        """Parse a dependency string into name and version specifier.
        
        Handles various formats:
        - "package" -> ("package", "")
        - "package>=1.0.0" -> ("package", ">=1.0.0")
        - "package[extra]>=1.0.0" -> ("package[extra]", ">=1.0.0")
        - "git+https://..." -> ("git+https://...", "")
        """
        # Handle git+ URLs and other direct references
        if any(dep.startswith(prefix) for prefix in ["git+", "hg+", "svn+", "bzr+"]):
            return dep, ""
            
        # Handle package with extras: package[extra1,extra2]>=1.0.0
        if "[" in dep and "]" in dep and dep.index("[") < dep.index("]"):
            # Find the end of the extras section
            end_extras = dep.index("]") + 1
            name_part = dep[:end_extras]
            version_part = dep[end_extras:].strip()
            
            # If there's a version part, parse it
            if version_part and version_part[0] in "=<>~!^":
                version = version_part
            else:
                version = ""
            
            return name_part, version
        
        # Handle standard version specifiers
        for op in [">=", "==", ">", "<=", "<", "~=", "!=", "^", "~"]:
            if dep.startswith(op):
                continue  # Skip if the dependency itself starts with an operator
                
            # Use regex to match the operator followed by a version number
            # This handles cases like "package>=1.0.0,<2.0.0"
            match = re.match(fr'^(.+?)({re.escape(op)}[^,;\s]+)(.*)$', dep)
            if match:
                name = match.group(1).strip()
                version = match.group(2).strip()
                rest = match.group(3).strip()
                
                # Handle multiple version specifiers
                if rest and rest[0] == ",":
                    version += rest
                
                return name, version
        
        # If no version specifier found, return the whole string as name
        return dep.strip(), ""
    
    # Convert main dependencies
    for dep in project.get("dependencies", []):
        name, version = parse_dependency(dep)
        if name:  # Only add if we have a valid name
            pkg["dependencies"][name] = version if version else "*"
    
    # Convert optional dependencies
    for group, deps in project.get("optional-dependencies", {}).items():
        pkg["optionalDependencies"][group] = {}
        for dep in deps:
            name, version = parse_dependency(dep)
            if name:  # Only add if we have a valid name
                pkg["optionalDependencies"][group][name] = version if version else "*"
    
    # Process entry points (console_scripts)
    if "project" in toml_content and "entry-points" in toml_content["project"]:
        entry_points = toml_content["project"]["entry-points"]
        if "console_scripts" in entry_points:
            for name, path in entry_points["console_scripts"].items():
                pkg["cli"][name] = path
    
    # Create .old directory if it doesn't exist
    old_dir = Path(".old")
    old_dir.mkdir(exist_ok=True)
    
    # Move pyproject.toml to .old directory with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = old_dir / f"pyproject.toml.{timestamp}"
    toml_path.rename(backup_path)
    console.print(f"[yellow]Moved original pyproject.toml to {backup_path}[/]")
    
    # Write the new pypackage.json
    output_file = Path("pypackage.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(pkg, f, indent=2, ensure_ascii=False)
    
    console.print(f"[green]Successfully created {output_file.absolute()}[/]")

def convert_to_format(to: str, hashes: bool, outdir: Optional[Path] = None):
    """Convert pypackage.json to the specified format."""
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
    
    # For TOML, use the specified output directory or current directory
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
    extended: bool = typer.Option(False, "--extended", help="Also show packages with no known vulnerabilities"),
    interactive: bool = typer.Option(True, "--interactive/--non-interactive", help="Ask before creating virtual environment")
):
    """Audit dependencies using pip-audit and show a concise summary (no --logs required)."""
    try:
        venv_python = ensure_venv(interactive=interactive)
        if venv_python is None:
            console.print("[yellow]Using system Python for audit (no virtual environment).")
    except RuntimeError as e:
        console.print(f"[red]Error: {e}")
        raise typer.Exit(1)
    
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
