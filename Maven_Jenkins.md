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


#  Compilation Process (Deep Dive)

---

# 1. What is Compilation?

Compilation is the process of converting:

Human-readable code → Machine-understandable code

For Java:

.java → .class

---

# 2. Key Tools Involved

| Tool     | Role                          |
|----------|-------------------------------|
| Jenkins  | Automates the process         |
| Maven    | Manages build lifecycle       |
| javac    | Compiles the code (actual)    |

---

# 3. Important Concept

Maven does NOT compile code directly.

Maven → calls → javac → compiles code

---

# 4. Step-by-Step Compilation Flow

## Step 1: Write Code

Example:

public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello Teja");
    }
}

File:
Hello.java

---

## Step 2: Run Maven Command

mvn clean install

---

## Step 3: Maven Reads Configuration

Maven reads:

pom.xml

This file contains:
- Project details
- Dependencies
- Build instructions

---

## Step 4: Maven Enters Compile Phase

Build lifecycle:

clean → compile → test → package → install

---

## Step 5: Maven Calls Java Compiler

Maven internally invokes:

javac

---

## Step 6: Compilation Happens

Conversion:

Hello.java → Hello.class

---

## Step 7: Output Stored

Compiled files are stored in:

target/classes/

---

# 5. Output Structure

target/
   ├── classes/        → .class files (compiled code)
   ├── test-classes/
   ├── *.jar           → final application

---

# 6. What is .class File?

- Binary file (bytecode)
- Executed by JVM (Java Virtual Machine)

---

# 7. Full Compilation Flow

You write code (.java)
        ↓
Run mvn clean install
        ↓
Maven reads pom.xml
        ↓
Maven triggers compile phase
        ↓
Maven calls javac
        ↓
javac converts .java → .class
        ↓
Stored in target/classes

---

# 8. Role of Each Tool

Jenkins:
- Automates build process

Maven:
- Manages build lifecycle
- Triggers compilation

javac:
- Actually compiles the code

---

# 9. Key Differences

| Concept     | Description                  |
|-------------|------------------------------|
| Compilation | .java → .class               |
| Packaging   | .class → .jar                |
| Build       | Full process (all steps)     |

---

# 10. Important Commands

Compile only:
mvn compile

Full build:
mvn clean install

---

# 11. Interview Answer

Compilation is the process of converting Java source code into bytecode using the Java compiler (javac). In Maven projects, the compile phase triggers javac to generate .class files, which are stored in the target/classes directory.

---

# 12. Summary

- Compilation converts .java to .class
- javac performs compilation
- Maven triggers compilation
- Jenkins automates the process
- Output stored in target/classes

---

# DevOps Day 10 - Code Review using Jenkins + PMD

---

## 1. What is Code Review?

Code review is the process of checking code quality before merging it into the main branch.

Types:
- Manual Review → Done by developers  
- Automated Review → Done using Jenkins + PMD  

---

## 2. Tools Used

| Tool      | Role                          |
|-----------|-------------------------------|
| Jenkins   | Automation server             |
| Maven     | Build tool                    |
| PMD       | Static code analysis tool     |
| GitHub    | Source code repository        |

---

## 3. What is PMD?

PMD is a static code analysis tool that scans Java code for:

- Unused variables  
- Duplicate code  
- Bad coding practices  
- Code complexity issues  

---

## 4. Project Flow

GitHub → Jenkins → Maven → PMD → Jenkins Dashboard

---

## 5. Implementation Steps

### Step 1: Add PMD Plugin in `pom.xml`

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-pmd-plugin</artifactId>
  <version>3.21.0</version>
  <configuration>
    <failOnViolation>false</failOnViolation>
  </configuration>
</plugin>   

mvn clean install pmd:pmd


## 🧪 Unit Testing with Jenkins (Windows)

### 📌 What is Unit Testing?

Unit Testing is the process of testing individual components (methods/functions) to ensure they work correctly.

#### Example:

```java
int add(int a, int b) {
    return a + b;
}
```

#### Test Case:

```java
assertEquals(5, add(2, 3));
```

---

### 🎯 Why Unit Testing?

* Detect bugs early
* Improve code quality
* Ensure reliability
* Essential for CI/CD pipelines

---

### 🧰 Tools Used

* **JUnit** → Writing test cases
* **Maven** → Running tests
* **Jenkins** → Automating execution

---

### ⚙️ Running Unit Tests (Windows)

```bat
mvn clean test
```

#### What Happens:

1. Code compiles
2. Tests are executed
3. Reports are generated

---

### 📂 Test Report Location

```
target/surefire-reports/
```

* `.xml` → Used by Jenkins
* `.txt` → Detailed logs

---

### 🔗 Jenkins Configuration

#### 🔹 Build Step

Use: **Execute Windows batch command**

```bat
mvn clean test
```

---

#### 🔹 Post Build Action

Use: **Publish JUnit test result report**

```
target/surefire-reports/*.xml
```

---

### ⚠️ Common Errors

#### ❌ No test reports found

```
target/surefire-reports/*.xml doesn't match anything
```

✔ Reason:

* Build didn’t run
* Tests didn’t execute

---

#### ❌ Git clone failed

```
Failed to connect to github.com port 443
```

✔ Fix:

* Check internet
* Configure proxy/firewall

---

### ⚔️ Shell vs Windows Commands

