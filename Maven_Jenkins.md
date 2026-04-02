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


# DevOps Day 9 Notes
# Jenkins, Maven Build & CI Pipeline

---

# 1. Jenkins Setup

## What is Jenkins?
Jenkins is an automation server used to implement CI/CD pipelines.

---

## Installation Steps

1. Install Java 17
2. Install Jenkins (.msi installer)
3. Open Jenkins in browser:
   http://localhost:8080
4. Unlock Jenkins using:
   C:\ProgramData\Jenkins\.jenkins\secrets\initialAdminPassword
5. Install suggested plugins
6. Create admin user

---

# 2. First Jenkins Job

## Steps to Create Job

1. Go to Jenkins Dashboard
2. Click "New Item"
3. Enter name:
   my-first-job
4. Select:
   Freestyle Project
5. Click OK

---

# 3. Configure Jenkins Job

## Source Code Management

Select:
Git

Repository URL:
https://github.com/spring-projects/spring-petclinic.git

---

## Branch Configuration (Important)

Default:
*/master ❌

Correct:
*/main ✅

Reason:
New repositories use "main" instead of "master"

---

## Build Step

Add build step:
Invoke top-level Maven targets

Goals:
clean install

---

# 4. Running the Job

1. Click "Build Now"
2. Go to "Console Output"

---

## Expected Result

BUILD SUCCESS

---

# 5. What Happens Internally

Step-by-step flow:

1. Jenkins connects to GitHub
2. Downloads source code
3. Runs Maven command:
   mvn clean install
4. Maven performs:
   - Clean
   - Compile
   - Test
   - Package
5. Creates artifact:
   target/*.jar
6. Jenkins shows build result

---

# 6. CI Pipeline Explanation

CI (Continuous Integration) means:

Automatically building and testing code whenever changes are made.

---

## CI Pipeline Flow

Code → GitHub → Jenkins → Maven → Build → Result

---

# 7. Tools Used

| Tool    | Role                          |
|--------|-------------------------------|
| GitHub | Stores source code            |
| Jenkins| Automates pipeline            |
| Maven  | Builds application            |

---

# 8. Issue Faced & Fix

## Error:
Couldn't find any revision to build

## Cause:
Branch mismatch (master vs main)

## Fix:
Change branch:
*/master → */main

---

# 9. Key Learnings

- Jenkins job creation
- Git integration with Jenkins
- Maven build execution
- CI pipeline basics
- Debugging branch issues

---

# 10. DevOps Workflow (Current)

GitHub
   ↓
Jenkins
   ↓
Maven Build
   ↓
Artifact (.jar)

---

# 11. Next Step (Upcoming)

- Jenkins + Docker integration
- Build Docker image from Jenkins
- Run container using Jenkins

---

End of Day 9 Notes
