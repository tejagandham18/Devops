# ☁️ AWS Day 1 – Introduction to Cloud Computing

---

# 📌 What is Cloud Computing?

Cloud computing is the delivery of computing services such as:

- Servers
- Storage
- Databases
- Networking
- Software

over the internet on-demand.

Instead of purchasing and maintaining physical servers, organizations can rent infrastructure from cloud providers.

---

## ✅ Simple Definition

Cloud computing means accessing IT resources over the internet instead of managing physical infrastructure manually.

---

# 🏢 Traditional On-Premises Infrastructure

Before cloud computing, companies managed everything inside their own data centers.

This included:

- Physical servers
- Networking devices
- Storage systems
- Cooling systems
- Power management

This model is called:

# On-Premises Infrastructure

---

## ❌ Problems with On-Premises Infrastructure

### High Initial Cost
Companies must purchase expensive hardware.

### Maintenance Responsibility
Dedicated teams are required to manage servers.

### Difficult Scaling
Adding new servers takes time and money.

### Hardware Failures
Physical devices can fail unexpectedly.

### Space & Power Requirements
Data centers require electricity and cooling systems.

---

# 🖥️ What is Virtualization?

Virtualization is a technology that allows multiple virtual machines (VMs) to run on a single physical server.

---

## Before Virtualization

```text
1 Physical Server = 1 Application
```

Large amount of resources remained unused.

---

## After Virtualization

```text
1 Physical Server
    ├── Virtual Machine 1
    ├── Virtual Machine 2
    ├── Virtual Machine 3
```

Benefits:

- Better resource utilization
- Reduced cost
- Improved scalability
- Efficient infrastructure usage

---

# 🚀 Evolution of Infrastructure

```text
Traditional Infrastructure
        ↓
Virtualization
        ↓
Cloud Computing
```

Cloud providers use virtualization internally to manage infrastructure efficiently.

---

# ☁️ Types of Cloud

---

# 1️⃣ Public Cloud

Infrastructure is owned and managed by cloud providers.

Examples:

- AWS (Amazon Web Services)
- Microsoft Azure
- Google Cloud Platform (GCP)

Users rent infrastructure using a:

```text
Pay-As-You-Go
```

pricing model.

---

## ✅ Characteristics of Public Cloud

- Highly scalable
- Cost effective
- Accessible globally
- No hardware maintenance
- Faster deployment

---

# 2️⃣ Private Cloud

Infrastructure is managed internally by the organization itself.

Mostly used by:

- Banks
- Government organizations
- Military
- Healthcare companies

---

## ✅ Characteristics of Private Cloud

- Better security control
- More customization
- Higher maintenance cost
- Limited scalability compared to public cloud

---

# ⚔️ Public Cloud vs Private Cloud

| Feature | Public Cloud | Private Cloud |
|----------|--------------|---------------|
| Ownership | Cloud Provider | Organization |
| Cost | Lower | Higher |
| Scalability | High | Limited |
| Maintenance | Provider | Organization |
| Security Control | Shared | Full Control |

---

# 🌍 Why AWS?

AWS stands for:

# Amazon Web Services

AWS is the world’s leading cloud platform.

---

## ✅ Why AWS is Popular

### First Mover Advantage
AWS entered the cloud market earlier than competitors.

### Massive Global Infrastructure
AWS operates data centers worldwide.

### Huge Service Ecosystem
Provides hundreds of cloud services.

### Strong Market Share
AWS dominates the cloud industry.

### High Job Opportunities
Large demand for AWS professionals.

---

# 🔥 Popular AWS Services

| Service | Purpose |
|----------|----------|
| EC2 | Virtual Servers |
| S3 | Object Storage |
| IAM | Access Management |
| VPC | Networking |

---

# 🔄 What is Cloud Repatriation?

Cloud repatriation means:

```text
Cloud → On-Premises
```

Moving workloads or applications from cloud platforms back to company-owned infrastructure.

---

## ✅ Reasons for Cloud Repatriation

