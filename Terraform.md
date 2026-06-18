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

# Terraform Zero to Hero - Day 2 Notes

# Overview

Day 2 focuses on writing reusable and production-ready Terraform code.

Key Topics:

* Providers
* Variables
* Outputs
* Project Structure
* Terraform TFVars
* Conditional Expressions
* Built-in Functions

---

# 1. Providers

## What is a Provider?

A Provider is a plugin that allows Terraform to communicate with a platform such as AWS, Azure, GCP, Docker, or Kubernetes.

Example:

```hcl
provider "aws" {
  region = "ap-south-1"
}
```

Architecture:

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
AWS Resources
```

---

## Why Providers?

Terraform itself cannot create AWS resources.

It needs a provider to:

* Authenticate with AWS
* Communicate with AWS APIs
* Create and manage AWS resources

---

## Multi Region Provider Example

```hcl
provider "aws" {
  region = "ap-south-1"
}

provider "aws" {
  alias  = "singapore"
  region = "ap-southeast-1"
}
```

Purpose:

```text
Mumbai Resources
Singapore Resources
```

using the same Terraform project.

---

# 2. Variables

## What is a Variable?

Variables are used to avoid hardcoded values and make Terraform code reusable.

Without Variables:

```hcl
instance_type = "t3.micro"
```

Problem:

Every environment requires code changes.

---

## Variable Declaration

File:

```text
variables.tf
```

Example:

```hcl
variable "instance_type" {
  description = "EC2 Instance Type"
}
```

Meaning:

```text
Terraform, I need a variable called instance_type.
The value will be provided later.
```

---

## Variable Usage

Example:

```hcl
resource "aws_instance" "server" {

  instance_type = var.instance_type

}
```

Terraform reads:

```text
var.instance_type
```

and replaces it with the actual value.

---

# 3. Terraform TFVars

## What is terraform.tfvars?

The terraform.tfvars file contains the actual values for variables.

Example:

File:

```text
terraform.tfvars
```

Content:

```hcl
instance_type = "t3.micro"
```

Meaning:

```text
Variable Name
      ↓
instance_type
      ↓
Value
      ↓
t3.micro
```

---

## Why Use TFVars?

Different environments need different values.

Example:

### Development

```hcl
instance_type = "t3.micro"
```

### Production

```hcl
instance_type = "t3.large"
```

Same Terraform code.

Different values.

---

## Real Company Structure

```text
dev.tfvars
qa.tfvars
prod.tfvars
```

Usage:

```bash
terraform apply -var-file=prod.tfvars
```

---

# Variables vs TFVars

## variables.tf

Used to declare variables.

Example:

```hcl
variable "instance_type" {}
```

---

## terraform.tfvars

Used to assign values.

Example:

```hcl
instance_type = "t3.micro"
```

---

# 4. Outputs

## What is an Output?

Outputs display useful information after Terraform creates resources.

Example:

```hcl
output "public_ip" {

  value = aws_instance.server.public_ip

}
```

After:

```bash
terraform apply
```

Output:

```text
public_ip = 3.110.118.137
```

---

## Why Outputs?

Without Output:

```text
Open AWS Console
Copy Public IP
```

With Output:

```text
Terraform prints it automatically
```

Useful for automation.

---

# 5. Project Structure

## Beginner Structure

```text
main.tf
```

Everything inside one file.

Works for learning.

Not recommended for production.

---

## Professional Structure

```text
terraform-project
│
├── provider.tf
├── variables.tf
├── terraform.tfvars
├── main.tf
└── outputs.tf
```

---

## provider.tf

Contains:

```hcl
provider "aws" {
  region = "ap-south-1"
}
```

Purpose:

```text
AWS Connection Configuration
```

---

## variables.tf

Contains:

```hcl
variable "instance_type" {}
```

Purpose:

```text
Variable Declaration
```

---

## terraform.tfvars

Contains:

```hcl
instance_type = "t3.micro"
```

Purpose:

```text
Variable Values
```

---

## main.tf

Contains:

```hcl
resource "aws_instance" "server" {

}
```

Purpose:

```text
Infrastructure Resources
```

---

## outputs.tf

Contains:

```hcl
output "public_ip" {

}
```

Purpose:

```text
Display Useful Information
```

---

# Complete Flow

```text
variables.tf
     ↓
Declare Variables

terraform.tfvars
     ↓
Provide Values

main.tf
     ↓
Create Infrastructure

outputs.tf
     ↓
Display Results
```

---

# 6. Conditional Expressions

Terraform supports IF-ELSE logic using:

```hcl
condition ? value1 : value2
```

---

## Syntax

```hcl
var.environment == "prod"
? "t3.large"
: "t3.micro"
```

Read as:

```text
IF environment = prod
    Use t3.large
ELSE
    Use t3.micro
