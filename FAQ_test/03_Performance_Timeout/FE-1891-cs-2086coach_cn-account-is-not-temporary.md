---
project: FE
title: "FE-1891: CS-2086:Coach_CN| Account is Not temporary Prohibited while Login With Locked Account As Cashier & In Admin"
issue_key: FE-1891
issue_type: Bug QA
status: Closed
faq_score: 6.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, fe, performance_timeout, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1891"
created: 2026-02-24
resolved: 
resolution: 
has_images: True
---

# FE-1891: CS-2086:Coach_CN| Account is Not temporary Prohibited while Login With Locked Account As Cashier & In Admin

## 問題描述

### **Defect Description: Your User Account is Not temporary Prohibited for Login**

### **🔁 ****Steps to Replicate:**

1. **Launch the CSPLUS application. ( POS 10.34.103.4 )**

2. **Log in using ****in-valid credentials.**** (User Name: AM0001)**

3. **Try inputting wrong password more than ****4-times**** section.**

4. **Observed that account is getting locked.**

5. **Validate Login With Locked Account As Cashier & in Admin**

### **❌ ****Actual Result:**** No error throwing**

### **✅ Expected Result: Error should reflect as Your User Account is Now temporary Prohibited for Login**

---

Comment from Joy:

**Issue:**
When a user enters an invalid password more than four times in the CSPLUS application (POS 10.34.103.4), the account becomes locked as expected. However, when attempting to log in again—whether as a Cashier or Admin—the system does **not** display the required error message.

**Actual Result:**

- No error message is shown when trying to log in with a locked account.

**Expected Result:**

- The system should display the following error:
**“Your User Account is Now Temporarily Prohibited for Login.”**

Login 

> 📎 **image-20260224-021041.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/fffdf0b6-cebe-48a1-be81-6ae7cf62b014)（需 Jira 登入）
login cashier:

> 📎 **image-20260224-021253.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/69949611-8b68-4dec-8cd3-9d8186c3ace2)（需 Jira 登入）
Admin - Change cash flow:

> 📎 **image-20260224-021418.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/570c1735-e060-4b65-8faa-bbab1bffe6fa)（需 Jira 登入）

> 📎 **image-20260224-021442.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a024f940-c012-4cc3-8570-98ef40c05873)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260224-021041.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/fffdf0b6-cebe-48a1-be81-6ae7cf62b014)
2. 📎 **image-20260224-021253.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/69949611-8b68-4dec-8cd3-9d8186c3ace2)
3. 📎 **image-20260224-021418.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/570c1735-e060-4b65-8faa-bbab1bffe6fa)
4. 📎 **image-20260224-021442.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a024f940-c012-4cc3-8570-98ef40c05873)

## 相關資訊

- **Jira:** [FE-1891](https://ctil.atlassian.net/browse/FE-1891)