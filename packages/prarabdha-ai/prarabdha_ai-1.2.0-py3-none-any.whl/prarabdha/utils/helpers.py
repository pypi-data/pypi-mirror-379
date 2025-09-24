"""
Helper utilities for prarabdha CLI.
"""

import os
import sys
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def display_banner():
    """Display the prarabdha banner."""
    banner_text = Text("🚀 Prarabdha", style="bold blue")
    banner_text.append("\nBackend Service Scaffolding Tool", style="italic")
    
    panel = Panel(
        banner_text,
        border_style="blue",
        padding=(1, 2)
    )
    console.print(panel)


def get_project_name():
    """Get project name from user input."""
    while True:
        name = console.input("\n[bold blue]Enter project name:[/bold blue] ").strip()
        if name:
            # Validate project name
            if name.replace('-', '').replace('_', '').isalnum():
                return name
            else:
                console.print("[red]Project name can only contain letters, numbers, hyphens, and underscores.[/red]")
        else:
            console.print("[red]Project name cannot be empty.[/red]")


def get_output_directory():
    """Get output directory from user input."""
    while True:
        output_dir = console.input("\n[bold blue]Enter output directory (press Enter for current directory):[/bold blue] ").strip()
        if not output_dir:
            return os.getcwd()
        
        output_path = Path(output_dir)
        if output_path.exists() and output_path.is_dir():
            return str(output_path.absolute())
        else:
            console.print(f"[red]Directory '{output_dir}' does not exist.[/red]")


def create_directory(path):
    """Create directory if it doesn't exist."""
    Path(path).mkdir(parents=True, exist_ok=True)


def write_file(file_path, content):
    """Write content to file."""
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def display_success_message(project_name, project_path):
    """Display success message after project creation."""
    success_text = Text(f"✅ Project '{project_name}' created successfully!", style="bold green")
    success_text.append(f"\n📁 Location: {project_path}")
    success_text.append("\n\n🚀 Next steps:")
    success_text.append("\n   • Navigate to your project directory")
    success_text.append("\n   • Install dependencies")
    success_text.append("\n   • Run your project")
    
    panel = Panel(
        success_text,
        border_style="green",
        padding=(1, 2)
    )
    console.print(panel)


def display_error_message(message):
    """Display error message."""
    error_text = Text(f"❌ Error: {message}", style="bold red")
    panel = Panel(
        error_text,
        border_style="red",
        padding=(1, 2)
    )
    console.print(panel)