```

---

## Example 1

```hcl
environment = "prod"
```

Result:

```text
t3.large
```

---

## Example 2

```hcl
environment = "dev"
```

Result:

```text
t3.micro
```

---

# Easy Memory Trick

```text
?
=
IF TRUE

:
=
ELSE
```

Equivalent Java Code:

```java
if(environment.equals("prod")){
    instanceType = "t3.large";
}else{
    instanceType = "t3.micro";
}
```

---

# 7. Built-in Functions

Terraform provides built-in functions.

---

## length()

Example:

```hcl
length(["EC2","S3","VPC"])
```

Output:

```text
3
```

---

## map()

Example:

```hcl
{
  dev  = "t3.micro"
  prod = "t3.large"
}
```

Stores key-value pairs.

---

# Most Important Learning From Day 2

Day 1 taught:

```text
Terraform creates infrastructure.
```

Day 2 teaches:

```text
Terraform code should be reusable.
```

Goals:

* Avoid hardcoding
* Separate code from values
* Support multiple environments
* Make code maintainable

---

# Interview Questions

## What is a Provider?

A provider is a plugin that enables Terraform to communicate with AWS, Azure, GCP, Docker, Kubernetes, etc.

---

## What is a Variable?

Variables are used to make Terraform configurations reusable and avoid hardcoded values.

---

## What is terraform.tfvars?

terraform.tfvars stores the actual values assigned to variables.

---

## What is an Output?

Outputs display useful information after resources are created.

---

## Difference Between variables.tf and terraform.tfvars?

variables.tf

```text
Declares Variables
```

terraform.tfvars

```text
Assigns Values
```

---

## What does this mean?

```hcl
var.environment == "prod"
? "t3.large"
: "t3.micro"
```

Answer:

```text
IF environment is prod
    Use t3.large

ELSE
    Use t3.micro
```

---

# Day 2 Summary

Completed Topics:

✅ Providers

✅ Multi Region Providers

✅ Variables

✅ terraform.tfvars

✅ Outputs

✅ Project Structure

✅ Conditional Expressions

✅ Built-in Functions

✅ Reusable Terraform Code

Status:

```text
Terraform Day 2 Complete ✅
```


# Terraform Zero to Hero - Day 3 Notes

# Overview

Day 3 focuses on one of the most important Terraform concepts:

```text
Terraform Modules
```

Modules help us avoid code duplication by creating reusable infrastructure components.

Think:

```text
Variables = Reusable Values

Modules = Reusable Infrastructure
```

---

# Problem Before Modules

Suppose a company needs:

```text
Dev EC2
QA EC2
Prod EC2
```

Without modules:

```hcl
resource "aws_instance" "dev" {
}

resource "aws_instance" "qa" {
}

resource "aws_instance" "prod" {
}
```

Problem:

* Duplicate code
* Difficult maintenance
* Hard to scale
* Higher chance of mistakes

---

# Why Modules?

Modules solve:

```text
Code Duplication
Maintenance Problems
Standardization Issues
```

Benefits:

* Reusability
* Maintainability
* Standardization
* Team Collaboration
* Easier Debugging

---

# Real World Example

Think about building houses.

Without Modules:

```text
Design House 1
Design House 2
Design House 3
```

Every house designed separately.

---

With Modules:

```text
Create One Blueprint

House Blueprint
      ↓
House 1
House 2
House 3
```

Terraform Modules work the same way.

---

# What Is A Terraform Module?

Definition:

A Terraform Module is a reusable collection of Terraform configurations used to create infrastructure components.

Examples:

```text
EC2 Module
VPC Module
S3 Module
Security Group Module
RDS Module
```

---

# Variables vs Modules

## Variables

Variables make values reusable.

Examples:

```text
Instance Type
Environment
Region
CIDR
```

Example:

```hcl
variable "instance_type" {}
```

---

## Modules

Modules make infrastructure reusable.

Examples:

```text
EC2 Creation Logic
VPC Creation Logic
S3 Creation Logic
```

Example:

```hcl
module "ec2_server" {
}
```

---

# Terraform Project Without Modules

```text
project

├── provider.tf
├── variables.tf
├── terraform.tfvars
├── main.tf
└── outputs.tf
```

All resources are written directly inside main.tf.

---

# Terraform Project With Modules

```text
project

├── provider.tf
├── variables.tf
├── terraform.tfvars
├── main.tf
├── outputs.tf
│
└── modules
      │
      └── ec2
           │
           ├── main.tf
           ├── variables.tf
           └── outputs.tf
```

---

# Understanding Module Structure

## modules/ec2/main.tf

Contains actual EC2 creation logic.

Example:

```hcl
resource "aws_instance" "server" {

  ami           = var.ami

  instance_type = var.instance_type

}
```

Purpose:

```text
EC2 Blueprint
```

---

## modules/ec2/variables.tf

Declares variables used inside the module.

Example:

```hcl
variable "instance_type" {}

