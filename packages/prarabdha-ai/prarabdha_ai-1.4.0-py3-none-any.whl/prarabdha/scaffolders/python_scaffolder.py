"""
Python project scaffolder for Flask and FastAPI.
"""

import os
from pathlib import Path
from rich.console import Console

from ..utils.helpers import create_directory, write_file

console = Console()


class PythonScaffolder:
    """Scaffolder for Python projects."""
    
    def create_project(self, project_name, output_dir, framework):
        """Create a Python project with the specified framework."""
        project_path = Path(output_dir) / project_name
        create_directory(project_path)
        
        if framework == "Flask":
            self._create_flask_project(project_path, project_name)
        elif framework == "FastAPI":
            self._create_fastapi_project(project_path, project_name)
        
        return str(project_path)
    
    def _create_flask_project(self, project_path, project_name):
        """Create production-ready Flask project structure."""
        # Create main application file
        app_content = '''"""
Flask application entry point with production-ready features.
"""

import os
import logging
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.exceptions import HTTPException
from datetime import timedelta
import os

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

def create_app():
    """Application factory pattern."""
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'jwt-secret-string')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    limiter.init_app(app)
    CORS(app)
    
    # Configure logging
    if not app.debug:
        logging.basicConfig(level=logging.INFO)
    
    # Register blueprints
    from app.blueprints.auth import auth_bp
    from app.blueprints.users import users_bp
    from app.blueprints.api import api_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    
    # Error handlers
    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        return jsonify({
            'error': e.name,
            'message': e.description,
            'status_code': e.code
        }), e.code
    
    @app.errorhandler(429)
    def handle_rate_limit(e):
        return jsonify({
            'error': 'Rate limit exceeded',
            'message': 'Too many requests',
            'status_code': 429
        }), 429
    
    @app.route('/')
    def home():
        """Home endpoint."""
        return jsonify({
            "message": "Welcome to your Flask API!",
            "version": "1.0.0",
            "status": "success"
        })
    
    @app.route('/api/health')
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "service": "flask-api"
    })

@app.route('/api/echo', methods=['POST'])
def echo():
    """Echo endpoint for testing."""
    data = request.get_json()
    return jsonify({
        "message": "Echo successful",
        "data": data
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
'''
        
        write_file(project_path / "app.py", app_content)
        
        # Create requirements.txt
        requirements_content = '''Flask==2.3.3
Flask-CORS==4.0.0
python-dotenv==1.0.0
gunicorn==21.2.0
'''
        write_file(project_path / "requirements.txt", requirements_content)
        
        # Create .env file
        env_content = '''FLASK_APP=app.py
FLASK_ENV=development
PORT=5000
'''
        write_file(project_path / ".env", env_content)
        
        # Create .gitignore
        gitignore_content = '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
'''
        write_file(project_path / ".gitignore", gitignore_content)
        
        # Create README.md
        readme_content = f'''# {project_name}

A Flask API project created with Prarabdha.

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# On Windows
venv\\Scripts\\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
python app.py
```

The API will be available at `http://localhost:5000`

### API Endpoints

- `GET /` - Welcome message
- `GET /api/health` - Health check
- `POST /api/echo` - Echo endpoint for testing

### Development

To run in development mode:
```bash
export FLASK_ENV=development
python app.py
```

### Production

To run in production:
```bash
gunicorn app:app
```
'''
        write_file(project_path / "README.md", readme_content)
        
        console.print(f"[green]✅ Flask project '{project_name}' created successfully![/green]")
    
    def _create_fastapi_project(self, project_path, project_name):
        """Create FastAPI project structure."""
        # Create main application file
        app_content = '''"""
FastAPI application entry point.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(
    title="FastAPI Application",
    description="A FastAPI application created with Prarabdha",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EchoRequest(BaseModel):
    message: str
    data: Dict[str, Any] = {}

@app.get("/")
async def home():
    """Home endpoint."""
    return {
        "message": "Welcome to your FastAPI API!",
        "status": "success"
    }

@app.get("/api/health")
async def health():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "fastapi-api"
    }

@app.post("/api/echo")
async def echo(request: EchoRequest):
    """Echo endpoint for testing."""
    return {
        "message": "Echo successful",
        "data": request.dict()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
'''
        
        write_file(project_path / "main.py", app_content)
        
        # Create requirements.txt
        requirements_content = '''fastapi==0.104.1
uvicorn[standard]==0.24.0
python-dotenv==1.0.0
pydantic==2.5.0
'''
        write_file(project_path / "requirements.txt", requirements_content)
        
        # Create .env file
        env_content = '''PORT=8000
HOST=0.0.0.0
'''
        write_file(project_path / ".env", env_content)
        
        # Create .gitignore
        gitignore_content = '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
'''
        write_file(project_path / ".gitignore", gitignore_content)
        
        # Create README.md
        readme_content = f'''# {project_name}

A FastAPI application created with Prarabdha.

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# On Windows
venv\\Scripts\\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
python main.py
```

The API will be available at `http://localhost:8000`

### API Documentation

- Interactive API docs: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

### API Endpoints

- `GET /` - Welcome message
- `GET /api/health` - Health check
- `POST /api/echo` - Echo endpoint for testing

### Development

To run in development mode:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production

To run in production:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
'''
        write_file(project_path / "README.md", readme_content)
        
        console.print(f"[green]✅ FastAPI project '{project_name}' created successfully![/green]")
