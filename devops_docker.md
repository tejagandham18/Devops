# DevOps Day 4 Notes
# Containers & Docker Fundamentals

---

# 1️⃣ What is a Container?

A container is a lightweight package that includes:

- Application code
- Runtime
- Libraries
- Dependencies
- Configuration files

It ensures the application runs the same in every environment.

---

## 📌 Simple Definition

A container is a portable unit that packages an application and its dependencies so it runs consistently everywhere.

---

## 🧠 Why Containers Are Needed

Before containers:

- Application works on developer machine
- Fails in testing server
- Breaks in production

This problem is called:
"It works on my machine" problem.

Containers solve this by packaging everything together.

---

# 2️⃣ Container vs Virtual Machine

| Feature | Container | Virtual Machine |
|----------|------------|----------------|
| OS | Shares host OS | Separate OS |
| Size | Lightweight (MBs) | Heavy (GBs) |
| Startup Time | Seconds | Minutes |
| Resource Usage | Low | High |

Containers are faster and more efficient.

---

# 3️⃣ What is Docker?

Docker is a container platform used to:

- Build containers
- Run containers
- Manage containers

It is the most widely used container tool in DevOps.

---

## 📌 Simple Definition

Docker is a tool that allows you to create, deploy, and run applications inside containers.

---

# 4️⃣ Important Docker Concepts

## 🔹 Docker Image
Blueprint of an application.

## 🔹 Docker Container
Running instance of an image.

## 🔹 Dockerfile
Instruction file used to build a Docker image.

## 🔹 Docker Hub
Online registry where Docker images are stored.

---

# 5️⃣ Can DevOps Run Only on Linux?

No.

DevOps can run on:
- Windows
- macOS
- Linux
- Cloud platforms

---

## 🧠 Why Linux is Popular in DevOps?

- Most production servers use Linux
- Cloud systems are Linux-based
- Docker runs natively on Linux
- Better stability and performance

You can practice on Windows, but production mostly uses Linux.

---

# 6️⃣ What is Containerization?

Containerization is the process of packaging an application and its dependencies into a Docker container.

---

# 7️⃣ How We Containerize an Application

Step 1: Write application code

Step 2: Create Dockerfile

Example Dockerfile:

FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]

---

Step 3: Build Docker Image

docker build -t myapp .

---

Step 4: Run Container

docker run myapp

---

# 8️⃣ DevOps Workflow with Docker

Code → Dockerfile → Build Image → Push to Registry → Deploy Container → CI/CD Automation

---

# 🎯 Interview Summary

Container:
A lightweight portable package that includes application and dependencies.

Docker:
A container platform used to build and manage containers.

Containerization:
The process of packaging an application into a container.

DevOps OS:
DevOps is not limited to Linux, but Linux is widely used in production.

---

✅ End of Day 4 DevOps Notes

# DevOps Day 5 Notes
# Mandatory Docker Commands

---

# 1️⃣ Introduction

Docker is a container platform used to build, run, and manage containers.

In DevOps projects, we do not use all Docker commands.
We mainly use a core set of essential commands daily.

This document covers the most important Docker commands that every DevOps engineer must know.

---

# 2️⃣ Image Management Commands

These commands are used to manage Docker images.

---

## 🔹 docker --version

docker --version

Purpose:
Checks whether Docker is installed properly and displays the version.

---

## 🔹 docker pull

docker pull nginx

Purpose:
Downloads an image from Docker Hub.
Used when running ready-made applications.

---

## 🔹 docker images

docker images

Purpose:
Lists all downloaded Docker images available locally.

---

## 🔹 docker build

docker build -t myapp .

Purpose:
Builds a Docker image from a Dockerfile.
Used to containerize custom applications.

---

# 3️⃣ Container Management Commands

These commands are used to create, run, and manage containers.

---

## 🔹 docker run

docker run nginx

Purpose:
Creates and starts a container from an image.

---

## 🔹 docker run -d

docker run -d nginx

Purpose:
Runs a container in detached (background) mode.
Used in production environments.

---

## 🔹 docker ps

docker ps

Purpose:
Shows currently running containers.

---

## 🔹 docker ps -a

docker ps -a

Purpose:
Shows all containers (running + stopped).

---

## 🔹 docker stop

docker stop container_id

Purpose:
Stops a running container safely.

---

## 🔹 docker rm

docker rm container_id

Purpose:
Removes (deletes) a stopped container.

---

# 4️⃣ Debugging & Monitoring Commands

These commands help in troubleshooting containers.

---

## 🔹 docker logs

docker logs container_id

Purpose:
Displays logs of a container.
Used to debug application errors.

---

## 🔹 docker exec

docker exec -it container_id bash

Purpose:
Accesses the running container terminal.
Used for troubleshooting inside container.

---

## 🔹 docker system df

docker system df

Purpose:
Displays Docker disk usage.
Helps monitor storage usage.

---

# 5️⃣ Cleanup Commands

These commands help free disk space.

---

## 🔹 docker rmi

docker rmi image_name

Purpose:
Removes a Docker image.

---

## 🔹 docker system prune -a

docker system prune -a

Purpose:
Removes unused containers, images, and networks.
Used to clean up disk space.

---

# 6️⃣ Most Important Docker Commands (Top 10)

These commands are most frequently used in DevOps:

- docker pull
- docker images
- docker build
- docker run
- docker ps
- docker stop
- docker rm
- docker logs
- docker exec
- docker system prune

Mastering these commands allows handling most real-world Docker tasks.

---

# 7️⃣ Real DevOps Workflow Example

Step 1: Build Image  
docker build -t myapp .

Step 2: Run Container  
docker run -d -p 8080:80 myapp

Step 3: Check Running Containers  
docker ps

Step 4: Check Logs  
docker logs container_id

Step 5: Stop Container  
docker stop container_id

---

# 🎯 Interview Summary

Docker is a container platform used in DevOps to build and manage containers.

Mandatory Docker commands include:
docker build, docker run, docker ps, docker stop, docker logs, docker exec, and docker system prune.

These commands are used for building images, running containers, monitoring applications, and managing system resources.

---

✅ End of Day 5 DevOps Notes
