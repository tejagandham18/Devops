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
