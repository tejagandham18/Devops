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
