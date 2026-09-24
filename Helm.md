# 🚀 Kubernetes - Helm (Phase 1: Helm Fundamentals)

## 📌 Objective

Learn the fundamentals of Helm, understand why it is used, create a Helm Chart, understand its structure, generate Kubernetes manifests using templates, and deploy the first Helm application.

---

# What is Helm?

Helm is the **Package Manager for Kubernetes**.

It simplifies the deployment and management of Kubernetes applications by packaging multiple Kubernetes YAML files into a reusable package called a **Helm Chart**.

### Linux Example

```
Ubuntu      → apt
Python      → pip
NodeJS      → npm
Kubernetes  → Helm
```

---

# Why Helm?

Imagine an application contains:

```
Deployment
Service
ConfigMap
Secret
Ingress
PVC
HPA
ServiceAccount
```

Without Helm:

```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml
kubectl apply -f ingress.yaml
...
```

As applications grow, managing many YAML files becomes difficult.

Helm packages everything into a single reusable Chart.

```
helm install my-app ./my-chart
```

---

# Helm Core Components

## 1. Helm

The CLI tool used to manage Kubernetes applications.

Examples:

```bash
helm create
helm install
helm list
helm upgrade
helm rollback
helm uninstall
```

---

## 2. Chart

A Chart is a package containing Kubernetes resource templates.

Think of it as:

```
Application Package
```

Example:

```
teja-nginx/

├── Chart.yaml
├── values.yaml
├── templates/
├── charts/
└── .helmignore
```

A Chart contains everything required to deploy an application.

---

## 3. Release

A Release is an installed instance of a Chart.

Example:

Chart

```
teja-nginx
```

Installation

```bash
helm install teja-app ./teja-nginx
```

Result

```
Chart

↓

teja-nginx

↓

Release

↓

teja-app
```

One Chart can create multiple Releases.

Example:

```
helm install website ./teja-nginx

helm install customer-app ./teja-nginx
```

Result

```
Chart

↓

website

customer-app
```

---

# Helm Chart Structure

Running

```bash
helm create teja-nginx
```

creates:

```
teja-nginx/

├── Chart.yaml
├── values.yaml
├── templates/
├── charts/
└── .helmignore
```

The folder structure remains the same for every application.

Only the configuration changes based on the application.

Example:

```
Nginx
MongoDB
Redis
Java App
Python App
```

All use the same Helm structure.

---

# Chart.yaml

Chart.yaml contains information about the Helm Chart.

Example:

```yaml
apiVersion: v2
name: teja-nginx
description: A Helm chart for Kubernetes
type: application
version: 0.1.0
appVersion: "1.16.0"
```

Meaning:

| Field | Purpose |
|--------|---------|
| apiVersion | Helm Chart API Version |
| name | Chart Name |
| description | Description of Chart |
| type | application / library |
| version | Chart Version |
| appVersion | Application Version |

---

## Difference between version and appVersion

Example

```
Chart Version

0.1.0

↓

0.2.0
```

Means the Helm Chart changed.

Application Version

```
1.16.0

↓

1.17.0
```

Means the application image/version changed.

---

# values.yaml

values.yaml stores application configuration.

Example

```yaml
replicaCount: 1

image:
  repository: nginx
  tag: ""

service:
  port: 80
```

Instead of editing Deployment YAML directly, we change values here.

Example

Development

```yaml
replicaCount: 1
```

Testing

```yaml
replicaCount: 2
```

Production

```yaml
replicaCount: 5
```

The Deployment template remains unchanged.

Only values.yaml changes.

---

# templates/

The templates folder contains Kubernetes YAML templates.

Example:

```
deployment.yaml

service.yaml

ingress.yaml

serviceaccount.yaml
```

Unlike normal Kubernetes YAML files, templates contain placeholders.

Example

```yaml
replicas: {{ .Values.replicaCount }}
```

Helm reads:

```yaml
replicaCount: 3
```

from values.yaml

and generates

```yaml
replicas: 3
```

