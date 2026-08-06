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

# Kubernetes Zero to Hero - Day 2 Notes
# Topic: Kubernetes Installation & Pods

## Overview

In this session, I learned how to set up a local Kubernetes environment using **Minikube** and understood the most fundamental object in Kubernetes: the **Pod**.

Unlike Docker, where we directly create and manage containers, Kubernetes manages applications through **Pods**, which act as wrappers around one or more containers.

---

# Why Do We Need a Local Kubernetes Cluster?

In real-world environments, Kubernetes clusters are usually deployed on cloud platforms such as:

- AWS Elastic Kubernetes Service (EKS)
- Azure Kubernetes Service (AKS)
- Google Kubernetes Engine (GKE)

However, using cloud resources for learning can incur costs.

To avoid these costs, Kubernetes can be installed locally using **Minikube**, allowing developers to practice and test applications on their own computers.

---

# What is Minikube?

**Minikube** is a tool that creates a **single-node Kubernetes cluster** on your local machine.

Instead of manually installing every Kubernetes component, Minikube automatically performs the setup.

When we execute:

```bash
minikube start
```

Minikube automatically:

- Creates a Virtual Machine (or Container depending on the driver)
- Installs Kubernetes
- Starts the API Server
- Starts the Scheduler
- Starts etcd
- Starts the Controller Manager
- Creates a Worker Node
- Makes the cluster ready for use

Flow:

```text
minikube start
        │
        ▼
Create Local Kubernetes Cluster
        │
        ▼
Start Control Plane Components
        │
        ▼
Create Worker Node
        │
        ▼
Cluster Ready
```

---

# Minimum Requirements

To run Minikube smoothly, the system should have:

- 2 CPUs
- 2 GB RAM
- 20 GB Free Disk Space
- Hypervisor (VirtualBox, HyperKit, Docker Driver, etc.)

---

# What is a Hypervisor?

A Hypervisor is software that allows a Virtual Machine (VM) to run on your computer.

Example:

```text
Laptop
   │
   ▼
Hypervisor
   │
   ▼
Virtual Machine
   │
   ▼
Kubernetes Cluster
```

---

# Tools Required

## 1. Minikube

Minikube creates and manages a local Kubernetes cluster.

It is mainly used for:

- Learning Kubernetes
- Local Development
- Testing Applications

---

## 2. kubectl

**kubectl** is the command-line tool used to communicate with the Kubernetes cluster.

Just as Docker uses the `docker` command, Kubernetes uses the `kubectl` command.

Examples:

Docker

```bash
docker ps
docker images
docker run
```

Kubernetes

```bash
kubectl get pods
kubectl get nodes
kubectl apply -f pod.yaml
```

---

# Starting the Kubernetes Cluster

Command:

```bash
minikube start
```

This command starts the local Kubernetes cluster.

---

# Verifying the Cluster

To verify whether the cluster is running:

```bash
kubectl get nodes
```

Example Output:

```text
NAME         STATUS
minikube     Ready
```

If the node status is **Ready**, the cluster has started successfully.

---

# Understanding Pods

A **Pod** is the **smallest deployable unit in Kubernetes**.

Unlike Docker, Kubernetes does **not** manage containers directly.

Instead, Kubernetes manages **Pods**, and Pods contain one or more containers.

---

# Docker vs Kubernetes

## Docker

Docker directly manages containers.

```text
Docker
   │
Container
```

---

## Kubernetes

Kubernetes manages Pods.

Pods manage Containers.

```text
Kubernetes
      │
      ▼
     Pod
      │
      ▼
Container
```

This is one of the biggest differences between Docker and Kubernetes.

---

# What is a Pod?

A Pod is a wrapper around one or more containers.

It provides:

- Shared Network
- Shared Storage
- Shared Lifecycle

Containers inside a Pod start together, stop together, and communicate easily with each other.

---

# Single Container Pod

Most applications use one container inside one Pod.

Example:

```text
Pod
 │
 └── Nginx Container
```

This is the most common deployment pattern.

---

# Multi-Container Pod

Sometimes multiple containers need to work together.

Example:

```text
Pod
│
├── Application Container
└── Logging Container
```

Both containers:

- Share the same network
- Share storage
- Start together
- Stop together

This pattern is commonly used for:

- Sidecar Containers
- Logging Agents
- Monitoring Agents
- Init Containers

---

# Why Does Kubernetes Use Pods?

Instead of managing individual containers, Kubernetes groups related containers inside a Pod.

Benefits include:

- Easier Management
- Shared Resources
- Better Communication
- Single Scheduling Unit

This makes application management much simpler in large-scale environments.

---

# Kubernetes Uses YAML Files

Docker usually creates containers using long command-line instructions.

Example:

```bash
docker run -d -p 80:80 nginx
```

Kubernetes follows a **Declarative** approach.

Instead of giving long commands, we define the desired configuration inside a YAML file.

Example:

```yaml
apiVersion: v1
kind: Pod

metadata:
  name: nginx-pod

spec:
  containers:
    - name: nginx
      image: nginx
```

Kubernetes reads this file and creates the Pod automatically.

---

# Imperative vs Declarative

## Docker (Imperative)

We tell Docker **how** to run the application.

Example:

```bash
docker run nginx
```

---

## Kubernetes (Declarative)

We describe **what** we want.

Example:

```yaml
kind: Pod
```

Kubernetes decides how to achieve the desired state.

---

# Creating a Pod

Command:

```bash
kubectl apply -f pod.yaml
```

Execution Flow:

```text
Developer
     │
     ▼
kubectl apply
     │
     ▼
API Server
     │
     ▼
Scheduler
     │
     ▼
Worker Node
     │
     ▼
Kubelet
     │
     ▼
Container Runtime
     │
     ▼
Pod Created
```

---

# Pod Limitations

Although Pods are the smallest deployment unit, they are **not recommended for production environments**.

If a Pod crashes:

```text
Pod
 │
Crash
 │
 ▼
Application Down
```

Kubernetes will **not automatically recreate** a standalone Pod.

---

# How Is This Solved?

Kubernetes introduces higher-level objects called **Deployments**.

A Deployment manages Pods by providing:

- Auto Healing
- Auto Scaling
- Rolling Updates
- Rollbacks

Example:

```text
Deployment
      │
      ▼
3 Pods

One Pod Crashes

↓

Deployment Creates New Pod

↓

Application Continues Running
```

Deployments will be covered in upcoming classes.

---

# Docker vs Kubernetes Comparison

| Docker | Kubernetes |
|---------|------------|
| Smallest Unit: Container | Smallest Unit: Pod |
| docker CLI | kubectl CLI |
| Imperative Commands | Declarative YAML |
| Manages Containers | Manages Pods |
| Best for Single Host | Best for Cluster Management |

---

# Topics Learned

After completing today's session, I learned:

- Why we use Minikube
- Local Kubernetes Installation
- Hypervisor Basics
- kubectl
- Starting a Kubernetes Cluster
- Verifying Cluster Status
- What is a Pod
- Pod Architecture
- Single Container Pods
- Multi-Container Pods
- Why Kubernetes Uses Pods
- YAML Manifests
- Imperative vs Declarative Configuration
- Pod Creation Flow
- Limitations of Pods
- Why Deployments Are Needed

---

# Interview Questions

## What is Minikube?

Minikube is a tool that creates a local single-node Kubernetes cluster for development, testing, and learning purposes.

---

## What is kubectl?

kubectl is the command-line interface used to communicate with and manage Kubernetes clusters.

---

## What is a Pod?

A Pod is the smallest deployable unit in Kubernetes. It acts as a wrapper around one or more containers that share networking, storage, and lifecycle.

---

## Why does Kubernetes use Pods instead of directly managing containers?

Pods provide a shared execution environment for one or more closely related containers, making scheduling, networking, and resource sharing easier.

---

## Can a Pod contain multiple containers?

Yes. Although most Pods contain a single container, Kubernetes supports multiple containers within the same Pod when they need to work together closely.

---

## Why are standalone Pods not used in production?

