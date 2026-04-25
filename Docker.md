# 📦 Docker Phase 2 – Foundations (Summary Notes)

## 🧠 1. Introduction to Docker

Docker solves the problem of:

> ❌ “It works on my machine but not on server”

### 🚀 Solution:

Docker packages applications into **containers** that run consistently everywhere.

---

## 📦 2. Image vs Container (Core Concept)

### 📦 Image

* Blueprint / Template
* Contains app + dependencies
* Static (not running)

### ▶️ Container

* Running instance of an image
* Active and executing

### 🔥 Analogy:

* Image → Recipe
* Container → Cooked food

---

## 🧱 3. Container Basics

* Containers are built using **layers**
* Each layer represents:

  * OS base
  * Libraries
  * Application code

👉 All layers combine to form a working container.

---

## ⚔️ 4. Docker vs Virtual Machines

| Feature | Virtual Machine | Docker Container |
| ------- | --------------- | ---------------- |
| OS      | Full OS per VM  | Shared OS        |
| Size    | Heavy           | Lightweight      |
| Speed   | Slow            | Fast             |
| Usage   | Less in DevOps  | Highly used      |

---

## ⚙️ 5. Docker Installation

* Installed Docker Desktop
* Enabled WSL integration
* Verified using:

```bash
docker run hello-world
```

---

## 🔧 6. Main Docker Commands

### 🔹 Pull Image

```bash
docker pull nginx
```

👉 Downloads image from Docker Hub

---

### 🔹 Run Container

```bash
docker run nginx
```

👉 Creates and starts a container

---

### 🔹 List Running Containers

```bash
docker ps
```

### 🔹 List All Containers

```bash
docker ps -a
```

---

### 🔹 Stop Container

```bash
docker stop <container_id>
```

---

### 🔹 Start Container

```bash
docker start <container_id>
```

---

## 🌐 7. Port Mapping (Very Important)

```bash
docker run -p 8080:80 nginx
```

### 🧠 Meaning:

* Host machine → Port 8080
* Container → Port 80

👉 Access in browser:

```
http://localhost:8080
```

---

## 🔁 8. Docker Workflow

1. Pull image
2. Run container
3. Check running containers
4. Stop container
5. Restart container
6. Access application

---

## 🧠 Final Understanding

Docker helps to:

* Run applications anywhere
* Maintain consistency
* Simplify deployments

---

## 🚀 Current Level

You are now at:

🔥 **Docker Beginner → Intermediate Level**

---  

# 📦 Docker Multi-Container Setup (MongoDB + Mongo Express)

## 🧠 Overview

This setup demonstrates how to run **multiple containers** and allow them to communicate using a **Docker Network**.

We use:

* MongoDB → Database
* Mongo Express → UI to access database

---

## 🎯 Goal

* Run MongoDB in a container
* Run Mongo Express in another container
* Connect both containers
* Access Mongo Express from browser

---

## 🧱 Step 1: Create a Docker Network

```bash
docker network create mongo-network
```

### 🧠 Explanation:

* Creates a private network
* Containers inside this network can communicate with each other

---

## 🗄️ Step 2: Run MongoDB Container

```bash
docker run -d \
--name mongodb \
--network mongo-network \
mongo
```

### 🧠 Explanation:

* Starts MongoDB in a container
* `--name mongodb` → container name
* `--network mongo-network` → joins the network

---

## 🌐 Step 3: Run Mongo Express Container

```bash
docker run -d \
--name mongo-express \
--network mongo-network \
-p 8081:8081 \
-e ME_CONFIG_MONGODB_SERVER=mongodb \
mongo-express
```

### 🧠 Explanation:

* Runs Mongo Express UI
* `-p 8081:8081` → access via browser
* `-e ME_CONFIG_MONGODB_SERVER=mongodb` → connect to Mongo container

---

## 🔗 How Containers Communicate

* Containers are in the same network
* They use **container names** to communicate

```text
mongo-express → mongodb
```

---

## 🌐 Access the Application

Open in browser:

```text
http://localhost:8081
```

---

## 🔍 Verify Running Containers

```bash
docker ps
```

---

## 🧠 Important Concepts

### 🔹 Docker Network

* Enables communication between containers
* Containers talk using names (not IP)

### 🔹 Container Name

* Acts as hostname inside network

### 🔹 Port Mapping (`-p`)

* Used to access container from your system
* NOT used for container-to-container communication

---

## ⚠️ Key Difference

| Feature     | Purpose                             |
| ----------- | ----------------------------------- |
| Network     | Container ↔ Container communication |
| Port (`-p`) | System ↔ Container access           |

