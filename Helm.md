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

# Helm Phase 3 — Chart Customization and Configuration

**Project:** `teja-nginx`  
**Goal:** Customize a Helm chart using values and override files instead of editing templates for every configuration change.

## 1. Quick recap

In Phase 3, we covered:

- `values.yaml` — the chart's default configuration.
- `--set` — override a value directly from a Helm command.
- `-f` / `--values` — load overrides from a YAML file.
- Precedence — `--set` overrides conflicting values from `-f`; when multiple `-f` files define the same key, the last file wins.
- Data types — strings, numbers, and booleans must be represented correctly.
- Nested values — access fields such as `.Values.image.repository` using dot notation.
- Environment-specific configuration — use different values files for development and production.

Our chart structure:

```text
teja-nginx/
├── Chart.yaml
├── values.yaml
├── templates/
├── charts/
└── .helmignore
```

A **chart** is the package of templates and configuration. A **release** is an installed instance of that chart, such as `teja-app` or `teja-prod`.

## 2. How Helm values work

A template can contain a placeholder:

```yaml
spec:
  replicas: {{ .Values.replicaCount }}
```

If `values.yaml` contains:

```yaml
replicaCount: 1
```

Helm renders the template with `replicas: 1`. Values let us configure a chart without changing its templates.

Conceptually:

```text
Templates + default values + override values
                    |
                    v
             Helm renders YAML
                    |
                    v
        Install or upgrade a release
```

**Important:** `helm template` renders manifests locally; it does not deploy them to Kubernetes.

## 3. Topic 1 — `--set` overrides

Use `--set` to override a value directly in a command:

```bash
helm upgrade --install teja-app ./teja-nginx --set replicaCount=3
```

Override a nested value:

```bash
helm template teja-app ./teja-nginx --set image.tag="1.28"
```

This does not edit the local `values.yaml` file. `--set` is convenient for quick overrides; values files are easier to review and reuse for larger configurations.

## 4. Topic 2 — Values files with `-f`

Example `custom-values.yaml`:

```yaml
replicaCount: 2

image:
  repository: nginx
  tag: "1.27"
```

Use the file:

```bash
helm upgrade --install teja-app ./teja-nginx \
  -f ./teja-nginx/custom-values.yaml
```

Preview the rendered manifests first:

```bash
helm template teja-app ./teja-nginx \
  -f ./teja-nginx/custom-values.yaml
```

The path in these commands assumes the current directory is the parent directory containing `teja-nginx`. Adjust the path if you run the command elsewhere.

Values supplied in an override file replace conflicting chart defaults. Keys not specified in the override generally retain their default values.

## 5. Topic 3 — Values precedence

For the overrides practiced in this phase, remember this simplified order:

1. Chart defaults from `values.yaml`
2. Values from `-f` files
3. Values from `--set`

Example:

`values.yaml`:

```yaml
replicaCount: 1
```

`values-prod.yaml`:

```yaml
replicaCount: 3
```

Command:

```bash
helm template teja-prod ./teja-nginx \
  -f ./teja-nginx/values-prod.yaml \
  --set replicaCount=5
```

The selected replica count is **5**, because `--set` overrides the conflicting value from the file.

**Upgrade nuance:** Helm upgrades can also use flags such as `--reuse-values` and `--reset-values`, which affect how previous release values are handled. Check those flags when you need precise control over an existing release's values.

## 6. Topic 4 — Data types

YAML values have types. Use the type expected by the chart.

```yaml
replicaCount: 3       # Number
image:
  tag: "1.28"         # String
autoscaling:
  enabled: false      # Boolean
```

- `replicaCount: 3` is numeric.
- `tag: "1.28"` is a string, appropriate for an image tag.
- `enabled: false` is a boolean.
- `enabled: "false"` is a string, not a boolean.

A type mismatch can cause unexpected rendering or template errors. Follow the structure and types in the chart's existing values and templates.

