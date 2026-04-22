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
