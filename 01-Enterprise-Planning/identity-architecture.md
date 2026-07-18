# Identity Architecture

## Overview

NorthStar Health Systems uses a centralized Identity and Access Management (IAM) architecture to securely manage workforce identities, privileged accounts, and machine identities.

The environment follows Zero Trust principles by authenticating every identity, authorizing access based on least privilege, and continuously monitoring user activity.

---

# Identity Sources

Primary source of truth:

- Human Resources Information System (HRIS)

Identity Providers:

- Active Directory
- Microsoft Entra ID

Applications:

- Electronic Health Record (EHR)
- Microsoft 365
- Splunk Enterprise
- VPN
- AWS Cloud
- GitHub Enterprise
- Jira
- ServiceNow

---

# Identity Types

## Workforce Identities

- Physicians
- Nurses
- Pharmacists
- Billing Specialists
- Human Resources
- Help Desk
- Security Engineers
- System Administrators

## Privileged Identities

- Domain Administrators
- Cloud Administrators
- Security Administrators
- Database Administrators

## Machine Identities

- Service Accounts
- API Accounts
- Application Identities
- Scheduled Task Accounts

---

# Identity Lifecycle

Joiner

HR creates employee

↓

Identity created

↓

Department assigned

↓

Role assigned

↓

Applications provisioned

↓

MFA enrolled

---

Mover

Department changes

↓

Previous permissions removed

↓

New permissions assigned

↓

Manager approval logged

---

Leaver

Termination recorded

↓

Account disabled

↓

Sessions terminated

↓

VPN revoked

↓

Cloud access removed

↓

Audit log generated

---

# Security Principles

- Least Privilege
- Role-Based Access Control (RBAC)
- Multi-Factor Authentication
- Single Sign-On (SSO)
- Conditional Access
- Continuous Monitoring
- Zero Trust