- High cloud costs
- Security requirements
- Compliance regulations
- Vendor lock-in concerns
- Performance requirements

---

## ⚠️ Important Note

Cloud repatriation is rare.

Most organizations still continue using public cloud platforms.

---

# 🎯 Benefits of Cloud Computing

---

## 🔹 Scalability

Resources can be increased or decreased easily.

---

## 🔹 Cost Optimization

Pay only for resources being used.

---

## 🔹 Flexibility

Access cloud services from anywhere.

---

## 🔹 High Availability

Cloud providers offer reliable infrastructure.

---

## 🔹 Faster Deployment

Infrastructure can be created within minutes.

---

## 🔹 Global Access

Applications can serve users worldwide.

---

# 🧾 AWS Account Creation

Basic steps for creating an AWS account:

1. Open AWS signup page
2. Enter email and password
3. Choose Personal account
4. Add debit/credit card
5. Verify mobile number
6. Select Basic Support Plan
7. Login to AWS Console

---

# 🔐 AWS Best Practices

## ✅ Never Use Root Account Daily

Create IAM users for regular access.

---

## ✅ Enable MFA

Use Multi-Factor Authentication for account security.

---

## ✅ Stop Unused Resources

Avoid unnecessary AWS billing.

---

# 📚 Important Terms

| Term | Meaning |
|------|----------|
| On-Premises | Company-owned infrastructure |
| Virtualization | Multiple VMs on one server |
| Cloud Computing | Renting IT resources over internet |
| Public Cloud | Provider-managed infrastructure |
| Private Cloud | Organization-managed infrastructure |

---

# 🎤 Interview Questions

---

## What is Cloud Computing?

Cloud computing is the delivery of IT services over the internet on-demand.

---

## What is On-Premises Infrastructure?

Infrastructure managed internally using physical servers and data centers.

---

## What is Virtualization?

Technology that allows multiple virtual machines to run on one physical server.

---

## Difference Between Public and Private Cloud?

Public cloud is managed by cloud providers.
Private cloud is managed internally by organizations.

---

## What is Cloud Repatriation?

Moving applications or workloads from cloud platforms back to on-premises infrastructure.

---

## Why is AWS Popular?

AWS is popular because of its scalability, large infrastructure, strong ecosystem, and high industry demand.

---

# 🚀 Next Topic

# AWS IAM (Identity and Access Management)

Topics to Learn:

- Users
- Groups
- Policies
- Roles
- Permissions

---

# ✅ End of AWS Day 1 Notes

# ☁️ AWS Day 2 Notes
# Amazon EC2 (Elastic Compute Cloud)

---

# 📌 What is EC2?

EC2 stands for:

# Elastic Compute Cloud

EC2 is a virtual server provided by AWS.

Instead of purchasing and maintaining physical servers, AWS allows users to rent virtual machines on-demand.

---

## ✅ Simple Definition

EC2 is a cloud-based virtual server used to run applications, websites, databases, Jenkins, Docker containers, and DevOps tools.

---

# 🧠 Understanding the Term EC2

---

## 🔹 Elastic

Elastic means resources can scale up or down easily.

Examples:

- Increase CPU
- Increase RAM
- Change server size

based on workload requirements.

---

## 🔹 Compute

Compute refers to:

- CPU
- Memory (RAM)
- Storage
- Processing Power

These are the actual hardware resources.

---

## 🔹 Cloud

Cloud means the infrastructure is hosted and managed by AWS globally.

Users access servers over the internet.

---

# 🏢 Traditional Servers vs EC2

---

# Before AWS

Companies needed to:

- Buy physical servers
- Maintain hardware
- Manage networking
- Handle power and cooling
- Replace failed hardware

This required large infrastructure and operations teams.

---

# With EC2

AWS manages:

- Physical infrastructure
- Hardware maintenance
- Global networking
- Availability

Users only manage:

- Applications
- Software
- Configurations

---

# 💰 Pay-As-You-Go Model

AWS follows a:

