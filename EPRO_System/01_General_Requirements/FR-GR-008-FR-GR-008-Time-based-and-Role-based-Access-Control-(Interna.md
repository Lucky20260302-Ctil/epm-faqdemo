---
project: EPRO
issue_key: ''
issue_type: Functional Requirement
status: Specified
tags:
- epro
- functional-requirement
- spec
title: 'FR-GR-008: Time-based and Role-based Access Control (Internal Users)'
quality: complete
category_label: General Requirements
created: '2026-05-22'
---

## 需求描述

3.1.8	The Contractor shall propose a comprehensive set of roles and responsibilities, including viewer, preparer, reviewer, approver, administrator, and various levels of approval, within the Platform. These proposals should align with HKTDC's organisational chart and comply with the PPG and other relevant policies. The system settings should be intelligently designed to ensure the seamless assignment of appropriate access and privileges to users, taking into consideration their specific roles, requirements, and the hierarchical approval process. Unless stated otherwise, all users of the Platform within HKTDC are collectively referred to as “Internal Users”.

## 驗收標準

The Platform have the capability to assign Procurement Officer / Buyer to specific user groups based on their division or department within the organization. This assignment ensures that users can only access procurement activities within their designated user group and are restricted from accessing activities in other user groups.
Each user can have multiple user roles under the designated user account type.
Access rights to system functions/modules should be granted to user roles:
The Platform to display user names that include the user's title and the department/division they belong to. For example, the display name for Andy Lau would be Andy Lau, Director, Enforcement Division.
Time-based access control related to Internal Users on RFQ / Tender is outlined as follows:
The Use Case will be documented in the RFQ and Tender section of the e-Procurement Requirements and Supplier Management Requirements.

## 依賴項

FR-GR-028 Customization Requirements to the Platform


