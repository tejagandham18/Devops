# Jenkins — Phase 3 Complete Notes

## What is Jenkins?

Jenkins is an automation server used to automate software development tasks.

Main use cases:

- Build automation
- Testing automation
- Packaging
- Deployment
- CI/CD pipelines

Jenkins helps reduce manual work.

---

# Why Jenkins?

Without Jenkins:

Developer pushes code  
↓  
Manual build  
↓  
Manual testing  
↓  
Manual deployment  

Problems:

- Time consuming
- Human errors
- Slow delivery

With Jenkins:

Developer pushes code  
↓  
Jenkins automatically builds  
↓  
Runs tests  
↓  
Creates package  
↓  
Deploys

Benefits:

- Fast
- Automated
- Reliable

---

# What Jenkins Does

Jenkins can automate:

1. Pull code from GitHub
2. Build application
3. Run tests
4. Package application
5. Build Docker image
6. Push Docker image
7. Deploy application

---

# Jenkins Architecture

Basic flow:

Developer
↓
GitHub
↓
Jenkins Server
↓
Build
↓
Test
↓
Package
↓
Deploy

Components:

## Jenkins Server

Main automation server.

Handles:

- Jobs
- Pipelines
- Plugins

---

## Jenkins Agents

Workers that execute jobs.

Types:

- Static agent
- Dynamic agent
- Docker agent

---

# Jenkins Dashboard

Main sections:

## New Item

Create new job.

---

## Build History

Shows build history.

Example:

Build #1
Build #2
Build #3

---

## Workspace

Stores project files.

Path example:

```text
C:\ProgramData\Jenkins\.jenkins\workspace
```

---

## Console Output

Shows logs of pipeline execution.

Used for debugging.

---

# Jenkins Job Types

## Freestyle Project

Simple build jobs.

Used for:

- Simple scripts
- Basic automation

Example:

Run shell script.

---

## Pipeline Project

Used for CI/CD automation.

Best for:

- Multi-stage pipelines
- Real-world projects

---

## Multibranch Pipeline

Used when project has multiple branches.

Example:

main
dev
test

---

# Jenkins Pipeline

Pipeline = sequence of stages.

Example:

Clone
↓
Build
↓
Test
↓
Package

Pipeline automates everything.

---

# Pipeline Types

## Declarative Pipeline

Structured format.

Easy to read.

Example:

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'mvn clean compile'
            }
        }
    }
}
```

---

## Scripted Pipeline

Flexible pipeline.

More coding.

Example:

```groovy
node {
    stage('Build') {
        bat 'mvn clean compile'
    }
}
```

---

# Jenkinsfile

Jenkinsfile is a file containing pipeline code.

Purpose:

Store pipeline inside project.

Benefits:

- Version controlled
- Reusable
- Easy to maintain

File name:

```text
Jenkinsfile
```

---

# Jenkinsfile Structure

Basic syntax:

```groovy
pipeline {
    agent any

    stages {
        stage('Stage Name') {
            steps {
                bat 'command'
            }
        }
    }
}
```

Main keywords:

## pipeline

Main block.

---

## agent

Where pipeline runs.

Example:

```groovy
agent any
```

Meaning:

Run anywhere.

---

## stages

Collection of stages.

---

## stage

Individual phase.

Examples:

Build
Test
Deploy

---

## steps

Actual commands.

Example:

```groovy
steps {
    bat 'mvn test'
}
```

---

# Jenkins Pipeline Stages

## Clone Stage

Purpose:

Pull code from GitHub.

Example:

```groovy
stage('Clone') {
    steps {
        git branch: 'main', url: 'repo-url'
    }
}
```

---

## Build Stage

Purpose:

Compile application.

Example:

```groovy
stage('Build') {
    steps {
        bat 'mvn clean compile'
    }
}
```

---

## Test Stage

Purpose:

Run tests.

Example:

```groovy
stage('Test') {
    steps {
        bat 'mvn test'
    }
}
```

---

## Package Stage

Purpose:

Create artifact.

Example:

```groovy
stage('Package') {
    steps {
        bat 'mvn package'
    }
}
```

Output:

.jar

---

## Deploy Stage

Purpose:

Deploy application.

Can include:

Docker build  
Docker push  
Server deployment

---

# Creating Jenkins Pipeline Job

Steps:

1. Open Jenkins
2. Click New Item
3. Enter job name
4. Select Pipeline
5. Configure pipeline
6. Save
7. Build Now

---

# Pipeline Configuration Methods

## Pipeline Script

Write pipeline directly in Jenkins UI.

Used for quick testing.

---

## Pipeline Script from SCM

Pipeline code stored in GitHub.

Used for real projects.

SCM:

Git

Repository URL:

GitHub URL

Script path:

Jenkinsfile

---

# Jenkins with GitHub

Jenkins can connect with GitHub.

Purpose:

Pull latest source code.

Flow:

GitHub
↓
Jenkins

Benefits:

- Automatic updates
- Centralized source code

---

# Jenkins with Maven

Jenkins executes Maven commands.

Examples:

Build:

```bash
mvn clean compile
```

Test:

```bash
mvn test
```

Package:

```bash
mvn package
```

Purpose:

Automate Java builds.

---

# Jenkins Build Process

Complete flow:

Code
↓
Clone
↓
Build
↓
Test
↓
Package

---

# Build Status

## Success

Build completed successfully.

Green.

---

## Failed

Build failed.

Red.

---

## Unstable

Tests failed.

Yellow.

---

# Console Output

Used to view:

- Build logs
- Errors
- Test results

Used for troubleshooting.

Path:

Build History → Console Output

---

# Common Jenkins Errors

## Maven not found

Reason:

Maven not configured.

Fix:

Manage Jenkins → Tools

---

## Java not found

Reason:

JDK not configured.

Fix:

Set JAVA_HOME.

---

## Git not found

Reason:

Git not installed.

Fix:

Install Git.

---

## Pipeline syntax error

Reason:

Wrong Jenkinsfile syntax.

Fix:

Correct syntax.

---

# Useful Jenkins Features

## Replay

Re-run pipeline with modifications.

---

## Workspace Cleanup

Clean old files.

---

## Build History

Track previous builds.

---

## Plugins

Extend Jenkins functionality.

Examples:

Git plugin  
Maven plugin  
Docker plugin

---

# Real Project Practice

Project:

Spring PetClinic

Pipeline stages used:

Clone
Build
Test
Package

Tools used:

GitHub
Jenkins
Maven

---

# Interview Questions

## What is Jenkins?

Jenkins is an automation server used for CI/CD.

---

## What is Jenkinsfile?

A file containing pipeline instructions.

---

## What is pipeline?

A sequence of automated stages.

---

## Difference between freestyle and pipeline?

Freestyle:

Simple jobs

Pipeline:

Multi-stage automation

---

## What is agent in Jenkins?

Execution environment.

---

## What is stage?

Individual phase in pipeline.

---

## What is steps?

Commands inside stage.

---



Status:

Phase 3 Jenkins Topic Completed
