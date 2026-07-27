# Ansible Zero to Hero - Day 1 Notes (Abhishek Veeramalla)

## Overview

Day 1 introduces Ansible, explains why it is used, how it differs from
shell scripting and Python automation, and how it complements Terraform.

## What is Ansible?

Ansible is an open-source IT automation and configuration management
tool.

It can automate: - Configuration Management - Application Deployment -
Software Installation - Cloud Provisioning - Network Automation -
Security Automation

## Why Do We Need Ansible?

Imagine 100 Linux servers need Docker, Git, Python and Nginx installed.

### Manual Method

-   SSH into each server
-   Install software one by one

Problems: - Slow - Error-prone - Not scalable

### Shell Script

Works well for Linux but is platform dependent and difficult to maintain
across environments.

### Python

Very flexible but requires SSH programming, libraries like Paramiko,
exception handling and more maintenance.

### Ansible

Write a YAML playbook and execute:

``` bash
ansible-playbook install.yml
```

Ansible configures all servers automatically.

## Why Companies Choose Ansible

-   Agentless
-   Easy YAML syntax
-   Reusable playbooks
-   Easy maintenance
-   Scales to hundreds of servers

## Agentless Architecture

Unlike agent-based tools, Ansible requires no agent on managed nodes.

Communication: - Linux → SSH - Windows → WinRM

Benefits: - Simple setup - Lightweight - Secure - Lower maintenance

## YAML

Example:

``` yaml
---
- name: Install Git
  apt:
    name: git
    state: present
```

Advantages: - Human readable - Easy to maintain - Minimal syntax

## Terraform vs Ansible

  Terraform                Ansible
  ------------------------ ----------------------------------
  Creates infrastructure   Configures infrastructure
  Uses cloud APIs          Uses SSH/WinRM
  Creates EC2/VPC          Installs software & deploys apps

Workflow:

Terraform → Create Infrastructure → Ansible → Configure Servers → Deploy
Application

## Installation

Windows: - WSL - Ubuntu - Python - Install Ansible with pip

VS Code Extensions: - YAML (Red Hat) - Ansible (Red Hat)

## Upcoming Topics

-   Passwordless Authentication
-   Inventory
-   Ad-hoc Commands
-   Playbooks
-   Roles
-   Variables
-   Templates
-   Handlers
-   Vault
-   Network Automation

## Interview Questions

1.  What is Ansible?
2.  Why is Ansible called agentless?
3.  Why use Ansible instead of shell scripts?
4.  Difference between Terraform and Ansible?

## Key Takeaways

-   Understand Ansible's purpose.
-   Understand why automation is needed.
-   Learn agentless architecture.
-   Learn YAML basics.
-   Understand how Terraform and Ansible complement each other.

# Ansible Zero to Hero - Day 2 Notes (Abhishek Veeramalla)

## Overview

Day 2 covers three core concepts: 1. Passwordless Authentication 2.
Inventory 3. Ad-hoc Commands

These concepts explain how Ansible connects to servers, knows which
servers to manage, and executes commands.

------------------------------------------------------------------------

## Ansible Architecture

``` text
Control Node (Laptop/WSL)
        |
       SSH
        |
 --------------------------
 |          |             |
Managed1  Managed2    Managed3
```

### Control Node

Machine where Ansible is installed.

### Managed Nodes

Servers managed by Ansible (AWS EC2, Azure VM, Linux servers, etc.).

------------------------------------------------------------------------

# 1. Passwordless Authentication

Automation cannot stop for passwords.

### SSH Key Authentication

``` text
Private Key (Laptop)
        |
       SSH
        |
Public Key (Server)
        |
 Authentication
```

Generate keys:

``` bash
ssh-keygen
```

Copy public key:

``` bash
ssh-copy-id ubuntu@<server-ip>
```

Public key is copied into:

``` text
~/.ssh/authorized_keys
```

AWS already follows this model using `.pem` files.

Benefits: - Secure - Fast - Required for automation - No manual password
entry

------------------------------------------------------------------------

# 2. Inventory

Inventory tells Ansible which servers to manage.

Example (INI):

``` ini
[web]
10.0.1.10
10.0.1.11

[database]
10.0.2.10
```

Benefits: - Groups servers - Targets only required machines - Easier
management

Default inventory:

``` text
/etc/ansible/hosts
```

Best practice: maintain a project-specific inventory.

------------------------------------------------------------------------

# 3. Ad-hoc Commands

Used for quick one-time tasks.

Syntax:

``` bash
ansible <target> -i <inventory> -m <module> -a "<arguments>"
```

Examples:

Check connectivity:

``` bash
ansible all -m ping
```

Check hostname:

``` bash
ansible all -m shell -a "hostname"
```

Check disk usage:

``` bash
ansible all -m shell -a "df -h"
```

------------------------------------------------------------------------

## Common Modules

-   ping
-   shell
-   command
-   copy
-   apt
-   yum
-   file
-   service

------------------------------------------------------------------------

## Ad-hoc vs Playbooks

Ad-hoc: - One-time tasks - Testing - Troubleshooting

Playbooks: - Reusable - Multi-step automation - Application deployment -
Server configuration

------------------------------------------------------------------------

## Workflow

``` text
Control Node
      |
Reads Inventory
      |
Passwordless SSH
      |
Runs Ad-hoc Command / Playbook
      |
Managed Nodes
```

------------------------------------------------------------------------

## Terraform + Ansible

Terraform: - Creates infrastructure

Ansible: - Configures infrastructure

Workflow:

Terraform → Create EC2 → Inventory → SSH → Ansible → Configure Server →
Deploy Application

------------------------------------------------------------------------

## Interview Questions

1.  What is Passwordless Authentication?
2.  What is Inventory?
3.  Why use project-specific inventory?
4.  What are Ad-hoc commands?
5.  Difference between Ad-hoc commands and Playbooks?

------------------------------------------------------------------------

## Key Takeaways

# Ansible Zero to Hero - Day 3 Notes (Abhishek Veeramalla)