Standalone Pods do not provide features such as auto-healing, auto-scaling, or rolling updates. These capabilities are provided by Deployments.

---

# Key Takeaways

- Minikube creates a local Kubernetes cluster.
- kubectl is the CLI used to communicate with Kubernetes.
- Kubernetes manages Pods, not individual containers.
- Pods wrap one or more containers.
- YAML files define the desired state of Kubernetes resources.
- Kubernetes follows a Declarative approach.
- Standalone Pods are mainly used for learning and testing.
- Deployments are used in production to manage Pods.

---

# One-Line Summary

**Today's class focused on setting up a local Kubernetes environment using Minikube and understanding Pods, the smallest deployable unit in Kubernetes that encapsulates one or more containers and serves as the foundation for running applications in a Kubernetes cluster.**

# Kubernetes Zero to Hero - Day 3 Notes
# Topic: Kubernetes Deployments

## Overview

In this session, I learned about **Deployments**, one of the most important resources in Kubernetes.

Although a **Pod** is the smallest deployable unit in Kubernetes, it is **not suitable for production environments** because it does not provide features like Auto-Healing or Auto-Scaling.

To overcome these limitations, Kubernetes provides **Deployments**, which manage Pods through **ReplicaSets** and ensure applications remain highly available.

---

# Why Do We Need Deployments?

Suppose we create a standalone Pod.

```text
Pod
│
└── Nginx Container
```

The application is running successfully.

Now imagine the Pod crashes.

```text
Pod
│
❌ Crash
```

Result:

```text
Running Pods = 0
```

The application becomes unavailable because Kubernetes will **not automatically recreate a standalone Pod**.

This is why Deployments are used.

---

# What is a Deployment?

A **Deployment** is a Kubernetes resource that manages the lifecycle of Pods.

It provides:

- Auto Healing
- Auto Scaling
- Rolling Updates
- Rollbacks
- Desired State Management

Instead of creating Pods directly, we create a Deployment.

---

# Kubernetes Hierarchy

Deployments do not create Pods directly.

The actual hierarchy is:

```text
Deployment
      │
      ▼
ReplicaSet
      │
      ▼
Pods
      │
      ▼
Containers
```

Each component has its own responsibility.

---

# Role of Each Component

## Deployment

The Deployment is responsible for:

- Managing ReplicaSets
- Scaling applications
- Performing Rolling Updates
- Performing Rollbacks
- Maintaining the desired application state

---

## ReplicaSet

The ReplicaSet is responsible for:

- Creating Pods
- Monitoring Pods
- Maintaining the required number of Pod replicas

---

## Pod

The Pod is responsible for running one or more containers.

---

## Container

The Container runs the actual application.

Example:

- Nginx
- Node.js
- Python Application
- Java Application

---

# Desired State vs Actual State

This is one of the most important concepts in Kubernetes.

## Desired State

Desired State refers to what the user wants.

Example:

```yaml
replicas: 3
```

Meaning:

> "I always want 3 Pods running."

---

## Actual State

Actual State refers to what is currently running inside the cluster.

Initially:

```text
Pod 1

Pod 2

Pod 3
```

Desired State = 3 Pods

Actual State = 3 Pods

Everything is working correctly.

---

Suppose Pod 2 crashes.

Now:

```text
Pod 1

Pod 3
```

Actual State = 2 Pods

Desired State = 3 Pods

ReplicaSet detects the difference.

```text
Desired = 3

Actual = 2
```

ReplicaSet immediately creates a new Pod.

```text
Pod 1

Pod 2 (New)

Pod 3
```

Actual State becomes equal to the Desired State.

---

# Auto Healing

Auto Healing means automatically recovering from failures.

Example:

```text
Deployment

↓

ReplicaSet

↓

3 Pods

↓

One Pod Crashes

↓

ReplicaSet Creates New Pod

↓

Again 3 Pods Running
```

The application continues running without manual intervention.

---

# Auto Scaling

Deployments also support scaling.

Suppose the application initially requires:

```yaml
replicas: 3
```

Later, user traffic increases.

We simply update:

```yaml
replicas: 6
```

Kubernetes automatically creates three additional Pods.

Similarly, decreasing the replica count removes unnecessary Pods.

---

# Deployment Workflow

When we execute:

```bash
kubectl apply -f deployment.yaml
```

The execution flow is:

```text
Developer
      │
      ▼
kubectl apply
      │
      ▼
API Server
      │
      ▼
Deployment Created
      │
      ▼
Deployment Creates ReplicaSet
      │
      ▼
ReplicaSet Creates Pods
      │
      ▼
Scheduler Selects Worker Node
      │
      ▼
Kubelet Starts Containers
      │
      ▼
Application Running
```

---

# Why Not Create Pods Directly?

Creating Pods directly has several disadvantages.

- No Auto Healing
- No Auto Scaling
- No Rolling Updates
- No Rollbacks
- Not suitable for production

Instead, Deployments should be used.

---

# Standalone Pod vs Deployment

| Standalone Pod | Deployment |
|----------------|------------|
| Creates a Pod directly | Creates and manages ReplicaSets |
| No Auto Healing | Supports Auto Healing |
| No Auto Scaling | Supports Scaling |
| Suitable for learning/testing | Suitable for production |
| Manual management | Automated management |

---

# Advantages of Deployments

- Maintains the desired number of Pods
- Automatically recreates failed Pods
- Easy scaling by changing replica count
- Supports Rolling Updates
- Supports Rollbacks
- Enterprise-ready
- High Availability

---

# Real-World Analogy

Imagine a company.

Employees perform the actual work.

A Manager supervises the employees.

If one employee resigns, the manager hires another employee.

Similarly:

```text
Deployment
      │
Manager
      │
      ▼
ReplicaSet
      │
Supervisor
      │
      ▼
Pods
      │
Employees
```

The Deployment manages the ReplicaSet, and the ReplicaSet ensures that the required number of Pods are always available.

---

# Docker vs Kubernetes

| Docker | Kubernetes |
|---------|------------|
| docker run creates a container | Deployment creates Pods through ReplicaSets |
| Manual restart if container crashes | Automatic Pod recreation |
| Manual scaling | Automatic scaling |
| Single-machine management | Cluster-wide management |

---

# Topics Learned

After completing today's session, I learned:

- What is a Deployment
- Why Deployments are needed
- Limitations of Standalone Pods
- Deployment Architecture
- ReplicaSets
- Desired State
- Actual State
- Auto Healing
- Auto Scaling
- Deployment Workflow
- Deployment vs Standalone Pod

---

# Interview Questions

## What is a Deployment in Kubernetes?

A Deployment is a Kubernetes resource that manages Pods through ReplicaSets and provides features such as Auto-Healing, Auto-Scaling, Rolling Updates, and Rollbacks.

---

## Why are Deployments used instead of Pods?

Standalone Pods do not automatically recover from failures or support scaling. Deployments solve these problems by managing ReplicaSets and maintaining the desired number of Pods.

---

## What is a ReplicaSet?

A ReplicaSet is responsible for creating and maintaining the required number of Pod replicas. If a Pod fails, it automatically creates a replacement Pod.

---

## What is Desired State?

Desired State is the configuration defined by the user, such as the number of Pod replicas that should always be running.

---

## What is Actual State?

Actual State is the current condition of the Kubernetes cluster, including the number of Pods that are actually running.

---

## What is Auto Healing?

Auto Healing is the ability of Kubernetes to automatically recreate failed Pods so that the actual state matches the desired state.

---

## What is Auto Scaling?

Auto Scaling allows Kubernetes to increase or decrease the number of Pods based on the configured replica count or workload requirements.

---

# Key Takeaways

- Pods are the smallest deployable unit in Kubernetes.
- Standalone Pods are not suitable for production.
- Deployments manage applications through ReplicaSets.
- ReplicaSets maintain the desired number of Pods.
- Desired State is defined by the user.
- Actual State is continuously monitored by Kubernetes.
- If a Pod crashes, ReplicaSet automatically creates a replacement.
- Deployments provide Auto-Healing, Auto-Scaling, Rolling Updates, and Rollbacks.

