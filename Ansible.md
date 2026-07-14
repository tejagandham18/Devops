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
