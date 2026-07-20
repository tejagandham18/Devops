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

# Ansible Zero to Hero - Day 7: Collections, Variables & Variable Precedence

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
