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
    Start the interactive menu to scaffold a new service.
    """
    try:
        # Use current directory as default
        output_dir = output_dir or os.getcwd()
        
        # Display infrastructure selection menu
        infrastructure = select_infrastructure()
        
        if infrastructure == "Frontend":
            create_frontend_project(output_dir)
        elif infrastructure == "Backend":
            create_backend_project(output_dir)
        
    except KeyboardInterrupt:
        console.print("\n[yellow]Operation cancelled by user.[/yellow]")
        sys.exit(0)
    except Exception as e:
        display_error_message(str(e))
        sys.exit(1)


def select_infrastructure():
    """Display infrastructure selection menu."""
    console.print("\n[bold blue]Select infrastructure type:[/bold blue]")
    
    infrastructures = ["Frontend", "Backend"]
    
    for i, infra in enumerate(infrastructures, 1):
        console.print(f"  {i}. {infra}")
    
    while True:
        try:
            choice = int(Prompt.ask("\nEnter your choice", default="2"))
            if 1 <= choice <= len(infrastructures):
                return infrastructures[choice - 1]
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
    
    # Create project
    if framework == "React":
        create_react_project(project_name, output_dir)
    elif framework == "Next.js":
        create_nextjs_project(project_name, output_dir)


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
    
    # Create project based on selected language
    if language == "Python":
        create_python_project(project_name, output_dir)
    elif language == "Java":
        create_java_project(project_name, output_dir)
    elif language == "Node.js":
        create_nodejs_project(project_name, output_dir)


def create_nodejs_project(project_name, output_dir):
    """Create Node.js project."""
    scaffolder = NodeJSScaffolder()
    project_path = scaffolder.create_project(project_name, output_dir)
    display_success_message(project_name, project_path)


def create_react_project(project_name, output_dir):
    """Create React project."""
    # For now, create a basic React project structure
    project_path = Path(output_dir) / project_name
    create_directory(project_path)
    
    # Create basic React project files
    package_json = {
        "name": project_name,
        "version": "1.0.0",
        "description": "A React application created with Prarabdha",
        "main": "src/index.js",
        "scripts": {
            "start": "react-scripts start",
            "build": "react-scripts build",
            "test": "react-scripts test",
            "eject": "react-scripts eject"
        },
        "dependencies": {
            "react": "^18.2.0",
            "react-dom": "^18.2.0",
            "react-scripts": "5.0.1"
        },
        "browserslist": {
            "production": [">0.2%", "not dead", "not op_mini all"],
            "development": ["last 1 chrome version", "last 1 firefox version", "last 1 safari version"]
        }
    }
    
    write_file(project_path / "package.json", json.dumps(package_json, indent=2))
    
    # Create src directory and basic files
    src_dir = project_path / "src"
    create_directory(src_dir)
    
    # Create App.js
    app_content = '''import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to React!</h1>
        <p>Your React app is ready to go.</p>
      </header>
    </div>
  );
}

export default App;
'''
    write_file(src_dir / "App.js", app_content)
    
    # Create index.js
    index_content = '''import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
'''
    write_file(src_dir / "index.js", index_content)
    
    # Create public directory
    public_dir = project_path / "public"
    create_directory(public_dir)
    
    # Create index.html
    html_content = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>React App</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
'''
    write_file(public_dir / "index.html", html_content)
    
    console.print(f"[green]✅ React project '{project_name}' created successfully![/green]")
    display_success_message(project_name, str(project_path))


def create_nextjs_project(project_name, output_dir):
    """Create Next.js project."""
    # For now, create a basic Next.js project structure
    project_path = Path(output_dir) / project_name
    create_directory(project_path)
    
    # Create package.json
    package_json = {
        "name": project_name,
        "version": "1.0.0",
        "description": "A Next.js application created with Prarabdha",
        "scripts": {
            "dev": "next dev",
            "build": "next build",
            "start": "next start",
            "lint": "next lint"
        },
        "dependencies": {
            "next": "^14.0.0",
            "react": "^18.2.0",
            "react-dom": "^18.2.0"
        },
        "devDependencies": {
            "eslint": "^8.0.0",
            "eslint-config-next": "^14.0.0"
        }
    }
    
    write_file(project_path / "package.json", json.dumps(package_json, indent=2))
    
    # Create pages directory
    pages_dir = project_path / "pages"
    create_directory(pages_dir)
    
    # Create index.js
    index_content = '''import Head from 'next/head'

export default function Home() {
  return (
    <div>
      <Head>
        <title>Next.js App</title>
        <meta name="description" content="Generated by Next.js" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <h1>Welcome to Next.js!</h1>
        <p>Your Next.js app is ready to go.</p>
      </main>
    </div>
  )
}
'''
    write_file(pages_dir / "index.js", index_content)
    
    # Create next.config.js
    next_config = '''/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
}

module.exports = nextConfig
'''
    write_file(project_path / "next.config.js", next_config)
    
    console.print(f"[green]✅ Next.js project '{project_name}' created successfully![/green]")
    display_success_message(project_name, str(project_path))