## Overview

Day 3 introduces **Ansible Playbooks**, the core automation feature of
Ansible. It explains YAML basics, playbook structure, tasks, modules,
and demonstrates deploying a static website by installing Apache and
copying an `index.html` file to an EC2 instance.

------------------------------------------------------------------------

## What is a Playbook?

A Playbook is a YAML file that defines one or more automation tasks to
be executed on managed nodes.

Instead of manually running commands:

-   Install Apache
-   Copy website files
-   Start Apache

You write them once in a playbook and execute:

``` bash
ansible-playbook webserver.yml
```

------------------------------------------------------------------------

## Why Playbooks?

Benefits: - Reusable - Repeatable - Version controlled - Easy to
maintain - Consistent deployments

Workflow:

Playbook → SSH → Execute Tasks → Configured Server

------------------------------------------------------------------------

## YAML Basics

### String

``` yaml
name: Apache
```

### Number

``` yaml
port: 80
```

### Boolean

``` yaml
enabled: true
```

### List

``` yaml
packages:
  - git
  - docker
  - nginx
```

### Dictionary

``` yaml
name: apache2
state: present
```

### List of Dictionaries

``` yaml
users:
  - name: Teja
    role: DevOps
  - name: Rahul
    role: Developer
```

------------------------------------------------------------------------

## Playbook Structure

Hierarchy:

Playbook → Play → Hosts → Tasks → Modules → Arguments

### Hosts

Example:

``` yaml
hosts: web
```

Targets the "web" group from the Inventory.

### Remote User

``` yaml
remote_user: ubuntu
```

Defines the SSH user.

### Tasks

A task performs one operation such as:

-   Install Apache
-   Copy HTML
-   Restart Service

------------------------------------------------------------------------

## Modules

Common modules:

-   apt
-   copy
-   service
-   shell
-   command
-   ping
-   file

Example:

``` yaml
- name: Install Apache
  apt:
    name: apache2
    state: present
```

------------------------------------------------------------------------

## Official Documentation

Documentation:

https://docs.ansible.com/

Use it to understand: - Parameters - Examples - Return values - Module
behavior

------------------------------------------------------------------------

## Practical Demo

Objective:

Deploy a static website.

Steps:

1.  Install Apache
2.  Copy index.html to `/var/www/html`
3.  Start Apache
4.  Browse to `http://<EC2-Public-IP>`

Website becomes accessible.

------------------------------------------------------------------------

## Ad-hoc vs Playbooks

Ad-hoc: - Quick checks - Ping - Hostname - Troubleshooting

Playbooks: - Application deployment - Multi-step automation - Repeatable
workflows

------------------------------------------------------------------------

## Terraform + Ansible

Terraform: - Creates Infrastructure

Ansible: - Configures Infrastructure

Workflow:

Terraform → EC2 Created → Ansible Playbook → Apache Installed → Website
Deployed

------------------------------------------------------------------------

## Interview Questions

1.  What is a Playbook?
2.  Why does Ansible use YAML?
3.  What is a Task?
4.  What is a Module?
5.  Difference between Ad-hoc Commands and Playbooks?

------------------------------------------------------------------------

## Key Takeaways

-   Understand YAML basics.
-   Understand Playbook structure.
-   Learn Hosts, Tasks and Modules.
-   Learn Apache deployment using Playbooks.
-   Understand how Playbooks fit into Terraform + Ansible workflows.


-   Understand Control Node and Managed Nodes.
-   Learn SSH key authentication.
-   Learn Inventory and grouping.
-   Learn Ad-hoc commands.
-   Understand how Ansible works with Terraform.


# Ansible Zero to Hero - Day 4 Notes (Roles)

## Overview

Day 4 explains **Ansible Roles**, which help organize large playbooks
into reusable and maintainable components.

Learning Flow: - Day 1 → What is Ansible? - Day 2 → Connecting to
servers - Day 3 → Automating with Playbooks - Day 4 → Organizing
automation with Roles

------------------------------------------------------------------------

## Why Roles?

Large playbooks with dozens of tasks become difficult to maintain.

Instead of putting everything into one `site.yml`, split related
automation into separate roles.

Benefits: - Modular - Reusable - Easy to maintain - Easy for teams to
collaborate

------------------------------------------------------------------------

## What is a Role?

A Role is a standardized folder structure containing everything needed
for one specific configuration.

Examples: - apache - mysql - docker - security

Each role has one responsibility.

------------------------------------------------------------------------

## Create a Role

``` bash
ansible-galaxy role init apache
```

This creates:

``` text
roles/
└── apache/
    ├── tasks/
    ├── handlers/
    ├── files/
    ├── templates/
    ├── vars/
    ├── defaults/
    ├── meta/
    └── tests/
```

------------------------------------------------------------------------

## Folder Purpose

### tasks/

Main automation logic (`tasks/main.yml`).

### handlers/

Runs only when notified (example: restart Apache).

### files/

Static files such as HTML, CSS, images.

### templates/

Dynamic Jinja2 templates using variables.

### vars/

Role-specific variables.

### defaults/

Default variable values that users can override.

### meta/

Author, dependencies, metadata.

### tests/

Testing files for the role.

------------------------------------------------------------------------

## Converting a Playbook into a Role

Move: - Installation tasks → tasks/main.yml - Static files → files/

Main playbook:

``` yaml
- hosts: web
  roles:
    - apache
```

------------------------------------------------------------------------

## Internal Workflow

Run Playbook → Read Role → Execute tasks → Read vars/defaults → Copy
files → Render templates → Execute handlers if notified

------------------------------------------------------------------------

## Idempotency

Run 1: Apache not installed → Install Apache

Run 2: Apache already installed → No change

Benefits: - Safe - Fast - No duplicate work - Consistent server state

------------------------------------------------------------------------

## Terraform vs Ansible

  Terraform            Ansible
  -------------------- ----------------
  Module               Role
  Infrastructure       Configuration
  Reusable Resources   Reusable Tasks

------------------------------------------------------------------------

