---
project: FE
issue_key: FE-1779
issue_type: Bug PRD
status: Closed
faq_score: 7.5
faq_category: 01_Install_Deploy
faq_category_label: 安裝與部署
tags: [faq, fe, install_deploy, fe]
jira_url: "https://ctil.atlassian.net/browse/FE-1779"
created: 2025-10-30
resolved: 
resolution: 
has_images: True
---

# FE-1779: [CS-1818] KR_PIP_AuditLog_FE_AuditLog Worker service Not executed

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 安裝與部署 | **FAQ 分數:** 7.5
> **負責人:** Tovi Wang
> **組件:** fe

## 問題描述

While performing **CS2K FE POS - Audit Log testing for KR region** we have the below steps to be performed 

**Testing Machine** : 10.34.103.3

**Location**: OCQ96

Version Deployed: 

- V75.004.1404.0000
**Steps to recreate:**

1. Launch CS2000 application

2. Perform member Inquiry/ member search

(Any action like accessing member profiles, conducting searches)

**Expected results:**

1. The system should display the corresponding member's details.

2.  The sqlite log in CS2K test machine **has the latest logs updated -**  **AuditPCD.db in C:\Retdata**

3. The **AuditLogWorkerService** should be executed

4.  **audit_vip records** should contain **1 log for each action performed in FRont End (Cs2K)**

**Actual result:**

1. The system should display the corresponding member's details. - **Working Fine** 

2.  The sqlite log in CS2K test machine **has the latest logs updated -**  **AuditPCD.db in C:\Retdata -** **Working Fine** **

3. The **AuditLogWorkerService** should be executed - **Not working as expected** 

4.  **audit_vip records** should contain **1 log for each action performed in FRont End (Cs2K) -** **Not working as expected** **

 

**Ple**ase find the screenshots from the testing machine and the database validation results herewith

**Database - CS16 schema** 

> 📎 **image-20251030-024847.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/f92abf15-0767-49d8-82a3-88e66eeb8ea3)（需 Jira 登入）
**Auditpcd Log**

> 📎 **image-20251030-025143.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ce253ccd-80b1-4876-b05d-f346ab80c8cf)（需 Jira 登入）
Auditlogworkerservice Log

> 📎 **image-20251030-025225.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7a24aebb-f58c-490d-adfb-258c5637ed5c)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20251030-024847.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/f92abf15-0767-49d8-82a3-88e66eeb8ea3)
2. 📎 **image-20251030-025143.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ce253ccd-80b1-4876-b05d-f346ab80c8cf)
3. 📎 **image-20251030-025225.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7a24aebb-f58c-490d-adfb-258c5637ed5c)

## 相關資訊

- **Jira:** [FE-1779](https://ctil.atlassian.net/browse/FE-1779)