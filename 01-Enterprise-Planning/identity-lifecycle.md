# Identity Lifecycle

## Joiner

1. HR creates employee.
2. IAM platform creates identity.
3. Active Directory account created.
4. Microsoft Entra ID account synchronized.
5. Default department groups assigned.
6. MFA enrollment required.
7. Manager verifies access.

---

## Mover

1. HR updates department.
2. Old permissions removed.
3. New RBAC role assigned.
4. Manager approval required.
5. Audit event logged.

---

## Leaver

1. HR records termination.
2. Disable Active Directory account.
3. Disable Microsoft Entra ID account.
4. Revoke VPN access.
5. Disable cloud access.
6. Remove privileged group memberships.
7. Archive mailbox.
8. Generate audit report.