---

# One-Line Summary

**A Deployment is a Kubernetes resource that manages ReplicaSets and Pods, ensuring the application's desired state is maintained through features like Auto-Healing, Auto-Scaling, Rolling Updates, and Rollbacks, making it the standard way to run applications in production.**


# Kubernetes Zero to Hero - Day 4 Notes
# Topic: Kubernetes Services

## Overview

In this session, I learned about **Kubernetes Services**, which provide a stable way to access applications running inside a Kubernetes cluster.

Pods are **ephemeral**, meaning they can be restarted, recreated, or deleted at any time. Because of this, their IP addresses change frequently, making it unreliable to access Pods directly.

A **Service** solves this problem by providing a **stable network endpoint** that routes traffic to the correct Pods.

---

# Why Do We Need a Service?

Suppose we have a Deployment with three Pods.

```text
Deployment
      │
      ▼
ReplicaSet
      │
      ▼
Pod 1 → 10.244.1.5

Pod 2 → 10.244.1.8

Pod 3 → 10.244.1.10
```

A user accesses:

```text
10.244.1.5
```

Everything works.

Now Pod 1 crashes.

ReplicaSet automatically creates a new Pod.

```text
Old Pod

10.244.1.5 ❌

↓

New Pod

10.244.1.25
```

The old IP no longer exists.

Any application trying to access the old IP will fail.

This is why Kubernetes introduces **Services**.

---

# What is a Kubernetes Service?

A Service is a Kubernetes resource that provides a **stable IP address and DNS name** for accessing one or more Pods.

Instead of communicating directly with Pod IP addresses, applications communicate with the Service.

Flow:

```text
Users
   │
   ▼
Service
   │
   ▼
Pods
```

The Service remains constant even if Pods are recreated.

---

# Responsibilities of a Service

A Kubernetes Service provides three major functionalities:

- Load Balancing
- Service Discovery
- Exposing Applications

---

# 1. Load Balancing

Load Balancing means distributing incoming requests evenly across multiple Pods.

Suppose a Deployment creates three Pods.

```text
Pod 1

Pod 2

Pod 3
```

If 300 users access the application, sending all traffic to one Pod would overload it.

Without Load Balancing:

```text
300 Users

↓

Pod 1 ❌

Pod 2 (Idle)

Pod 3 (Idle)
```

With Load Balancing:

```text
            Service
               │
    ┌──────────┼──────────┐
    ▼          ▼          ▼
  Pod 1      Pod 2      Pod 3
```

Traffic distribution:

```text
User 1 → Pod 1

User 2 → Pod 2

User 3 → Pod 3

User 4 → Pod 1

User 5 → Pod 2

User 6 → Pod 3
```

Benefits:

- Better Performance
- Even Resource Utilization
- High Availability
- Prevents Overloading

---

# Real-World Example

Imagine a supermarket.

One cashier:

```text
100 Customers

↓

Cashier 1
```

Long waiting time.

Three cashiers:

```text
100 Customers

↓

Cashier 1

Cashier 2

Cashier 3
```

Customers are distributed evenly.

Kubernetes Services work the same way.

---

# 2. Service Discovery

Pods are temporary.

Whenever a Pod restarts, its IP address changes.

Example:

```text
Backend Pod

↓

10.244.1.5
```

After restart:

```text
10.244.1.20
```

If another application is using the old IP, communication fails.

Instead, Kubernetes provides a Service.

Example:

```text
Frontend

↓

backend-service

↓

Backend Pods
```

Applications communicate using the Service name instead of Pod IP addresses.

Benefits:

- Stable Communication
- No Need to Track Pod IPs
- Reliable Networking

---

# Real-World Example

Instead of calling an employee directly, customers call the company's customer care number.

Employees may change.

The customer care number remains the same.

Similarly:

```text
Applications

↓

Service

↓

Pods
```

---

# 3. Exposing Applications

Pods are only accessible inside the Kubernetes cluster.

To allow communication, Kubernetes provides different Service types.

---

# Service Types

## 1. ClusterIP

ClusterIP is the default Service type.

It allows communication **only inside the Kubernetes cluster**.

Example:

```text
Frontend Pod

↓

ClusterIP Service

↓

Backend Pods
```

Internet users cannot access the application.

Use Cases:

- Backend APIs
- Databases
- Redis
- Internal Microservices

Diagram:

```text
Internet

❌

---------------------------

Kubernetes Cluster

↓

ClusterIP Service

↓

Backend Pods
```

---

## 2. NodePort

NodePort exposes the application on a specific port of every Worker Node.

Example:

```text
Worker Node

192.168.1.20:30080
```

Anyone who has access to the Worker Node can access the application.

Flow:

```text
User

↓

Worker Node

↓

NodePort

↓

Pods
```

Example URL:

```
http://192.168.1.20:30080
```

Use Cases:

- Local Testing
- Learning Kubernetes
- Small Applications

---

## 3. LoadBalancer

LoadBalancer is mainly used in cloud environments such as:

- AWS EKS
- Azure AKS
- Google GKE

When we create:

```yaml
type: LoadBalancer
```

The cloud provider automatically provisions a Load Balancer.

Flow:

```text
Internet

↓

Cloud Load Balancer

↓

Kubernetes Service

↓

Pods
```

Benefits:

- Public IP Address
- External Access
- Automatic Load Balancing

Use Cases:

- Production Applications
- Public Websites
- Enterprise Systems

---

# How Does a Service Know Which Pods to Send Traffic To?

Services identify Pods using **Labels** and **Selectors**.

---

## Step 1: Labels

Each Pod contains labels.

Example:

```yaml
metadata:
  labels:
    app: nginx
```

Suppose we have:

```text
Pod 1

app = nginx

----------------

Pod 2

app = nginx

----------------

Pod 3

app = nginx
```

---

## Step 2: Selector

The Service defines a selector.

Example:

```yaml
selector:
  app: nginx
```

The Service compares the selector with Pod labels.

Matching Pods receive traffic.

Flow:

```text
Service

↓

Selector

app = nginx

↓

Pod 1 ✔

Pod 2 ✔

Pod 3 ✔
```

---

## What Happens If Labels Don't Match?

Suppose:

```text
Pod 1

app = nginx ✔

----------------

Pod 2

app = nginx ✔

----------------

Pod 3

app = apache ❌
```

Service:

```yaml
selector:
  app: nginx
```

Traffic is sent only to:

```text
Pod 1

Pod 2
```

Pod 3 is ignored because its label does not match.

---

# Complete Request Flow

Suppose a user accesses the application.

```text
Browser
     │
     ▼
LoadBalancer / NodePort
     │
     ▼
Kubernetes Service
     │
Selector: app=nginx
     │
     ▼
Pod 1

Pod 2

Pod 3
```

The Service automatically distributes traffic among the matching Pods.

---

# Kubernetes Workflow So Far

After completing today's class, the Kubernetes workflow looks like this:

```text
Deployment
      │
      ▼
ReplicaSet
      │
      ▼
Pods
      │
      ▼
Service
      │
      ▼
Users
```

Cloud Deployment:

```text
Internet
      │
      ▼
Cloud Load Balancer
      │
      ▼
Kubernetes Service
      │
      ▼
Pods
```

---

# KubeShark

KubeShark is a network monitoring and visualization tool for Kubernetes.

It helps developers:

- Monitor network traffic
- View communication between Pods
- Debug Service requests
- Analyze request and response flow

It is similar to Wireshark but designed specifically for Kubernetes environments.

---

# Docker vs Kubernetes Networking

| Docker | Kubernetes |
|---------|------------|
| Access Container IP | Access Service |
| Container IP | Stable Service IP/DNS |
| Manual Networking | Automatic Networking |
| Manual Load Balancing | Built-in Load Balancing |

---

# Topics Learned

After completing today's session, I learned:

