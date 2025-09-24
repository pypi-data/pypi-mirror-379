"""
Start command implementation.
"""

import os
import sys
from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.text import Text

from ..scaffolders.python_scaffolder import PythonScaffolder
from ..scaffolders.java_scaffolder import JavaScaffolder
from ..scaffolders.nodejs_scaffolder import NodeJSScaffolder
from ..utils.helpers import (
    get_project_name, 
    get_output_directory, 
    display_success_message,
    display_error_message
)

console = Console()


def start_command(project_name=None, output_dir=None):
    """
    Start the interactive menu to scaffold a new backend service.
    """
    try:
        # Get project name if not provided
        if not project_name:
            project_name = get_project_name()
        
        # Get output directory if not provided
        if not output_dir:
            output_dir = get_output_directory()
        
        # Display language selection menu
        language = select_language()
        
        # Create project based on selected language
        if language == "Python":
            create_python_project(project_name, output_dir)
        elif language == "Java":
            create_java_project(project_name, output_dir)
        elif language == "Node.js":
            create_nodejs_project(project_name, output_dir)
        
    except KeyboardInterrupt:
        console.print("\n[yellow]Operation cancelled by user.[/yellow]")
        sys.exit(0)
    except Exception as e:
        display_error_message(str(e))
        sys.exit(1)


def select_language():
    """Display language selection menu."""
    console.print("\n[bold blue]Select a programming language:[/bold blue]")
    
    languages = ["Python", "Java", "Node.js"]
    
    for i, lang in enumerate(languages, 1):
        console.print(f"  {i}. {lang}")
    
    while True:
        try:
            choice = int(Prompt.ask("\nEnter your choice", default="1"))
            if 1 <= choice <= len(languages):
                return languages[choice - 1]
            else:
                console.print("[red]Invalid choice. Please try again.[/red]")
        except ValueError:
            console.print("[red]Please enter a valid number.[/red]")


def create_python_project(project_name, output_dir):
    """Create Python project with framework selection."""
    console.print("\n[bold blue]Select a Python framework:[/bold blue]")
    
    frameworks = ["Flask", "FastAPI"]
    
    for i, framework in enumerate(frameworks, 1):
        console.print(f"  {i}. {framework}")
    
    while True:
        try:
            choice = int(Prompt.ask("\nEnter your choice", default="1"))
            if 1 <= choice <= len(frameworks):
                framework = frameworks[choice - 1]
                break
            else:
                console.print("[red]Invalid choice. Please try again.[/red]")
        except ValueError:
            console.print("[red]Please enter a valid number.[/red]")
    
    # Create project
    scaffolder = PythonScaffolder()
    project_path = scaffolder.create_project(project_name, output_dir, framework)
    display_success_message(project_name, project_path)


def create_java_project(project_name, output_dir):
    """Create Java project."""
    scaffolder = JavaScaffolder()
    project_path = scaffolder.create_project(project_name, output_dir)
    display_success_message(project_name, project_path)


def create_nodejs_project(project_name, output_dir):
    """Create Node.js project."""
    scaffolder = NodeJSScaffolder()
    project_path = scaffolder.create_project(project_name, output_dir)
    display_success_message(project_name, project_path)
