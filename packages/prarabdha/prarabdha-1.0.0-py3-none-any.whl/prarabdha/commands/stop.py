"""
Stop command implementation.
"""

import os
import sys
import signal
import subprocess
import psutil
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def stop_command(project_path):
    """
    Stop a running project.
    """
    try:
        project_path = Path(project_path).resolve()
        
        if not project_path.exists():
            console.print(f"[red]Error: Project path '{project_path}' does not exist.[/red]")
            sys.exit(1)
        
        # Detect project type
        project_type = detect_project_type(project_path)
        
        if not project_type:
            console.print("[red]Error: Could not detect project type. Make sure you're in a valid project directory.[/red]")
            sys.exit(1)
        
        # Stop the project
        stop_project(project_path, project_type)
        
    except KeyboardInterrupt:
        console.print("\n[yellow]Operation cancelled by user.[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]Error stopping project: {str(e)}[/red]")
        sys.exit(1)


def detect_project_type(project_path):
    """Detect the type of project (Python, Java, Node.js)."""
    if (project_path / "requirements.txt").exists() or (project_path / "app.py").exists() or (project_path / "main.py").exists():
        return "python"
    elif (project_path / "pom.xml").exists():
        return "java"
    elif (project_path / "package.json").exists():
        return "nodejs"
    return None


def stop_project(project_path, project_type):
    """Stop the running project."""
    console.print(f"\n[bold blue]Stopping {project_type} project...[/bold blue]")
    
    # Find and kill processes
    killed_processes = []
    
    if project_type == "python":
        killed_processes = kill_python_processes(project_path)
    elif project_type == "java":
        killed_processes = kill_java_processes(project_path)
    elif project_type == "nodejs":
        killed_processes = kill_nodejs_processes(project_path)
    
    if killed_processes:
        console.print(f"[green]✅ Stopped {len(killed_processes)} process(es)[/green]")
        for process in killed_processes:
            console.print(f"  - PID {process.pid}: {process.name()}")
    else:
        console.print("[yellow]No running processes found for this project.[/yellow]")


def kill_python_processes(project_path):
    """Kill Python processes related to the project."""
    killed_processes = []
    
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['name'] and 'python' in proc.info['name'].lower():
                cmdline = proc.info['cmdline']
                if cmdline and any(str(project_path) in ' '.join(cmdline) for cmd in cmdline):
                    proc.terminate()
                    killed_processes.append(proc)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    return killed_processes


def kill_java_processes(project_path):
    """Kill Java processes related to the project."""
    killed_processes = []
    
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['name'] and 'java' in proc.info['name'].lower():
                cmdline = proc.info['cmdline']
                if cmdline and any(str(project_path) in ' '.join(cmdline) for cmd in cmdline):
                    proc.terminate()
                    killed_processes.append(proc)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    return killed_processes


def kill_nodejs_processes(project_path):
    """Kill Node.js processes related to the project."""
    killed_processes = []
    
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['name'] and 'node' in proc.info['name'].lower():
                cmdline = proc.info['cmdline']
                if cmdline and any(str(project_path) in ' '.join(cmdline) for cmd in cmdline):
                    proc.terminate()
                    killed_processes.append(proc)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    return killed_processes


def stop_by_port(port):
    """Stop processes running on a specific port."""
    killed_processes = []
    
    for proc in psutil.process_iter(['pid', 'name', 'connections']):
        try:
            connections = proc.info['connections']
            if connections:
                for conn in connections:
                    if conn.laddr.port == port:
                        proc.terminate()
                        killed_processes.append(proc)
                        break
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    return killed_processes
