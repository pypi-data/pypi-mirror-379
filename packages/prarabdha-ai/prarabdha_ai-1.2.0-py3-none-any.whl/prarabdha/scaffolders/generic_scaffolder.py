"""
Generic scaffolder that creates projects with the standard folder structure.
"""

import os
from pathlib import Path
from rich.console import Console

from ..utils.helpers import create_directory, write_file

console = Console()


class GenericScaffolder:
    """Generic scaffolder for all project types with standard folder structure."""
    
    def create_project(self, project_name, output_dir, project_type, framework):
        """Create a project with the generic folder structure."""
        project_path = Path(output_dir) / project_name
        create_directory(project_path)
        
        # Create root-level directories
        create_directory(project_path / "backend")
        create_directory(project_path / "frontend")
        create_directory(project_path / "scripts")
        create_directory(project_path / "docs")
        
        # Create backend structure
        self._create_backend_structure(project_path, framework)
        
        # Create frontend structure
        self._create_frontend_structure(project_path, framework)
        
        # Create root-level files
        self._create_root_files(project_path, project_name)
        
        return str(project_path)
    
    def _create_backend_structure(self, project_path, framework):
        """Create backend directory structure."""
        backend_dir = project_path / "backend"
        
        # Create backend subdirectories
        create_directory(backend_dir / "src")
        create_directory(backend_dir / "tests")
        
        # Create src subdirectories
        src_dir = backend_dir / "src"
        create_directory(src_dir / "api")
        create_directory(src_dir / "services")
        create_directory(src_dir / "models")
        create_directory(src_dir / "middlewares")
        create_directory(src_dir / "utils")
        create_directory(src_dir / "config")
        
        # Create framework-specific files
        if framework == "Flask":
            self._create_flask_backend(backend_dir, src_dir)
        elif framework == "FastAPI":
            self._create_fastapi_backend(backend_dir, src_dir)
        elif framework == "Spring Boot":
            self._create_spring_boot_backend(backend_dir, src_dir)
        elif framework == "Express":
            self._create_express_backend(backend_dir, src_dir)
    
    def _create_frontend_structure(self, project_path, framework):
        """Create frontend directory structure."""
        frontend_dir = project_path / "frontend"
        
        # Create frontend subdirectories
        create_directory(frontend_dir / "public")
        create_directory(frontend_dir / "src")
        create_directory(frontend_dir / "tests")
        
        # Create src subdirectories
        src_dir = frontend_dir / "src"
        create_directory(src_dir / "components")
        create_directory(src_dir / "pages")
        create_directory(src_dir / "features")
        create_directory(src_dir / "hooks")
        create_directory(src_dir / "services")
        create_directory(src_dir / "store")
        create_directory(src_dir / "utils")
        
        # Create framework-specific files
        if framework == "React":
            self._create_react_frontend(frontend_dir, src_dir)
        elif framework == "Next.js":
            self._create_nextjs_frontend(frontend_dir, src_dir)
    
    def _create_flask_backend(self, backend_dir, src_dir):
        """Create Flask backend with generic structure."""
        # Create main app file
        app_content = '''"""
Flask application with generic folder structure.
"""

from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    """Application factory pattern."""
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'dev-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)
    
    # Import and register blueprints
    from api.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    @app.route('/')
    def home():
        return jsonify({
            "message": "Welcome to your Flask API!",
            "version": "1.0.0",
            "status": "success"
        })
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
'''
        write_file(backend_dir / "src" / "app.py", app_content)
        
        # Create API routes
        api_routes = '''"""
API routes for the Flask application.
"""

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

api_bp = Blueprint('api', __name__)

@api_bp.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "service": "flask-api"
    })

@api_bp.route('/users')
@jwt_required()
def get_users():
    """Get all users."""
    return jsonify({
        "users": [],
        "message": "Users endpoint"
    })
'''
        write_file(backend_dir / "src" / "api" / "routes.py", api_routes)
        
        # Create services
        user_service = '''"""
User service for business logic.
"""

class UserService:
    """User service class."""
    
    @staticmethod
    def get_all_users():
        """Get all users."""
        return []
    
    @staticmethod
    def create_user(user_data):
        """Create a new user."""
        return {"id": 1, **user_data}
    
    @staticmethod
    def get_user_by_id(user_id):
        """Get user by ID."""
        return {"id": user_id, "name": "John Doe"}
'''
        write_file(backend_dir / "src" / "services" / "user_service.py", user_service)
        
        # Create models
        user_model = '''"""
User model for database operations.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User model."""
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    def __repr__(self):
        return f'<User {self.username}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }
'''
        write_file(backend_dir / "src" / "models" / "user.py", user_model)
        
        # Create middlewares
        auth_middleware = '''"""
Authentication middleware.
"""

from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

def require_auth(f):
    """Decorator to require authentication."""
    def decorated_function(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({'error': 'Authentication required'}), 401
    return decorated_function
'''
        write_file(backend_dir / "src" / "middlewares" / "auth.py", auth_middleware)
        
        # Create utils
        utils = '''"""
Utility functions.
"""

import hashlib
from datetime import datetime

def hash_password(password):
    """Hash a password."""
    return hashlib.sha256(password.encode()).hexdigest()

def get_current_timestamp():
    """Get current timestamp."""
    return datetime.utcnow()
'''
        write_file(backend_dir / "src" / "utils" / "helpers.py", utils)
        
        # Create config
        config = '''"""
Configuration settings.
"""

import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-string'

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
'''
        write_file(backend_dir / "src" / "config" / "settings.py", config)
        
        # Create requirements.txt
        requirements = '''Flask==2.3.3
Flask-SQLAlchemy==3.0.5
Flask-Migrate==4.0.5
Flask-JWT-Extended==4.5.3
Flask-CORS==4.0.0
Werkzeug==2.3.7
SQLAlchemy==2.0.21
psycopg2-binary==2.9.7
python-dotenv==1.0.0
gunicorn==21.2.0
pytest==7.4.2
pytest-flask==1.2.0
'''
        write_file(backend_dir / "requirements.txt", requirements)
    
    def _create_fastapi_backend(self, backend_dir, src_dir):
        """Create FastAPI backend with generic structure."""
        # Create main app file
        app_content = '''"""
FastAPI application with generic folder structure.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FastAPI Application",
    description="A production-ready FastAPI application",
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

# Import routes
from api.routes import router
app.include_router(router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to your FastAPI application!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
'''
        write_file(backend_dir / "src" / "main.py", app_content)
        
        # Create API routes
        api_routes = '''"""
API routes for FastAPI application.
"""

from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

@router.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy", "service": "fastapi-app"}

@router.get("/users")
async def get_users():
    """Get all users."""
    return {"users": [], "message": "Users endpoint"}
'''
        write_file(backend_dir / "src" / "api" / "routes.py", api_routes)
        
        # Create requirements.txt
        requirements = '''fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.21
alembic==1.12.1
psycopg2-binary==2.9.7
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
pytest==7.4.2
pytest-asyncio==0.21.1
httpx==0.25.2
'''
        write_file(backend_dir / "requirements.txt", requirements)
    
    def _create_spring_boot_backend(self, backend_dir, src_dir):
        """Create Spring Boot backend with generic structure."""
        # Create main application class
        main_app = '''package com.example.app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
'''
        write_file(backend_dir / "src" / "main" / "java" / "com" / "example" / "app" / "Application.java", main_app)
        
        # Create controller
        controller = '''package com.example.app.api;

import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class ApiController {
    
    @GetMapping("/health")
    public ResponseEntity<Map<String, String>> health() {
        Map<String, String> response = new HashMap<>();
        response.put("status", "healthy");
        response.put("service", "spring-boot-app");
        return ResponseEntity.ok(response);
    }
    
    @GetMapping("/users")
    public ResponseEntity<Map<String, Object>> getUsers() {
        Map<String, Object> response = new HashMap<>();
        response.put("users", new Object[0]);
        response.put("message", "Users endpoint");
        return ResponseEntity.ok(response);
    }
}
'''
        write_file(backend_dir / "src" / "main" / "java" / "com" / "example" / "app" / "api" / "ApiController.java", controller)
        
        # Create service
        user_service = '''package com.example.app.services;

import org.springframework.stereotype.Service;
import java.util.ArrayList;
import java.util.List;

@Service
public class UserService {
    
    public List<String> getAllUsers() {
        return new ArrayList<>();
    }
    
    public String createUser(String userData) {
        return "User created: " + userData;
    }
    
    public String getUserById(Long id) {
        return "User with ID: " + id;
    }
}
'''
        write_file(backend_dir / "src" / "main" / "java" / "com" / "example" / "app" / "services" / "UserService.java", user_service)
        
        # Create model
        user_model = '''package com.example.app.models;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "users")
public class User {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(unique = true, nullable = false)
    private String username;
    
    @Column(unique = true, nullable = false)
    private String email;
    
    @Column(name = "created_at")
    private LocalDateTime createdAt;
    
    // Constructors
    public User() {}
    
    public User(String username, String email) {
        this.username = username;
        this.email = email;
        this.createdAt = LocalDateTime.now();
    }
    
    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    
    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }
    
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
}
'''
        write_file(backend_dir / "src" / "main" / "java" / "com" / "example" / "app" / "models" / "User.java", user_model)
        
        # Create pom.xml
        pom_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.1.0</version>
        <relativePath/>
    </parent>
    
    <groupId>com.example</groupId>
    <artifactId>app</artifactId>
    <version>1.0.0</version>
    <name>app</name>
    <description>Spring Boot Application</description>
    
    <properties>
        <java.version>17</java.version>
    </properties>
    
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-security</artifactId>
        </dependency>
        
        <dependency>
            <groupId>org.postgresql</groupId>
            <artifactId>postgresql</artifactId>
            <scope>runtime</scope>
        </dependency>
        
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>
    
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
'''
        write_file(backend_dir / "pom.xml", pom_xml)
    
    def _create_express_backend(self, backend_dir, src_dir):
        """Create Express.js backend with generic structure."""
        # Create main app file
        app_content = '''const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');