- Why Kubernetes Services are required
- Problems with Pod IP addresses
- What is a Service
- Load Balancing
- Service Discovery
- Exposing Applications
- ClusterIP
- NodePort
- LoadBalancer
- Labels
- Selectors
- Request Flow
- KubeShark

---

# Interview Questions

## What is a Kubernetes Service?

A Kubernetes Service provides a stable network endpoint for accessing one or more Pods, regardless of changes to Pod IP addresses.

---

## Why do we need Services?

Pods are ephemeral and their IP addresses change when they are recreated. Services provide a stable way to access applications.

---

## What is Load Balancing?

Load Balancing distributes incoming requests across multiple Pods to improve performance and availability.

---

## What is Service Discovery?

Service Discovery allows applications to communicate using a stable Service name instead of changing Pod IP addresses.

---

## What are the three main Service types?

- ClusterIP
- NodePort
- LoadBalancer

---

## What is ClusterIP?

ClusterIP exposes the application only inside the Kubernetes cluster.

---

## What is NodePort?

NodePort exposes the application on a fixed port of every Worker Node.

---

## What is LoadBalancer?

LoadBalancer requests the cloud provider to create an external Load Balancer, allowing public access to the application.

---

## How does a Service identify Pods?

A Service uses **Selectors** to match **Labels** defined on Pods.

Only matching Pods receive traffic.

---

# Key Takeaways

- Pods have temporary IP addresses.
- Services provide a stable IP and DNS name.
- Services distribute traffic using Load Balancing.
- Services allow applications to discover each other using Service Discovery.
- ClusterIP is used for internal communication.
- NodePort exposes applications through Worker Nodes.
- LoadBalancer exposes applications publicly using cloud infrastructure.
- Labels and Selectors connect Services to the correct Pods.

---

# One-Line Summary

**A Kubernetes Service provides a stable network endpoint that enables load balancing, service discovery, and application exposure by routing traffic to the 


# Kubernetes Zero to Hero - Interview Revision Notes
# Topic: Kubernetes Interview Questions & Important Concepts

## Overview

This session focused on revising the core Kubernetes concepts commonly asked in DevOps interviews. Instead of introducing new Kubernetes objects, it reinforced previously learned topics such as Kubernetes Architecture, Pods, Deployments, Services, and Namespaces, while also discussing the day-to-day responsibilities of a Kubernetes/DevOps Engineer.

---

# 1. Docker vs Kubernetes

This is one of the most frequently asked Kubernetes interview questions.

## Docker

Docker is a **Container Platform**.

Responsibilities:

- Build Images
- Create Containers
- Run Containers
- Stop Containers
- Remove Containers

Example:

```text
Docker

↓

Container
```

Docker works well on a single machine.

---

## Kubernetes

Kubernetes is a **Container Orchestration Platform**.

Responsibilities:

- Deploy Applications
- Manage Containers
- Scale Applications
- Recover Failed Pods
- Manage Networking
- Manage Clusters

Architecture:

```text
Deployment

↓

ReplicaSet

↓

Pods

↓

Containers
```

---

## Why Kubernetes is Better than Docker

Kubernetes provides enterprise-grade features such as:

- Auto Healing
- Auto Scaling
- High Availability
- Load Balancing
- Service Discovery
- Rolling Updates
- Rollbacks
- Namespace Isolation

These features are not available in Docker by default.

---

# Docker vs Kubernetes Comparison

| Docker | Kubernetes |
|---------|------------|
| Container Platform | Container Orchestration Platform |
| Runs Containers | Manages Containers |
| Single Host | Multiple Nodes |
| Manual Scaling | Auto Scaling |
| Manual Recovery | Auto Healing |
| Basic Networking | Advanced Networking |

---

# 2. Kubernetes Architecture

A Kubernetes cluster consists of two major components.

```text
          Kubernetes Cluster

        ┌──────────┴──────────┐

        ▼                     ▼

 Control Plane           Worker Nodes
```

---

## Control Plane

The Control Plane is the brain of Kubernetes.

Components:

- API Server
- Scheduler
- etcd
- Controller Manager
- Cloud Controller Manager

Responsibilities:

- Accept User Requests
- Store Cluster State
- Schedule Pods
- Maintain Desired State
- Manage Cluster

---

## Worker Nodes

Worker Nodes execute the applications.

Components:

- Kubelet
- Kube Proxy
- Container Runtime

Responsibilities:

- Run Pods
- Manage Containers
- Handle Networking
- Report Node Status

---

# 3. Pods vs Deployments

## Pod

A Pod is the smallest deployable unit in Kubernetes.

```text
Pod

↓

Container
```

Limitations:

- No Auto Healing
- No Auto Scaling
- Not Production Ready

---

## Deployment

A Deployment manages Pods through ReplicaSets.

Architecture:

```text
Deployment

↓

ReplicaSet

↓

Pods
```

Advantages:

- Auto Healing
- Auto Scaling
- Rolling Updates
- Rollbacks
- Desired State Management

---

# Desired State vs Actual State

Desired State:

What the user wants.

Example:

```yaml
replicas: 3
```

Actual State:

What is currently running.

If one Pod crashes:

```text
Desired Pods = 3

Actual Pods = 2
```

ReplicaSet automatically creates another Pod until:

```text
Desired = Actual
```

---

# 4. Kubernetes Services

Pods have temporary IP addresses.

Whenever Pods restart, their IP addresses change.

A Kubernetes Service provides a stable endpoint for accessing Pods.

Responsibilities:

- Load Balancing
- Service Discovery
- Exposing Applications

Flow:

```text
Users

↓

Service

↓

Pods
```

---

# Service Types

## ClusterIP

Default Service.

Accessible only inside the Kubernetes cluster.

Use Cases:

- Backend APIs
- Databases
- Internal Microservices

---

## NodePort

Exposes the application on every Worker Node.

Example:

```
http://Node-IP:30080
```

Use Cases:

- Learning
- Testing
- Small Applications

---

## LoadBalancer

Creates a Cloud Load Balancer.

Flow:

```text
Internet

↓

Cloud Load Balancer

↓

Service

↓

Pods
```

Used in:

- AWS EKS
- Azure AKS
- Google GKE

---

# kube-proxy

kube-proxy is responsible for networking inside Kubernetes.

Responsibilities:

- Routing Traffic
- Managing Network Rules
- Forwarding Requests
- Supporting Load Balancing

Flow:

```text
Browser

↓

Service

↓

kube-proxy

↓

Pods
```

---

# 5. Namespace

Namespaces provide logical separation inside a Kubernetes cluster.

Example:

```text
Kubernetes Cluster

│

├── Development

├── Testing

└── Production
```

Benefits:

- Resource Isolation
- Better Organization
- Team Separation
- Security
- Resource Quotas

---

# Real-Life Example

Think of an apartment building.

The building is shared.

Each family has its own apartment.

Similarly:

```text
Cluster

↓

Namespaces

↓

Resources
```

Different teams work independently inside their own Namespace.

---

# 6. Day-to-Day Responsibilities of a Kubernetes Engineer

A Kubernetes Engineer is responsible for maintaining the Kubernetes environment.

Common responsibilities include:

### Monitoring

Tools:

- Prometheus
- Grafana

Monitor:

- CPU
- Memory
- Pod Health
- Cluster Health

---

### Troubleshooting

Common issues:

- Pod CrashLoopBackOff
- Pending Pods
- ImagePullBackOff
- Network Problems
- Service Connectivity Issues

---

### Cluster Maintenance

Activities:

- Kubernetes Version Upgrades
- Worker Node Maintenance
- Security Patches
- Backup and Recovery

---

### Developer Support

Help developers by:

- Debugging Deployments
- Checking Pod Logs
- Troubleshooting Services
- Resolving Networking Issues
- Assisting with Application Deployment

---

# Kubernetes Workflow (Revision)

Everything learned so far connects as follows:

```text
Developer

↓

kubectl apply

↓

API Server

↓

Deployment

↓

ReplicaSet

↓

Pods

↓

Service

↓

kube-proxy

↓

Users
```

---

# Topics Revised

During this interview revision session, I revised:

- Docker vs Kubernetes
- Kubernetes Architecture
- Control Plane
- Worker Nodes
- Pods
- Deployments
- ReplicaSets
- Desired State
- Actual State
- Services
- ClusterIP
- NodePort
- LoadBalancer
- kube-proxy
- Namespace
- Kubernetes Engineer Responsibilities

---

# Interview Questions

## What is Kubernetes?

Kubernetes is an open-source container orchestration platform used to automate the deployment, scaling, networking, and management of containerized applications.

---

## Difference between Docker and Kubernetes?

Docker builds and runs containers.

Kubernetes manages containers across multiple machines and provides enterprise features like Auto-Healing, Auto-Scaling, and Load Balancing.

---

## What is a Pod?

A Pod is the smallest deployable unit in Kubernetes that wraps one or more containers.

---

## What is a Deployment?

A Deployment manages ReplicaSets and Pods while maintaining the desired state of the application.

---

## What is a ReplicaSet?

A ReplicaSet ensures that the desired number of Pod replicas are always running.

---

## What is a Kubernetes Service?

A Service provides a stable endpoint for accessing Pods while offering Load Balancing and Service Discovery.

---

## What is kube-proxy?

kube-proxy manages networking rules and routes Service traffic to the correct Pods.

---

## What is a Namespace?

A Namespace provides logical isolation of Kubernetes resources inside a cluster.

---

## What are the responsibilities of a Kubernetes Engineer?

- Deploy Applications
- Monitor Clusters
- Troubleshoot Issues
- Upgrade Kubernetes
- Maintain Cluster Health
- Support Development Teams

---

# Key Takeaways

- Docker creates containers, while Kubernetes manages them.
- Deployments provide Auto-Healing and Auto-Scaling.
- ReplicaSets maintain the desired number of Pods.
- Services provide stable networking for Pods.
- kube-proxy routes traffic inside the cluster.
- Namespaces isolate resources between teams and environments.
- Kubernetes Engineers are responsible for cluster operations, monitoring, troubleshooting, and supporting developers.

---

# One-Line Summary

**This session served as a comprehensive interview revision of Kubernetes fundamentals, covering architecture, Pods, Deployments, Services, Networking, Namespaces, and the day-to-day responsibilities of a Kubernetes Engineer, reinforcing the core concepts required for DevOps interviews.**correct Pods using labels and selectors, even when Pods are recreated or scaled.**


# Kubernetes Zero to Hero - Day 5 Notes
# Topic: Deep Dive into Kubernetes Services using Kubeshark

## Overview

In this session, I learned how Kubernetes Services work internally by using **Kubeshark**, a Kubernetes network traffic analyzer.

Unlike previous sessions where Services were explained conceptually, this class demonstrated how network requests actually travel inside a Kubernetes cluster.

The session mainly focused on:

- Kubeshark
- Service Discovery
- Load Balancing
- Exposing Applications
- Packet Flow Analysis
- kube-proxy Traffic Routing

---

# What is Kubeshark?

Kubeshark is a **network traffic analyzer for Kubernetes**.

It captures and displays all network communication happening inside a Kubernetes cluster.

It allows DevOps engineers to observe how requests move between:

- Users
- Services
- Pods
- Namespaces

It is similar to **Wireshark**, but specifically designed for Kubernetes environments.

---

# Why Do We Need Kubeshark?

Normally, when an application is running inside Kubernetes, we cannot directly see how requests travel.

For example:

```text
Browser

↓

???

↓

Application
```

If the application is slow or not responding, it becomes difficult to identify where the issue occurred.

Kubeshark solves this problem by showing the complete request flow.

Example:

```text
Browser

↓

Service

↓

Pod

↓

Response
```

This makes debugging much easier.

---

# Features of Kubeshark

Kubeshark allows engineers to:

- Capture Network Traffic
- Monitor HTTP Requests
- Monitor HTTP Responses
- View Source and Destination Pods
- Analyze Response Time
- Inspect Headers and Payloads
- Debug Networking Issues
- Visualize Communication Between Services

---

# Real-Life Example

Imagine tracking a courier package.

Without tracking:

```text
Package Sent

↓

Delivered
```

You don't know where the package is.

With tracking:

```text
Customer

↓

Warehouse

↓

Sorting Center

↓

Delivery Hub

↓

Delivered
```

Kubeshark provides similar visibility for Kubernetes network traffic.

---

# Service Discovery (Practical Demonstration)

Pods are temporary.

Whenever a Pod is recreated, its IP address changes.

Example:

Old Pod

```text
10.244.1.5
```

New Pod

```text
10.244.1.20
```

Applications should never communicate directly with Pod IP addresses.

Instead, they communicate with a Kubernetes Service.

Example:

```text
Frontend

↓

backend-service

↓

Backend Pods
```

Even if Backend Pods restart, the Service name remains unchanged.

This mechanism is called **Service Discovery**.

---

# Benefits of Service Discovery

- Stable Communication
- No Dependency on Pod IP Addresses
- Automatic Routing
- Simplified Microservice Communication

---

# Exposing Applications

Pods are private resources inside the Kubernetes cluster.

External users cannot directly access them.

A Kubernetes Service exposes applications to users.

Example:

Without Service

```text
Browser

↓

❌ Cannot Reach Pod
```

With Service

```text
Browser

↓

Service

↓

Pod
```

The application becomes accessible.

---

# Types of Services

## 1. ClusterIP

Default Service Type.

Only accessible inside the Kubernetes cluster.

Example:

```text
Frontend

↓

ClusterIP Service

↓

Backend Pods
```

Use Cases:

- Backend APIs
- Databases
- Redis
- Internal Applications

---

## 2. NodePort

Exposes the application through a Worker Node.

Example:

```text
Browser

↓

Worker Node

↓

NodePort

↓

Pods
```

Example URL:

```
http://Node-IP:30080
```

Use Cases:

- Learning Kubernetes
- Local Testing
- Development Environments

---

## 3. LoadBalancer

Used in cloud environments.

Cloud providers automatically create an external Load Balancer.

Flow:

```text
Internet

↓

Cloud Load Balancer

↓

Kubernetes Service

↓

Pods
```

Supported Platforms:

- AWS EKS
- Azure AKS
- Google GKE

Used for production applications.

---

# Load Balancing Demonstration

A Deployment was configured with multiple Pod replicas.

Example:

```text
Pod 1

Pod 2

Pod 3
```

Kubeshark showed how incoming requests were distributed among these Pods.

Example:

```text
Request 1 → Pod 1

Request 2 → Pod 2

Request 3 → Pod 3

Request 4 → Pod 1

Request 5 → Pod 2

Request 6 → Pod 3
```

This ensures that no single Pod receives all requests.

---

# Round Robin Load Balancing

Kubeshark demonstrated that Kubernetes Services commonly distribute requests using a **Round Robin** approach.

Example:

```text
Request 1 → Pod 1

Request 2 → Pod 2

Request 3 → Pod 3

Request 4 → Pod 1

Request 5 → Pod 2

Request 6 → Pod 3
```

Benefits:

- Equal Distribution
- Better Performance
- Reduced Load
- High Availability

---

# Packet Flow Analysis

One of Kubeshark's most useful features is visualizing the complete request journey.

Example:

```text
Browser

↓

NodePort

↓

Service

↓

kube-proxy

↓

Pod

↓

Response

↓

Browser
```

Kubeshark captures every step involved in processing the request.

This helps engineers understand exactly where a request succeeds or fails.

---

# Role of kube-proxy

kube-proxy manages networking rules inside Kubernetes.

Responsibilities include:

- Routing Service Traffic
- Forwarding Requests
- Managing Network Rules
- Supporting Load Balancing

Traffic Flow:

```text
Browser

↓

Service

↓

kube-proxy

↓

Pod
```

Kubeshark helps visualize how kube-proxy routes requests to the appropriate Pods.

---

# Layer 4 and Layer 7 Monitoring

Kubeshark supports monitoring at multiple networking layers.

## Layer 4

Focuses on transport-level communication.

Includes:

- TCP
- UDP
- Ports
- IP Addresses

Example:

```text
IP Address

↓

Port 80
```

---

## Layer 7

Focuses on application-level communication.

Includes:

- HTTP Requests
- HTTP Responses
- REST APIs
- URLs

Example:

```text
GET /products

POST /login

DELETE /users
```

Kubeshark can inspect both Layer 4 and Layer 7 traffic.

---

# Complete Request Flow

A typical request inside Kubernetes follows this path:

```text
User

↓

Browser

↓

LoadBalancer / NodePort

↓

Kubernetes Service

↓

kube-proxy

↓

Pod

↓

Application

↓

Response

↓

Browser
```

Kubeshark visualizes every stage of this communication.

---

# Why Kubeshark is Useful

Without Kubeshark:

```text
Application Error

↓

Unknown Cause
```

With Kubeshark:

```text
Application Error

↓

Request Captured

↓

Reached Service?

↓

Reached Pod?

↓

Response Generated?

↓

Issue Identified
```

It significantly simplifies Kubernetes networking troubleshooting.

---

# Real-World DevOps Use Cases

Kubeshark is commonly used to:

- Debug Networking Issues
- Verify Load Balancing
- Monitor Microservice Communication
- Inspect API Requests
- Analyze Response Times
- Validate Service Routing
- Troubleshoot Production Problems

---

# Topics Learned

After completing today's session, I learned:

- What is Kubeshark
- Why Kubeshark is Used
- Features of Kubeshark
- Service Discovery in Practice
- Exposing Applications
- Kubernetes Service Types
- Load Balancing Visualization
- Round Robin Traffic Distribution
- Packet Flow Analysis
- kube-proxy Traffic Routing
- Layer 4 Monitoring
- Layer 7 Monitoring
- Kubernetes Network Debugging

---

# Interview Questions

## What is Kubeshark?

Kubeshark is a Kubernetes network traffic analyzer that captures and visualizes communication between Services, Pods, and other Kubernetes resources for debugging and monitoring.

---

## Why is Kubeshark used?

Kubeshark is used to monitor network traffic, debug communication issues, inspect HTTP requests and responses, and understand how traffic flows inside a Kubernetes cluster.

---

## How does Kubeshark help in Load Balancing?

Kubeshark shows which Pod receives each incoming request, allowing engineers to verify that traffic is being distributed evenly across multiple Pods.

---

## What is Packet Flow Analysis?

Packet Flow Analysis is the process of tracing the complete journey of a network request from the client through Kubernetes Services and Pods until the response is returned.

---

## What role does kube-proxy play?

kube-proxy manages networking rules and routes incoming Service traffic to the correct Pods.

---

## What is the difference between Layer 4 and Layer 7 traffic?

**Layer 4** deals with transport protocols such as TCP, UDP, IP addresses, and ports.

**Layer 7** deals with application protocols such as HTTP requests, REST APIs, URLs, and application data.

---

# Key Takeaways

- Kubeshark is a powerful traffic analysis tool for Kubernetes.
- It helps visualize how requests move through a Kubernetes cluster.
- Service Discovery allows applications to communicate using stable Service names instead of Pod IP addresses.
- Kubernetes Services distribute traffic across Pods using Load Balancing.
- Packet Flow Analysis helps identify networking issues quickly.
- kube-proxy is responsible for routing Service traffic to Pods.
- Kubeshark supports monitoring at both Layer 4 and Layer 7.

---

# One-Line Summary

**Today's session focused on using Kubeshark to visualize Kubernetes networking, demonstrating how Services, kube-proxy, and Pods work together to provide service discovery, load balancing, application exposure, and end-to-end packet flow analysis inside a Kubernetes cluster.**

# Kubernetes Zero to Hero - Day 6 Notes
# Topic: Kubernetes Ingress & Ingress Controller

## Overview

In this session, I learned about **Kubernetes Ingress**, one of the most important networking components used in production Kubernetes clusters.

Before Ingress, applications were exposed using **NodePort** or **LoadBalancer** Services. Although these methods work, they become expensive and difficult to manage when multiple applications need external access.

Ingress solves this problem by providing a **single entry point** that intelligently routes incoming HTTP/HTTPS traffic to different Services inside the Kubernetes cluster.

---

# Recap

So far, the Kubernetes workflow looks like this:

```text
Deployment
      │
      ▼
ReplicaSet
      │
      ▼
Pods
      │
      ▼
Service
```

Users access applications through a Service.

For external access, we usually create:

```yaml
type: LoadBalancer
```

or

```yaml
type: NodePort
```

---

# Problem Before Ingress

Suppose a company has five applications.

- Shopping
- Payments
- Orders
- Inventory
- Customer Support

Without Ingress:

```text
Internet
    │
    ▼
LoadBalancer
    │
Shopping Service
    │
Shopping Pods
```

```text
Internet
    │
    ▼
LoadBalancer
    │
Payment Service
    │
Payment Pods
```

```text
Internet
    │
    ▼
LoadBalancer
    │
Orders Service
    │
Orders Pods
```

Each application requires:

- One Service
- One LoadBalancer
- One Public IP

---

# Problems with LoadBalancer Services

Using a separate LoadBalancer for every application creates several challenges.

### 1. Higher Cost

Cloud providers charge for each LoadBalancer.

Example:

```text
Shopping

↓

LoadBalancer

↓

Public IP

₹₹₹
```

```text
Payments

↓

LoadBalancer

↓

Public IP

₹₹₹
```

```text
Orders

↓

LoadBalancer

↓

Public IP

₹₹₹
```

As applications increase, infrastructure costs also increase.

---

### 2. Multiple Public IPs

Without Ingress:

```text
Shopping

54.10.10.10

-------------------

Payments

54.10.10.11

-------------------

Orders

54.10.10.12
```

Users must remember different IPs or domains.

This is not ideal.

---

### 3. Difficult Management

Managing multiple LoadBalancers becomes increasingly difficult.

For example:

- SSL Certificates
- Security Rules
- Firewall Configuration
- DNS Management

Everything has to be configured separately.

---

# What is Ingress?

Ingress is a Kubernetes resource that defines **routing rules** for incoming HTTP and HTTPS traffic.

It does **not** expose applications by itself.

Instead, it tells Kubernetes:

- Which request should go where.
- Which Service should receive the request.

Think of Ingress as a **traffic rulebook**.

---

# Important Point

Ingress is **NOT** a LoadBalancer.

Ingress is simply a YAML configuration containing routing rules.

Example:

```text
If URL = /shop

↓

Shopping Service
```

```text
If URL = /payment

↓

Payment Service
```

```text
If URL = /orders

↓

Orders Service
```

Ingress itself does not process traffic.

---

# What is an Ingress Controller?

An Ingress Controller is an application running inside Kubernetes.

It continuously watches for Ingress resources.

Whenever an Ingress YAML is created or modified, the controller updates its routing configuration automatically.

Without an Ingress Controller:

```text
Ingress YAML

↓

Nothing Happens
```

Because nobody is reading the rules.

---

# Popular Ingress Controllers

Some commonly used Ingress Controllers include:

- NGINX Ingress Controller
- HAProxy Ingress Controller
- Traefik
- F5 BIG-IP Controller
- AWS Load Balancer Controller

The choice depends on the organization's requirements.

---

# How Does Ingress Work?

Step 1

Deploy an Ingress Controller.

```text
Internet

↓

Ingress Controller
```

---

Step 2

Create an Ingress Resource.

Example:

```yaml
kind: Ingress
```

This file contains routing rules.

---

Step 3

Ingress Controller detects the new Ingress Resource.

```text
Ingress YAML

↓

Ingress Controller

↓

Routing Rules Updated
```

---

Step 4

Incoming traffic is routed to the correct Service.

---

# Complete Workflow

```text
Browser

↓

Cloud LoadBalancer

↓

Ingress Controller

↓

Ingress Rules

↓

Service

↓

Pods

↓

Application
```

---

# Path-Based Routing

Path-Based Routing routes requests based on the URL path.