## Interview Questions

-   What is an Ansible Role?
-   Why do we use Roles?
-   What is Ansible Galaxy?
-   What is Idempotency?
-   Explain the purpose of tasks, handlers, files, templates, vars,
    defaults and meta.

------------------------------------------------------------------------

## Key Takeaways

-   Roles organize automation.
-   One role = one responsibility.
-   Use `ansible-galaxy role init` to generate the structure.
-   Store content in the correct folders.
-   Roles improve readability, modularity and reusability.
-   Idempotency ensures repeated executions are safe.

# Ansible Zero to Hero - Day 5: Ansible Galaxy

## 📖 Overview

Day 5 introduces **Ansible Galaxy**, the official marketplace for
reusable Ansible Roles and Collections.

Instead of writing common automation from scratch, you can download
community-created roles and use them in your projects.

------------------------------------------------------------------------

## Learning Flow

``` text
Day 1 → Introduction
Day 2 → Inventory & SSH
Day 3 → Playbooks
Day 4 → Roles
Day 5 → Ansible Galaxy
```

------------------------------------------------------------------------

# What is Ansible Galaxy?

Ansible Galaxy is a community repository where DevOps engineers share
reusable roles.

Examples: - Docker - Apache - Nginx - MySQL - Jenkins - Prometheus

------------------------------------------------------------------------

# Why Use Ansible Galaxy?

Instead of writing the same automation repeatedly:

-   Search for a role
-   Install it
-   Use it

Benefits: - Saves time - Reuses tested code - Improves productivity -
Standardizes automation

------------------------------------------------------------------------

# Install a Role

``` bash
ansible-galaxy role install geerlingguy.docker
```

Downloaded roles are stored in:

``` text
~/.ansible/roles
```

------------------------------------------------------------------------

# Using a Role

``` yaml
- hosts: all
  become: true

  roles:
    - geerlingguy.docker
```

------------------------------------------------------------------------

# Internal Workflow

``` text
Search Role
      │
      ▼
Install Role
      │
      ▼
Stored in ~/.ansible/roles
      │
      ▼
Reference in Playbook
      │
      ▼
Execute Role
```

------------------------------------------------------------------------

# Publishing Your Own Role

1.  Create a role.

``` bash
ansible-galaxy role init apache
```

2.  Push it to GitHub.

3.  Update `meta/main.yml`.

Example:

``` yaml
galaxy_info:
  author: Your Name
  description: Apache Role
  license: MIT
```

4.  Import the repository into Ansible Galaxy.

------------------------------------------------------------------------

# Best Practices

-   Use trusted roles.
-   Read documentation before using.
-   Pin versions in production.
-   Don't modify downloaded roles directly.

------------------------------------------------------------------------

# Terraform vs Ansible Galaxy

  Terraform              Ansible
  ---------------------- ---------------------
  Registry               Galaxy
  Modules                Roles
  Infrastructure Reuse   Configuration Reuse

------------------------------------------------------------------------

# Interview Questions

## What is Ansible Galaxy?

The official marketplace for Ansible Roles and Collections.

## Why use it?

To reuse automation and reduce development effort.

## Where are roles stored?

``` text
~/.ansible/roles
```

## How do you install a role?

``` bash
ansible-galaxy role install <role_name>
```

## How do you publish a role?

-   Create Role
-   Push to GitHub
-   Update meta/main.yml
-   Import into Galaxy

------------------------------------------------------------------------

# Key Takeaways

-   Galaxy is the official repository for reusable roles.
-   Install roles using `ansible-galaxy role install`.
-   Downloaded roles are stored in `~/.ansible/roles`.
-   Roles can be referenced directly in playbooks.
-   Publish your own roles through GitHub and Ansible Galaxy.

# Ansible Zero to Hero - Day 6: Collections, Variables & Variable Precedence

> **Topics Covered**
>
> - Understanding Ansible Collections
> - AWS Collection & boto3
> - Creating AWS Resources using Ansible
> - Ansible Vault
> - Variables
> - Variable Precedence
> - Best Practices
> - Interview Questions

---

# 📚 Table of Contents

1. Introduction
2. Understanding Ansible Collections
3. Why Collections?
4. Collections vs Roles vs Modules
5. AWS Collection Architecture
6. boto3 Library
7. Creating AWS Resources
8. Ansible Vault
9. Variables
10. Variables inside Roles
11. Variable Precedence
12. Real World Example
13. Best Practices
14. Interview Questions
15. Key Takeaways

---

# Introduction

Until now we have learned:

```text
Day 1 → Introduction
Day 2 → Inventory & SSH
Day 3 → Playbooks
Day 4 → Roles
Day 5 → Galaxy
Day 6 → Collections
Day 7 → Variables & Variable Precedence
```

Day 7 combines everything we've learned so far.

Instead of only managing Linux servers, we'll learn how Ansible can manage cloud platforms like AWS, Azure, and GCP.

---

# Understanding Ansible Collections

## What is an Ansible Collection?

An **Ansible Collection** is a **versioned package** that contains:

- Modules
- Roles
- Plugins
- Documentation
- Utilities

Collections extend Ansible by providing functionality for specific platforms.

Examples:

- amazon.aws
- azure.azcollection
- kubernetes.core
- cisco.ios

---

## Why Do We Need Collections?

Imagine your manager asks you to create an EC2 instance.

Can Ansible use SSH?

```
Laptop
   │
 SSH
   │
AWS ❌
```

No.

AWS isn't a Linux server.

Instead, AWS exposes an API.

Ansible communicates with AWS through that API.

---

# SSH vs API

## Managing Linux Servers

```
Ansible

↓

SSH

↓

Ubuntu Server
```

---

## Managing AWS

```
Ansible

↓

AWS Collection

↓

boto3

↓

AWS API

↓

AWS Cloud
```

Notice that **SSH is not involved**.

---

# Why Collections Exist

If every AWS, Azure, Cisco, VMware, Kubernetes, and GCP module were included inside Ansible Core, Ansible would become enormous.

