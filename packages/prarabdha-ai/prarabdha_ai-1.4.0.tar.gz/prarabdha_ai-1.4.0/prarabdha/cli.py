#!/usr/bin/env python3
"""
Main CLI interface for prarabdha.
"""

import click
import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from .commands.start import start_command
from .commands.deploy import deploy_command
from .commands.stop import stop_command
from .utils.helpers import display_banner

console = Console()


@click.group()
@click.version_option(version="1.0.0", prog_name="prarabdha")
def main():
    """
    Prarabdha - A CLI tool for scaffolding backend services.
    
    Get started with: prarabdha start
    """
    display_banner()


@main.command()
@click.option('--project-name', '-n', help='Name of the project')
@click.option('--output-dir', '-o', help='Output directory for the project')
def start(project_name, output_dir):
    """
    Start the interactive menu to scaffold a new backend service.
    """
    start_command(project_name, output_dir)


@main.command()
@click.argument('project_path')
@click.option('--service', '-s', help='Deployment service (heroku, railway, render)')
def deploy(project_path, service):
    """
    Deploy your project to a free backend-as-a-service offering.
    """
    deploy_command(project_path, service)


@main.command()
@click.argument('project_path')
def stop(project_path):
    """
    Stop a running project.
    """
    stop_command(project_path)


if __name__ == '__main__':
    main()
