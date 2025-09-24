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
    """Create modern React project with TypeScript, Redux, React Router."""
    project_path = Path(output_dir) / project_name
    create_directory(project_path)
    
    # Create package.json with modern dependencies
    package_json = {
        "name": project_name,
        "version": "1.0.0",
        "description": "A modern React application created with Prarabdha",
        "private": True,
        "scripts": {
            "start": "react-scripts start",
            "build": "react-scripts build",
            "test": "react-scripts test",
            "eject": "react-scripts eject",
            "lint": "eslint src --ext .ts,.tsx",
            "lint:fix": "eslint src --ext .ts,.tsx --fix",
            "type-check": "tsc --noEmit"
        },
        "dependencies": {
            "react": "^18.2.0",
            "react-dom": "^18.2.0",
            "react-router-dom": "^6.8.0",
            "react-redux": "^8.0.5",
            "@reduxjs/toolkit": "^1.9.3",
            "axios": "^1.3.4",
            "react-query": "^3.39.3",
            "styled-components": "^5.3.6",
            "react-hook-form": "^7.43.5",
            "react-hot-toast": "^2.4.0",
            "date-fns": "^2.29.3"
        },
        "devDependencies": {
            "@types/react": "^18.0.28",
            "@types/react-dom": "^18.0.11",
            "@types/node": "^18.15.0",
            "@typescript-eslint/eslint-plugin": "^5.54.0",
            "@typescript-eslint/parser": "^5.54.0",
            "eslint": "^8.35.0",
            "eslint-plugin-react": "^7.32.2",
            "eslint-plugin-react-hooks": "^4.6.0",
            "typescript": "^4.9.5",
            "react-scripts": "5.0.1"
        },
        "browserslist": {
            "production": [">0.2%", "not dead", "not op_mini all"],
            "development": ["last 1 chrome version", "last 1 firefox version", "last 1 safari version"]
        }
    }
    
    write_file(frontend_dir / "package.json", json.dumps(package_json, indent=2))
    
    # Create TypeScript configuration
    tsconfig = {
        "compilerOptions": {
            "target": "es5",
            "lib": ["dom", "dom.iterable", "es6"],
            "allowJs": True,
            "skipLibCheck": True,
            "esModuleInterop": True,
            "allowSyntheticDefaultImports": True,
            "strict": True,
            "forceConsistentCasingInFileNames": True,
            "noFallthroughCasesInSwitch": True,
            "module": "esnext",
            "moduleResolution": "node",
            "resolveJsonModule": True,
            "isolatedModules": True,
            "noEmit": True,
            "jsx": "react-jsx"
        },
        "include": ["src"]
    }
    
    write_file(frontend_dir / "tsconfig.json", json.dumps(tsconfig, indent=2))
    
    # Create frontend directory structure
    frontend_dir = project_path / "frontend"
    create_directory(frontend_dir)
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
    create_directory(src_dir / "styles")
    
    # Create main App.tsx
    app_content = '''import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import { QueryClient, QueryClientProvider } from 'react-query';
import { Toaster } from 'react-hot-toast';
import { store } from './store/store';
import { GlobalStyle } from './styles/GlobalStyle';
import Layout from './components/Layout';
import Home from './pages/Home';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import Profile from './pages/Profile';

const queryClient = new QueryClient();

function App() {
  return (
    <Provider store={store}>
      <QueryClientProvider client={queryClient}>
        <Router>
          <GlobalStyle />
          <Layout>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/login" element={<Login />} />
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/profile" element={<Profile />} />
            </Routes>
          </Layout>
          <Toaster position="top-right" />
        </Router>
      </QueryClientProvider>
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
    
    # Create Redux store
    store_content = '''import { configureStore } from '@reduxjs/toolkit';
import authReducer from './slices/authSlice';
import userReducer from './slices/userSlice';