```text
Pay-As-You-Go
```

pricing model.

---

## ✅ Meaning

Users pay only for the resources they use.

Example:

- Run server for 2 hours
- Pay only for 2 hours

If the instance is stopped, billing reduces.

---

# 🖥️ EC2 Instance Types

Instance types define the server configuration.

Different workloads require different hardware resources.

---

# 1️⃣ General Purpose Instances

Balanced CPU and memory.

Examples:

```text
t2.micro
t3.micro
```

Used for:

- Learning
- Small applications
- Jenkins
- DevOps practice

---

# 2️⃣ Compute Optimized Instances

High CPU performance.

Used for:

- Gaming
- Scientific computing
- High-performance applications

---

# 3️⃣ Memory Optimized Instances

High RAM capacity.

Used for:

- Databases
- Caching systems
- Memory-intensive applications

---

# 4️⃣ Storage Optimized Instances

Optimized for high-speed storage access.

Used for:

- Big data
- Analytics
- Large-scale storage systems

---

# 5️⃣ Accelerated Compute Instances

GPU-based instances.

Used for:

- Artificial Intelligence
- Machine Learning
- Video rendering

---

# 🌍 AWS Global Infrastructure

AWS infrastructure is distributed globally.

Main components:

- Regions
- Availability Zones (AZ)

---

# 🌐 What is a Region?

A region is a physical geographic location containing AWS data centers.

Examples:

- Mumbai
- Hyderabad
- Singapore
- US-East

---

## ✅ Why Region Selection is Important

### Low Latency

Choose regions closer to users for better performance.

Example:

Indian users → Mumbai region

---

### Data Sovereignty

Some countries require data to remain inside the country.

This is called:

# Data Sovereignty

---

# 🏢 What is an Availability Zone (AZ)?

Each AWS region contains multiple Availability Zones.

Example:

```text
Mumbai Region
   ├── AZ-1
   ├── AZ-2
   ├── AZ-3
```

Each AZ is an independent data center with separate:

- Power
- Networking
- Infrastructure

---

## ✅ Why Availability Zones are Important

Used for:

# High Availability

If one AZ fails, applications can continue running in another AZ.

This reduces downtime.

---

# 🔑 SSH Key Pair

AWS Linux servers use SSH key pairs instead of passwords.

During EC2 creation, AWS generates:

```text
.pem file
```

This file is used for secure SSH login.

---

## ✅ Purpose of Key Pair

- Secure server access
- Authentication mechanism
- SSH connectivity

---

# 🔥 Security Groups

Security Groups act as a firewall for EC2 instances.

They control:

- Incoming traffic
- Outgoing traffic
- Port access

---

# Important Ports

| Port | Purpose |
|------|----------|
| 22 | SSH Access |
| 80 | HTTP |
| 443 | HTTPS |
| 8080 | Jenkins |

---

# 🚀 Launching an EC2 Instance

Basic Steps:

1. Open AWS Console
2. Go to EC2 Service
3. Click Launch Instance
4. Select AMI
5. Select Instance Type
6. Create Key Pair
7. Configure Security Group
8. Launch Instance

---

# 🐧 AMI (Amazon Machine Image)

AMI is a preconfigured operating system template.

Examples:

- Ubuntu
- Amazon Linux
- Red Hat

AMI contains:

- Operating system
- Software packages
- Configurations

---

# 🔗 SSH Connection

SSH is used to connect securely to Linux EC2 instances.

Example command:

```bash
ssh -i key.pem ubuntu@public-ip
```

---

# 🚀 Jenkins Deployment on EC2

The video demonstrates deploying Jenkins on EC2.

---

## Steps

### Step 1

Launch EC2 instance.

---

### Step 2

Connect using SSH.

---

### Step 3

Install Java.

---

### Step 4

Install Jenkins.

---

### Step 5

Open Port 8080 in Security Group.

---

### Step 6

Access Jenkins in browser.

---

# 🧠 Public IP vs Private IP

---

## Public IP

Accessible over internet.

Used for:

