# DevOps Day 1 Notes

## 1. Why DevOps?
Traditional software development had separate Development and Operations teams which caused:
- Slow releases
- Communication gaps
- Deployment failures
- Blame culture

**DevOps solves this by combining development and operations for faster and reliable delivery.**

---

## 2. What is DevOps?
**DevOps = Development + Operations**

It is a culture, practice, and set of tools that helps teams:
- Build faster
- Deploy frequently
- Fix bugs quickly
- Collaborate efficiently

**Definition:**  
DevOps is a methodology that improves software delivery speed and quality by automating and integrating development and IT operations.

---

## 3. DevOps Lifecycle
Plan → Code → Build → Test → Release → Deploy → Operate → Monitor → Repeat

---

## 4. What is Version Control?
Version Control is a system that tracks changes in files over time so developers can:
- Track history
- Restore old versions
- Collaborate safely
- Avoid overwriting code

**Simple Definition:**  
Version control is a tool that manages changes to source code.

---

## 5. Types of Version Control Systems

### Local Version Control
- Stores versions on local system
- No collaboration support

---

### Centralized Version Control (CVCS)
- One central server stores code
- Developers connect to server

**Advantages**
- Easy to manage
- Central control

**Disadvantages**
- Server failure risk
- Requires internet
- Slower

---

### Distributed Version Control (DVCS)
- Each developer has full repository copy
- Works offline
- Faster and safer

**Advantages**
- No single point of failure
- Fast operations
- Built-in backup
- Better branching

**Disadvantages**
- Slightly harder to learn
- Initial clone can be large

---

## 6. CVCS vs DVCS Differences

| Feature | CVCS | DVCS |
|--------|------|------|
| Repo Copy | Only server | Everyone has copy |
| Internet | Required | Not required |
| Speed | Slower | Faster |
| Backup | Server only | Every system |
| Failure Risk | High | Very Low |

---

## 7. Important Version Control Concepts

**Repository** — Storage for project files and history  
**Commit** — Saved snapshot of code  
**Branch** — Separate development line  
**Merge** — Combine branches  
**Clone** — Download repository  
**Push** — Upload changes  
**Pull** — Download latest changes  
**Conflict** — When two edits clash

---

## 8. Why Version Control is Important in DevOps
Version control enables:
- CI/CD pipelines
- Automation
- Collaboration
- Rollbacks
- Bug tracking

Without version control, modern DevOps practices are impossible.

---

## Interview One-Line Definitions

**DevOps:**  
A collaborative approach that integrates development and operations to deliver software faster and reliably.

**Version Control:**  
A system that tracks file changes and allows collaboration and recovery of previous versions.

---

✅ *End of Day-1 DevOps Notes*


# DevOps Day 2 Notes
# Git Lifecycle, Branches & Most Used Git Commands

---

# 1️⃣ Git Lifecycle

Git lifecycle explains the stages a file goes through in Git.

Git is a Distributed Version Control System used in DevOps to track and manage code changes.

---

## 🔁 Git File States

A file moves through three main stages:

Working Directory → Staging Area → Repository

---

## 🟢 1. Working Directory

- This is where you create or modify files.
- Git sees the file but is not tracking changes yet.

Example:
You edit `app.py`.

---

## 🟢 2. Staging Area (Index)

- Files are prepared before saving permanently.
- You choose which changes to include in the next commit.

Command used:
git add filename

Purpose:
Moves changes from Working Directory to Staging Area.

---

## 🟢 3. Repository (Commit Stage)

- Changes are saved permanently as a snapshot.
- Each save is called a commit.

Command used:
git commit -m "message"

Purpose:
Stores changes safely with a meaningful message.

---

## 🔁 Complete Lifecycle Flow

Edit → Add → Commit → Push

Edit  → Modify file  
Add   → Prepare changes  
Commit → Save version  
Push  → Upload to remote repository  

---

# 2️⃣ What are Branches in Git?

A branch in Git is a separate line of development.

It allows developers to work on features or fixes without affecting the main (production) code.

---

## 🌿 Why Branches are Important in DevOps

- Keeps production code stable
- Allows parallel development
- Supports CI/CD workflows
- Enables team collaboration
- Reduces risk of breaking main branch

---

## 🧠 How Branches Work

When you create a branch:
- Git does NOT copy the entire project.
- It creates a new pointer to the current commit.
- You can modify files safely.
- Main branch remains unchanged.

---

## 🔁 Branch Workflow Example

1. main → Stable production code
2. Create feature branch
3. Make changes
4. Test locally
5. Merge into main
6. Push to remote
7. CI/CD pipeline triggers

---

## 🌳 Example Branch Structure

main (Production)
│
├── develop (Testing)
│
├── feature-login
├── feature-payment
└── hotfix-bug

---

# 3️⃣ Top 10 Most Used Git Commands in DevOps

These commands are used daily in real DevOps environments.

---

## 1. git clone

git clone repository-url

Why it is used:
To copy an existing remote repository to your local system.
Used when starting work on a project.

---

## 2. git status

git status