Example:

```text
example.com/shop

↓

Shopping Service
```

```text
example.com/payment

↓

Payment Service
```

```text
example.com/orders

↓

Orders Service
```

One domain.

Different paths.

Different applications.

---

## Flow

```text
Browser

↓

example.com/payment

↓

Ingress Controller

↓

Payment Service

↓

Payment Pods
```

---

# Host-Based Routing

Host-Based Routing routes requests based on the hostname.

Example:

```text
shop.example.com

↓

Shopping Service
```

```text
payment.example.com

↓

Payment Service
```

```text
admin.example.com

↓

Admin Service
```

Different subdomains.

Different Services.

---

## Flow

```text
Browser

↓

shop.example.com

↓

Ingress Controller

↓

Shopping Service

↓

Shopping Pods
```

---

# Why Enterprises Prefer Ingress

Ingress provides several enterprise-level advantages.

## Cost Reduction

Instead of:

```text
5 Applications

↓

5 LoadBalancers

↓

5 Public IPs
```

Ingress allows:

```text
5 Applications

↓

1 LoadBalancer

↓

1 Public IP
```

This significantly reduces cloud costs.

---

## Centralized Traffic Management

All incoming traffic is managed from one place.

This simplifies:

- Routing
- Security
- SSL Certificates
- Monitoring

---

## Better Security

Ingress supports:

- HTTPS
- TLS Certificates
- Authentication
- Rate Limiting

This improves application security.

---

## Advanced Routing

Ingress supports:

- Path-Based Routing
- Host-Based Routing
- URL Rewriting
- Traffic Splitting

These features are commonly used in enterprise environments.

---

# Real-Life Example

Imagine a shopping mall.

Without Ingress:

Each shop has its own entrance.

```text
Shopping

Own Entrance
```

```text
Cinema

Own Entrance
```

```text
Restaurant

Own Entrance
```

Expensive.

Hard to manage.

---

With Ingress:

```text
Main Entrance

↓

Security Desk

↓

Shopping

Cinema

Restaurant
```

One entrance.

Visitors are directed to the correct shop.

Ingress works exactly like this.

---

# LoadBalancer vs Ingress

| LoadBalancer | Ingress |
|--------------|---------|
| Exposes one Service | Routes traffic to multiple Services |
| One Public IP per Service | One Public IP for many Services |
| Basic Load Balancing | Advanced Routing |
| Expensive for many applications | Cost-effective |
| No Path-Based Routing | Supports Path-Based Routing |
| No Host-Based Routing | Supports Host-Based Routing |

---

# Ingress vs Ingress Controller

## Ingress

- Kubernetes Resource
- YAML Configuration
- Contains Routing Rules
- Does Not Handle Traffic

Example:

```yaml
kind: Ingress
```

---

## Ingress Controller

- Kubernetes Application
- Watches Ingress Resources
- Applies Routing Rules
- Handles Incoming Traffic

Without an Ingress Controller, an Ingress resource has no effect.

---

# Complete Kubernetes Architecture

```text
                      Internet
                          │
                          ▼
                Cloud LoadBalancer
                          │
                          ▼
                 Ingress Controller
                          │
                Reads Ingress Rules
                          │
         ┌────────────────┼────────────────┐
         ▼                ▼                ▼
 Shopping Service   Payment Service   Orders Service
         │                │                │
         ▼                ▼                ▼
 Shopping Pods      Payment Pods      Orders Pods
```

---

# Advantages of Ingress

- Single Entry Point
- Lower Cloud Cost
- Advanced Routing
- HTTPS Support
- Centralized Management
- Better Scalability
- Enterprise Ready
- Easier Maintenance

---

# Topics Learned

After today's session, I learned:

- Why Ingress is Needed
- Limitations of LoadBalancer Services
- What is Ingress
- What is an Ingress Controller
- Popular Ingress Controllers
- How Ingress Works
- Path-Based Routing
- Host-Based Routing
- Complete Request Flow
- Enterprise Advantages of Ingress
- Ingress vs LoadBalancer
- Ingress vs Ingress Controller

---

# Interview Questions

## What is Kubernetes Ingress?

Ingress is a Kubernetes resource that defines routing rules for external HTTP and HTTPS traffic to Services inside the cluster.

---

## What is an Ingress Controller?

An Ingress Controller is an application that watches Ingress resources and implements the routing rules defined in them.

---

## Why do we need Ingress?

Ingress allows multiple applications to share a single external entry point, reducing infrastructure cost and providing advanced routing capabilities.

---

## What are the advantages of Ingress?

- Cost Reduction
- Centralized Traffic Management
- HTTPS Support
- Path-Based Routing
- Host-Based Routing
- Better Security

---

## What is Path-Based Routing?

Routing requests based on the URL path.

Example:

```text
example.com/orders

↓

Orders Service
```

---

## What is Host-Based Routing?

Routing requests based on the hostname.

Example:

```text
orders.example.com

↓

Orders Service
```

---

## Difference between LoadBalancer and Ingress?

A LoadBalancer exposes a single Service externally.

Ingress provides intelligent routing to multiple Services using a single external entry point.

---

## Difference between Ingress and Ingress Controller?

Ingress is a Kubernetes resource containing routing rules.

Ingress Controller is the application that watches those rules and routes traffic accordingly.

---

# Key Takeaways

- Ingress is a routing resource, not a LoadBalancer.
- An Ingress Controller is required for Ingress to function.
- Ingress reduces cloud costs by allowing multiple applications to share a single LoadBalancer.
- It supports Path-Based and Host-Based routing.
- Ingress is the standard method for exposing HTTP/HTTPS applications in production Kubernetes environments.
- Most enterprise Kubernetes clusters use an Ingress Controller such as NGINX or HAProxy.

---

# One-Line Summary

**Kubernetes Ingress provides a centralized and cost-effective way to expose multiple applications through a single external entry point by using an Ingress Controller to route HTTP/HTTPS traffic to the appropriate Services based on hostnames or URL paths.**


# Kubernetes Zero to Hero - Day 7 Notes
# Topic: Kubernetes ConfigMaps & Secrets

## Overview

In this session, I learned about **ConfigMaps** and **Secrets**, which are used to manage application configuration and sensitive data in Kubernetes.

Instead of storing configuration inside the application or Docker image, Kubernetes allows us to store configuration separately using **ConfigMaps** and sensitive information using **Secrets**.

This makes applications more flexible, secure, and easier to manage across multiple environments.

---

# Why Do We Need ConfigMaps and Secrets?

Suppose we have a Java or Python application running inside a Docker container.

The application needs the following information:

- Database Host
- Database Port
- Database Name
- Username
- Password

A beginner might hardcode these values inside the application.

Example:

```python
DB_HOST = "dev-db.company.com"
DB_PORT = "3306"
DB_USER = "admin"
DB_PASSWORD = "password123"
```

The application works perfectly.

Now imagine we have three environments.

```text
Development

↓

dev-db.company.com

------------------------

Testing

↓

test-db.company.com

------------------------

Production

↓

prod-db.company.com
```

The application code is exactly the same.

Only the database configuration changes.

---

# Problem Without ConfigMaps

If configuration is stored inside the application:

Whenever the database changes, we must:

```text
Modify Source Code

↓

Build Docker Image Again

↓

Push Image to Registry

↓

Pull Image

↓

Deploy Again
```

This process is time-consuming and inefficient.

---

# Kubernetes Solution

Instead of storing configuration inside the application,

Kubernetes stores configuration separately.

```text
Application

↓

Reads Configuration

↓

ConfigMap
```

Now the Docker image never changes.

Only the ConfigMap changes.

---

# What is a ConfigMap?

A ConfigMap is a Kubernetes resource used to store **non-sensitive configuration data**.

Examples include:

- Database Host
- Database Port
- Application Name
- Log Level
- Feature Flags
- Environment Variables
- Configuration Files

Example:

```text
ConfigMap

Database Host

↓

mysql.company.com

---------------------

Database Port

↓

3306

---------------------

Log Level

↓

INFO

---------------------

Application Name

↓

Shopping App
```