## 7. Topic 5 — Nested values and dot notation

Example values:

```yaml
image:
  repository: nginx
  tag: "1.27"
  pullPolicy: IfNotPresent

service:
  port: 80
  type: ClusterIP
```

Corresponding template expressions:

| Values key | Helm template expression |
|---|---|
| `image.repository` | `.Values.image.repository` |
| `image.tag` | `.Values.image.tag` |
| `service.port` | `.Values.service.port` |
| `service.type` | `.Values.service.type` |

Example template:

```yaml
image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
```

With `repository: nginx` and `tag: "1.27"`, this renders as `nginx:1.27`.

Override a nested field:

```bash
helm template teja-app ./teja-nginx --set service.port=8080
```

Dot notation follows the hierarchy: `.Values` → `image` → `repository`.

## 8. Topic 6 — Environment-specific values files

The same chart can be configured differently for development and production.

Example directory:

```text
teja-nginx/
├── Chart.yaml
├── values.yaml
├── values-dev.yaml
├── values-prod.yaml
└── templates/
```

Default `values.yaml`:

```yaml
replicaCount: 1

image:
  repository: nginx
  tag: "1.27"
```

Development `values-dev.yaml`:

```yaml
replicaCount: 1

image:
  repository: nginx
  tag: "1.27"
```

Production `values-prod.yaml`:

```yaml
replicaCount: 3

image:
  repository: nginx
  tag: "1.27"
```

Deploy or upgrade the development release:

```bash
helm upgrade --install teja-app ./teja-nginx \
  -f ./teja-nginx/values-dev.yaml
```

Deploy or upgrade the production release:

```bash
helm upgrade --install teja-prod ./teja-nginx \
  -f ./teja-nginx/values-prod.yaml
```

Here, development uses one replica and production uses three. The templates remain reusable. The different release names identify separate Helm releases; running both in the same namespace depends on the resources and names generated by the chart.

**Security reminder:** Do not commit passwords, tokens, or other secrets in plain-text values files, especially in public repositories. Use an appropriate secrets-management approach for sensitive settings.

## 9. Topic 7 — Multiple values files

If multiple `-f` files define the same key, the **last file wins**.

`values-dev.yaml`:

```yaml
replicaCount: 1

image:
  tag: "1.27"
```

`values-prod.yaml`:

```yaml
replicaCount: 3

image:
  tag: "1.28"
```

Command:

```bash
helm upgrade --install teja-prod ./teja-nginx \
  -f ./teja-nginx/values-dev.yaml \
  -f ./teja-nginx/values-prod.yaml
```

For the keys shown, the final configuration is:

```yaml
replicaCount: 3

image:
  tag: "1.28"
```

Helm reads the development file first, then the production file. Production overrides duplicate keys because it is listed last.

A later file only overrides keys it defines. Non-conflicting keys from earlier files can remain in the merged values.

## 10. Useful commands

Run from the parent directory containing `teja-nginx`, adjusting paths if necessary.

Render defaults:

```bash
helm template teja-app ./teja-nginx
```

Render with a values file:

```bash
helm template teja-app ./teja-nginx \
  -f ./teja-nginx/values-dev.yaml
```

Render with a direct override:

```bash
helm template teja-app ./teja-nginx --set replicaCount=3
```

Render with multiple files:

```bash
helm template teja-prod ./teja-nginx \
  -f ./teja-nginx/values-dev.yaml \
  -f ./teja-nginx/values-prod.yaml
```

Install or upgrade using production values:

```bash
helm upgrade --install teja-prod ./teja-nginx \
  -f ./teja-nginx/values-prod.yaml
```

Inspect releases:

```bash
helm list
helm status teja-prod
```

`helm template` previews rendered YAML. `helm upgrade --install` installs a release if it does not exist, or upgrades it if it already exists.

## 11. Common mistakes