Instead:

```
Ansible Core

↓

Install only the Collections you need
```

Benefits:

- Lightweight
- Modular
- Easy to update
- Vendor maintained

---

# Collections vs Roles vs Modules

| Module | Role | Collection |
|----------|------|------------|
| Performs one task | Groups related tasks | Groups Modules, Roles, Plugins & Docs |
| Example: apt | docker | amazon.aws |
| Smallest Unit | Reusable Automation | Complete Platform Toolkit |

Hierarchy:

```
Collection
│
├── Modules
├── Roles
├── Plugins
├── Documentation
└── Utilities
```

---

# Installing Collections

Example:

```bash
ansible-galaxy collection install amazon.aws
```

This downloads the AWS toolkit.

---

# AWS Collection

The AWS Collection provides modules like:

- ec2_instance
- ec2_vpc_net
- s3_bucket
- iam_user
- ec2_security_group
- autoscaling_group

Instead of clicking through the AWS Console, you can automate everything using Playbooks.

---

# What is boto3?

One of the most common interview questions.

**boto3** is the official Python SDK for AWS.

It translates Ansible requests into AWS API calls.

Architecture:

```
Playbook

↓

amazon.aws Collection

↓

boto3

↓

AWS API

↓

AWS Cloud
```

Without boto3, the AWS Collection cannot communicate with AWS.

Install it using:

```bash
pip install boto3 botocore
```

---

# Creating AWS Resources

Example Workflow:

```
Playbook

↓

AWS Collection

↓

boto3

↓

AWS API

↓

EC2 Created
```

Everything happens automatically.

No manual AWS Console interaction is required.

---

# AWS Credentials

To communicate with AWS, Ansible requires:

- Access Key
- Secret Key

These credentials authenticate your requests.

Never hardcode them inside playbooks.

Bad Example:

```yaml
access_key: AKIAxxxxxxxx
secret_key: mysecretkey
```

---

# Ansible Vault

Sensitive information should always be encrypted.

Ansible Vault protects:

- AWS Access Keys
- Passwords
- Database Credentials
- API Tokens

Example:

```bash
ansible-vault create secrets.yml
```

Encrypted files look like:

```
$ANSIBLE_VAULT;1.1;AES256
```

During execution:

```
Encrypted File

↓

Vault Password

↓

Decrypt

↓

Playbook
```

---

# Variables

Hardcoding values makes playbooks difficult to reuse.

Bad:

```yaml
name: apache2
```

Better:

```yaml
name: "{{ package_name }}"
```

Variable:

```yaml
package_name: apache2
```

Tomorrow:

```yaml
package_name: nginx
```

The playbook remains unchanged.

---

# Variables Inside Roles

Variables are usually stored in:

```
roles/

defaults/

main.yml
```

Example:

```yaml
package_name: apache2

service_name: apache2

port: 80
```

Tasks:

```yaml
apt:
  name: "{{ package_name }}"
```

---

# Why Use Variables?

Benefits:

- Reusable Playbooks
- Cleaner Code
- Easy Configuration
- Environment-specific Deployments
- Better Maintenance

---

# Variable Precedence

Sometimes the same variable is defined in multiple places.

Example:

```
defaults/

↓

group_vars/

↓

host_vars/

↓

Extra Variables
```

Which value does Ansible use?

The highest precedence.

---

# Variable Hierarchy

```
Lowest Priority

↓

Role Defaults

↓

Inventory Variables

↓

Group Variables

↓

Host Variables

↓

Play Variables

↓

Task Variables

↓

Extra Variables (-e)

↓

Highest Priority
```

Remember:

> Highest precedence always wins.

---

# Role Defaults

Located in:

```
defaults/main.yml
```

Example:

```yaml
package_name: apache2
```

These are default values.

Easy to override.

---

# Group Variables

Example:

```
group_vars/

web.yml

database.yml
```

web.yml

```yaml
package_name: apache2
```

database.yml

```yaml
package_name: mysql-server
```

Each server group receives different values.

---

# Extra Variables

Highest priority.

Example:

```bash
ansible-playbook site.yml -e "package_name=nginx"
```

This overrides every other variable definition.

---

# Real World Example

Suppose your company has three environments.

Development:

```yaml
region: us-east-1
```

Testing:

```yaml
region: us-west-2
```

Production:

```bash
ansible-playbook deploy.yml -e "region=ap-south-1"
```

Production deployment overrides all other values.

---

# Best Practices

✅ Never hardcode secrets.

✅ Store sensitive data in Vault.

✅ Keep default values in `defaults/main.yml`.

✅ Use Group Variables for environment-specific configuration.

✅ Use Extra Variables only when temporary overrides are needed.

✅ Install only required Collections.

---

# Interview Questions

## What is an Ansible Collection?

A versioned package containing modules, roles, plugins, documentation, and utilities.

---

## Why do we use Collections?

To extend Ansible with platform-specific capabilities without increasing the size of Ansible Core.

---

## What is boto3?

The official Python SDK that allows Ansible's AWS Collection to communicate with AWS APIs.

---

## Why use Ansible Vault?

To encrypt sensitive information such as passwords, API keys, and AWS credentials.

---

## Why use Variables?

To avoid hardcoded values and make playbooks reusable.

---

## Where should Role variables be stored?

```
defaults/main.yml
```

---

## Which variable has the highest precedence?

Extra Variables (`-e`)

---

## Which variable has the lowest precedence?

Role Defaults (`defaults/main.yml`)

---

# Key Takeaways

- Collections extend Ansible for cloud providers and network platforms.
- AWS Collections communicate through AWS APIs, not SSH.
- boto3 acts as the communication layer between Ansible and AWS.
- Sensitive credentials should always be stored using Ansible Vault.
- Variables make playbooks reusable and configurable.
- Variable precedence determines which value Ansible ultimately uses.
- Extra Variables have the highest priority, while Role Defaults have the lowest.

---

# Quick Revision

