"""
Node.js project scaffolder using Express.
"""

import os
from pathlib import Path
from rich.console import Console

from ..utils.helpers import create_directory, write_file

console = Console()


class NodeJSScaffolder:
    """Scaffolder for Node.js projects using Express."""
    
    def create_project(self, project_name, output_dir):
        """Create a Node.js Express project."""
        project_path = Path(output_dir) / project_name
        create_directory(project_path)
        
        self._create_express_project(project_path, project_name)
        
        return str(project_path)
    
    def _create_express_project(self, project_path, project_name):
        """Create Express project structure."""
        # Create src directory
        src_dir = project_path / "src"
        create_directory(src_dir)
        
        # Create main application file
        app_content = '''/**
 * Express application entry point.
 */

const express = require('express');
const cors = require('cors');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.get('/', (req, res) => {
    res.json({
        message: 'Welcome to your Express API!',
        status: 'success'
    });
});

app.get('/api/health', (req, res) => {
    res.json({
        status: 'healthy',
        service: 'express-api'
    });
});

app.post('/api/echo', (req, res) => {
    res.json({
        message: 'Echo successful',
        data: req.body
    });
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({
        message: 'Something went wrong!',
        error: process.env.NODE_ENV === 'development' ? err.message : {}
    });
});

// 404 handler
app.use('*', (req, res) => {
    res.status(404).json({
        message: 'Route not found',
        status: 'error'
    });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
    console.log(`Environment: ${process.env.NODE_ENV || 'development'}`);
});

module.exports = app;
'''
        
        write_file(src_dir / "app.js", app_content)
        
        # Create server.js
        server_content = '''/**
 * Server entry point.
 */

const app = require('./src/app');

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
'''
        
        write_file(project_path / "server.js", server_content)
        
        # Create package.json
        package_json_content = f'''{{
    "name": "{project_name.lower().replace(' ', '-')}",
    "version": "1.0.0",
    "description": "A Node.js Express application created with Prarabdha",
    "main": "server.js",
    "scripts": {{
        "start": "node server.js",
        "dev": "nodemon server.js",
        "test": "jest",
        "lint": "eslint src/",
        "lint:fix": "eslint src/ --fix"
    }},
    "keywords": ["express", "nodejs", "api"],
    "author": "",
    "license": "MIT",
    "dependencies": {{
        "express": "^4.18.2",
        "cors": "^2.8.5",
        "dotenv": "^16.3.1"
    }},
    "devDependencies": {{
        "nodemon": "^3.0.1",
        "jest": "^29.7.0",
        "eslint": "^8.53.0"
    }},
    "engines": {{
        "node": ">=16.0.0",
        "npm": ">=8.0.0"
    }}
}}
'''
        
        write_file(project_path / "package.json", package_json_content)
        
        # Create .env file
        env_content = '''NODE_ENV=development
PORT=3000
HOST=localhost
'''
        write_file(project_path / ".env", env_content)
        
        # Create .env.example
        env_example_content = '''NODE_ENV=development
PORT=3000
HOST=localhost
'''
        write_file(project_path / ".env.example", env_content)
        
        # Create .gitignore
        gitignore_content = '''# Dependencies
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Coverage directory used by tools like istanbul
coverage/
*.lcov

# nyc test coverage
.nyc_output

# Grunt intermediate storage
.grunt

# Bower dependency directory
bower_components

# node-waf configuration
.lock-wscript

# Compiled binary addons
build/Release

# Dependency directories
node_modules/
jspm_packages/

# TypeScript cache
*.tsbuildinfo

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

# dotenv environment variables file
.env
.env.test
.env.local
.env.development.local
.env.test.local
.env.production.local

# parcel-bundler cache
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

# Logs
logs
*.log

# Runtime data
pids
*.pid
*.seed
*.pid.lock

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

A Node.js Express application created with Prarabdha.

## Getting Started

### Prerequisites
- Node.js 16+
- npm 8+

### Installation

1. Install dependencies:
```bash
npm install
```

### Running the Application

#### Development mode:
```bash
npm run dev
```

#### Production mode:
```bash
npm start
```

The API will be available at `http://localhost:3000`

### API Endpoints

- `GET /` - Welcome message
- `GET /api/health` - Health check
- `POST /api/echo` - Echo endpoint for testing

### Development

To run in development mode with auto-restart:
```bash
npm run dev
```

### Testing

To run tests:
```bash
npm test
```

### Linting

To run linting:
```bash
npm run lint
```

To fix linting issues:
```bash
npm run lint:fix
```

### Environment Variables

Copy `.env.example` to `.env` and modify as needed:
```bash
cp .env.example .env
```

### Production

To run in production:
```bash
NODE_ENV=production npm start
```
'''
        write_file(project_path / "README.md", readme_content)
        
        console.print(f"[green]✅ Node.js Express project '{project_name}' created successfully![/green]")
