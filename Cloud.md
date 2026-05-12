# ☁️ AWS Day 1 Notes
# Introduction to Cloud Computing

---

# 1️⃣ What is Cloud Computing?

Cloud computing is the delivery of computing services such as:

- Servers
- Storage
- Databases
- Networking
- Software

over the internet on-demand.

Instead of buying and maintaining physical servers, companies can rent resources from cloud providers.

---

## 📌 Simple Definition

Cloud computing means using IT resources over the internet instead of managing physical infrastructure manually.

---

# 2️⃣ Traditional On-Premises Infrastructure

Before cloud computing, companies used:

- Physical servers
- Data centers
- Networking hardware
- Storage devices

inside their own office or organization.

This model is called:

## On-Premises Infrastructure

---

## Problems with On-Premises

- High hardware cost
- Maintenance responsibility
- Power and cooling cost
- Difficult scaling
- Hardware failures
- Requires dedicated IT teams

---

# 3️⃣ What is Virtualization?

Virtualization allows multiple virtual machines (VMs) to run on a single physical server.

Before virtualization:

```text
1 Server = 1 Application

This improved:

Resource utilization
Cost efficiency
Scalability
4️⃣ Evolution to Cloud Computing

Infrastructure evolution:

Traditional Servers
        ↓
Virtualization
        ↓
Cloud Computing

Cloud providers use virtualization internally to efficiently manage resources.

5️⃣ Types of Cloud
🔹 Public Cloud

Infrastructure is owned and managed by cloud providers.

Examples:

Amazon Web Services (AWS)
Microsoft Azure
Google Cloud Platform (GCP)

Users rent resources using a:

Pay-As-You-Go

model.

Characteristics
Highly scalable
Cost effective
Accessible over internet
No infrastructure maintenance
🔹 Private Cloud

Infrastructure is managed inside the organization itself.

Used mostly by:

Banks
Government
Military
Healthcare
Characteristics
More security
Better control
Higher maintenance cost
6️⃣ Public Cloud vs Private Cloud
Feature	Public Cloud	Private Cloud
Ownership	Cloud Provider	Organization
Cost	Lower	Higher
Scalability	High	Limited
Security Control	Shared	Full Control
Maintenance	Provider	Organization
7️⃣ Why AWS?

AWS stands for:

Amazon Web Services

AWS is the world's leading cloud platform.

Why AWS is Popular
First major cloud provider
Largest market share
Massive global infrastructure
Large service ecosystem
Huge job opportunities
Popular AWS Services
EC2 → Virtual servers
S3 → Storage
IAM → Access management
VPC → Networking
8️⃣ Cloud Repatriation

Cloud repatriation means:

Cloud → Back to On-Premises

Some companies move workloads back from cloud to their own servers.

Reasons for Cloud Repatriation
High cloud costs
Security requirements
Compliance needs
Vendor lock-in concerns
Performance requirements
Important Point

Cloud repatriation is rare.

Most companies still continue using cloud platforms.

9️⃣ Benefits of Cloud Computing
Scalability

Increase or decrease resources easily.

Cost Optimization

Pay only for resources used.

Flexibility

Access services from anywhere.

High Availability

Cloud providers offer reliable infrastructure.

Faster Deployment

Resources can be created quickly.

Global Access

Applications can serve users worldwide.

🔟 AWS Account Creation

Basic steps:

Open AWS signup page
Enter email and password
Choose Personal account
Add debit/credit card
Verify mobile number
Select Basic Support Plan
Login to AWS Console
Important AWS Best Practices
Never use root account daily

Create IAM users instead.

Enable MFA

Adds extra security to AWS account.

Stop unused resources

Prevents unexpected billing.

1️⃣1️⃣ Important Terms
Term	Meaning
On-Premises	Company-owned infrastructure
Virtualization	Multiple VMs on one server
Cloud Computing	Renting IT resources over internet
Public Cloud	Provider-managed infrastructure
Private Cloud	Organization-managed infrastructure
