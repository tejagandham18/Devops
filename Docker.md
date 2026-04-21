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