1. **Expecting `helm template` to deploy resources:** It only renders YAML locally.
2. **Using the wrong file path:** `-f` must point to the actual file relative to your current directory, or use an absolute path.
3. **Reversing file order:** The last values file wins for duplicate keys.
4. **Mixing types:** `false` is a boolean, while `"false"` is a string.
5. **Editing templates for every environment:** Prefer values overrides for settings the chart already exposes.
6. **Assuming the last file replaces everything:** It overrides overlapping keys; other keys may remain from earlier files.

## 12. Quick revision quiz

Try answering before reading the answer key.

1. What is the purpose of `values.yaml`?
2. What does `-f` do?
3. If the default replica count is `1` and a production file sets it to `3`, what value is used when that file is supplied?
4. Which wins for a conflicting key in our examples: `-f` or `--set`?
5. If two values files define the same key, which wins?
6. What does `.Values.image.repository` refer to?
7. What is the difference between `enabled: false` and `enabled: "false"`?
8. Does `helm template` deploy resources?
9. Why maintain separate development and production values files?
10. Development sets one replica and image tag `"1.27"`; production sets three replicas and tag `"1.28"`. If development is loaded first and production second, what are the final values?

### Answer key

1. It stores chart defaults.
2. It loads overrides from a YAML file.
3. `3`.
4. `--set`.
5. The last values file.
6. The `repository` field nested under `image` in the chart values.
7. The first is a boolean; the second is a string.
8. No; it renders manifests locally.
9. To reuse the same chart with different environment configuration.
10. `replicaCount: 3` and `image.tag: "1.28"`.

## 13. Phase 3 summary

- **`values.yaml`** — chart defaults.
- **`--set`** — command-line override.
- **`-f`** — load a YAML values file.
- **Precedence** — `--set` overrides conflicting file values in the examples; the last `-f` file wins for duplicate keys.
- **Data types** — use the correct string, number, or boolean type.
- **Nested values** — use expressions such as `.Values.image.tag`.
- **Environment-specific configuration** — keep development and production settings in separate files.
- **Preview** — use `helm template` to inspect rendered Kubernetes YAML before deployment.

### Next phase

**Phase 4 — Advanced Helm Templates**, beginning with conditional templates using `if` and `else`.

---

*These notes are based on the Helm Phase 3 topics covered in our learning session, with practical examples for the `teja-nginx` chart.*


# Helm Phase 4: Advanced Helm Templates
## Topic 1: Conditional Templates and Topic 2: Loops

These notes cover conditional logic and loops in Helm templates, with examples and hands-on exercises.

---

# Topic 1: Conditional Templates

## 1. What Are Conditional Templates?

Conditional templates allow Helm to generate different Kubernetes YAML depending on values supplied in `values.yaml`.

In simple words, a condition tells Helm:

- If a condition is true, generate some YAML.
- Otherwise, generate alternative YAML or skip that section.

Helm templates use Go template syntax.

The main keywords are:

- `if`
- `else`
- `end`

## 2. Basic Syntax

```yaml
{{ if CONDITION }}
# YAML generated when the condition is true
{{ else }}
# YAML generated when the condition is false
{{ end }}
```

Important:

- `if` starts the condition.
- `else` is optional.
- `end` closes the conditional block.

## 3. Example: Using a Boolean Value

### Step 1: Add a value to `values.yaml`

```yaml
featureEnabled: true
```

Here, `featureEnabled` is a Boolean value.

It can be either `true` or `false`.

### Step 2: Create a template

Create a file named `templates/feature-configmap.yaml`:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-feature-config
data:
  featureStatus: {{ if .Values.featureEnabled }}"enabled"{{ else }}"disabled"{{ end }}
```

### Step 3: Understand the template

- `.Values.featureEnabled` reads the value from `values.yaml`.
- If the value is `true`, Helm generates `"enabled"`.
- If the value is `false`, Helm generates `"disabled"`.

### Step 4: Render the template

Run this command from the chart directory:

```bash
helm template teja-app .
```

With `featureEnabled: true`, the generated ConfigMap contains:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: teja-app-feature-config
data:
  featureStatus: "enabled"
```

