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

# DevOps Day 6 Notes
# Linux Basics, Namespaces, cgroups & Docker Architecture

---

# 1. How Linux Works

Linux is an operating system that manages system hardware and runs applications.

Linux architecture consists of several layers.
Applications
↓
System Libraries
↓
Linux Kernel
↓
Hardware


## Components

### Applications
Programs such as web servers, databases, browsers, and command-line tools.

### System Libraries
Provide functions that allow applications to communicate with the Linux kernel.

### Linux Kernel
The core part of the operating system that manages system resources.

### Hardware
Physical components such as CPU, memory, disk, and network devices.

---

# 2. Responsibilities of the Linux Kernel

The Linux kernel manages the following:

- Process management
- Memory management
- Device drivers
- File systems
- Networking
- Resource allocation

All applications interact with hardware through the kernel.

---

# 3. What is Linux Namespace

A namespace provides **isolation for processes** in Linux.

It ensures that processes running inside a container cannot see or affect processes outside that container.

## Simple Definition

A Linux namespace isolates system resources for a group of processes.

This is one of the key technologies used to create containers.

---

## Example

Without namespace:

System  
├── Process A  
├── Process B  
└── Process C  

All processes can see each other.

With namespace:

Container 1  
└── Process A  

Container 2  
└── Process B  

Processes are isolated.

---

## Types of Namespaces

| Namespace | Purpose |
|----------|--------|
| PID | Isolates process IDs |
| NET | Isolates network interfaces |
| MNT | Isolates file system mounts |
| IPC | Isolates interprocess communication |
| UTS | Isolates hostname and domain name |
| USER | Isolates user and group IDs |

---

# 4. What is Linux cgroups

cgroups stands for **Control Groups**.

It is used to **limit and manage system resources** used by processes.

## Simple Definition

Linux cgroups control how much CPU, memory, disk, or network resources a process can use.

---

## Example

Without cgroups:

Container A uses 90% CPU  
Container B gets very little CPU

With cgroups:

Container A limited to 50% CPU  
Container B limited to 50% CPU

Resources are distributed properly.

---

## Resources Controlled by cgroups

- CPU usage
- Memory usage
- Disk I/O
- Network bandwidth

---

# 5. Containers Use Namespaces and cgroups

Containers rely on two Linux features:

Namespaces → Process isolation  
cgroups → Resource control

Together they allow multiple containers to run safely on the same host system.

---

# 6. Docker Architecture

Docker follows a **client-server architecture**.

Main components:

- Docker Client
- Docker Daemon
- Docker Host
- Docker Images
- Docker Containers
- Docker Registry

---

# 7. Docker Client

The Docker Client is the interface used to interact with Docker.

Example commands:
docker run nginx
docker build .
docker pull ubuntu


The client sends commands to the Docker daemon.

---

# 8. Docker Daemon

The Docker daemon (dockerd) runs in the background and manages Docker operations.

Responsibilities include:

- Building images
- Running containers
- Managing networks
- Managing volumes
- Communicating with Docker registries

---

# 9. Docker Host

The Docker Host is the machine where Docker runs.

It contains:

- Docker daemon
- Containers
- Images
- Networks
- Volumes

The host can be:

- Local machine
- Server
- Cloud instance

---

# 10. Docker Images

A Docker image is a blueprint used to create containers.

Images include:

- Application code
- Libraries
- Dependencies
- Runtime environment

Example images:

- nginx
- ubuntu
- python

Images are read-only templates.

---

# 11. Docker Containers

A container is a running instance of a Docker image.

Example:

Image → Blueprint  
Container → Running application

Example command:
docker run nginx


---

# 12. Docker Registry

A Docker registry stores Docker images.

The most popular registry is **Docker Hub**.

Developers can:

- Pull images
- Push images
- Share images

Example commands:
docker pull nginx
docker push myimage


---

# 13. Docker Workflow

When a container is started:

1. User runs a command using Docker client
2. Client sends request to Docker daemon
3. Daemon checks if the image exists locally
4. If not, it pulls the image from Docker registry
5. Docker daemon creates the container
6. Container starts running

---

# Interview Summary

Linux Kernel manages system resources and hardware.

Linux Namespaces provide process isolation.

Linux cgroups control resource allocation such as CPU and memory.

Docker uses namespaces and cgroups to run containers.

Docker architecture consists of Docker Client, Docker Daemon, Docker Images, Containers, and Docker Registry.

---

End of Day 6 DevOps Notes
