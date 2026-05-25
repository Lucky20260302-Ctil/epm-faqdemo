---
project: EPRO
issue_key: ''
issue_type: Functional Requirement
status: Specified
tags:
- epro
- functional-requirement
- spec
title: 'FR-GR-011: Approval and Operational Delegation'
quality: complete
category_label: General Requirements
created: '2026-05-22'
---

## 需求描述

    - **3.1.10** The Platform shall provide the capability to assign another Internal User as a proxy to handle selected operations / approvals within a prescribed period (e.g. during leave), subject to pre-determined rules.
## 驗收標準

External Suppliers are prohibited from appointing a proxy.
The Platform allows an active user designated as a proxy by an Internal User to perform specific operations/approvals within a set timeframe and according to predefined rulesregardless of their division/department.
Another user is delegated as a proxy by the delegator:
The delegation can be canceled by the delegated person at any time while the delegation is still active.
The delegation is cancelled by the delegator:
During the delegation timeframe, the delegated-to person will receive a daily reminder email listing any new and pending operations/approvals they can handle, with the option for the delegated person to handle them independently.
Both the delegated person and the delegated-to person can view the list of delegations with statuses including Active, Cancelled, and Expired.
Delegation and cancellation can be facilitated by the Platform admin user on behalf of the Internal User.
The delegator is helped by the System admin user to delegate another user as a proxy:
The delegator is helped by the System admin user to cancel the delegation:
The Use Case will be documented in the RFQ and Tender section of the e-Procurement Requirements and Supplier Management Requirements.


