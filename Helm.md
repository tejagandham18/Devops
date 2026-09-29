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

# Helm Phase 2 — Release Management

## 📌 Phase Overview

**Phase:** Helm Phase 2  
**Topic:** Release Management  
**Chart:** `teja-nginx`  
**Release:** `teja-app`  
**Namespace:** `default`

### 🎯 Objective

In Phase 2, we learn how to manage an already-installed Helm release.

We cover:

- `helm list`
- `helm status`
- `helm upgrade`
- `helm history`
- `helm rollback`
- `helm uninstall`

The complete lifecycle we performed:

```text
helm install
     ↓
Revision 1
     ↓
helm upgrade
     ↓
Revision 2
     ↓
helm history
     ↓
helm rollback
     ↓
Revision 3
     ↓
helm uninstall
     ↓
Release removed
```

---

# 1. Chart vs Release

Before learning release management, we need to understand the difference between a **Chart** and a **Release**.

## 📦 Chart

A Helm Chart is a package/blueprint containing:

- Kubernetes templates
- Configuration values
- Chart metadata
- Other files required to deploy an application

Our chart:

```text
teja-nginx
```

## 🚀 Release

A Release is an **installed instance of a Helm Chart**.

Our release:

```text
teja-app
```

Relationship:

```text
Chart
teja-nginx
    │
    │ helm install
    ▼
Release
teja-app
```

One chart can create multiple releases.

For example:

```text
teja-nginx
    ├── teja-app-dev
    ├── teja-app-uat
    └── teja-app-prod
```

Each release can be managed independently.

---

# 2. What is a Helm Revision?

A **revision** represents a version/state of a particular Helm release.

When a release is installed for the first time:

```text
Revision 1
```

After an upgrade:

```text
Revision 2
```

After another change:

```text
Revision 3
```

A rollback also creates a **new revision**.

### Important

Helm revision numbers move forward.

For example:

```text
Revision 1 → Install
Revision 2 → Upgrade
Revision 3 → Rollback
```

A rollback does **not** change the current revision number back to an older number.

---

# 3. `helm list`

## Purpose

`helm list` displays the Helm releases installed in the current namespace/context.

### Command

```bash
helm list
```

Initially, our output was:

```text
NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART                 APP VERSION
teja-app        default         1               2026-09-24 10:27:45.045417256 +0000 UTC deployed        teja-nginx-0.1.0      1.16.0
```

## Understanding the Columns

### NAME

```text
teja-app
```

This is the **Helm Release name**.

### NAMESPACE

```text
default
```

The release is installed in the `default` Kubernetes namespace.

### REVISION

```text
1
```

This means it is currently Revision 1.

### STATUS

```text
deployed
```

The release was successfully deployed.

### CHART

```text
teja-nginx-0.1.0
```

This represents:

```text
Chart Name - Chart Version
```

So:

```text
Chart Name:    teja-nginx
Chart Version: 0.1.0
```

### APP VERSION

```text
1.16.0
```

This comes from `Chart.yaml`:

```yaml
appVersion: "1.16.0"
```

---

# 4. `helm status`

## Purpose

`helm status` provides detailed information about a particular Helm release.

### Command

```bash
helm status teja-app
```

Our initial output contained:

```text
NAME: teja-app
NAMESPACE: default
STATUS: deployed
REVISION: 1
DESCRIPTION: Install complete
```

It also showed the Kubernetes resources created by the chart.

Our Helm release created:

```text
ServiceAccount
Service
Deployment
Pod
```

The Deployment initially showed:

```text
READY: 1/1
UP-TO-DATE: 1
AVAILABLE: 1
```

So initially we had:

```text
Deployment
    ↓
1 Pod
```

---

# 5. Initial Configuration

Our `values.yaml` initially contained:

```yaml
replicaCount: 1
```

This value was used by the Deployment template.

Therefore:

```text
values.yaml
    │
    │ replicaCount: 1
    ▼
Deployment
    │
    ▼
1 Pod
```

---

# 6. `helm upgrade`

## Purpose

`helm upgrade` updates an existing Helm release using a new configuration/chart.

General syntax:

```bash
helm upgrade <release-name> <chart-path>
```

Our command:

