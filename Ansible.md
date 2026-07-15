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

-   Understand Control Node and Managed Nodes.
-   Learn SSH key authentication.
-   Learn Inventory and grouping.
-   Learn Ad-hoc commands.
-   Understand how Ansible works with Terraform.