export const store = configureStore({
  reducer: {
    auth: authReducer,
    user: userReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
'''
    write_file(src_dir / "store" / "store.ts", store_content)
    
    # Create auth slice
    auth_slice = '''import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface AuthState {
  isAuthenticated: boolean;
  token: string | null;
  user: User | null;
}

interface User {
  id: string;
  email: string;
  name: string;
}

const initialState: AuthState = {
  isAuthenticated: false,
  token: null,
  user: null,
};

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    login: (state, action: PayloadAction<{ token: string; user: User }>) => {
      state.isAuthenticated = true;
      state.token = action.payload.token;
      state.user = action.payload.user;
    },
    logout: (state) => {
      state.isAuthenticated = false;
      state.token = null;
      state.user = null;
    },
  },
});

export const { login, logout } = authSlice.actions;
export default authSlice.reducer;
'''
    write_file(src_dir / "store" / "slices" / "authSlice.ts", auth_slice)
    
    # Create user slice
    user_slice = '''import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface UserState {
  profile: UserProfile | null;
  loading: boolean;
  error: string | null;
}

interface UserProfile {
  id: string;
  name: string;
  email: string;
  avatar?: string;
  bio?: string;
}

const initialState: UserState = {
  profile: null,
  loading: false,
  error: null,
};

const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    setProfile: (state, action: PayloadAction<UserProfile>) => {
      state.profile = action.payload;
    },
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.loading = action.payload;
    },
    setError: (state, action: PayloadAction<string | null>) => {
      state.error = action.payload;
    },
  },
});

export const { setProfile, setLoading, setError } = userSlice.actions;
export default userSlice.reducer;
'''
    write_file(src_dir / "store" / "slices" / "userSlice.ts", user_slice)
    
    # Create custom hooks
    hooks_content = '''import { useDispatch, useSelector, TypedUseSelectorHook } from 'react-redux';
import type { RootState, AppDispatch } from '../store/store';

export const useAppDispatch = () => useDispatch<AppDispatch>();
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;
'''
    write_file(src_dir / "hooks" / "redux.ts", hooks_content)
    
    # Create API service
    api_service = '''import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor to add auth token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default api;
'''
    write_file(src_dir / "services" / "api.ts", api_service)
    
    # Create sample pages
    home_page = '''import React from 'react';
import styled from 'styled-components';
import { useAppSelector } from '../hooks/redux';

const Container = styled.div`
  padding: 2rem;
  text-align: center;
`;

const Title = styled.h1`
  color: #333;
  margin-bottom: 1rem;
`;

const Subtitle = styled.p`
  color: #666;
  font-size: 1.2rem;
`;

const Home: React.FC = () => {
  const { isAuthenticated, user } = useAppSelector((state) => state.auth);

  return (
    <Container>
      <Title>Welcome to React App</Title>
      <Subtitle>
        {isAuthenticated 
          ? `Hello, ${user?.name}!` 
          : 'Please log in to access your dashboard'
        }
      </Subtitle>
    </Container>
  );
};

export default Home;
'''
    write_file(src_dir / "pages" / "Home.tsx", home_page)
    
    # Create Layout component
    layout_component = '''import React from 'react';
import styled from 'styled-components';
import { Outlet } from 'react-router-dom';
import Navbar from './Navbar';

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
      <Navbar />
      <Main>
        {children}
      </Main>
    </LayoutContainer>
  );
};

export default Layout;
'''
    write_file(src_dir / "components" / "Layout.tsx", layout_component)
    
    # Create Navbar component
    navbar_component = '''import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import styled from 'styled-components';
import { useAppSelector, useAppDispatch } from '../hooks/redux';
import { logout } from '../store/slices/authSlice';

const Nav = styled.nav`
  background: #333;
  color: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

const Logo = styled(Link)`
  color: white;
  text-decoration: none;
  font-size: 1.5rem;
  font-weight: bold;
`;

const NavLinks = styled.div`
  display: flex;
  gap: 1rem;
`;

const NavLink = styled(Link)`
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.2s;

  &:hover {
    background-color: #555;
  }
`;

const Button = styled.button`
  background: #007bff;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s;

  &:hover {
    background: #0056b3;
  }
