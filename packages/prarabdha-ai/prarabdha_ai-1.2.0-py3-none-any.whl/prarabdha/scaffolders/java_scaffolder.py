"""
Java project scaffolder using Spring Boot.
"""

import os
from pathlib import Path
from rich.console import Console

from ..utils.helpers import create_directory, write_file

console = Console()


class JavaScaffolder:
    """Scaffolder for Java projects using Spring Boot."""
    
    def create_project(self, project_name, output_dir):
        """Create a Java Spring Boot project."""
        project_path = Path(output_dir) / project_name
        create_directory(project_path)
        
        self._create_spring_boot_project(project_path, project_name)
        
        return str(project_path)
    
    def _create_spring_boot_project(self, project_path, project_name):
        """Create Spring Boot project structure."""
        # Create Maven directory structure
        src_main_java = project_path / "src" / "main" / "java" / "com" / "example" / project_name.lower().replace("-", "")
        src_main_resources = project_path / "src" / "main" / "resources"
        src_test_java = project_path / "src" / "test" / "java" / "com" / "example" / project_name.lower().replace("-", "")
        
        create_directory(src_main_java)
        create_directory(src_main_resources)
        create_directory(src_test_java)
        
        # Create main application class
        main_class_content = f'''package com.example.{project_name.lower().replace("-", "")};

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.CrossOrigin;

import java.util.Map;

@SpringBootApplication
@RestController
@CrossOrigin(origins = "*")
public class {project_name.replace("-", "").replace("_", "")}Application {{

    public static void main(String[] args) {{
        SpringApplication.run({project_name.replace("-", "").replace("_", "")}Application.class, args);
    }}

    @GetMapping("/")
    public Map<String, String> home() {{
        return Map.of(
            "message", "Welcome to your Spring Boot API!",
            "status", "success"
        );
    }}

    @GetMapping("/api/health")
    public Map<String, String> health() {{
        return Map.of(
            "status", "healthy",
            "service", "spring-boot-api"
        );
    }}

    @PostMapping("/api/echo")
    public Map<String, Object> echo(@RequestBody Map<String, Object> data) {{
        return Map.of(
            "message", "Echo successful",
            "data", data
        );
    }}
}}
'''
        
        write_file(src_main_java / f"{project_name.replace('-', '').replace('_', '')}Application.java", main_class_content)
        
        # Create pom.xml
        pom_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.2.0</version>
        <relativePath/>
    </parent>

    <groupId>com.example</groupId>
    <artifactId>{project_name.lower().replace("-", "")}</artifactId>
    <version>1.0.0</version>
    <name>{project_name}</name>
    <description>A Spring Boot application created with Prarabdha</description>

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
        
        write_file(project_path / "pom.xml", pom_content)
        
        # Create application.properties
        app_properties_content = '''server.port=8080
server.servlet.context-path=/

# Logging
logging.level.com.example=INFO
logging.pattern.console=%d{{yyyy-MM-dd HH:mm:ss}} - %msg%n
'''
        write_file(src_main_resources / "application.properties", app_properties_content)
        
        # Create test class
        test_class_content = f'''package com.example.{project_name.lower().replace("-", "")};

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.TestPropertySource;

@SpringBootTest
@TestPropertySource(properties = {{
    "server.port=0"
}})
class {project_name.replace("-", "").replace("_", "")}ApplicationTests {{

    @Test
    void contextLoads() {{
        // This test ensures the application context loads successfully
    }}
}}
'''
        
        write_file(src_test_java / f"{project_name.replace('-', '').replace('_', '')}ApplicationTests.java", test_class_content)
        
        # Create .gitignore
        gitignore_content = '''# Compiled class file
*.class

# Log file
*.log

# BlueJ files
*.ctxt

# Mobile Tools for Java (J2ME)
.mtj.tmp/

# Package Files
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# Virtual machine crash logs
hs_err_pid*

# Maven
target/
pom.xml.tag
pom.xml.releaseBackup
pom.xml.versionsBackup
pom.xml.next
release.properties
dependency-reduced-pom.xml
buildNumber.properties
.mvn/timing.properties
.mvn/wrapper/maven-wrapper.jar

# IDE
.idea/
*.iws
*.iml
*.ipr
.vscode/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
'''
        write_file(project_path / ".gitignore", gitignore_content)
        
        # Create README.md
        readme_content = f'''# {project_name}

A Spring Boot application created with Prarabdha.

## Getting Started

### Prerequisites
- Java 17+
- Maven 3.6+

### Installation

1. Clone or download the project
2. Navigate to the project directory

### Running the Application

#### Using Maven:
```bash
mvn spring-boot:run
```

#### Using JAR:
```bash
mvn clean package
java -jar target/{project_name.lower().replace("-", "")}-1.0.0.jar
```

The API will be available at `http://localhost:8080`

### API Endpoints

- `GET /` - Welcome message
- `GET /api/health` - Health check
- `POST /api/echo` - Echo endpoint for testing

### Development

To run in development mode with hot reload:
```bash
mvn spring-boot:run -Dspring-boot.run.jvmArguments="-Dspring.devtools.restart.enabled=true"
```

### Testing

To run tests:
```bash
mvn test
```

### Building for Production

To build a production JAR:
```bash
mvn clean package -Pproduction
```
'''
        write_file(project_path / "README.md", readme_content)
        
        console.print(f"[green]✅ Spring Boot project '{project_name}' created successfully![/green]")