```
Collections
        │
        ├── Modules
        ├── Roles
        ├── Plugins
        └── Documentation

↓

AWS Collection

↓

boto3

↓

AWS API

↓

Cloud Resources

↓

Variables

↓

Role Defaults

↓

Group Variables

↓

Extra Variables

↓

Deployment
```

> **Remember:**  
> **Module → One Task**  
> **Role → Collection of Tasks**  
> **Collection → Complete Platform Toolkit**  
> **Variables → Reusable Configuration**  
> **Vault → Secure Secrets**  
> **Extra Variables → Highest Priority**


# Ansible Zero to Hero - Day 7 Project
## AWS Infrastructure Automation using Ansible

> **Project Goal**
>
> Learn how to automate the complete lifecycle of AWS infrastructure using Ansible.
>
> This project combines everything learned from Day 1 to Day 6 and introduces practical concepts such as Loops, Facts, Conditionals, Tags, and Idempotency.

---

# 📚 Table of Contents

1. Project Overview
2. Project Architecture
3. Technologies Used
4. Project Workflow
5. Phase 1 - Provisioning EC2 Instances
6. Understanding Idempotency
7. Understanding Loops
8. Securing AWS Credentials using Vault
9. Passwordless SSH Authentication
10. Ansible Facts
11. Debug Module
12. Conditionals
13. Tags
14. Complete Workflow
15. Real World Scenario
16. Best Practices
17. Interview Questions
18. Key Takeaways

---

# Project Overview

Imagine you're working as a DevOps Engineer.

Your manager assigns the following task:

- Create EC2 instances on AWS
- Secure AWS credentials
- Configure SSH access
- Connect to servers
- Gather system information
- Shutdown only Ubuntu machines
- Leave Amazon Linux untouched

Instead of performing everything manually, we automate the entire process using Ansible.

---

# Project Architecture

```text
                   DevOps Engineer
                          │
                          ▼
                  Ansible Control Node
                          │
          ┌───────────────┴───────────────┐
          │                               │
          ▼                               ▼
     Ansible Vault                 AWS Collection
          │                               │
          ▼                               ▼
   Encrypted Credentials             boto3 Library
                                            │
                                            ▼
                                         AWS API
                                            │
               ┌────────────────────────────┴────────────────────────────┐
               ▼                         ▼                              ▼
        Ubuntu EC2                Ubuntu EC2                  Amazon Linux EC2
```

Everything is controlled from a single Ansible Control Node.

---

# Technologies Used

- Ansible
- AWS EC2
- AWS Collection
- boto3
- SSH
- Ansible Vault
- YAML
- Playbooks
- Inventory
- Variables

---

# Project Workflow

```text
Write Playbook
       │
       ▼
Authenticate to AWS
       │
       ▼
Provision EC2 Instances
       │
       ▼
Configure Passwordless SSH
       │
       ▼
Gather Facts
       │
       ▼
Apply Conditions
       │
       ▼
Execute Tasks
```

---

# Phase 1 - Provisioning EC2 Instances

## Objective

Create multiple EC2 instances automatically using Ansible.

Instead of manually clicking through the AWS Console, Ansible communicates directly with AWS APIs.

Architecture:

```text
Playbook
     │
     ▼
amazon.aws Collection
     │
     ▼
boto3
     │
     ▼
AWS API
     │
     ▼
EC2 Instance Created
```

---

# Why Collections?

Standard Ansible modules communicate using SSH.

AWS is not a Linux server.

Therefore SSH cannot create EC2 instances.

Instead Ansible uses:

- AWS Collection
- boto3
- AWS APIs

---

# Understanding Idempotency

One of Ansible's core principles is **Idempotency**.

Running the same playbook multiple times should produce the same desired state.

Example:

```
Run #1

EC2 Created

Run #2

No Changes
```

This prevents accidental duplicate infrastructure.

---

# Why Did the Video Use Loops?

Suppose you need:

- Ubuntu Server 1
- Ubuntu Server 2
- Amazon Linux Server

Instead of writing three almost identical tasks, Ansible uses **Loops**.

Concept:

```
List of Instances

↓

Loop

↓

Create Instance 1

↓

Create Instance 2

↓

Create Instance 3
```

Loops reduce duplicate code and make playbooks easier to maintain.

---

# Securing AWS Credentials

AWS APIs require authentication.

Authentication uses:

- Access Key
- Secret Key

Never hardcode credentials inside playbooks.

Bad Practice:

```yaml
access_key: XXXXX
secret_key: XXXXX
```

If this code is pushed to GitHub, anyone could access your AWS account.

---

# Ansible Vault

Ansible Vault encrypts sensitive information.

Workflow:

```
AWS Keys

↓

Vault Encrypt

↓

Encrypted File

↓

Git Repository

↓

Safe
```

During execution:

```
Encrypted File

↓

Vault Password

↓

Decrypt

↓

Playbook
```

Real organizations often use:

- Ansible Vault
- AWS Secrets Manager
- HashiCorp Vault

---

# Passwordless SSH Authentication

After EC2 instances are created, Ansible must connect to them.

Architecture:

```
Control Node

↓

SSH Key

↓

Managed Node
```

SSH keys eliminate the need to type passwords repeatedly.

This is why Ansible is called an **Agentless Configuration Management Tool**.

---

# Gathering Facts

Before making decisions, Ansible collects system information.

These are called **Facts**.

Facts include:

- Operating System
- Distribution
- Distribution Family
- Hostname
- CPU
- Memory
- Kernel Version
- Architecture
- Network Interfaces

Think of Facts as the identity card of a server.

---

# Debug Module

The Debug module helps display gathered information.

Example uses:

- Verify Operating System
- Check Distribution Family
- Display Variables
- Troubleshoot Playbooks

Debug is commonly used during development and testing.

---

# Conditionals

Imagine you have three servers.

```
Ubuntu

Ubuntu

Amazon Linux
```

Your manager says:

Shutdown only Ubuntu servers.

Ansible first gathers Facts.

Then it checks:

```
Is Distribution Family Debian?

↓

Yes

↓

Shutdown

↓

No

↓

Skip
```

The same playbook behaves differently depending on the target server.

---

# Why Conditionals Matter

Organizations usually have mixed environments.

Example:

- Ubuntu
- Red Hat
- Amazon Linux
- CentOS

Instead of writing separate playbooks, one playbook can automatically detect the operating system and execute the correct tasks.

---

# Tags

Large playbooks may contain multiple tasks.

Example:

- Provision EC2
- Configure SSH
- Install Software
- Configure Application
- Verify Deployment

Sometimes you only want to execute one section.

Tags allow selective execution.

Example:

```
Run Only

Provision

OR

Configure

OR

Verify
```

Tags save time during development.

---

# Complete Workflow

```
Write Playbook

↓

Authenticate AWS

↓

Create EC2

↓

Configure SSH

↓

Gather Facts

↓

Evaluate Conditions

↓

Execute Tasks

↓

Verification
```

---

# Concepts Learned

| Topic | Purpose |
|--------|----------|
| Collections | AWS Communication |
| boto3 | AWS API Communication |
| Vault | Secure Credentials |
| EC2 Module | Provision Infrastructure |
| Inventory | Target Servers |
| SSH | Passwordless Authentication |
| Facts | Gather Server Information |
| Debug | Display Facts |
| Loops | Reduce Duplicate Tasks |
| Conditionals | Execute Tasks Selectively |
| Tags | Run Specific Tasks |
| Idempotency | Avoid Duplicate Infrastructure |

---

# Real World Example

Suppose your company has:

```
Ubuntu Web Servers

Amazon Linux Monitoring Servers

Red Hat Database Servers
```

A maintenance window is scheduled.

Requirements:

- Restart Ubuntu Web Servers
- Skip Monitoring Servers
- Leave Database Servers Running

Instead of manually checking every server, Ansible:

1. Gathers Facts
2. Evaluates Conditions
3. Executes the correct tasks automatically

This is exactly how enterprise automation works.

---

# Best Practices

- Never hardcode AWS credentials.
- Always use Ansible Vault.
- Use Loops to reduce duplicate code.
- Gather Facts before using Conditions.
- Use Tags for faster execution.
- Verify infrastructure after deployment.
- Keep playbooks idempotent.
- Store reusable values as Variables.

---

# Interview Questions

## What is Idempotency?

Running the same playbook multiple times produces the same desired state without creating duplicate resources.

---

## Why use Ansible Vault?

To securely encrypt passwords, API keys, and other sensitive information.

---

## What are Ansible Facts?

Facts are automatically collected information about managed nodes, such as operating system, CPU, memory, and network details.

---

## Why use the Debug module?

To inspect variables and gathered Facts during development and troubleshooting.

---

## Why use Conditionals?

To execute tasks only when specific conditions are met.

---

## Why use Loops?

To repeat the same task for multiple items while avoiding duplicate code.

---

## Why use Tags?

To execute only selected portions of a playbook.

---

# Key Takeaways

- Automate infrastructure provisioning using AWS Collections.
- Secure AWS credentials using Ansible Vault.
- Configure passwordless SSH access.
- Gather Facts before making decisions.
- Use Conditionals for intelligent automation.
- Use Loops to simplify repetitive tasks.
- Use Tags to control playbook execution.
- Ensure playbooks remain idempotent.

---

# Summary

This project is the first complete end-to-end Ansible automation project.

It combines:

- Infrastructure Provisioning
- Configuration Management
- Security
- Automation
- Decision Making
- Reusability

into a single practical workflow.

By completing this project, you understand how Ansible is used in real DevOps environments to automate cloud infrastructure efficiently and safely.


# Ansible Zero to Hero - Day 8 Notes
# Topic: Error Handling in Ansible Playbooks

## Overview

In this session, I learned how Ansible handles task failures and how to control the execution flow using different error-handling techniques. By default, Ansible stops executing further tasks on a host if a task fails. However, in real-world DevOps environments, not every failure should stop the automation. Ansible provides several mechanisms to handle these scenarios.

---

# Why Error Handling is Important

In production environments:

- Some tasks are expected to fail.
- Some commands are only used to verify the system state.
- Different servers may have different configurations.
- We may want to continue execution even after certain failures.
- We may also want to define our own conditions for considering a task as failed.

Error handling makes playbooks more robust, reliable, and production-ready.

---

# Default Ansible Behavior

By default, if a task fails on a host, Ansible stops executing the remaining tasks for that host.

Example:

```yaml
tasks:
  - Install Docker
  - Start Docker
  - Deploy Application
```

If **Install Docker** fails:

```text
Install Docker        ❌ Failed
Start Docker          ❌ Skipped
Deploy Application    ❌ Skipped
```

This is the default behavior because the remaining tasks depend on the successful completion of the previous task.

---

# ignore_errors

## Purpose

The `ignore_errors` keyword tells Ansible to continue executing the remaining tasks even if the current task fails.

Example:

```yaml
- name: Check Docker
  command: docker --version
  ignore_errors: true
```

### Execution Flow

```text
Run Command
      ↓
Command Failed
      ↓
Ignore Failure
      ↓
Continue to Next Task
```

### Important Notes

- The task is still marked as **FAILED**.
- Only the playbook execution continues.
- It should only be used when a failure is expected and acceptable.

---

# register

## Purpose

The `register` keyword stores the output of a task into a variable.

Example:

```yaml
- name: Check Docker
  command: docker --version
  register: docker_check
```

The registered variable stores information such as:

- Standard Output (stdout)
- Standard Error (stderr)
- Exit Code (rc)
- Failed Status
- Changed Status

Example Output:

```yaml
docker_check:
  stdout: Docker version 28.0
  stderr:
  rc: 0
  failed: false
```

If Docker is not installed:

```yaml
docker_check:
  stdout:
  stderr: docker: command not found
  rc: 127
  failed: true
```

---

# when

## Purpose

The `when` statement allows conditional execution of tasks.