| Linux         | Windows        |
| ------------- | -------------- |
| sh 'mvn test' | bat 'mvn test' |

---

### ❌ What Happens If Tests Fail?

* Maven build fails
* Jenkins marks build as **FAILED**
* Pipeline stops

---

### 🛠️ How to Fix Failed Tests

1. Check Jenkins console output
2. Open test report
3. Identify failing test
4. Fix code/test
5. Push changes
6. Re-run pipeline

---

### ⚠️ Important Rule

🚫 Never deploy code with failing tests

---

### 🟡 Optional (Not Recommended)

```bat
mvn clean install -DskipTests
```

---

### 🧠 Key Takeaways

* Unit testing ensures code quality
* Maven executes tests
* Jenkins automates testing
* Reports are stored in `target/`
* Failing tests stop deployment

---


# 🚀 CI Pipeline using Jenkins + Maven (Windows)

## 📌 Overview

This document covers the complete CI pipeline implementation using:

* Jenkins
* Maven
* GitHub
* PMD (Code Review)
* JUnit (Unit Testing)
* JaCoCo (Code Coverage)

---

## 🔗 Project Setup

### Source Code Repository

* GitHub repository integrated with Jenkins
* Jenkins pulls code using Git

---

## ⚙️ GitHub Configuration in Jenkins

1. Install Plugins:

   * Git Plugin
   * GitHub Plugin

2. Configure Git:

   ```
   Manage Jenkins → Global Tool Configuration
   ```

   Set path:

   ```
   C:\Program Files\Git\bin\git.exe
   ```

3. Configure Job:

   * Source Code Management → Git
   * Add repository URL

---

## 🏗️ Maven Build Lifecycle

Maven executes phases in order:

```
validate → compile → test → verify → package
```

---

## 🧪 Manual Commands (Step-by-Step)

```bat
mvn clean
mvn validate
mvn compile
mvn pmd:pmd
mvn test
mvn jacoco:report
mvn package
```

---

## 🔥 Recommended Command (Industry Standard)

```bat
mvn clean verify
```

### What it does:

* Cleans project
* Compiles code
* Runs unit tests
* Performs code review (PMD)
* Generates coverage (JaCoCo)
* Packages application

---

## 🧰 Tools Used

| Tool    | Purpose          |
| ------- | ---------------- |
| Maven   | Build automation |
| Jenkins | CI orchestration |
| PMD     | Code review      |
| JUnit   | Unit testing     |
| JaCoCo  | Code coverage    |

---

## 🧪 Unit Testing

### Run tests:

```bat
mvn test
```

### Report location:

```
target/surefire-reports/
```

---

## 📊 Code Coverage (JaCoCo)

### Run:

```bat
mvn jacoco:report
```

### Report:

```
target/site/jacoco/index.html
```

---

## 🔍 Code Review (PMD)

### Run:

```bat
mvn pmd:pmd
```

### Report:

```
target/pmd.xml
```

---

## 🔗 Jenkins Build Configuration (Windows)

### Build Step:

* Execute Windows batch command:

```bat
mvn clean verify
```

---

## 📊 Post Build Actions

### JUnit Report:

```
target/surefire-reports/*.xml
```

### PMD Report:

```
target/pmd.xml
```

### JaCoCo Coverage:

```
target/jacoco.exec
```

---

## 🔄 CI Pipeline Flow

1. Code pushed to GitHub
2. Jenkins triggers build
3. Code is cloned
4. Maven runs lifecycle
5. Reports are generated
6. Build status displayed

---

## ⚠️ What Happens If Tests Fail?

* Build becomes **FAILED**
* Pipeline stops
* Developer must fix the issue

---

## ⚔️ Shell vs Windows Commands

| Linux         | Windows        |
| ------------- | -------------- |
| sh 'mvn test' | bat 'mvn test' |

---

## 🎯 Jenkins Pipeline (Manual Stages – Learning)

```groovy
stage('Validate') {
    steps { bat 'mvn validate' }
}
stage('Compile') {
    steps { bat 'mvn compile' }
}
stage('Code Review') {
    steps { bat 'mvn pmd:pmd' }
}
stage('Unit Test') {
    steps { bat 'mvn test' }
}
stage('Coverage') {
    steps { bat 'mvn jacoco:report' }
}
stage('Package') {
    steps { bat 'mvn package' }
}
```

---

## 🚀 Jenkins Pipeline (Recommended)

```groovy
stage('CI Pipeline') {
    steps {
        bat 'mvn clean verify'
    }
}
```

---

## 📊 Pipeline Visualization

### Plugins Used:

* Pipeline Stage View
* Blue Ocean

### Where to View:

* Jenkins → Job → Build → Stages
* Blue Ocean Dashboard

---

## ⚠️ Important Concepts

* Maven handles lifecycle automatically
* Jenkins triggers and monitors pipeline
* Plugins generate reports
* Visualization depends on pipeline stages

---

## 🧠 Key Learnings

* CI pipeline automates build and testing
* `mvn clean verify` runs complete pipeline
* PMD ensures code quality
* JaCoCo measures test coverage
* Jenkins displays reports and status
* Pipeline visualization depends on stages

---

## 🚀 Next Steps

* GitHub Webhooks (Auto Trigger)
* SonarQube (Advanced Code Quality)
* Docker Integration
* Deployment to Cloud (AWS)

---
