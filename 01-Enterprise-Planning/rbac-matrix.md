# Role-Based Access Control (RBAC) Matrix

## Purpose

This document defines which roles have access to which enterprise applications.

The objective is to enforce the Principle of Least Privilege while enabling employees to perform their job responsibilities.

| Role | EHR | Microsoft 365 | VPN | Splunk | AWS | HR System | Payroll | GitHub |
|------|:---:|:-------------:|:---:|:------:|:---:|:---------:|:-------:|:------:|
| Physician | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Nurse | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Pharmacist | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Billing Specialist | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ |
| HR Specialist | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ |
| Help Desk | ❌ | ✅ | ✅ | Limited | ❌ | ❌ | ❌ | ✅ |
| SOC Analyst | ❌ | ✅ | ✅ | ✅ | Read Only | ❌ | ❌ | ✅ |
| IAM Engineer | ❌ | ✅ | ✅ | ✅ | Admin | ❌ | ❌ | ✅ |
| System Administrator | ❌ | ✅ | ✅ | Admin | Admin | ❌ | ❌ | Admin |

---

## Access Principles

- All users receive only the minimum permissions required.
- Administrative access requires MFA.
- Privileged roles are reviewed every 90 days.
- Temporary elevated access must be approved and logged.
- All access changes are auditable.