`;

const Navbar: React.FC = () => {
  const { isAuthenticated, user } = useAppSelector((state) => state.auth);
  const dispatch = useAppDispatch();
  const navigate = useNavigate();

  const handleLogout = () => {
    dispatch(logout());
    navigate('/');
  };

  return (
    <Nav>
      <Logo to="/">MyApp</Logo>
      <NavLinks>
        <NavLink to="/">Home</NavLink>
        {isAuthenticated ? (
          <>
            <NavLink to="/dashboard">Dashboard</NavLink>
            <NavLink to="/profile">Profile</NavLink>
            <Button onClick={handleLogout}>Logout</Button>
          </>
        ) : (
          <NavLink to="/login">Login</NavLink>
        )}
      </NavLinks>
    </Nav>
  );
};

export default Navbar;
'''
    write_file(src_dir / "components" / "Navbar.tsx", navbar_component)
    
    # Create GlobalStyle
    global_style = '''import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
      'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
      sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    background-color: #f5f5f5;
  }

  code {
    font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
      monospace;
  }
`;

export default GlobalStyle;
'''
    write_file(src_dir / "styles" / "GlobalStyle.ts", global_style)
    
    # Create public directory
    public_dir = frontend_dir / "public"
    create_directory(public_dir)
    
    # Create index.html
    html_content = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta name="description" content="Modern React application" />
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>
'''
    write_file(public_dir / "index.html", html_content)
    
    # Create .env.example
    env_example = '''REACT_APP_API_URL=http://localhost:8000/api
REACT_APP_APP_NAME=My React App
'''
    write_file(project_path / ".env.example", env_example)
    
    # Create .gitignore
    gitignore_content = '''# Dependencies
node_modules/
/.pnp
.pnp.js

# Testing
/coverage

# Production
/build

# Misc
.DS_Store
.env.local
.env.development.local
.env.test.local
.env.production.local

# Logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
Thumbs.db
'''
    write_file(project_path / ".gitignore", gitignore_content)
    
    # Create comprehensive README
    readme_content = f'''# {project_name}

A modern React application built with TypeScript, Redux Toolkit, React Router, and styled-components.

## 🚀 Features

- **TypeScript** for type safety
- **Redux Toolkit** for state management
- **React Router** for navigation
- **Styled Components** for styling
- **React Query** for data fetching
- **React Hook Form** for form handling
- **Axios** for API calls
- **Hot Toast** for notifications

## 📁 Project Structure

```
src/
├── components/          # Reusable UI components
├── pages/              # Page components
├── hooks/              # Custom React hooks
├── store/              # Redux store and slices
├── services/           # API services
├── types/              # TypeScript type definitions
├── utils/              # Utility functions
└── styles/             # Global styles
```

## 🛠️ Getting Started

### Prerequisites

- Node.js 16+ 
- npm or yarn

### Installation

1. Install dependencies:
```bash
npm install
```

2. Copy environment variables:
```bash
cp .env.example .env
```

3. Start the development server:
```bash
npm start
```

The app will be available at `http://localhost:3000`

## 📝 Available Scripts

- `npm start` - Start development server
- `npm build` - Build for production
- `npm test` - Run tests
- `npm run lint` - Run ESLint
- `npm run lint:fix` - Fix ESLint issues
- `npm run type-check` - Run TypeScript type checking

## 🧪 Testing

```bash
npm test
```

## 🚀 Deployment

### Build for Production

```bash
npm run build
```

### Docker Deployment

```bash
docker build -t {project_name} .
docker run -p 3000:3000 {project_name}
```

## 📚 Documentation

- [React Documentation](https://reactjs.org/)
- [TypeScript Documentation](https://www.typescriptlang.org/)
- [Redux Toolkit Documentation](https://redux-toolkit.js.org/)
- [React Router Documentation](https://reactrouter.com/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.
'''
    write_file(project_path / "README.md", readme_content)
    
    console.print(f"[green]✅ Modern React project '{project_name}' created successfully![/green]")
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