It works similarly to an **if condition** in programming languages.

Example:

```yaml
- name: Install Docker
  apt:
    name: docker.io
    state: present
  when: docker_check.failed
```

Execution Flow:

```text
Check Docker
      ↓
Register Output
      ↓
Did Task Fail?
      ↓
Yes
      ↓
Install Docker
```

If Docker already exists, the installation task is skipped.

---

# failed_when

## Purpose

By default, Ansible decides whether a task has failed based on the command's exit code.

Exit Code:

| Exit Code | Meaning |
|-----------|---------|
| 0 | Success |
| Non-zero | Failure |

Sometimes this default behavior is not sufficient.

The `failed_when` keyword allows us to define our own condition for considering a task as failed.

In simple words:

> Instead of Ansible deciding what is a failure, we define our own failure condition.

---

## Example 1

Suppose we execute:

```yaml
- name: Check Disk Usage
  command: df -h
  register: disk
```

The command executes successfully.

Exit Code:

```text
0
```

Normally Ansible marks it as successful.

Suppose the output contains:

```text
Filesystem   Use%
/dev/xvda1   99%
```

Although the command succeeded, 99% disk usage is dangerous.

We can define:

```yaml
failed_when: "'99%' in disk.stdout"
```

Execution Flow:

```text
Command Executed Successfully
        ↓
Exit Code = 0
        ↓
Normally Success
        ↓
failed_when Checks Output
        ↓
Found 99%
        ↓
Mark Task as FAILED
```

---

## Example 2

Suppose Docker version 18 is installed but our application requires version 28.

```yaml
- name: Check Docker
  command: docker --version
  register: docker_check

  failed_when: "'18.' in docker_check.stdout"
```

Although Docker exists, the task will fail because our custom condition evaluates to true.

---

## Example 3

Suppose a command returns a non-zero exit code, but we do not want Ansible to consider it a failure.

```yaml
- name: Example
  command: grep hello file.txt

  failed_when: false
```

Normally:

```text
Exit Code = 1
```

Ansible marks it as failed.

With:

```yaml
failed_when: false
```

The task is considered successful.

---

# Difference Between ignore_errors and failed_when

## ignore_errors

Purpose:

Continue execution even after a task fails.

Execution Flow:

```text
Task Failed
      ↓
Ignore Failure
      ↓
Continue Execution
```

The task is still reported as failed.

---

## failed_when

Purpose:

Override Ansible's definition of task failure.

Execution Flow:

```text
Command Executed
      ↓
Evaluate Custom Condition
      ↓
Condition True
      ↓
Mark Task as FAILED
```

or

```text
Command Failed
      ↓
Custom Condition False
      ↓
Mark Task as SUCCESS
```

---

# Key Differences

| ignore_errors | failed_when |
|---------------|-------------|
| Task actually fails | Defines whether task should fail |
| Continues execution | Changes failure criteria |
| Failure is ignored | Failure logic is overridden |

---

# Best Practices

- Use `ignore_errors` only when task failures are expected.
- Use `register` whenever task output will be used later.
- Use `when` for conditional execution instead of unnecessary tasks.
- Use `failed_when` only when Ansible's default failure detection is insufficient.

---

# Interview Questions

## What is `ignore_errors`?

`ignore_errors` allows the playbook to continue executing subsequent tasks even if the current task fails.

---

## What is `register`?

`register` stores the output of a task in a variable so it can be referenced by later tasks.

---

## What is `when`?

`when` is a conditional statement that executes a task only if the specified condition evaluates to true.

---

## What is `failed_when`?

`failed_when` overrides Ansible's default success or failure status by allowing us to define our own condition for marking a task as failed.

---

# Key Takeaways

After completing this session, I learned:

- Default task failure behavior in Ansible.
- Using `ignore_errors` to continue execution after expected failures.
- Capturing task output using `register`.
- Writing conditional tasks using `when`.
- Overriding default failure conditions using `failed_when`.
- Building more intelligent and production-ready Ansible playbooks.

---

# One-Line Summary

**By default, Ansible decides whether a task has failed. Using `failed_when`, we take control and define our own criteria for determining task failure.**

# Ansible Zero to Hero - Day 9 Notes
# Topic: Ansible Vault (Securing Sensitive Data)

## Overview

In this session, I learned about **Ansible Vault**, a built-in Ansible feature used to securely store sensitive information such as passwords, API keys, SSH keys, and cloud credentials.

Instead of storing secrets in plain text inside playbooks or variable files, Ansible Vault encrypts them using AES-256 encryption. The encrypted data can only be accessed using the correct vault password.

---

# Why Do We Need Ansible Vault?

Imagine an Ansible playbook that creates AWS EC2 instances.

To create an EC2 instance, we need AWS credentials.

Example:

```yaml
aws_access_key: AKIAxxxxxxxxxxxxx
aws_secret_key: xxxxxxxxxxxxxxxxxxxxxxxxx
```

If this file is pushed to GitHub, anyone can view the credentials and misuse the AWS account.

This creates major security risks such as:

- Unauthorized AWS resource creation
- Deletion of cloud resources
- Access to sensitive data
- Increased cloud costs

To avoid exposing secrets, Ansible provides **Vault**.

---

# What is Ansible Vault?

Ansible Vault is a built-in encryption mechanism that encrypts files, variables, or strings containing sensitive information.

Only users with the correct vault password can decrypt and use the data.

It allows developers to safely store secrets inside version control systems like GitHub without exposing confidential information.

---

# How Ansible Vault Works

```text
Sensitive Information
        │
        ▼
Encrypt Using Vault Password
        │
        ▼
Encrypted File
        │
        ▼
Store in Git Repository
        │
        ▼
Run Playbook
        │
        ▼
Enter Vault Password
        │
        ▼
Secrets Decrypted in Memory
        │
        ▼
Playbook Executes
```

---

# Creating an Encrypted File

Command:

```bash
ansible-vault create secrets.yml
```

Ansible asks for:

```text
New Vault Password:
Confirm Vault Password:
```