const app = express();

// Middleware
app.use(helmet());
app.use(cors());
app.use(morgan('combined'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
const apiRoutes = require('./api/routes');
app.use('/api', apiRoutes);

// Health check
app.get('/', (req, res) => {
    res.json({
        message: 'Welcome to your Express.js application!',
        version: '1.0.0',
        status: 'success'
    });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

module.exports = app;
'''
        write_file(backend_dir / "src" / "index.js", app_content)
        
        # Create API routes
        api_routes = '''const express = require('express');
const router = express.Router();

// Health check
router.get('/health', (req, res) => {
    res.json({
        status: 'healthy',
        service: 'express-app'
    });
});

// Users endpoint
router.get('/users', (req, res) => {
    res.json({
        users: [],
        message: 'Users endpoint'
    });
});

module.exports = router;
'''
        write_file(backend_dir / "src" / "api" / "routes.js", api_routes)
        
        # Create services
        user_service = '''class UserService {
    constructor() {
        this.users = [];
    }
    
    getAllUsers() {
        return this.users;
    }
    
    createUser(userData) {
        const user = {
            id: Date.now(),
            ...userData,
            createdAt: new Date()
        };
        this.users.push(user);
        return user;
    }
    
    getUserById(id) {
        return this.users.find(user => user.id === id);
    }
}

module.exports = new UserService();
'''
        write_file(backend_dir / "src" / "services" / "userService.js", user_service)
        
        # Create models
        user_model = '''const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    username: {
        type: String,
        required: true,
        unique: true
    },
    email: {
        type: String,
        required: true,
        unique: true
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});

module.exports = mongoose.model('User', userSchema);
'''
        write_file(backend_dir / "src" / "models" / "User.js", user_model)
        
        # Create package.json
        package_json = '''{
    "name": "express-app",
    "version": "1.0.0",
    "description": "Express.js application",
    "main": "src/index.js",
    "scripts": {
        "start": "node src/index.js",
        "dev": "nodemon src/index.js",
        "test": "jest"
    },
    "dependencies": {
        "express": "^4.18.2",
        "cors": "^2.8.5",
        "helmet": "^7.0.0",
        "morgan": "^1.10.0",
        "mongoose": "^7.4.0",
        "jsonwebtoken": "^9.0.1",
        "bcryptjs": "^2.4.3",
        "dotenv": "^16.3.1"
    },
    "devDependencies": {
        "nodemon": "^3.0.1",
        "jest": "^29.6.2",
        "supertest": "^6.3.3"
    }
}
'''
        write_file(backend_dir / "package.json", package_json)
    
    def _create_react_frontend(self, frontend_dir, src_dir):
        """Create React frontend with generic structure."""
        # Create package.json
        package_json = '''{
    "name": "react-app",
    "version": "1.0.0",
    "description": "React application",
    "private": true,
    "scripts": {
        "start": "react-scripts start",
        "build": "react-scripts build",
        "test": "react-scripts test",
        "eject": "react-scripts eject"
    },
    "dependencies": {
        "react": "^18.2.0",
        "react-dom": "^18.2.0",
        "react-router-dom": "^6.8.0",
        "react-redux": "^8.0.5",
        "@reduxjs/toolkit": "^1.9.3",
        "axios": "^1.3.4",
        "styled-components": "^5.3.6"
    },
    "devDependencies": {
        "@types/react": "^18.0.28",
        "@types/react-dom": "^18.0.11",
        "typescript": "^4.9.5",
        "react-scripts": "5.0.1"
    }
}
'''
        write_file(frontend_dir / "package.json", package_json)
        
        # Create main App component
        app_content = '''import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import { store } from './store/store';
import Layout from './components/Layout';
import Home from './pages/Home';
import Dashboard from './pages/Dashboard';

function App() {
  return (
    <Provider store={store}>
      <Router>
        <Layout>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/dashboard" element={<Dashboard />} />
          </Routes>
        </Layout>
      </Router>
    </Provider>
  );
}

export default App;
'''
        write_file(src_dir / "App.tsx", app_content)
        
        # Create index.tsx
        index_content = '''import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
'''
        write_file(src_dir / "index.tsx", index_content)
        
        # Create components
        layout_component = '''import React from 'react';
import styled from 'styled-components';

const LayoutContainer = styled.div`
  min-height: 100vh;
  display: flex;
  flex-direction: column;
`;

const Main = styled.main`
  flex: 1;
  padding: 2rem;
`;

const Layout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return (
    <LayoutContainer>
      <Main>
        {children}
      </Main>
    </LayoutContainer>
  );
};

export default Layout;
'''
        write_file(src_dir / "components" / "Layout.tsx", layout_component)
        
        # Create pages
        home_page = '''import React from 'react';
import styled from 'styled-components';

const Container = styled.div`
  padding: 2rem;
  text-align: center;
`;

const Title = styled.h1`
  color: #333;
  margin-bottom: 1rem;
`;

const Home: React.FC = () => {
  return (
    <Container>
      <Title>Welcome to React App</Title>
      <p>Your React application is ready to go!</p>
    </Container>
  );
};

export default Home;
'''
        write_file(src_dir / "pages" / "Home.tsx", home_page)
        
        # Create store
        store_content = '''import { configureStore } from '@reduxjs/toolkit';
import authReducer from './slices/authSlice';

export const store = configureStore({
  reducer: {
    auth: authReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
'''
        write_file(src_dir / "store" / "store.ts", store_content)
        
        # Create auth slice
        auth_slice = '''import { createSlice } from '@reduxjs/toolkit';

interface AuthState {
  isAuthenticated: boolean;
  user: any | null;
}

const initialState: AuthState = {
  isAuthenticated: false,
  user: null,
};

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    login: (state, action) => {
      state.isAuthenticated = true;
      state.user = action.payload;
    },
    logout: (state) => {
      state.isAuthenticated = false;
      state.user = null;
    },
  },
});

export const { login, logout } = authSlice.actions;
export default authSlice.reducer;
'''
        write_file(src_dir / "store" / "slices" / "authSlice.ts", auth_slice)
        
        # Create services
        api_service = '''import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;
'''
        write_file(src_dir / "services" / "api.ts", api_service)
        
        # Create public/index.html
        html_content = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>
'''
        write_file(frontend_dir / "public" / "index.html", html_content)
    
    def _create_nextjs_frontend(self, frontend_dir, src_dir):
        """Create Next.js frontend with generic structure."""
        # Create package.json
        package_json = '''{
    "name": "nextjs-app",
    "version": "1.0.0",
    "description": "Next.js application",
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
'''
        write_file(frontend_dir / "package.json", package_json)
        
        # Create pages/index.js
        index_page = '''import Head from 'next/head'

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
        write_file(src_dir / "pages" / "index.js", index_page)
        
        # Create next.config.js
        next_config = '''/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
}

module.exports = nextConfig
'''
        write_file(frontend_dir / "next.config.js", next_config)
    
    def _create_root_files(self, project_path, project_name):
        """Create root-level files."""
        # Create .env.example
        env_example = '''# Backend Configuration
BACKEND_URL=http://localhost:5000
DATABASE_URL=postgresql://username:password@localhost:5432/dbname

# Frontend Configuration
REACT_APP_API_URL=http://localhost:5000/api
NEXT_PUBLIC_API_URL=http://localhost:5000/api

# JWT Configuration
JWT_SECRET_KEY=your-jwt-secret-key-here

# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=app_db
DB_USER=postgres
DB_PASSWORD=password
'''
        write_file(project_path / ".env.example", env_example)
        
        # Create .gitignore
        gitignore_content = '''# Dependencies
node_modules/
*/node_modules/

# Production builds
build/
dist/
*/build/
*/dist/

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

# Logs
*.log
logs/

# Runtime data
pids/
*.pid
*.seed
*.pid.lock

# Coverage directory used by tools like istanbul
coverage/
*.lcov

# nyc test coverage
.nyc_output

# Dependency directories
jspm_packages/

# Optional npm cache directory
.npm

# Optional eslint cache
.eslintcache

# Microbundle cache
.rpt2_cache/
.rts2_cache_cjs/
.rts2_cache_es/
.rts2_cache_umd/

# Optional REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# Yarn Integrity file
.yarn-integrity

# parcel-bundler cache (https://parceljs.org/)
.cache
.parcel-cache

# Next.js build output
.next

# Nuxt.js build / generate output
.nuxt
dist

# Gatsby files
.cache/
public

# Storybook build outputs
.out
.storybook-out

# Temporary folders
tmp/
temp/
'''
        write_file(project_path / ".gitignore", gitignore_content)
        
        # Create docker-compose.yml
        docker_compose = '''version: '3.8'

services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/app_db
    depends_on:
      - db
    volumes:
      - ./backend:/app

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - REACT_APP_API_URL=http://localhost:5000/api
    volumes:
      - ./frontend:/app

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=app_db
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
'''
        write_file(project_path / "docker-compose.yml", docker_compose)
        
        # Create comprehensive README
        readme_content = f'''# {project_name}

A full-stack application with modern architecture and best practices.

## 🏗️ Project Structure

```
{project_name}/
├── backend/              # Server-side code
│   ├── src/
│   │   ├── api/          # Routes / Controllers
│   │   ├── services/     # Business logic
│   │   ├── models/       # Database models
│   │   ├── middlewares/  # Auth, logging, validation
│   │   ├── utils/        # Helpers, constants
│   │   ├── config/       # Configuration
│   │   └── index.*       # Entry point
│   ├── tests/            # Backend tests
│   └── requirements.txt  # Python dependencies
│
├── frontend/             # Client-side code
│   ├── public/           # Static assets
│   ├── src/
│   │   ├── components/   # Reusable UI components
│   │   ├── pages/        # Route-based pages
│   │   ├── features/     # Feature-specific modules
│   │   ├── hooks/        # Custom hooks
│   │   ├── services/     # API calls
│   │   ├── store/        # State management
│   │   └── utils/        # Helpers, constants
│   ├── tests/            # Frontend tests
│   └── package.json      # Node.js dependencies
│
├── scripts/              # Deployment scripts
├── docs/                 # Documentation
├── .env.example          # Environment variables template
├── .gitignore
├── docker-compose.yml    # Multi-container setup
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Node.js 16+
- Python 3.11+ (for backend)
- PostgreSQL 13+
- Docker (optional)

### Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd {project_name}
```

2. **Environment setup:**
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. **Backend setup:**
```bash
cd backend
pip install -r requirements.txt
python src/app.py  # or main.py for FastAPI
```

4. **Frontend setup:**
```bash
cd frontend
npm install
npm start
```

### Docker Setup

```bash
# Build and run all services
docker-compose up --build

# Run in background
docker-compose up -d
```

## 🛠️ Development

### Backend Development

- **Flask:** `python src/app.py`
- **FastAPI:** `python src/main.py`
- **Spring Boot:** `mvn spring-boot:run`
- **Express:** `npm start`

### Frontend Development

- **React:** `npm start`
- **Next.js:** `npm run dev`

## 📚 API Documentation

- **Flask/FastAPI:** http://localhost:5000/docs
- **Spring Boot:** http://localhost:8080/swagger-ui.html
- **Express:** http://localhost:3000/api

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest  # Python
npm test  # Node.js
mvn test  # Java
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 🚀 Deployment

### Production Build

```bash
# Backend
cd backend
pip install -r requirements.txt
gunicorn src.app:app  # Flask
uvicorn src.main:app  # FastAPI

# Frontend
cd frontend
npm run build
```

### Docker Deployment

```bash
docker-compose -f docker-compose.prod.yml up -d
```

## 📝 Available Scripts

### Backend
- `python src/app.py` - Start Flask app
- `python src/main.py` - Start FastAPI app
- `npm start` - Start Express app
- `mvn spring-boot:run` - Start Spring Boot app

### Frontend
- `npm start` - Start development server
- `npm run build` - Build for production
- `npm test` - Run tests

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.
'''
        write_file(project_path / "README.md", readme_content)
