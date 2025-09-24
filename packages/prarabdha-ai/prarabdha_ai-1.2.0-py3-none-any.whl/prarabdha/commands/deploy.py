"""
Deploy command implementation.
"""

import os
import sys
import subprocess
from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.text import Text

console = Console()


def deploy_command(project_path, service=None):
    """
    Deploy project to a free backend-as-a-service offering.
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
        
        # Select deployment service if not provided
        if not service:
            service = select_deployment_service()
        
        # Deploy based on service
        if service == "heroku":
            deploy_to_heroku(project_path, project_type)
        elif service == "railway":
            deploy_to_railway(project_path, project_type)
        elif service == "render":
            deploy_to_render(project_path, project_type)
        else:
            console.print(f"[red]Error: Unsupported deployment service '{service}'.[/red]")
            sys.exit(1)
            
    except KeyboardInterrupt:
        console.print("\n[yellow]Deployment cancelled by user.[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]Error during deployment: {str(e)}[/red]")
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


def select_deployment_service():
    """Select deployment service."""
    console.print("\n[bold blue]Select a deployment service:[/bold blue]")
    
    services = ["Heroku", "Railway", "Render"]
    
    for i, service in enumerate(services, 1):
        console.print(f"  {i}. {service}")
    
    while True:
        try:
            choice = int(Prompt.ask("\nEnter your choice", default="1"))
            if 1 <= choice <= len(services):
                return services[choice - 1].lower()
            else:
                console.print("[red]Invalid choice. Please try again.[/red]")
        except ValueError:
            console.print("[red]Please enter a valid number.[/red]")


def deploy_to_heroku(project_path, project_type):
    """Deploy to Heroku."""
    console.print("\n[bold blue]Deploying to Heroku...[/bold blue]")
    
    # Check if Heroku CLI is installed
    try:
        subprocess.run(["heroku", "--version"], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        console.print("[red]Error: Heroku CLI is not installed. Please install it from https://devcenter.heroku.com/articles/heroku-cli[/red]")
        return
    
    # Get app name
    app_name = Prompt.ask("Enter Heroku app name (or press Enter for auto-generated)")
    
    # Create Heroku app
    if app_name:
        cmd = ["heroku", "create", app_name]
    else:
        cmd = ["heroku", "create"]
    
    try:
        result = subprocess.run(cmd, cwd=project_path, check=True, capture_output=True, text=True)
        console.print(f"[green]✅ Heroku app created successfully![/green]")
        console.print(result.stdout)
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error creating Heroku app: {e.stderr}[/red]")
        return
    
    # Create Procfile if needed
    if project_type == "python":
        create_procfile(project_path, "python")
    elif project_type == "nodejs":
        create_procfile(project_path, "nodejs")
    
    # Deploy
    try:
        subprocess.run(["git", "add", "."], cwd=project_path, check=True)
        subprocess.run(["git", "commit", "-m", "Deploy to Heroku"], cwd=project_path, check=True)
        subprocess.run(["git", "push", "heroku", "main"], cwd=project_path, check=True)
        console.print("[green]✅ Deployment successful![/green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error during deployment: {e}[/red]")


def deploy_to_railway(project_path, project_type):
    """Deploy to Railway."""
    console.print("\n[bold blue]Deploying to Railway...[/bold blue]")
    
    # Check if Railway CLI is installed
    try:
        subprocess.run(["railway", "--version"], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        console.print("[red]Error: Railway CLI is not installed. Please install it from https://docs.railway.app/develop/cli[/red]")
        return
    
    # Login to Railway
    try:
        subprocess.run(["railway", "login"], cwd=project_path, check=True)
    except subprocess.CalledProcessError:
        console.print("[red]Error: Failed to login to Railway. Please try again.[/red]")
        return
    
    # Initialize Railway project
    try:
        subprocess.run(["railway", "init"], cwd=project_path, check=True)
        console.print("[green]✅ Railway project initialized![/green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error initializing Railway project: {e}[/red]")
        return
    
    # Deploy
    try:
        subprocess.run(["railway", "up"], cwd=project_path, check=True)
        console.print("[green]✅ Deployment successful![/green]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error during deployment: {e}[/red]")


def deploy_to_render(project_path, project_type):
    """Deploy to Render."""
    console.print("\n[bold blue]Deploying to Render...[/bold blue]")
    
    console.print("[yellow]Render deployment requires manual setup through their web interface.[/yellow]")
    console.print("\n[bold]Steps to deploy to Render:[/bold]")
    console.print("1. Go to https://render.com")
    console.print("2. Sign up or log in")
    console.print("3. Click 'New +' and select 'Web Service'")
    console.print("4. Connect your GitHub repository")
    console.print("5. Configure build and start commands based on your project type:")
    
    if project_type == "python":
        console.print("   - Build Command: pip install -r requirements.txt")
        console.print("   - Start Command: python app.py (or gunicorn app:app)")
    elif project_type == "nodejs":
        console.print("   - Build Command: npm install")
        console.print("   - Start Command: npm start")
    elif project_type == "java":
        console.print("   - Build Command: mvn clean package")
        console.print("   - Start Command: java -jar target/*.jar")
    
    console.print("\n[green]✅ Follow the steps above to complete your Render deployment![/green]")


def create_procfile(project_path, project_type):
    """Create Procfile for Heroku deployment."""
    if project_type == "python":
        if (project_path / "app.py").exists():
            procfile_content = "web: python app.py"
        elif (project_path / "main.py").exists():
            procfile_content = "web: python main.py"
        else:
            procfile_content = "web: gunicorn app:app"
    elif project_type == "nodejs":
        procfile_content = "web: npm start"
    else:
        return
    
    with open(project_path / "Procfile", "w") as f:
        f.write(procfile_content)
    
    console.print("[green]✅ Procfile created![/green]")