- Browser access
- SSH connection

---

## Private IP

Used for internal AWS communication.

Not accessible publicly.

---

# 🎯 Why EC2 is Important in DevOps

EC2 is used to host:

- Jenkins
- Docker
- Kubernetes
- Web applications
- APIs
- Databases
- CI/CD pipelines

EC2 is one of the most important AWS services for DevOps engineers.

---

# 📚 Important Terms

| Term | Meaning |
|------|----------|
| EC2 | Virtual Server in AWS |
| Instance Type | Server configuration |
| Region | Geographic AWS location |
| Availability Zone | Separate data center inside region |
| Security Group | Firewall for EC2 |
| Key Pair | SSH authentication mechanism |
| AMI | Operating system template |

---

# 🎤 Interview Questions

---

## What is EC2?

EC2 is a cloud-based virtual server provided by AWS.

---

## What does EC2 stand for?

Elastic Compute Cloud.

---

## What is an Instance Type?

An instance type defines the CPU, RAM, and storage configuration of an EC2 server.

---

## What is a Region?

A geographic location containing AWS infrastructure.

---

## What is an Availability Zone?

An independent data center inside an AWS region.

---

## What is a Security Group?

A firewall that controls traffic to and from an EC2 instance.

---

## What is an AMI?

Amazon Machine Image used to launch EC2 instances.

---

## What is the purpose of a Key Pair?

Used for secure SSH login to EC2 instances.

---

# 🚀 Next Topic

AWS S3 (Simple Storage Service)

Topics:

- Buckets
- Objects
- Storage Classes
- Versioning
- Permissions

---

# ✅ End of AWS Day 2 Notes


# ☁️ AWS Day 3 Notes
# Amazon S3 (Simple Storage Service)

---

# 📌 What is Amazon S3?

S3 stands for:

# Simple Storage Service

Amazon S3 is an object storage service provided by AWS.

It is used to store and retrieve any amount of data from anywhere over the internet.

---

## ✅ Simple Definition

S3 is a cloud storage service used to store files such as:

- Images
- Videos
- Logs
- Backups
- Static website files
- Application data

---

# 🧠 Why S3 is Important

S3 is one of the most widely used AWS services.

It is used for:

- Backup storage
- Application logs
- Jenkins artifacts
- Static website hosting
- Database backups
- Terraform state files
- Media storage

---

# 🪣 What is a Bucket?

A Bucket is a container used to store objects/files in S3.

---

## Example

```text
teja-devops-backups
```

Inside the bucket:

```text
teja-devops-backups
    ├── logs.txt
    ├── backup.zip
    ├── image.png
```

---

# ⚠️ Important Rule

Bucket names must be:

- Globally unique
- Lowercase only
- No spaces allowed

---

# 📦 What is an Object?

An Object is the actual file stored inside a bucket.

Examples:

- image.jpg
- logs.txt
- app.zip
- database-backup.sql

---

# 🧱 S3 Structure

```text
Bucket
   ├── Object 1
   ├── Object 2
   ├── Object 3
```

---

# 🌍 Global Accessibility

Buckets are created in a specific AWS Region.

Example:

- Mumbai
- Singapore
- US-East

However, objects inside buckets can be accessed globally using:

```text
HTTP / HTTPS
```

---

# Example URL

```text
https://bucket-name.s3.amazonaws.com/file.jpg
```

---

# 💪 Scalability of S3

Amazon S3 provides unlimited storage scalability.

---

## ✅ Important Points

- No hard limit on total storage
- Automatically scales
- Single object size limit = 5 TB

---

# 🛡️ Durability of S3

Amazon S3 is famous for:

# 99.999999999% Durability

This is called:

# 11 Nines Durability

---

# ✅ Meaning

The probability of losing data is extremely low.

AWS stores multiple copies of data across infrastructure internally.

---

# 🧠 Simple Understanding

If one storage device fails, your data still survives because AWS maintains multiple copies.

---

# 🔄 Durability vs Availability

---

## Durability

