# DevOps Day 8 Notes
# Build Process, Maven, Jenkins & CI Pipeline

---

# 1. What is Build Code Process?

## Definition
The build process is the process of converting **source code into a runnable application**.

---

## Build Process Flow

Source Code → Compile → Test → Package → Artifact

---

## Steps in Build Process

### 1. Compile
Convert source code into machine-readable format.

Example:
.java → .class

---

### 2. Test
Run test cases to verify application functionality.

---

### 3. Package
Bundle the application into a deployable file.

Examples:
- JAR
- WAR

---

### 4. Artifact
Final output of build process is called an artifact.

Example:
target/myapp.jar

---

# 2. What is Build Automation?

## Definition
Build automation is the process of automatically performing build steps such as compile, test, and package using tools.

---

## Without Automation

Manual process:
Compile → Test → Package → Deploy

Problems:
- Time-consuming
- Error-prone
- Not scalable

---

## With Automation

Code change → Auto Build → Auto Test → Auto Package

---

# 3. Maven (Build Tool)

Maven is a build automation tool used to:

- Compile code
- Manage dependencies
- Run tests
- Package application

---

## Maven Command

mvn clean install

---

## What Maven Does

1. Cleans previous builds  
2. Downloads dependencies  
3. Compiles code  
4. Runs tests  
5. Packages application  

---

## Important File

pom.xml

Contains:
- Project configuration
- Dependencies
- Build settings

---

# 4. Jenkins (Automation Tool)

Jenkins is an automation server used to implement CI/CD pipelines.

---

## What Jenkins Does

- Automates build process  
- Triggers jobs when code changes  
- Runs pipelines  
- Integrates with tools like Maven  

---

## Jenkins Workflow

Developer → Git → Jenkins → Build → Test → Deploy

---

# 5. Difference Between Maven and Jenkins

| Feature | Maven | Jenkins |
|--------|------|--------|
| Type | Build Tool | Automation Tool |
| Role | Builds application | Automates workflow |
| Function | Compile, test, package | Trigger pipelines |
| Dependency management | Yes | No |
| Usage | Creates artifact | Manages CI/CD |

---

## Simple Understanding

Maven = Worker (builds code)  
Jenkins = Manager (automates process)

---

# 6. What is CI Pipeline?

## Definition
CI (Continuous Integration) pipeline is an automated process that builds and tests code whenever changes are made.

---

## CI Pipeline Flow

Code Push → Trigger → Build → Test → Result

---

## CI Pipeline Stages

1. Pull code from Git  
2. Build application (Maven)  
3. Run tests  
4. Generate result  

---

## Example Flow

Developer → GitHub → Jenkins → Maven → Build → Test → Artifact

---

# 7. Why CI Pipeline is Important

- Detects bugs early  
- Automates testing  
- Improves code quality  
- Speeds up development  
- Reduces manual effort  

---

# 8. Complete DevOps Flow

Code → Git → Jenkins → Maven → Build → Test → Artifact → Deploy

---

# 9. Summary

- Build process converts source code into executable format  
- Maven is used for building applications  
- Jenkins is used for automating workflows  
- CI pipeline automates integration, build, and testing  

---

End of Day 8 DevOps Notes