---

## 🧠 Final Understanding

* Docker allows running multiple services as containers
* Networking connects containers
* Ports expose services to users

---

## 🚀 Outcome

You have successfully:

* Run multiple containers
* Connected them using Docker network
* Accessed application via browser

---

## 🎯 Next Step

* Learn Docker Compose
* Simplify multi-container setup using a single file

---


## 🎯 Next Step

* Learn Dockerfile
* Build custom images
* Run your own applications in containers

---

# 📦 Docker Compose – Multi-Container Setup

## 🧠 Overview

Docker Compose is used to manage **multiple containers** using a single configuration file.

Instead of running multiple `docker run` commands, we define everything in one file:

```text
docker-compose.yml
```

---

## 🎯 Purpose

* Run multiple services together
* Simplify container management
* Avoid long manual commands
* Automatically handle networking

---

## 🧱 Basic Structure of docker-compose.yml

```yaml
version: '3'

services:
  service_name:
    image:
    container_name:
    ports:
    environment:
```

---

## 🧠 Explanation of Each Section

---

### 🔹 1. Version

```yaml
version: '3'
```

* Defines the version of Docker Compose
* Optional in newer versions

---

### 🔹 2. Services (Most Important)

```yaml
services:
```

* Main section of the file
* Each service = one container

---

### 🔹 3. Service Name

```yaml
services:
  mongodb:
  mongo-express:
```

* Logical name of the container
* Used for communication between containers

---

### 🔹 4. Image

```yaml
image: mongo
```

* Defines which Docker image to use
* Equivalent to `docker run mongo`

---

### 🔹 5. Container Name

```yaml
container_name: mongodb
```

* Optional
* Assigns a custom name to the container

---

### 🔹 6. Ports

```yaml
ports:
  - "8081:8081"
```

* Maps host port to container port
* Used to access application from browser

---

### 🔹 7. Environment Variables

```yaml
environment:
  - KEY=VALUE
```

* Pass configuration values to container
* Example:

```yaml
environment:
  - ME_CONFIG_MONGODB_SERVER=mongodb
```

---

## 🌐 Networking (Automatic 🔥)

* Docker Compose automatically creates a network
* All services are connected inside this network

👉 No need to run:

```bash
docker network create
```

---

## 🔗 Container Communication

Containers communicate using **service names**

```text
mongo-express → mongodb
```

👉 Because both are in the same network

---

## 🚀 Running the Application

```bash
docker-compose up -d
```

### 🧠 What happens:

* Reads YAML file
* Pulls images
* Creates containers
* Creates network
* Starts all services

---

## 🛑 Stopping the Application

```bash
docker-compose down
```

### 🧠 What happens:

* Stops containers
* Removes containers
* Removes network

---

## 🔁 Workflow

```text
Write docker-compose.yml
        ↓
docker-compose up
        ↓
Containers start
        ↓
Services communicate
        ↓
Use application
        ↓
docker-compose down
```

---

## ⚠️ Important Concepts

| Feature     | Purpose                        |
| ----------- | ------------------------------ |
| services    | Defines containers             |
| image       | Source of container            |
| ports       | Access from browser            |
| environment | Configuration                  |
| network     | Auto-created for communication |

---

## 🧠 Final Understanding

* Docker Compose = Blueprint for multi-container apps
* Simplifies setup and management
* Enables easy communication between services

---

## 🎯 Outcome

You can now:

* Define multiple containers in one file
* Run full application with one command
* Manage containers easily

---

## 🚀 Next Step

* Practice modifying compose file
* Learn Dockerfile
* Build your own custom images

---

# 📦 Docker Learning Notes – Dockerfile & Docker Compose

---

# 🧠 Dockerfile – Building Our Own Docker Image

## What is a Dockerfile?

A Dockerfile is a **blueprint** used to build a Docker image.

It contains instructions that Docker follows step-by-step to create a custom image.

---

## Why do we need Dockerfile?

Before Dockerfile:

* Use existing images like nginx, mongo
* Run pre-built applications

With Dockerfile:

* Package our own application
* Build our own custom image
* Run application anywhere

---

## Basic Dockerfile Structure

```dockerfile id="m1"
FROM <base-image>

WORKDIR <folder>

COPY <source> <destination>

CMD ["command"]
```

---

## Dockerfile Instructions Explained

---

### 1. FROM

```dockerfile id="m2"
FROM python:3.10-slim
```

Purpose:

Defines the base image.

Meaning:

Use an existing Python environment.

Without this:

Python will not exist inside container.

---

### 2. WORKDIR

```dockerfile id="m3"
WORKDIR /app
```

Purpose:

Creates and sets the working directory inside container.

Meaning:

All files will be managed inside:

```text id="m4"
/app
```

---

### 3. COPY

```dockerfile id="m5"
COPY app.py .
```

Purpose:

Copies local files into Docker image.

Before:

Local system:

```text id="m6"
app.py
```

After:

Inside image:

```text id="m7"
/app/app.py
```

---

### 4. CMD

```dockerfile id="m8"
CMD ["python", "app.py"]
```

Purpose:

Defines what command to run when container starts.

Meaning:

Runs:

```bash id="m9"
python app.py
```

automatically.

---

# Hands-on Project (Python Info App)

Project structure:

```text id="m10"
python-info-app/
 ├── app.py
 └── Dockerfile
```

---

## app.py

```python id="q1x8mn"
import socket
import platform
from datetime import datetime

print("Current Time:", datetime.now())
print("Hostname:", socket.gethostname())
print("Python Version:", platform.python_version())
```

Purpose:

Prints:

* current time
* hostname
* python version

---

## Dockerfile

```dockerfile id="m11"
FROM python:3.10-slim

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]
```

---

# Building Docker Image

Command:

```bash id="m12"
docker build -t python-info:1.0 .
```

---

## What happens internally?

Step 1:

Docker reads Dockerfile

↓

Step 2:

Pulls base image (python)

↓

Step 3:

Creates new layers

↓

Step 4:

Copies app.py

↓

Step 5:

Stores CMD instruction

↓

Creates final custom image

---

# Image Tagging

Example:

```text id="m13"
python-info:1.0
```

Breakdown:

```text id="m14"
python-info → image name
1.0         → image tag/version
```

Purpose:

Used for versioning.

Examples:

```text id="m15"
myapp:1.0
myapp:2.0
myapp:3.0
```

---

# Running Container

Command:

```bash id="m16"
docker run python-info:1.0
```

What happens:

Docker creates a container from image and executes:

```bash id="m17"
python app.py
```

because CMD says so.

---

# Viewing Images

Command:

```bash id="m18"
docker images
```

Purpose:

Lists all available images.

---

# Viewing Logs

Command:

```bash id="m19"
docker logs <container_id>
```

Purpose:

Displays application output or errors.

---

# Entering Container

Command:

```bash id="m20"
docker exec -it <container_id> /bin/sh
```

Purpose:

Enter container shell for debugging.

---

# Dockerfile Layering Concept

Docker images are built in layers.

Example:

Layer 1:

```text id="m21"
Base OS
```

Layer 2:

```text id="m22"
Python runtime
```

Layer 3:

```text id="m23"
Application code
```

Final:

```text id="m24"
Custom Docker image
```

---

# Docker Compose Recap

## What is Docker Compose?

Docker Compose is used to manage multiple containers using one YAML file.

Instead of:

```bash id="m25"
docker run ...
docker run ...
```

Use:

```text id="m26"
docker-compose.yml
```

---

## Basic Structure

```yaml id="m27"
version: '3'

services:
  service_name:
    image:
    container_name:
    ports:
    environment:
```

---

## Important Sections

---

### version

Defines compose version.

---

### services

Defines all containers.

Each service = one container.

---

### image

Defines which image to use.

---

### container_name

Custom container name.

---

### ports

Maps host port to container port.

Used for browser access.

---

### environment

Passes configuration variables.

---

# Docker Compose Commands

---

## Start all services

```bash id="m28"
docker-compose up -d
```

What happens:

* reads YAML file
* creates containers
* creates network
* starts services

---

## Stop all services

```bash id="m29"
docker-compose down
```

What happens:

* stops containers
* removes containers
* removes network

---

# Networking Concept

Important:

Docker Compose creates network automatically.

Containers communicate using service names.

Example:

```text id="m30"
mongo-express → mongodb
```

---

# Important Difference

| Feature | Purpose                             |
| ------- | ----------------------------------- |
| Network | Container ↔ Container communication |
| Ports   | System ↔ Container communication    |

---

# What You Learned Today

✅ Dockerfile basics
✅ Build custom images
✅ Run custom containers
✅ Understand image tagging
✅ Docker layering concept
✅ Docker Compose basics
✅ Multi-container management

---

# Current Docker Level

🔥 Strong Docker Basics + Custom Image Building

---

# Next Step

* Docker Volumes
* Docker Registry
* Push images to Docker Hub
* Multi-stage builds

---