```bash
helm upgrade teja-app ./teja-nginx
```

### Important

We don't need to:

```text
uninstall
    ↓
install again
```

just because configuration changes.

Instead:

```text
Existing Release
      ↓
helm upgrade
      ↓
Updated Release
```

---

# 7. Hands-On: Changing 1 Replica to 5 Replicas

Initially:

```yaml
replicaCount: 1
```

We changed it to:

```yaml
replicaCount: 5
```

Then we ran:

```bash
helm upgrade teja-app ./teja-nginx
```

Helm upgraded the existing release.

---

# 8. Verify the Upgrade

We checked the Kubernetes Pods:

```bash
kubectl get pods
```

The result showed **5 running Pods**.

Before the upgrade:

```text
Deployment
    ↓
1 Pod
```

After the upgrade:

```text
Deployment
    ↓
5 Pods
```

This confirmed that the new configuration was successfully applied.

---

# 9. Revision After Upgrade

After the upgrade, we ran:

```bash
helm list
```

The output showed:

```text
NAME            NAMESPACE       REVISION        STATUS
teja-app        default         2               deployed
```

The important change was:

```text
Revision 1
     ↓
Revision 2
```

The release name remained:

```text
teja-app
```

We did **not** create a new release.

We updated the existing release and Helm created a new revision.

---

# 10. `helm history`

## Purpose

`helm history` displays the revision history of a Helm release.

### Command

```bash
helm history teja-app
```

After the upgrade, we saw:

```text
REVISION        STATUS
1               superseded
2               deployed
```

Detailed output:

```text
REVISION        UPDATED                         STATUS          CHART                   APP VERSION     DESCRIPTION
1               Thu Sep 24 10:27:45 2026        superseded      teja-nginx-0.1.0        1.16.0          Install complete
2               Tue Sep 29 09:58:10 2026        deployed        teja-nginx-0.1.0        1.16.0          Upgrade complete
```

---

# 11. What Does `superseded` Mean?

When Revision 2 became the current revision:

```text
Revision 1 → superseded
Revision 2 → deployed
```

### `superseded`

It means:

> This revision is no longer the current active revision because a newer revision replaced it.

It does **not** mean the revision was deleted.

Helm still keeps the revision in the release history.

This is important because Helm can use previous revisions for rollback.

---

# 12. `helm rollback`

## Purpose

`helm rollback` restores the configuration represented by an earlier revision.

General syntax:

```bash
helm rollback <release-name> <revision-number>
```

For our release:

```bash
helm rollback teja-app 1
```

This means:

> Restore the configuration represented by Revision 1.

---

# 13. Important Rollback Concept

Before rollback:

```text
Revision 1 → superseded
Revision 2 → deployed
```

We ran:

```bash
helm rollback teja-app 1
```

Helm did **not** make Revision 1 the new current revision.

Instead, Helm created a new revision.

After rollback:

```text
Revision 1 → superseded
Revision 2 → superseded
Revision 3 → deployed
```

Revision 3 contains the configuration restored from Revision 1.

### This is very important:

```text
Rollback to Revision 1
           ↓
Creates Revision 3
           ↓
Revision 3 contains Revision 1 configuration
```

---

# 14. Verify the Rollback

After the rollback, we ran:

```bash
kubectl get pods
```

Only **1 Pod** was running.

That means the configuration returned to:

```yaml
replicaCount: 1
```

Our lifecycle was:

```text
Revision 1
1 replica
     │
     │ helm upgrade
     ▼
Revision 2
5 replicas
     │
     │ helm rollback teja-app 1
     ▼
Revision 3
1 replica
```

---

# 15. Final `helm history`

We ran:

```bash
helm history teja-app
```

The result was:

```text
REVISION        UPDATED                         STATUS          CHART                   APP VERSION     DESCRIPTION
1               Thu Sep 24 10:27:45 2026        superseded      teja-nginx-0.1.0        1.16.0          Install complete
2               Tue Sep 29 09:58:10 2026        superseded      teja-nginx-0.1.0        1.16.0          Upgrade complete
3               Tue Sep 29 10:02:14 2026        deployed        teja-nginx-0.1.0        1.16.0          Rollback to 1
```

