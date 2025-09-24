"""
Enhanced Python project scaffolder for Flask and FastAPI with production-ready features.
"""

import os
from pathlib import Path
from rich.console import Console

from ..utils.helpers import create_directory, write_file

console = Console()


class EnhancedPythonScaffolder:
    """Enhanced scaffolder for production-ready Python projects."""
    
    def create_project(self, project_name, output_dir, framework):
        """Create a production-ready Python project."""
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
            "service": "flask-api",
            "version": "1.0.0"
        })
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
'''
        write_file(project_path / "app.py", app_content)
        
        # Create app package structure
        app_dir = project_path / "app"
        create_directory(app_dir)
        create_directory(app_dir / "blueprints")
        create_directory(app_dir / "models")
        create_directory(app_dir / "services")
        create_directory(app_dir / "utils")
        create_directory(app_dir / "tests")
        
        # Create __init__.py files
        write_file(app_dir / "__init__.py", "")
        write_file(app_dir / "blueprints" / "__init__.py", "")
        write_file(app_dir / "models" / "__init__.py", "")
        write_file(app_dir / "services" / "__init__.py", "")
        write_file(app_dir / "utils" / "__init__.py", "")
        write_file(app_dir / "tests" / "__init__.py", "")
        
        # Create comprehensive requirements.txt
        requirements_content = '''Flask==2.3.3
Flask-SQLAlchemy==3.0.5
Flask-Migrate==4.0.5
Flask-JWT-Extended==4.5.3
Flask-CORS==4.0.0
Flask-Limiter==3.5.0
Werkzeug==2.3.7
SQLAlchemy==2.0.21
psycopg2-binary==2.9.7
python-dotenv==1.0.0
gunicorn==21.2.0
pytest==7.4.2
pytest-flask==1.2.0
pytest-cov==4.1.0
black==23.7.0
flake8==6.0.0
mypy==1.5.1
'''
        write_file(project_path / "requirements.txt", requirements_content)
        
        # Create Dockerfile
        dockerfile_content = '''FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update \\
    && apt-get install -y --no-install-recommends \\
        postgresql-client \\
        build-essential \\
        libpq-dev \\
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Create non-root user
RUN adduser --disabled-password --gecos '' appuser
RUN chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 5000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:create_app()"]
'''
        write_file(project_path / "Dockerfile", dockerfile_content)
        
        # Create docker-compose.yml
        docker_compose_content = '''version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=development
      - DATABASE_URL=postgresql://postgres:password@db:5432/flaskapp
    depends_on:
      - db
      - redis
    volumes:
      - .:/app
    command: python app.py

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=flaskapp
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
'''
        write_file(project_path / "docker-compose.yml", docker_compose_content)
        
        console.print(f"[green]✅ Production-ready Flask project '{project_name}' created successfully![/green]")
    
    def _create_fastapi_project(self, project_path, project_name):
        """Create production-ready FastAPI project structure."""
        # Create main application file
        app_content = '''"""
FastAPI application entry point with production-ready features.
"""

import os
import logging
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.security import HTTPBearer
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import redis.asyncio as redis

# Database setup
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///./app.db')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Redis setup
REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

# Security
security = HTTPBearer()

def create_app():
    """Application factory pattern."""
    app = FastAPI(
        title="FastAPI Application",
        description="A production-ready FastAPI application",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )
    
    # Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Configure appropriately for production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=["*"]  # Configure appropriately for production
    )
    
    # Rate limiting
    @app.on_event("startup")
    async def startup():
        redis_client = redis.from_url(REDIS_URL)
        await FastAPILimiter.init(redis_client)
    
    # Database dependency
    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
    
    # Routes
    @app.get("/")
    async def home():
        """Home endpoint."""
        return {
            "message": "Welcome to your FastAPI application!",
            "version": "1.0.0",
            "status": "success"
        }
    
    @app.get("/api/health")
    async def health():
        """Health check endpoint."""
        return {
            "status": "healthy",
            "service": "fastapi-app",
            "version": "1.0.0"
        }
    
    return app

# Create app instance
app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
'''
        write_file(project_path / "main.py", app_content)
        
        # Create requirements.txt for FastAPI
        requirements_content = '''fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.21
alembic==1.12.1
psycopg2-binary==2.9.7
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
fastapi-limiter==0.1.1
redis==5.0.1
pytest==7.4.2
pytest-asyncio==0.21.1
httpx==0.25.2
black==23.7.0
flake8==6.0.0
mypy==1.5.1
'''
        write_file(project_path / "requirements.txt", requirements_content)
        
        console.print(f"[green]✅ Production-ready FastAPI project '{project_name}' created successfully![/green]")