Notice that ConfigMaps do **not** store passwords or sensitive information.

---

# Advantages of ConfigMaps

- Separates configuration from application code.
- No need to rebuild Docker images when configuration changes.
- Easier environment management.
- Reusable across multiple Pods.
- Better application portability.

---

# Real-Life Example

Think of a television.

The television is the application.

The remote control changes the settings.

You don't replace the TV every time you change the volume.

Similarly,

ConfigMaps allow us to change application settings without rebuilding the application.

---

# What is a Secret?

Secrets are Kubernetes resources used to store **sensitive information**.

Examples include:

- Database Passwords
- API Keys
- OAuth Credentials
- JWT Tokens
- SSH Keys
- TLS Certificates
- AWS Access Keys

Example:

```text
Secret

Database Password

↓

********

----------------------

JWT Secret

↓

********

----------------------

API Key

↓

********
```

Unlike ConfigMaps, Secrets are specifically designed to protect confidential data.

---

# Why Not Store Passwords in ConfigMaps?

Imagine storing passwords inside a ConfigMap.

```text
ConfigMap

Database Host

↓

mysql.company.com

---------------------

Password

↓

admin123
```

Anyone with permission to read ConfigMaps can see the password.

This creates a security risk.

Instead:

```text
ConfigMap

↓

Database Host

Database Port

Application Name

------------------------

Secret

↓

Database Password

JWT Secret

API Keys
```

Configuration and credentials remain separated.

---

# ConfigMap vs Secret

| ConfigMap | Secret |
|------------|--------|
| Stores non-sensitive data | Stores sensitive data |
| Database Host | Database Password |
| Database Port | API Keys |
| Log Level | JWT Tokens |
| Application Name | OAuth Credentials |
| Feature Flags | TLS Certificates |
| Easy to read | Protected using RBAC |

---

# Where Are ConfigMaps and Secrets Stored?

Both ConfigMaps and Secrets are stored inside the Kubernetes cluster.

```text
Kubernetes Cluster

│

├── ConfigMap

└── Secret
```

Pods access them whenever needed.

---

# How Does a Pod Access ConfigMaps and Secrets?

There are two common methods.

---

# Method 1 - Environment Variables

Kubernetes injects values directly into the container's environment.

Example ConfigMap:

```text
DB_HOST

↓

mysql.company.com
```

Inside the Pod:

```text
Environment Variable

↓

DB_HOST

↓

mysql.company.com
```

Application:

```python
DB_HOST = os.getenv("DB_HOST")
```

The application reads the value without knowing where it came from.

---

# Method 2 - Volume Mounts

Instead of environment variables,

Kubernetes creates files inside the container.

Example:

```text
Container

↓

/config

↓

db_host

↓

mysql.company.com
```

The application simply reads the file.

Flow:

```text
ConfigMap

↓

Volume Mount

↓

Container

↓

Application
```

Secrets also support both methods.

---

# Accessing Secrets

Environment Variable:

```text
Secret

↓

PASSWORD

↓

Application
```

Volume Mount:

```text
Secret

↓

Mounted File

↓

Application
```

---

# RBAC (Role-Based Access Control)

Secrets contain confidential information.

Therefore, Kubernetes recommends protecting them using RBAC.

Example:

```text
Developer

↓

ConfigMap ✔

Secret ❌

-------------------------

Administrator

↓

ConfigMap ✔

Secret ✔
```

Only authorized users should access Secrets.

---

# Principle of Least Privilege

A fundamental security principle.

Meaning:

Give users **only the permissions they need**.

Example:

Frontend Developer

Needs:

- ConfigMaps ✔

Does Not Need:

- Database Password ❌

Administrator

Needs:

- ConfigMaps ✔

- Secrets ✔

This reduces security risks.

---

# Are Kubernetes Secrets Encrypted?

By default, Kubernetes stores Secrets as **Base64 encoded** values.

Example:

Original Password

```text
password123
```

Base64 Representation

```text
cGFzc3dvcmQxMjM=
```

**Important:**

Base64 is **encoding**, not strong encryption.

Anyone can decode it.

For production environments, stronger secret management solutions are recommended.

Examples:

- HashiCorp Vault
- AWS Secrets Manager
- Azure Key Vault
- Google Secret Manager
- Sealed Secrets

These provide:

- Strong Encryption
- Secret Rotation
- Audit Logs
- Fine-Grained Access Control

---

# Complete Workflow

```text
Deployment

↓

Pod

┌────────────┴────────────┐

▼                         ▼

ConfigMap              Secret

▼                         ▼

Configuration        Credentials

└────────────┬────────────┘

↓

Application
```

The application starts by reading both ConfigMaps and Secrets.

---

# Real-World Example

Suppose we deploy an E-Commerce application.

ConfigMap stores:

- Application Name
- Database Host
- Database Port
- Log Level
- Environment

Secret stores:

- Database Password
- JWT Secret
- Stripe API Key
- AWS Access Key

The application reads both resources when it starts.

---

# Advantages of ConfigMaps

- Easy Configuration Management
- Environment Separation
- No Docker Image Rebuild
- Reusable Across Applications
- Better Maintainability

---

# Advantages of Secrets

- Secure Storage of Credentials
- Better Security Practices
- RBAC Protection
- Separation of Sensitive Data
- Production-Ready Secret Management

---

# Kubernetes Architecture

```text
                     Deployment
                          │
                          ▼
                         Pod
                   ┌──────┴──────┐
                   ▼             ▼
              ConfigMap       Secret
                   │             │
                   ▼             ▼
            Configuration   Credentials
                   │             │
                   └──────┬──────┘
                          ▼
                     Application
```

---

# Topics Learned

After completing today's session, I learned:

- Why ConfigMaps are needed
- Why Secrets are needed
- Problems with Hardcoded Configuration
- ConfigMap Architecture
- Secret Architecture
- ConfigMap vs Secret
- Environment Variables
- Volume Mounts
- RBAC
- Principle of Least Privilege
- Base64 Encoding
- Enterprise Secret Management

---

# Interview Questions

## What is a ConfigMap?

A ConfigMap is a Kubernetes resource used to store non-sensitive configuration data separately from the application code, allowing configuration changes without rebuilding the Docker image.

---

## What is a Secret?

A Secret is a Kubernetes resource used to securely store sensitive information such as passwords, API keys, JWT tokens, OAuth credentials, and certificates.

---

## Why do we need ConfigMaps?

ConfigMaps separate application configuration from application code, making applications easier to configure and deploy across different environments.

---

## Why should passwords not be stored in ConfigMaps?

ConfigMaps are intended for non-sensitive configuration. Passwords and credentials should be stored in Secrets to improve security and enable access control.

---

## How can Pods access ConfigMaps and Secrets?

Pods can access ConfigMaps and Secrets in two ways:

- Environment Variables
- Volume Mounts

---

## What is RBAC?

Role-Based Access Control (RBAC) is a Kubernetes security mechanism that controls which users or services can access resources such as Secrets.

---

## What is the Principle of Least Privilege?

The Principle of Least Privilege means granting users or applications only the minimum permissions required to perform their tasks.

---

## Is Base64 Encoding the same as Encryption?

No.

Base64 is an encoding mechanism, not strong encryption. It only changes the representation of the data and can be easily decoded.

---

# Key Takeaways

- ConfigMaps store non-sensitive configuration.
- Secrets store sensitive credentials.
- Configuration should never be hardcoded inside applications.
- Docker images should remain unchanged across environments.
- ConfigMaps and Secrets can be injected into Pods using Environment Variables or Volume Mounts.
- RBAC protects access to sensitive information.
- Base64 encoding is not strong encryption.
- Enterprise applications use dedicated secret management tools like HashiCorp Vault or cloud secret managers.

---

# One-Line Summary

**ConfigMaps and Secrets separate application configuration from application code, allowing Kubernetes applications to receive configuration dynamically while securely managing sensitive credentials without rebuilding Docker images, making deployments flexible, secure, and production-ready.**