variable "ami" {}
```

Purpose:

```text
Module Inputs
```

---

## modules/ec2/outputs.tf

Returns values after resource creation.

Example:

```hcl
output "public_ip" {

 value = aws_instance.server.public_ip

}
```

Purpose:

```text
Module Outputs
```

---

# Calling A Module

From root project:

```hcl
module "dev_server" {

 source = "./modules/ec2"

 instance_type = "t3.micro"

 ami = "ami-12345"

}
```

Meaning:

```text
Go to EC2 Module

Create EC2

Use provided values
```

---

# Understanding source

Example:

```hcl
source = "./modules/ec2"
```

Meaning:

```text
Terraform

Navigate to:

modules/ec2

Read Module Files

Create Resources
```

Think:

```text
Module Location
```

---

# Module Inputs

Inputs are values passed into a module.

Example:

```hcl
module "server" {

 source = "./modules/ec2"

 instance_type = "t3.micro"

}
```

Input:

```text
instance_type
```

---

# Java Analogy

Java Method:

```java
public void createServer(String type){

}
```

Call:

```java
createServer("t3.micro");
```

---

Terraform Module:

```hcl
module "server" {

 instance_type = "t3.micro"

}
```

Exactly the same concept.

---

# Module Outputs

Suppose module creates:

```text
EC2 Instance
```

AWS returns:

```text
3.110.118.137
```

Public IP.

---

Inside Module:

```hcl
output "public_ip" {

 value = aws_instance.server.public_ip

}
```

---

Access From Root Project:

```hcl
output "server_ip" {

 value = module.server.public_ip

}
```

Terraform prints:

```text
3.110.118.137
```

---

# Reusing Modules

Same module can create multiple servers.

Example:

```hcl
module "dev" {

 source = "./modules/ec2"

 instance_type = "t3.micro"

}
```

---

```hcl
module "qa" {

 source = "./modules/ec2"

 instance_type = "t3.micro"

}
```

---

```hcl
module "prod" {

 source = "./modules/ec2"

 instance_type = "t3.large"

}
```

Result:

```text
One Module

Three Servers
```

---

# Why Companies Use Modules

Suppose company policy changes:

```text
Add Monitoring
Add New Tags
Enable Encryption
```

Without Modules:

```text
Edit 100 Terraform Files
```

---

With Modules:

```text
Edit Module Once

All Resources Updated
```

Huge benefit.

---

# Public Modules

Terraform provides:

```text
Terraform Registry
```

Think:

```text
GitHub For Terraform Modules
```

Contains:

```text
VPC Modules
EC2 Modules
EKS Modules
S3 Modules
```

Example:

```hcl
module "vpc" {

 source = "terraform-aws-modules/vpc/aws"

}
```

Terraform downloads and uses the module automatically.

---

# Private Modules

Most organizations create their own modules.

Reasons:

* Security
* Standardization
* Compliance
* Monitoring Requirements
* Tagging Standards

Examples:

```text
Company EC2 Module
Company VPC Module
Company Security Group Module
```

Stored in:

```text
GitHub Enterprise
GitLab
Bitbucket
```

---

# Real DevOps Example

Suppose company requires:

```text
Every EC2 Must Have

Monitoring
Approved Security Group
Mandatory Tags
Encryption
```

Instead of trusting every engineer:

Create:

```text
Company EC2 Module
```

All engineers use:

```hcl
module "ec2" {

 source = "company/ec2"

}
```

Standards automatically applied.

---

# Day 3 Deep Understanding

Day 1:

```text
Terraform Creates Infrastructure
```

---

Day 2:

```text
Variables Make Values Reusable
```

---

Day 3:

```text
Modules Make Infrastructure Reusable
```

---

# Memory Trick

```text
Variable
=
Reusable Value

Module
=
Reusable Infrastructure
```

---

# Interview Questions

## What Is A Terraform Module?

A Terraform Module is a reusable collection of Terraform resources used to standardize and simplify infrastructure creation.

---

## Why Use Modules?

* Reduce code duplication
* Improve maintainability
* Enable reusability
* Standardize infrastructure
* Simplify collaboration

---

## Difference Between Variables And Modules?

Variables:

```text
Reusable Values
```

Examples:

```text
Region
Environment
Instance Type
```

---

Modules:

```text
Reusable Infrastructure
```

Examples:

```text
EC2 Creation Logic
VPC Creation Logic
S3 Creation Logic
```

---

## What Does source Mean In A Module?

The source attribute tells Terraform where the module is located.

Example:

```hcl
source = "./modules/ec2"
```

Meaning:

```text
Use The EC2 Module Stored In modules/ec2
```

---

# Day 3 Summary

Completed Topics:

✅ Why Modules

✅ Module Structure

✅ Module Inputs

✅ Module Outputs

✅ Module Reusability

✅ Terraform Registry

✅ Public Modules

✅ Private Modules

✅ Industry Best Practices

Status:

```text
Terraform Day 3 Complete ✅
```