So:

```text
Revision 1 → Initial installation
Revision 2 → Upgrade
Revision 3 → Rollback
```

Current revision:

```text
3
```

Current status:

```text
deployed
```

---

# 16. `helm uninstall`

## Purpose

`helm uninstall` removes a Helm release and the Kubernetes resources managed by that release.

### Command

```bash
helm uninstall teja-app
```

This removes the installed release.

---

# 17. Verify the Uninstall

After uninstalling, we checked:

```bash
helm list
```

The `teja-app` release was no longer listed.

We also checked:

```bash
kubectl get pods
```

There were no Pods remaining for the release.

Therefore:

```text
Helm Release
    ↓
teja-app
    ↓
Removed
```

### Important

The local Helm chart was **not deleted**.

Our chart directory:

```text
teja-nginx/
```

still exists.

So:

```text
helm uninstall teja-app
```

removes the installed release/resources, not the local chart files.

---

# 18. Complete Phase 2 Lifecycle

Our complete hands-on flow:

```text
                    Chart
                 teja-nginx
                     │
                     │ helm install
                     ▼
                teja-app
               Revision 1
               1 replica
                     │
                     │ helm upgrade
                     ▼
                Revision 2
               5 replicas
                     │
                     │ helm history
                     │
                     │ helm rollback teja-app 1
                     ▼
                Revision 3
               1 replica
                     │
                     │ helm uninstall
                     ▼
              Release Removed
```

---

# 19. Helm Phase 2 Command Reference

| Command | Purpose |
|---|---|
| `helm list` | List Helm releases |
| `helm status teja-app` | Show detailed release status |
| `helm upgrade teja-app ./teja-nginx` | Upgrade an existing release |
| `helm history teja-app` | Show release revision history |
| `helm rollback teja-app 1` | Restore Revision 1 configuration |
| `helm uninstall teja-app` | Remove the Helm release |

---

# 20. When to Use Each Command

## `helm list`

Use when you want to know:

- What Helm releases are installed?
- What is the current revision?
- What is the release status?
- Which chart is being used?

```bash
helm list
```

---

## `helm status`

Use when you want detailed information about one specific release.

```bash
helm status teja-app
```

It shows:

- Release name
- Namespace
- Status
- Revision
- Resources
- Notes

---

## `helm upgrade`

Use when you want to apply configuration/chart changes to an existing release.

Example:

```yaml
replicaCount: 1
```

Change to:

```yaml
replicaCount: 5
```

Then:

```bash
helm upgrade teja-app ./teja-nginx
```

---

## `helm history`

Use when you want to see previous revisions of a release.

```bash
helm history teja-app
```

---

## `helm rollback`

Use when you need to restore a previous configuration.

```bash
helm rollback teja-app 1
```

---

## `helm uninstall`

Use when the release is no longer needed.

```bash
helm uninstall teja-app
```

---

# 21. Chart Version vs Application Version vs Revision

These are three different concepts.

## Chart Version

From `Chart.yaml`:

```yaml
version: 0.1.0
```

This identifies the version of the Helm Chart.

## Application Version

From `Chart.yaml`:

```yaml
appVersion: "1.16.0"
```

This represents the application version.

## Release Revision

Managed by Helm:

```text
Revision 1
Revision 2
Revision 3
```

This tracks changes to a particular installed release.

### Summary

```text
Chart Version
      ↓
    0.1.0

Application Version
      ↓
    1.16.0

Release Revision
      ↓
  1 → 2 → 3
```

---

# 22. Common Mistakes

## Mistake 1: Confusing Chart and Release

Incorrect:

```text
teja-nginx = Release
```

Correct:

```text
teja-nginx = Chart
teja-app = Release
```

---

## Mistake 2: Thinking Upgrade Means Reinstall

You do not need to uninstall first.

Use:

```bash
helm upgrade teja-app ./teja-nginx
```

---

## Mistake 3: Thinking Rollback Reuses an Old Revision

Suppose:

```text
Revision 1
Revision 2
```

Then:

```bash
helm rollback teja-app 1
```

The result is:

```text
Revision 1 → superseded
Revision 2 → superseded
Revision 3 → deployed
```

Rollback creates a new revision.