If you change the value to:

```yaml
featureEnabled: false
```

The generated ConfigMap contains:

```yaml
data:
  featureStatus: "disabled"
```

The exact rendered output also includes other resources from the chart.

## 4. Using `if` Without `else`

You can use `if` without `else` when you want to generate a section only when a condition is true.

Example:

```yaml
{{ if .Values.featureEnabled }}
apiVersion: v1
kind: ConfigMap
metadata:
  name: feature-config
data:
  message: "Feature is enabled"
{{ end }}
```

If `featureEnabled` is `true`, Helm generates the ConfigMap.

If it is `false`, Helm skips this entire block.

## 5. Using `if`, `else`, and `end`

Consider this example:

```yaml
{{ if .Values.featureEnabled }}
message: "Feature enabled"
{{ else }}
message: "Feature disabled"
{{ end }}
```

| Value | Result |
|---|---|
| `true` | `message: "Feature enabled"` |
| `false` | `message: "Feature disabled"` |

Only one branch is generated.

## 6. Conditional Templates With Different Values

You can override a value without modifying `values.yaml`.

For example:

```bash
helm template teja-app . --set featureEnabled=false
```

This renders the chart with the feature disabled.

The `--set` value overrides the corresponding value from `values.yaml` for this command.

To render with the feature enabled:

```bash
helm template teja-app . --set featureEnabled=true
```

## 7. Whitespace Control

Helm templates support whitespace-control characters:

- `{{-` trims whitespace to the left of a template action.
- `-}}` trims whitespace to the right of a template action.

Example:

```yaml
{{- if .Values.featureEnabled }}
featureStatus: enabled
{{- end }}
```

Be careful: trimming whitespace can accidentally join YAML lines or remove required newlines.

Always inspect the generated YAML after changing whitespace controls.

## 8. Important Notes

- `.Values` accesses configuration supplied through Helm values.
- `.Values.featureEnabled` reads the `featureEnabled` value.
- `if` evaluates a condition.
- `else` provides an alternative branch.
- `end` closes the block.
- `helm template` renders templates locally without installing the chart.

## 9. Common Mistakes

### Mistake 1: Forgetting `end`

Incorrect:

```yaml
{{ if .Values.featureEnabled }}
message: enabled
```

Correct:

```yaml
{{ if .Values.featureEnabled }}
message: enabled
{{ end }}
```

### Mistake 2: Using a string instead of a Boolean

Boolean:

```yaml
featureEnabled: true
```

String:

```yaml
featureEnabled: "true"
```

These are different data types. Use the Boolean form when the condition is intended to represent true or false.

### Mistake 3: Assuming `helm template` installs resources

`helm template` only renders the YAML. It does not install or update a release.

---

# Topic 2: Loops With `range`

## 1. What Is `range`?

The `range` keyword allows Helm to iterate over collections of values.

A collection might be:

- A list of items.
- A map containing keys and values.

In simple words, `range` repeats a template section for each item in a collection.

For example, instead of manually writing three entries, you can define a list in `values.yaml` and let Helm generate the entries automatically.

## 2. Basic Syntax

```yaml
{{ range COLLECTION }}
# Template content repeated for each item
{{ end }}
```

Important:

- `range` starts the loop.
- `COLLECTION` identifies the list or map.
- `.` represents the current item in a simple list loop.
- `end` closes the loop.

## 3. Example: Looping Through a List

### Step 1: Define a list in `values.yaml`

```yaml
tools:
  - Docker
  - Helm
  - Kubernetes
```

This list contains three items.

### Step 2: Create a template

Create `templates/tools-configmap.yaml`:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-tools
data:
  tools: |-
    {{- range .Values.tools }}
    - {{ . | quote }}
    {{- end }}
