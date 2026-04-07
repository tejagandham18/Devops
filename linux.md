# DevOps Phase 1 - Linux Basics Notes

## 📌 Overview

These notes cover the foundational Linux concepts required for DevOps:

* Navigation
* File handling
* Permissions
* Processes
* Basic networking

---

# 🧱 1. Linux Navigation Commands

## 🔹 pwd (Print Working Directory)

Shows current location:

```bash
pwd
```

---

## 🔹 ls (List Files)

Shows files and folders:

```bash
ls
```

### Detailed view:

```bash
ls -l
```

Displays:

* Permissions
* Owner
* Size
* Date

---

## 🔹 cd (Change Directory)

Move between folders:

```bash
cd foldername
cd ..      # go back
cd ~       # home directory
```

---

# 📂 2. File & Directory Commands

## 🔹 mkdir (Make Directory)

```bash
mkdir foldername
```

## 🔹 touch (Create File)

```bash
touch file.txt
```

Creates empty file

## 🔹 cp (Copy File)

```bash
cp file1.txt file2.txt
```

## 🔹 mv (Move/Rename)

```bash
mv old.txt new.txt
```

## 🔹 rm (Remove)

```bash
rm file.txt
```

---

# 🔐 3. Permissions

## 🔹 Understanding Permissions

Example:

```bash
-rwxr-xr--
```

Breakdown:

* First part: file (-) or directory (d)
* Next 3: user
* Next 3: group
* Last 3: others

## 🔹 Permission Types

* r → read
* w → write
* x → execute

---

## 🔹 chmod (Change Permissions)

### Symbolic Mode

```bash
chmod +x file.sh   # add execute
chmod -x file.sh   # remove execute
chmod u+x file.sh  # user execute
chmod o-rwx file.sh # remove others
```

### Numeric Mode

| Number | Meaning |
| ------ | ------- |
| 7      | rwx     |
| 6      | rw-     |
| 5      | r-x     |
| 4      | r--     |
| 0      | ---     |

Examples:

```bash
chmod 777 file.sh
chmod 700 file.sh
chmod 644 file.txt
```

---

## 🔹 Important Use Cases

### Make script executable

```bash
chmod +x deploy.sh
./deploy.sh
```

### Secure file

```bash
chmod 700 file.sh
```

---

# 📄 4. cat Command

## 🔹 View file content

```bash
cat file.txt
```

## 🔹 Create file with content

```bash
cat > file.txt
```

## 🔹 Append content

```bash
cat >> file.txt
```

---

# ⚙️ 5. Processes

## 🔹 ps (Process Status)

```bash
ps
ps aux
```

## 🔹 top (Live Monitoring)

```bash
top
```

Press `q` to exit

## 🔹 kill (Stop Process)

```bash
kill <pid>
kill -9 <pid>
```

---

# 🌐 6. Networking Commands

## 🔹 ping

```bash
ping google.com
```

Checks connectivity

## 🔹 curl

```bash
curl https://example.com
```

Fetches data from URL

---

# 🧪 Practice Summary

## ✅ Navigation

* pwd
* ls
* cd

## ✅ File Handling

* mkdir
* touch
* cp
* mv
* rm

## ✅ Permissions

* chmod
* symbolic & numeric

## ✅ Processes

* ps
* top
* kill

## ✅ Networking

* ping
* curl

---

# 💡 Key DevOps Takeaways

* Always check permissions before running scripts
* Use `chmod +x` for execution
* Use `ps` and `top` to monitor systems
* Use `kill` to stop stuck processes
* Use `cat` for quick debugging

---

# 🚀 Next Step

Proceed to:
➡️ Shell Scripting (Automation)

This is the most important skill for DevOps.

# 📘 Day 3 & Day 4 Notes

## 🧠 Topics Covered

* Process Management (Linux)
* Shell Scripting Basics

---

# ⚙️ 1. Process Management (Linux)

## 🔹 What is a Process?

A process is a running program in the system.

Example:

```bash
sleep 100
```

This creates a process that runs for 100 seconds.

---

## 🔹 Types of Processes

### Foreground Process

```bash
sleep 5
```

* Blocks terminal

### Background Process

```bash
sleep 5 &
```

* Runs in background

---

## 🔹 Important Commands

### 1. View Processes

```bash
ps
ps aux
```

* `ps` → current terminal processes
* `ps aux` → all system processes

---

### 2. Detailed View

```bash
ps -ef
```

* Shows process hierarchy

---

### 3. Live Monitoring

```bash
top
```

* Real-time CPU & memory usage
* Press `q` to exit

---

### 4. Find Specific Process

```bash
ps aux | grep sleep
```

* Filters processes by name

---

### 5. Get PID Quickly

```bash
pgrep sleep
```

* Returns process ID

---

### 6. Kill Process

```bash
kill <pid>
kill -9 <pid>
```

* Stops process

---

## 🔹 DevOps Use Cases

* Check if application is running
* Monitor system performance
* Kill stuck processes

---

# 🧱 2. Shell Scripting Basics

## 🔹 What is a Shell Script?

A file containing Linux commands executed automatically.

---

## 🔹 Basic Script Structure

```bash
#!/bin/bash

echo "Hello DevOps"
```

---

## 🔹 How to Run Script

```bash
chmod +x script.sh
./script.sh
```

---

## 🔹 Variables

```bash
name="Teja"
echo "Hello $name"
```

### Rules:

* No spaces around `=`
* Use `$` to access variable

---

## 🔹 Writing to Files

### Using echo

```bash
echo "Hello" > file.txt
echo "World" >> file.txt
```

### Using cat

```bash
cat file.txt
```

---

## 🔹 Key Differences (echo vs cat)

| Command | Usage                      |
| ------- | -------------------------- |
| echo    | Write content (automation) |
| cat     | Read content               |

---

## 🔹 DevOps Usage

* Automate tasks
* Write logs
* Build deployment scripts

---

# 🚀 Summary

## Process Commands

* ps aux
* ps -ef
* top
* grep
* pgrep
* kill

## Shell Scripting

* Script creation
* Variables
* echo for automation

---

# 💡 Key Takeaways

* A process is a running program
* Use `ps aux` to view processes
* Use `kill` to stop processes
* Shell scripts automate commands
* Use `echo` for writing inside scripts

---

# 🔥 Next Step

➡️ Practice conditions and loops
➡️ Build small automation scripts
