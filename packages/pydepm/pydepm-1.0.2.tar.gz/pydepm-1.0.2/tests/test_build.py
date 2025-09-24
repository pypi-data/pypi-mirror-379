import os
import sys
import json
import shutil
from pathlib import Path
import pytest
from unittest.mock import patch, MagicMock

from pydm.config import PyPackage
from pydm.cli import app

# Add the parent directory to the path so we can import from the package
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_build_module(tmp_path, monkeypatch):
    """Test building a module project."""
    # Create a test module project
    os.chdir(tmp_path)
    
    # Initialize a module project
    result = app.invoke(["init", "--type", "module", "--name", "test-module"])
    assert result.exit_code == 0
    
    # Create a simple module
    (tmp_path / "src" / "test_module").mkdir(parents=True)
    (tmp_path / "src" / "test_module" / "__init__.py").write_text("def hello(): return 'world'")
    
    # Mock the build module to avoid actual builds during testing
    with patch('pydm.cli.run_module') as mock_run_module:
        mock_run_module.return_value = 0
        result = app.invoke(["build"])
        
    assert result.exit_code == 0
    mock_run_module.assert_called_once_with("build", force_stream=True)


def test_build_app_with_executable(tmp_path, monkeypatch):
    """Test building an app project with executable configuration."""
    # Create a test app project
    os.chdir(tmp_path)
    
    # Initialize an app project
    result = app.invoke(["init", "--type", "app", "--name", "test-app"])
    assert result.exit_code == 0
    
    # Create a simple main.py
    (tmp_path / "main.py").write_text("print('Hello, World!')")
    
    # Update pypackage.json with executable config
    pkg = PyPackage.load()
    pkg.executable = {
        "target": "main.py",
        "parameters": ["--onefile"],
        "output": "dist/executable"
    }
    pkg.save()
    
    # Mock subprocess.run to avoid actual PyInstaller execution
    mock_run = MagicMock()
    mock_run.returncode = 0
    
    with patch('subprocess.run', return_value=mock_run) as mock_subprocess_run:
        result = app.invoke(["build"])
        
    assert result.exit_code == 0
    mock_subprocess_run.assert_called_once()
    
    # Check that the command includes our parameters
    cmd = mock_subprocess_run.call_args[0][0]
    assert "pyinstaller" in cmd[0]
    assert "--onefile" in cmd
    assert "--distpath" in cmd
    assert "dist/executable" in cmd
    assert "main.py" in cmd


def test_build_app_missing_target(tmp_path, capsys):
    """Test building an app with a missing target file."""
    # Create a test app project
    os.chdir(tmp_path)
    
    # Initialize an app project
    result = app.invoke(["init", "--type", "app", "--name", "test-app"])
    assert result.exit_code == 0
    
    # Update pypackage.json with executable config pointing to non-existent file
    pkg = PyPackage.load()
    pkg.executable = {
        "target": "non_existent.py",
        "parameters": ["--onefile"],
        "output": "dist/executable"
    }
    pkg.save()
    
    # Run the build command
    result = app.invoke(["build"])
    
    # Should fail because target file doesn't exist
    assert result.exit_code == 1
    captured = capsys.readouterr()
    assert "Target file not found" in captured.err
