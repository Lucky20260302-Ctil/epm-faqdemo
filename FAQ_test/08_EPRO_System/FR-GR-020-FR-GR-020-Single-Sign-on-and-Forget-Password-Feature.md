---
title: "FR-GR-020: FR-GR-020: Single Sign-on and Forget Password Feature"
tags: [epro, EPRO_System]
---

# FR-GR-020: FR-GR-020: Single Sign-on and Forget Password Feature

## 需求描述

Requirement ID:	FR-GR-020	Requirement Type:	General Requirements
Parent Requirement #:
None
Description:
3.1.23	Single Sign-on shall be integrated with the Platform for Internal Users. A “Forget Password” mechanism shall be available for external suppliers, enabling them to reset their passwords if needed.
Rationale:
None
Acceptance / Fit Criteria:
Internal users will each have an AD login ID and authenticate through Azure AD and Single Sign-on. Password control will be managed by Azure AD instead of the Platform.
External Suppliers are not supported to use Single Sign-on and are bounded by the password policy specified in FR-GR-001 Unsuccessful Login Attempts Locking Feature.
External Suppliers with master and sub-accounts have the ability to reset their passwords when necessary. They are required to use 2FA (One-time Password) before they can set a new password.
If an account is locked out due to unsuccessful login attempts, users have the option to unlock the account after resetting the password, based on the configuration settings in the password policy.
The Platform shall successfully perform all the actions outlined in the Use Case 19.4 and Use Case 20.
Dependencies:
None
Tailoring Guidelines:
None
Change History:
None