```

### Step 3: Understand the template

- `.Values.tools` selects the list.
- `range` visits each item.
- `.` represents the current item.
- `quote` wraps the item in double quotes.
- `end` closes the loop.

### Step 4: Render the chart

```bash
helm template teja-app .
```

The generated ConfigMap's `data.tools` value should contain:

```yaml
tools: |-
  - "Docker"
  - "Helm"
  - "Kubernetes"
```

The `tools` field is a string containing multiple lines because it uses YAML's block scalar syntax (`|-`).

The exact rendered output also includes other chart resources.

## 4. How Does the Loop Work?

For this list:

```yaml
tools:
  - Docker
  - Helm
  - Kubernetes
```

Helm processes the items as follows:

| Iteration | Current value (`.`) |
|---|---|
| 1 | Docker |
| 2 | Helm |
| 3 | Kubernetes |

The loop executes three times because the list contains three items.

If the list contains five items, the loop executes five times.

If the list is empty, the loop has no items to process.

## 5. Understanding `.` Inside a Loop

The dot (`.`) represents the current template context.

Inside a simple list loop, it represents the current list item.

Example:

```yaml
{{ range .Values.tools }}
- {{ . }}
{{ end }}
```

When the current item is `Docker`, `.` means `Docker`.

When the current item is `Helm`, `.` means `Helm`.

This behavior is important because the meaning of `.` can change inside nested template blocks.

## 6. Looping Through a Map

A map stores key-value pairs.

### Step 1: Define a map in `values.yaml`

```yaml
cloudVersions:
  AWS: "1"
  Azure: "2"
  GCP: "3"
```

Each cloud provider is a key, and its version is the associated value.

### Step 2: Use `range` with a key and value

```yaml
{{- range $key, $value := .Values.cloudVersions }}
{{ $key }}: {{ $value | quote }}
{{- end }}
```

Here:

- `$key` stores the current key.
- `$value` stores the value associated with that key.
- `:=` declares the variables.
- `end` closes the loop.

The rendered entries will represent:

```yaml
AWS: "1"
Azure: "2"
GCP: "3"
```

The order of map iteration should not be relied upon unless you explicitly sort the keys.

## 7. Understanding Root Context `$`

Inside a loop, `.` changes to the current item or current context.

Sometimes you still need to access a value from the chart's root context.

The dollar sign (`$`) provides access to the root context established for the template execution.

Example `values.yaml`:

```yaml
appName: nginx

tools:
  - Docker
  - Helm
  - Kubernetes
```

Template:

```yaml
{{- range .Values.tools }}
tool: {{ . | quote }}
app: {{ $.Values.appName | quote }}
{{- end }}
```

Explanation:

- `.` represents the current tool.
- `$.Values.appName` accesses the root-level `appName` value.

Conceptually, the output contains three pairs:

```yaml
tool: "Docker"
app: "nginx"
tool: "Helm"
app: "nginx"
tool: "Kubernetes"
app: "nginx"
```

This snippet illustrates the values generated by the loop. To use it as a real Kubernetes resource, place the generated fields inside an appropriate resource structure.

## 8. Nested Values Inside a Loop

Suppose `values.yaml` contains:

```yaml
appName: nginx

environments:
  - name: development
    replicas: 1
  - name: staging
    replicas: 2
  - name: production
    replicas: 3
