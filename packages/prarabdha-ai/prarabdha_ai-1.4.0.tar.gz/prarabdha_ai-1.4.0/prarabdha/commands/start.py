"""
Start command implementation.
"""

import os
import sys
import json
from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.text import Text

from ..scaffolders.generic_scaffolder import GenericScaffolder
from ..utils.helpers import (
    get_project_name, 
    get_output_directory, 
    display_success_message,
    display_error_message,
    create_directory,
    write_file
)

console = Console()


def start_command(project_name=None, output_dir=None):
    """Start the interactive menu to scaffold a new project."""
    # Use current directory as default
    if output_dir is None:
        output_dir = os.getcwd()
    
    # Start with infrastructure selection
    select_infrastructure(output_dir)


def select_infrastructure(output_dir):
    """Select infrastructure type (Frontend/Backend)."""
    console.print("\n[bold blue]Select infrastructure type:[/bold blue]")
    console.print("  1. Frontend")
    console.print("  2. Backend")
    
    while True:
        try:
            choice = int(Prompt.ask("\nEnter your choice", default="2"))
            if choice == 1:
                create_frontend_project(output_dir)
                break
            elif choice == 2:
                create_backend_project(output_dir)
                break
            else:
                console.print("[red]Invalid choice. Please try again.[/red]")
        except ValueError:
            console.print("[red]Please enter a valid number.[/red]")


def create_frontend_project(output_dir):
    """Create frontend project with framework selection."""
    console.print("\n[bold blue]Select a frontend framework:[/bold blue]")
    
    frameworks = ["React", "Next.js"]
    
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
    
    # Auto-generate project name
    project_name = f"frontend-{framework.lower().replace('.', '')}"
    
    # Create project using GenericScaffolder
    scaffolder = GenericScaffolder()
    project_path = scaffolder.create_project(project_name, output_dir, "frontend", framework)
    display_success_message(project_name, project_path)


def create_backend_project(output_dir):
    """Create backend project with language selection."""
    console.print("\n[bold blue]Select a backend language:[/bold blue]")
    
    languages = ["Python", "Java", "Node.js"]
    
    for i, lang in enumerate(languages, 1):
        console.print(f"  {i}. {lang}")
    
    while True:
        try:
            choice = int(Prompt.ask("\nEnter your choice", default="1"))
            if 1 <= choice <= len(languages):
                language = languages[choice - 1]
                break
            else:
                console.print("[red]Invalid choice. Please try again.[/red]")
        except ValueError:
            console.print("[red]Please enter a valid number.[/red]")
    
    # Auto-generate project name
    project_name = f"backend-{language.lower().replace('.', '')}"
    
    # Create project using GenericScaffolder
    scaffolder = GenericScaffolder()
    project_path = scaffolder.create_project(project_name, output_dir, "backend", language)
    display_success_message(project_name, project_path)