Another example

Template

```yaml
image:
{{ .Values.image.repository }}:{{ .Values.image.tag }}
```

values.yaml

```yaml
image:
  repository: nginx
  tag: "1.27"
```

Generated Deployment

```yaml
image: nginx:1.27
```

---

# Relationship between values.yaml and templates

```
values.yaml

↓

Configuration

↓

templates/

↓

Reads Configuration

↓

Generates Kubernetes YAML

↓

Deployment

↓

Pods Running
```

---

# Helm Template Command

Command

```bash
helm template teja-app ./teja-nginx
```

Purpose

Generates Kubernetes YAML locally.

Nothing is deployed to Kubernetes.

Think of it as a Preview.

Workflow

```
Chart

↓

Helm Template

↓

Generated YAML

↓

Terminal Output
```

---

# Helm Install

Command

```bash
helm install teja-app ./teja-nginx
```

Purpose

Deploys the Helm Chart into the Kubernetes Cluster.

Helm generates the manifests and automatically sends them to Kubernetes.

Workflow

```
Chart

↓

values.yaml

↓

templates

↓

Helm Engine

↓

Generated YAML

↓

Kubernetes API

↓

Deployment

↓

ReplicaSet

↓

Pods
```

Successful Output

```
NAME: teja-app

STATUS: deployed

REVISION: 1
```

This creates the first Helm Release.

---

# Difference Between helm template and helm install

## helm template

```
Reads Chart

↓

Generates YAML

↓

Prints Output

↓

No Deployment
```

## helm install

```
Reads Chart

↓

Generates YAML

↓

Deploys to Kubernetes

↓

Creates Deployment

↓

Creates Pods
```

---

# Real World Workflow

```
Chart.yaml

↓

Application Information

↓

values.yaml

↓

Application Configuration

↓

templates/

↓

Kubernetes Templates

↓

helm template

↓

Preview

↓

helm install

↓

Release Created

↓

Kubernetes Cluster
```

---

# Commands Used

## Create Helm Chart

```bash
helm create teja-nginx
```

---

## Show Chart Structure

```bash
ls -R teja-nginx
```

---

## Generate Kubernetes YAML

```bash
helm template teja-app ./teja-nginx
```

---

## Install Helm Chart

```bash
helm install teja-app ./teja-nginx
```

---

## Verify Helm Version

```bash
helm version
```

---

# Key Takeaways

✅ Helm is the Package Manager for Kubernetes.

✅ A Chart is a package containing Kubernetes templates.

✅ A Release is an installed instance of a Chart.

✅ Chart.yaml stores Chart information.

✅ values.yaml stores application configuration.

✅ templates/ contains Kubernetes YAML templates.

✅ Helm replaces template placeholders using values.yaml.

✅ helm template previews generated Kubernetes YAML.

✅ helm install deploys the application into Kubernetes.

---

# Interview Questions

### What is Helm?

Helm is the Package Manager for Kubernetes that packages Kubernetes resources into reusable Charts and simplifies deployment and lifecycle management.

---

### What is a Chart?

A Chart is a reusable package containing Kubernetes templates and configuration required to deploy an application.

---

### What is a Release?

A Release is a deployed instance of a Helm Chart.

---

### What is values.yaml?

values.yaml stores configurable values such as replicas, image, ports, resources, and environment-specific settings.

---

### What is the purpose of templates?

Templates contain Kubernetes resource definitions with placeholders that Helm replaces using values from values.yaml.

---

### Difference between helm template and helm install?

helm template generates Kubernetes manifests locally without deploying them.

helm install generates the manifests and deploys them into the Kubernetes cluster.

---

# Phase 1 Status

```
✅ Install Helm

✅ Create Helm Chart

✅ Chart.yaml

✅ values.yaml

✅ templates/

✅ helm template

✅ helm install

🎉 Helm Fundamentals Completed
```

---

# Next Phase

Helm Release Management

- helm list
- helm status
- helm upgrade
- helm rollback
- helm uninstall