```

A template can access the fields of each current item:

```yaml
{{- range .Values.environments }}
environment: {{ .name | quote }}
replicas: {{ .replicas }}
{{- end }}
```

Within each iteration:

- `.name` accesses the current item's name.
- `.replicas` accesses the current item's replica count.

The dot represents the current environment object during each iteration.

## 9. Combining `range` With `if`

Loops and conditions can be combined.

Example:

```yaml
{{- range .Values.tools }}
{{- if eq . "Helm" }}
selectedTool: {{ . | quote }}
{{- end }}
{{- end }}
```

This loops through the tools and generates the `selectedTool` entry only when the current item equals `Helm`.

The `eq` function compares values for equality.

This example demonstrates template logic; place generated fields inside a valid Kubernetes resource before using it as a deployable manifest.

## 10. Testing With `helm template`

Use this command from your chart directory:

```bash
helm template teja-app .
```

To save the rendered output to a file:

```bash
helm template teja-app . > rendered.yaml
```

To inspect a specific template's output, you can also use:

```bash
helm template teja-app . --show-only templates/tools-configmap.yaml
```

The path passed to `--show-only` must match the template's path inside the chart.

These commands render the chart locally. They do not install the release.

## 11. Common Mistakes

### Mistake 1: Forgetting `end`

Incorrect:

```yaml
{{ range .Values.tools }}
- {{ . }}
```

Correct:

```yaml
{{ range .Values.tools }}
- {{ . }}
{{ end }}
```

### Mistake 2: Confusing `.` and `$`

Inside a list loop:

- `.` means the current item.
- `$.Values.appName` accesses the root-level `appName`.

### Mistake 3: Incorrect YAML indentation

YAML indentation matters. Incorrect indentation can make the generated YAML invalid.

Always inspect the output from `helm template`.

### Mistake 4: Treating a map like a simple list

A list loop typically uses:

```yaml
{{ range .Values.tools }}
```

A map loop can use:

```yaml
{{ range $key, $value := .Values.cloudVersions }}
```

Use the syntax that matches the data structure.

### Mistake 5: Forgetting that `range` changes the current context

Within a loop, `.` may no longer represent the original root context.

Use `$` when you need to access root-level values.

---

# Practical Exercises

## Exercise 1: Conditional Templates

Add the following to `values.yaml`:

```yaml
featureEnabled: true
```

Create a ConfigMap template that outputs `"enabled"` when the value is true and `"disabled"` when it is false.

Render it with:

```bash
helm template teja-app .
```

Then override the value:

```bash
helm template teja-app . --set featureEnabled=false
```

Verify that the rendered status changes.

## Exercise 2: List Loop

Add the following to `values.yaml`:

```yaml
tools:
  - Docker
  - Helm
  - Kubernetes
```

Create a ConfigMap template that uses `range` to place these tools into a multiline string.

Render the chart and verify that all three tools appear.

## Exercise 3: Map Loop

Add the following to `values.yaml`:

```yaml
cloudVersions:
  AWS: "1"
  Azure: "2"
  GCP: "3"
```

Use `$key` and `$value` to generate an entry for each provider and its version.

Render the chart and verify that all three key-value pairs appear.

## Exercise 4: Root Context

Use this configuration:

```yaml
appName: nginx

tools:
  - Docker
  - Helm
  - Kubernetes
```

Write a loop that outputs the current tool and the root-level application name.

Verify that the tool changes on each iteration while the application name stays the same.

---

# Quick Revision

| Concept | Purpose |
|---|---|
| `if` | Generates content when a condition is true |
| `else` | Provides an alternative branch |
| `end` | Closes a conditional or loop block |
| `range` | Iterates through a list or map |
| `.` | Represents the current template context |
| `$` | Refers to the root context |
| `$key` | Stores the current map key |
| `$value` | Stores the current map value |
| `quote` | Converts a value into a quoted string representation |
| `helm template` | Renders chart templates locally |
| `--set` | Overrides chart values from the command line |

---

# Phase 4 Progress

- [x] Topic 1: Conditional Templates (`if`, `else`, `end`) — concepts covered
- [x] Topic 2: Loops (`range`) — concepts covered
- [ ] Topic 3: Named Templates and Helpers (`define`, `include`, `_helpers.tpl`)
- [ ] Topic 4: Template Functions (`quote`, `default`, `required`, etc.)

**Next topic:** Named Templates and Helpers.

These notes cover the core concepts. Before considering the first two topics fully verified, complete the practical exercises and inspect the rendered YAML for valid structure and indentation.