```text
Will my data survive?
```

Focuses on data safety.

---

## Availability

```text
Can I access my data right now?
```

Focuses on accessibility.

---

# 🔐 Security in S3

AWS provides multiple security mechanisms for S3.

---

# 1️⃣ Bucket Policies

Bucket Policies control access to buckets and objects.

Policies are written in:

```text
JSON
```

---

## Purpose

- Allow access
- Deny access
- Restrict users

---

## Example

Allow:

```text
Read access to objects
```

Deny:

```text
Delete access
```

---

# 2️⃣ Access Control Lists (ACLs)

ACLs provide object-level or bucket-level permissions.

Used to control:

- Read access
- Write access

---

# 3️⃣ Encryption

AWS provides Server-Side Encryption by default.

Purpose:

- Protect stored data
- Improve security

---

# 🗂️ Storage Classes in S3

S3 provides different storage classes based on:

- Cost
- Access frequency
- Retrieval speed

---

# 1️⃣ S3 Standard

Used for frequently accessed data.

Examples:

- Websites
- Applications
- Active data

---

# 2️⃣ S3 Glacier

Low-cost storage for long-term archival.

Used for:

- Backups
- Archive data
- Rarely accessed files

---

# 🧠 Simple Understanding

```text
Frequently used data → S3 Standard
Rarely used data → Glacier
```

---

# 🔄 Versioning in S3

Versioning allows storing multiple versions of the same object.

---

# Without Versioning

```text
file-v1
   ↓ overwrite
file-v2
```

Old file is lost.

---

# With Versioning

```text
file-v1
file-v2
file-v3
```

All versions are preserved.

---

# ✅ Benefits of Versioning

- Prevent accidental deletion
- Recover old files
- Protect against overwrites

---

# 🌐 Static Website Hosting

S3 can host static websites.

---

# Static Website Includes

- HTML
- CSS
- JavaScript

No backend server required.

---

# Steps for Static Website Hosting

1. Create S3 bucket
2. Upload website files
3. Enable Static Website Hosting
4. Configure bucket policy
5. Access using public URL

---

# ⚠️ Public Access Block

By default, S3 blocks public access for security.

For website hosting:

- Public access must be enabled carefully
- Bucket policy must allow access

---

# 🧰 Common DevOps Use Cases of S3

---

# 1️⃣ Jenkins Build Artifacts

Store:

- Build packages
- Deployment files
- Logs

---

# 2️⃣ Database Backups

Store backup files securely.

---

# 3️⃣ Application Logs

Centralized log storage.

---

# 4️⃣ Terraform Remote State

Terraform stores state files in S3.

Very common DevOps use case.

---

# 5️⃣ Static Website Hosting

Host frontend applications directly from S3.

---

# 🧠 Important Terms

| Term | Meaning |
|------|----------|
| Bucket | Container used to store objects |
| Object | Actual file stored in S3 |
| Storage Class | Type of storage based on cost and access |
| Versioning | Multiple versions of objects |
| Bucket Policy | Access control mechanism |
| ACL | Access Control List |
| Glacier | Low-cost archival storage |

---

# 🎤 Interview Questions

---

## What is Amazon S3?

Amazon S3 is an object storage service provided by AWS.

---

## What is a Bucket?

A bucket is a container used to store objects/files in S3.

---

## What is an Object?

An object is the actual file stored inside a bucket.

---

## What is Versioning?

Versioning stores multiple versions of the same object.

---

## What is S3 Glacier?

A low-cost storage class used for long-term archival.

---

## Difference Between Durability and Availability?

### Durability
Data survival.

### Availability
Data accessibility.

---

## What is Static Website Hosting in S3?

Hosting HTML, CSS, and JavaScript websites directly from an S3 bucket.

---

# 🚀 Next Topic

# AWS VPC (Virtual Private Cloud)

Topics:

- VPC
- Subnets
- Route Tables
- Internet Gateway
- NAT Gateway

---

# ✅ End of AWS Day 3 Notes