After entering the password, a text editor opens.

Example:

```yaml
aws_access_key: AKIAxxxxxxxx
aws_secret_key: xxxxxxxxxxxxx
```

After saving, the file is automatically encrypted.

Encrypted file:

```text
$ANSIBLE_VAULT;1.1;AES256
613934623432....
834acbcfd.....
```

The original content is no longer readable.

---

# Using Vault in Playbooks

Instead of writing secrets directly inside the playbook,

```yaml
vars:
  aws_access_key: AKIAxxxx
  aws_secret_key: xxxxx
```

store them in an encrypted file.

Example:

```yaml
vars_files:
  - vault/aws_credentials.yml
```

Run the playbook:

```bash
ansible-playbook playbook.yml --ask-vault-pass
```

Execution Flow:

```text
Run Playbook
      │
      ▼
Prompt for Vault Password
      │
      ▼
Decrypt Secret File
      │
      ▼
Load Variables
      │
      ▼
Execute Tasks
```

---

# Ansible Vault Commands

## 1. Create

Creates a new encrypted file.

```bash
ansible-vault create secrets.yml
```

---

## 2. View

Displays the contents of an encrypted file without permanently decrypting it.

```bash
ansible-vault view secrets.yml
```

The file remains encrypted after viewing.

---

## 3. Edit

Edits an encrypted file directly.

```bash
ansible-vault edit secrets.yml
```

Execution Flow:

```text
Encrypted File
      │
      ▼
Enter Password
      │
      ▼
Edit Content
      │
      ▼
Save
      │
      ▼
Automatically Re-encrypted
```

---

## 4. Encrypt

Encrypts an existing plain-text file.

```bash
ansible-vault encrypt secrets.yml
```

Useful when a file was created before Vault was introduced.

---

## 5. Decrypt

Removes encryption from a Vault file.

```bash
ansible-vault decrypt secrets.yml
```

The file becomes plain text.

Use this only when absolutely necessary.

---

## 6. Encrypt String

Encrypts only a specific variable instead of the entire file.

Command:

```bash
ansible-vault encrypt_string
```

Example Output:

```yaml
database_password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          393733346234....
```

Useful when only one or two variables are confidential.

---

# Our Project Example

During our AWS Ansible project, we created:

```text
vault/
└── aws_credentials.yml
```

Inside this file we stored:

```yaml
aws_access_key:
aws_secret_key:
aws_region:
```

Instead of exposing these values inside playbooks.

The playbook loaded them using:

```yaml
vars_files:
  - ../vault/aws_credentials.yml
```

Execution:

```bash
ansible-playbook playbooks/provision.yml --ask-vault-pass
```

Ansible decrypts the file temporarily in memory, uses the variables, and never exposes them in plain text.

---

# Why Shouldn't We Store the Vault Password?

Suppose the repository contains:

```text
project/
├── vault.yml
└── vault.pass
```

Although the secrets are encrypted, the password is also available.

This defeats the purpose of encryption.

Therefore:

**Never commit the vault password file to GitHub.**

---

# Where Should the Vault Password Be Stored?

In production environments, vault passwords are managed using secure secret management systems such as:

- AWS Secrets Manager
- AWS Systems Manager Parameter Store
- HashiCorp Vault
- Azure Key Vault
- Google Secret Manager

These tools securely store and manage secrets.

---

# Why Use Different Vault Passwords for Different Environments?

Production, Testing, and Development environments should not share the same vault password.

Example:

```text
Development
      │
      ▼
Vault Password A

-------------------------

Testing
      │
      ▼
Vault Password B

-------------------------

Production
      │
      ▼
Vault Password C
```

Benefits:

- Limits security risks.
- Prevents unauthorized production access.
- Follows the Principle of Least Privilege.

---

# Best Practices

- Never hardcode passwords or API keys in playbooks.
- Always encrypt sensitive files before pushing to Git.
- Never store the vault password in the repository.
- Use strong and random vault passwords.
- Store vault passwords in dedicated secret management systems.
- Use separate vault passwords for different environments.

---

# Advantages of Ansible Vault

- Built directly into Ansible.
- Uses AES-256 encryption.
- Protects sensitive credentials.
- Safe to store encrypted files in Git repositories.
- Easy integration with Ansible playbooks.
- Supports both file-level and variable-level encryption.

---

# Interview Questions

## What is Ansible Vault?

Ansible Vault is a built-in Ansible feature used to encrypt sensitive data such as passwords, API keys, and secret variables so they can be securely stored and used in playbooks.

---

## Why do we use Ansible Vault?

To protect confidential information from being exposed in source code repositories while allowing playbooks to access those secrets securely.

---

## Can we encrypt only a single variable?

Yes.

Using:

```bash
ansible-vault encrypt_string
```

we can encrypt individual variables instead of the entire file.

---

## Is it safe to push Vault files to GitHub?

Yes.

Encrypted Vault files can be stored in GitHub safely.

However, the **vault password must never be stored in the same repository.**

---

## Which encryption algorithm does Ansible Vault use?

Ansible Vault uses **AES-256** encryption.

---

# Commands Learned

```bash
ansible-vault create secrets.yml
ansible-vault view secrets.yml
ansible-vault edit secrets.yml
ansible-vault encrypt secrets.yml
ansible-vault decrypt secrets.yml
ansible-vault encrypt_string
```

---

# Key Takeaways

After completing this session, I learned:

- Why secret management is important.
- How Ansible Vault protects sensitive information.
- How to create encrypted files.
- How to view and edit encrypted files.
- How to encrypt existing files.
- How to encrypt individual variables.
- How to use encrypted variables inside playbooks.
- Security best practices for managing secrets.
- Why vault passwords should never be committed to Git.
- Why different environments should use different vault passwords.

---

# One-Line Summary

**Ansible Vault is a built-in security feature that encrypts sensitive information such as passwords, API keys, and cloud credentials, allowing them to be stored safely in Ansible projects and version control systems while remaining accessible only to authorized users with the correct vault password.**