---

## Mistake 4: Thinking `superseded` Means Deleted

It does not.

It means that the revision is no longer the current active revision.

The revision remains in Helm history.

---

## Mistake 5: Thinking Uninstall Deletes the Chart

This:

```bash
helm uninstall teja-app
```

does not delete:

```text
teja-nginx/
```

The local chart remains available.

---

# 23. Practical Helm Release Management Workflow

```bash
# List releases
helm list

# Inspect a release
helm status teja-app

# Modify values.yaml
# Example:
# replicaCount: 1 → 5

# Upgrade the release
helm upgrade teja-app ./teja-nginx

# Verify Kubernetes resources
kubectl get pods

# Check current revision
helm list

# View release history
helm history teja-app

# Roll back if required
helm rollback teja-app 1

# Verify rollback
kubectl get pods

# Remove the release when finished
helm uninstall teja-app
```

---

# 24. Interview Questions

## Basic Questions

### 1. What is a Helm Release?

A Helm Release is an installed instance of a Helm Chart.

---

### 2. What does `helm list` do?

It lists Helm releases installed in the current namespace/context.

---

### 3. What does `helm status` do?

It displays detailed information about a specific Helm release.

---

### 4. What does `helm upgrade` do?

It updates an existing Helm release using the specified chart and configuration.

---

### 5. What does `helm history` do?

It displays the revision history of a Helm release.

---

### 6. What does `superseded` mean?

It means the revision is no longer the current active revision because a newer revision replaced it.

---

### 7. What does `helm rollback` do?

It restores the configuration represented by an earlier revision.

---

### 8. Does rollback reuse the old revision number?

No.

Rollback creates a new revision.

Example:

```text
1 → Install
2 → Upgrade
3 → Rollback to 1
```

---

### 9. What does `helm uninstall` do?

It removes a Helm release and the Kubernetes resources managed by that release.

---

### 10. Does `helm uninstall` delete the local chart?

No.

The local Helm chart directory remains.

---

# 25. Scenario-Based Questions

## Scenario 1

You currently have:

```text
Revision 2
replicaCount: 5
```

You want to restore Revision 1.

### Command

```bash
helm rollback teja-app 1
```

---

## Scenario 2

You changed:

```yaml
replicaCount: 1
```

to:

```yaml
replicaCount: 5
```

You want to apply this change to the existing release.

### Command

```bash
helm upgrade teja-app ./teja-nginx
```

---

## Scenario 3

You want to see all revisions of a release.

### Command

```bash
helm history teja-app
```

---

## Scenario 4

You want to remove the installed release.

### Command

```bash
helm uninstall teja-app
```

---

# 26. Key Takeaways

1. **Chart = package/blueprint.**
2. **Release = installed instance of a Chart.**
3. `helm list` lists releases.
4. `helm status` shows detailed release information.
5. `helm upgrade` updates an existing release.
6. An upgrade creates a new revision.
7. `helm history` shows revision history.
8. `superseded` means an older revision is no longer current.
9. `helm rollback` restores an older configuration.
10. Rollback creates a **new revision**.
11. `helm uninstall` removes the release and its managed Kubernetes resources.
12. Uninstalling a release does not delete the local chart directory.

---

# 27. Phase 2 Completion Checklist

- [x] Understand Helm Release
- [x] Understand Release Revision
- [x] Use `helm list`
- [x] Use `helm status`
- [x] Perform a Helm upgrade
- [x] Change replicas from 1 → 5
- [x] Verify five Pods
- [x] Use `helm history`
- [x] Understand `superseded`
- [x] Perform a rollback
- [x] Verify rollback restored one replica
- [x] Understand that rollback creates a new revision
- [x] Perform `helm uninstall`
- [x] Verify the release is removed
- [x] Verify the Pods are removed

## 🏁 Status

**HELM PHASE 2 — COMPLETED ✅**

---

# 28. Next Phase

Phase 2 focused mainly on **Release Management**.

The next phase can focus on making Helm Charts more flexible and reusable, including topics such as:

- `--set`
- Multiple values files
- Advanced `values.yaml` usage
- Template customization
- Environment-specific configuration
- Reusable Helm configurations
- Advanced Helm templating
