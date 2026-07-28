# Kubernetes Zero to Hero - Day 1 Notes
# Topic: Introduction to Kubernetes & Kubernetes Architecture

## Overview

In this session, I learned the fundamentals of **Kubernetes (K8s)**, the industry-standard container orchestration platform. The session explained why Kubernetes is required in modern DevOps, how it differs from Docker, and how its architecture is designed to manage containerized applications at scale.

---

# What is Kubernetes?

Kubernetes (K8s) is an **open-source container orchestration platform** used to automate the deployment, scaling, networking, and management of containerized applications.

While Docker creates and runs containers, Kubernetes manages those containers across multiple servers.

---

# Docker vs Kubernetes

## Docker

- Container Platform
- Creates containers
- Runs containers
- Best for development and small-scale deployments

Example:

```text
Application
     │
     ▼
Docker Container
```

---

## Kubernetes

- Container Orchestration Platform
- Manages multiple containers
- Manages multiple servers
- Provides Auto Healing
- Provides Auto Scaling
- Enterprise-ready

Example:

```text
Application
      │
      ▼
Kubernetes Cluster
      │
      ├── Container 1
      ├── Container 2
      ├── Container 3
      └── Container 4
```

---

# Why Do We Need Kubernetes?

Running one or two Docker containers is easy.

However, production applications may have hundreds or thousands of containers.

Managing them manually becomes difficult because containers are **ephemeral**.

---

# What Does Ephemeral Mean?

Containers are temporary.

They can:

- Stop unexpectedly
- Crash
- Restart
- Be deleted
- Be recreated

Kubernetes automatically manages these lifecycle events.

---

# Four Major Advantages of Kubernetes

## 1. Cluster-Based Architecture

Kubernetes is designed to run applications across multiple machines called **Worker Nodes**.

Benefits:

- High Availability
- Fault Tolerance
- Better Resource Utilization
- Distributed Workloads

---

## 2. Auto Healing

Kubernetes continuously monitors application health.

If a container crashes:

```text
Container Crashes
        │
        ▼
Kubernetes Detects Failure
        │
        ▼
Creates a New Container Automatically
```

---

## 3. Auto Scaling

Kubernetes automatically increases or decreases the number of running containers depending on application traffic.

Low Traffic:

```text
2 Containers
```

High Traffic:

```text
10 Containers
```

---

## 4. Enterprise Features

Kubernetes provides several enterprise-grade capabilities:

- Load Balancing
- Service Discovery
- Advanced Networking
- Security
- Resource Management
- High Availability

---

# Docker vs Kubernetes Comparison

| Docker | Kubernetes |
|---------|------------|
| Container Platform | Container Orchestration Platform |
| Creates Containers | Manages Containers |
| Runs Individual Containers | Manages Multiple Containers |
| Limited Scaling | Automatic Scaling |
| Manual Recovery | Auto Healing |
| Single Machine | Cluster-Based |

---

# Kubernetes Architecture

A Kubernetes Cluster consists of two major parts:

```text
              Kubernetes Cluster
                     │
      ┌──────────────┴──────────────┐
      │                             │
      ▼                             ▼
 Control Plane                 Data Plane
 (Master Node)               (Worker Nodes)
```

---

# Control Plane (Master Node)

The Control Plane is the **brain** of Kubernetes.

It does **not** run applications.

Its responsibilities include:

- Managing the cluster
- Scheduling workloads
- Monitoring cluster state
- Maintaining the desired state

---

# Components of the Control Plane

```text
Control Plane
│
├── API Server
├── Scheduler
├── etcd
├── Controller Manager
└── Cloud Controller Manager
```

---

## 1. API Server

The API Server is the **heart of Kubernetes**.

Every request from users or tools passes through the API Server.

Example:

```bash
kubectl apply -f deployment.yaml
```

Flow:

```text
kubectl
    │
    ▼
API Server
    │
    ▼
Other Kubernetes Components
```

Responsibilities:

- Accepts requests
- Authenticates users
- Validates requests
- Communicates with other components

---

## 2. Scheduler

The Scheduler decides **which Worker Node should run a newly created Pod**.

It considers:

- CPU availability
- Memory availability
- Node resources
- Scheduling rules

Example:

```text
Worker 1
CPU: 90%

Worker 2
CPU: 20%

↓

Scheduler chooses Worker 2
```

---

## 3. etcd

etcd is Kubernetes' distributed **key-value database**.

It stores the complete cluster state.

Examples of stored data:

- Pods
- Nodes
- Deployments
- Services
- Secrets
- ConfigMaps
- Cluster Configuration

Flow:

```text
API Server
      │
      ▼
    etcd
```

---

## 4. Controller Manager

The Controller Manager continuously compares:

- Desired State
- Actual State

Example:

Desired Pods:

```text
3 Pods
```

Actual Pods:

```text
2 Pods
```

Controller Manager detects the difference and automatically creates another Pod.

Flow:

```text
Desired State

↓

Actual State

↓

Mismatch

↓

Create New Pod
```

This enables **Auto Healing**.

---

## 5. Cloud Controller Manager

This component integrates Kubernetes with cloud providers.

Examples:

- AWS EKS
- Azure AKS
- Google GKE

Responsibilities:

- Create Load Balancers
- Attach Cloud Storage
- Configure Cloud Networking

---

# Data Plane (Worker Nodes)

Worker Nodes perform the actual work.

Applications run here.

Each Worker Node contains:

```text
Worker Node
│
├── Kubelet
├── Kube Proxy
├── Container Runtime
└── Pods
```

---

## 1. Kubelet

Kubelet is the primary agent running on every Worker Node.

Responsibilities:

- Receives instructions from API Server
- Starts Pods
- Stops Pods
- Monitors Pod Health
- Reports Node Status

Flow:

```text
API Server

↓

Kubelet

↓

Container Runtime

↓

Pod Created
```

---

## 2. Container Runtime

The Container Runtime is responsible for running containers.

Examples:

- containerd
- CRI-O

Responsibilities:

- Pull Images
- Start Containers
- Stop Containers
- Delete Containers

---

## 3. Kube Proxy

Kube Proxy manages networking inside the cluster.

Responsibilities:

- Routes traffic
- Enables Pod communication
- Supports Service networking
- Performs Load Balancing

Example:

```text
User Request

↓

Kube Proxy

↓

Pod 1
Pod 2
Pod 3
```

---

# Kubernetes Request Flow

Example:

```bash
kubectl apply -f nginx.yaml
```

Execution Flow:

```text
User
   │
   ▼
kubectl
   │
   ▼
API Server
   │
   ▼
Store Desired State in etcd
   │
   ▼
Scheduler Selects Worker Node
   │
   ▼
Kubelet Receives Instructions
   │
   ▼
Container Runtime Starts Container
   │
   ▼
Kube Proxy Routes Traffic
```

---

# Docker vs Kubernetes Architecture

| Docker | Kubernetes |
|---------|------------|
| Docker CLI | kubectl |
| Docker Daemon | API Server |
| Docker Engine | Container Runtime |
| Single Machine | Cluster |
| Manual Container Management | Automated Cluster Management |

---

# Topics Learned

After completing Day 1, I learned:

- What Kubernetes is
- Difference between Docker and Kubernetes
- Container Orchestration
- Ephemeral Containers
- Cluster Architecture
- Auto Healing
- Auto Scaling
- Enterprise Features
- Kubernetes Control Plane
- Kubernetes Data Plane
- API Server
- Scheduler
- etcd
- Controller Manager
- Cloud Controller Manager
- Kubelet
- Container Runtime
- Kube Proxy
- Complete Kubernetes Request Flow

---

# Interview Questions

## What is Kubernetes?

Kubernetes is an open-source container orchestration platform used to automate the deployment, scaling, networking, and management of containerized applications.

---

## What is the difference between Docker and Kubernetes?

Docker creates and runs containers, whereas Kubernetes manages, scales, and orchestrates containers across multiple machines.

---

## What are the four major advantages of Kubernetes?

- Cluster-Based Architecture
- Auto Healing
- Auto Scaling
- Enterprise Features

---

## What is the Control Plane?

The Control Plane is the management layer of Kubernetes responsible for scheduling workloads, maintaining cluster state, and managing the entire cluster.

---

## What is the Data Plane?

The Data Plane consists of Worker Nodes that execute applications and run Pods.

---

## What is the role of the API Server?

The API Server is the central communication hub of Kubernetes. It receives, validates, and processes all requests.

---

## What is etcd?

etcd is Kubernetes' distributed key-value database that stores the complete cluster state and configuration.

---

## What is the Scheduler?

The Scheduler selects the best Worker Node for newly created Pods based on available resources.

---

## What is the Controller Manager?

It ensures that the actual cluster state always matches the desired state by continuously monitoring and correcting differences.

---

## What is Kubelet?

Kubelet is the primary agent running on every Worker Node. It manages Pods and communicates with the API Server.

---

## What is Kube Proxy?

Kube Proxy manages networking, routing, and communication between Pods and Services.

---

# Key Takeaways

- Docker creates and runs containers.
- Kubernetes manages containers across clusters.
- Containers are ephemeral, making orchestration essential.
- Kubernetes provides Auto Healing and Auto Scaling.
- The Control Plane makes decisions for the cluster.
- Worker Nodes execute workloads.
- Every Kubernetes request flows through the API Server.
- The Scheduler selects the best node for Pods.
- etcd stores the cluster state.
- The Controller Manager maintains the desired state.
- Kubelet, Container Runtime, and Kube Proxy work together to run and manage Pods.

---

# One-Line Summary

**Kubernetes is an open-source container orchestration platform that automates the deployment, scaling, networking, and management of containerized applications through a Control Plane that manages the cluster and Worker Nodes that execute application workloads.**