Why it is used:
To check file status.
Shows modified, staged, and untracked files.

---

## 3. git add .

git add .

Why it is used:
Moves all modified files to staging area.
Prepares files for commit.

---

## 4. git commit -m "message"

git commit -m "Added login feature"

Why it is used:
Saves changes permanently in repository.
Creates a snapshot version.

---

## 5. git branch

git branch

Why it is used:
Lists available branches.
Helps identify current working branch.

---

## 6. git checkout -b branch-name

git checkout -b feature-login

Why it is used:
Creates and switches to a new branch.
Used for feature development.

---

## 7. git switch branch-name

git switch main

Why it is used:
Switches between branches.
Keeps workflow organized.

---

## 8. git merge branch-name

git merge feature-login

Why it is used:
Combines changes from one branch into another.
Commonly merges feature into main.

---

## 9. git pull

git pull origin main

Why it is used:
Downloads latest changes from remote repository.
Keeps local code updated.

---

## 10. git push

git push origin main

Why it is used:
Uploads committed changes to remote repository.
Triggers CI/CD pipelines in DevOps.

---

# 4️⃣ Real DevOps Workflow Example

Step 1: Clone repository  
Step 2: Create feature branch  
Step 3: Make changes  
Step 4: Add and commit  
Step 5: Push feature branch  
Step 6: Merge into main  
Step 7: CI/CD automatically builds and deploys  

---

# 🎯 Interview Summary

Git Lifecycle:
The process of moving files from working directory to staging area and committing them to repository.

Branches:
A separate line of development that allows safe and parallel work without affecting main code.

Most Used Git Commands:
clone, status, add, commit, branch, checkout, switch, merge, pull, push.

These commands are essential for collaboration, automation, and CI/CD in DevOps.

---

✅ End of Day 2 DevOps Notes

# DevOps Day 3 Notes
# Git Merge, Git Rebase & Merge Conflicts

---

# 1️⃣ What is Git Merge?

Git merge is used to combine changes from one branch into another branch.

It preserves the history of both branches and creates a special commit called a "merge commit".

---

## 🔁 How Git Merge Works

Example:

main
A --- B

feature-login
        C --- D

If we run:

git checkout main
git merge feature-login

After merge:

main
A --- B -------- M
         \      /
          C --- D

M = Merge Commit

The merge commit connects both histories together.

---

## ✅ Why Git Merge is Used

- Safe and simple
- Preserves complete history
- Good for team collaboration
- Default strategy in many projects

---

# 2️⃣ What is Git Rebase?

Git rebase moves a branch to start from the latest commit of another branch.

Instead of creating a merge commit, it rewrites commit history to make it linear.

---

## 🔁 How Git Rebase Works

Before:

main
A --- B

feature-login
        C --- D

Command:

git checkout feature-login
git rebase main

After rebase:

main
A --- B

feature-login
          C' --- D'

C and D are recreated as new commits (C' and D').

History becomes clean and straight.

---

## ✅ Why Git Rebase is Used

- Creates clean linear history
- Makes git log easier to read
- Looks more professional
- Often used before merging to main

---

# 3️⃣ Git Merge vs Git Rebase

| Feature | Merge | Rebase |
|----------|--------|--------|
| History | Preserves branch history | Rewrites history |
| Extra Commit | Yes (merge commit) | No |
| Safe for shared branches | Yes | Be careful |
| Cleaner history | No | Yes |
| Beginner friendly | Yes | Slightly advanced |

---

# 4️⃣ What are Merge Conflicts?

A merge conflict occurs when two branches modify the same line of the same file and Git cannot decide which change to keep.

Git stops the merge and asks the developer to resolve it manually.

---

## 🧠 Example Conflict

Branch A:
print("Hello Teja")

Branch B:
print("Hello DevOps")

During merge, Git shows:

<<<<<<< HEAD
print("Hello Teja")
=======
print("Hello DevOps")
>>>>>>> feature-login

This is a conflict.

---

# 🔧 How to Resolve Merge Conflict

Step 1: Open the conflicted file  
Step 2: Decide which code to keep  
Step 3: Remove conflict markers  
Step 4: Save file  
Step 5: Run:

git add filename
git commit

Conflict resolved successfully.

---

# 5️⃣ Why Merge Conflicts Happen

- Multiple developers editing same file
- Working on outdated branches
- Large teams
- Lack of communication

---

# 6️⃣ How to Avoid Merge Conflicts

- Pull latest changes before starting work
- Use small feature branches
- Commit frequently
- Communicate with team
- Keep branches updated

---

# 7️⃣ DevOps Perspective

In DevOps:

- git merge is commonly used with Pull Requests
- git rebase is used to maintain clean history
- Conflicts must be resolved before CI/CD pipeline runs
- If conflicts exist, pipeline fails

---

# 🎯 Interview Summary

Git Merge:
Combines two branches and creates a merge commit.

Git Rebase:
Reapplies commits from one branch onto another to create linear history.

Merge Conflict:
Occurs when Git cannot automatically merge changes because the same lines were modified differently.

---

✅ End of Day 3 DevOps Notes
