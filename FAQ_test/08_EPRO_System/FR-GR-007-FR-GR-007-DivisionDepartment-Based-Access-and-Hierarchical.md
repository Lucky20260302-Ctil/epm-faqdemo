---
project: ''
issue_key: ''
issue_type: ''
status: ''
tags:
- epro
- epro_system
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: ''
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: ''
category_label: ''
quality: stub
title: 'FR-GR-007: FR-GR-007: Division/Department-Based Access and Hierarchical Access Control'
---
# FR-GR-007: FR-GR-007: Division/Department-Based Access and Hierarchical Access Control

## 需求描述

Requirement ID:	FR-GR-007	Requirement Type:	General Requirements
Parent Requirement #:
None
Description:
This requirement addresses the need for Division/Department-Based Access and Hierarchical Access Control of the Platform.
Rationale:
None
Acceptance / Fit Criteria:
During the system implementation, the configuration involves setting up user groups to facilitate procurement activities in both centralized and decentralized ways as outlined below:
Different divisions/departments/sections/teams
Different category teams under the Procurement department
Different project teams.
The diagram below illustrates the typical setup of corporate supplies:
Data alignment and access control primarily rely on user groups to standardize and allow access, reading, creation, and editing of RFX in procurement activities.
The user group has attributes that manage the functions below in procurement activities:
Procurement division/department is responsible for managing purchases or assisting others with the procurement activities
Budget division/department is responsible for procurement budgeting and payments
User division/department representing the requester of Purchase Requests
The specific user groups should be clearly defined and documented during the subsequent SA&D stage.
Note: 10 additional reserved user groups and set them as inactive. This will provide flexibility for HKTDC to change the user group names and activate them as needed, allowing for future modifications if required.
The Use Case will be documented in the RFQ and Tender section of the e-Procurement Requirements and Supplier Management Requirements.
Dependencies:
None
Tailoring Guidelines:
None
Change History:
None