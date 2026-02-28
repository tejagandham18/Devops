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
