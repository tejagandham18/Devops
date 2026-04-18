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

## 🎯 Next Step

* Learn Dockerfile
* Build custom images
* Run your own applications in containers

---

