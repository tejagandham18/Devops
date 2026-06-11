# Terraform Zero to Hero - Day 1 Notes

## Overview

Terraform is an **Infrastructure as Code (IaC)** tool developed by HashiCorp.

It allows us to create, modify, and manage infrastructure using code instead of manually creating resources through cloud consoles.

---

# Why Infrastructure as Code (IaC)?

## Traditional Approach

Manually creating infrastructure:

* Login to AWS Console
* Create EC2
* Create Security Group
* Create S3 Bucket
* Configure Networking

### Problems

* Time consuming
* Human errors
* Difficult to reproduce
* No version control

---

## IaC Approach

Infrastructure is created using code.

Example:

```hcl
resource "aws_instance" "server" {
  ami           = "ami-123456"
  instance_type = "t3.micro"
}
```

Run:

```bash
terraform apply
```

Terraform automatically creates the infrastructure.

---

# Why Terraform?

Different cloud providers have different tools:

| Cloud Provider | Native Tool        |
| -------------- | ------------------ |
| AWS            | CloudFormation     |
| Azure          | ARM Templates      |
| GCP            | Deployment Manager |

Problem:

Each cloud provider uses different syntax.

Terraform solves this problem by providing:

* One language
* One workflow
* Multi-cloud support

Supported Platforms:

* AWS
* Azure
* GCP
* Kubernetes
* Docker
* GitHub

---

# Terraform Architecture

```text
Terraform
    │
    ▼
Provider
    │
    ▼
Cloud API
    │
    ▼
Resources
```

Example:

```text
Terraform
    │
    ▼
AWS Provider
    │
    ▼
AWS API
    │
    ▼
EC2 Instance
```

---

# What is a Provider?

A provider is a plugin that allows Terraform to communicate with a platform.

Example:

```hcl
provider "aws" {
  region = "ap-south-1"
}
```

Purpose:

* Connect Terraform to AWS
* Authenticate requests
* Manage AWS resources

Think of Provider as a translator between Terraform and AWS.

---

# What is a Resource?

A resource represents infrastructure managed by Terraform.

Examples:

* EC2 Instance
* S3 Bucket
* VPC
* Security Group
* IAM User

Example:

```hcl
resource "aws_instance" "server" {
  ami           = "ami-123456"
  instance_type = "t3.micro"
}
```

This resource creates an EC2 instance.

---

# What is HCL?

HCL stands for:

```text
HashiCorp Configuration Language
```

Terraform uses HCL to define infrastructure.

Example:

```hcl
resource "aws_instance" "server" {
  ami           = "ami-123456"
  instance_type = "t3.micro"
}
```

Advantages:

* Easy to read
* Easy to write
* Human friendly

---

# AWS Authentication

Terraform needs AWS credentials to create resources.

Configure credentials using:

```bash
aws configure
```

AWS asks for:

```text
Access Key ID
Secret Access Key
Region
Output Format
```

These credentials allow Terraform to communicate with AWS.

---

# Terraform Configuration File

Terraform configurations are stored in:

```text
main.tf
```

Example:

```hcl
provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "server" {
  ami           = "ami-123456"
  instance_type = "t3.micro"
}
```

Think of:

```text
main.tf = Infrastructure Blueprint
```

---

# Terraform Lifecycle

Terraform follows four main phases.

---

## 1. terraform init

Command:

```bash
terraform init
```

Purpose:

* Initialize Terraform project
* Download required providers
* Prepare working directory

Think:

```text
Project Setup
```

---

## 2. terraform plan

Command:

```bash
terraform plan
```

Purpose:

* Preview changes
* Verify infrastructure before creation

Example:

```text
Plan: 1 to add, 0 to change, 0 to destroy
```

Important:

No resources are created.

Think:

```text
Dry Run
```

---

## 3. terraform apply

Command:

```bash
terraform apply
```

Purpose:

* Create infrastructure
* Apply changes to AWS

Example:

```text
Creating EC2 Instance...
Apply Complete!
```

Think:

```text
Execute Changes
```

---

## 4. terraform destroy

Command:

```bash
terraform destroy
```

Purpose:

* Remove infrastructure
* Prevent unnecessary AWS charges

Example:

```text
Destroy complete!
```

Think:

```text
Cleanup Resources
```

---

# Terraform State

Terraform creates a state file:

```text
terraform.tfstate
```

Purpose:

* Tracks created resources
* Stores resource IDs
* Maintains infrastructure state

Example:

```text
EC2 ID
Security Group ID
S3 Bucket ID
```

Terraform uses this file to determine what changes are required.

---

# Terraform Workflow

```text
Write Code
    │
    ▼
terraform init
    │
    ▼
terraform plan
    │
    ▼
terraform apply
    │
    ▼
Infrastructure Created
```

To remove resources:

```text
terraform destroy
```

---

# Key Interview Questions

## What is Terraform?

Terraform is an Infrastructure as Code (IaC) tool developed by HashiCorp that allows us to provision and manage infrastructure using code.

---

## What is a Provider?

A provider is a plugin that enables Terraform to communicate with cloud platforms such as AWS, Azure, and GCP.

---

## What is a Resource?

A resource is any infrastructure component managed by Terraform, such as EC2, S3, VPC, Security Groups, and IAM Users.

---

## Difference Between terraform plan and terraform apply?

### terraform plan

Shows what changes will occur without making any modifications.

### terraform apply

Executes the changes and creates/modifies infrastructure.

---

## Terraform Lifecycle Commands

```bash
terraform init
terraform plan
terraform apply
terraform destroy
```

---

# Day 1 Summary

Completed Topics:

* Infrastructure as Code (IaC)
* Why Terraform
* Providers
* Resources
* HCL Basics
* AWS Authentication
* main.tf
* Terraform Lifecycle
* Terraform State
* Interview Questions

Status:

```text
Terraform Day 1 Complete ✅
```
