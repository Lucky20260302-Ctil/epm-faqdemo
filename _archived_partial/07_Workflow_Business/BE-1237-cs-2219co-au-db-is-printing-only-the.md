---
project: BE
issue_key: BE-1237
issue_type: Bug PRD
status: Open
tags:
- 07_workflow_business
- be
- faq
- table
- workflow_business
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1237
created: '2026-03-20'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'BE-1237: [CS-2219]CO - AU - DB is printing only the first line of the Remarks field, ignoring the remaining lines'
---
# BE-1237: [CS-2219]CO - AU - DB is printing only the first line of the Remarks field, ignoring the remaining lines

## 問題描述

**CO - AU - DB is printing only the first line of the Remarks field, ignoring the remaining lines**

**Steps:**

1. Add an item

2. Go to remark field.

3. Add four lines of remarks having 4*40 letters

4. Complete the transactions

5. Go to DB

6. Check the memo number on jouinv table.

7. Check the remark column

Actual result: DB is printing only the first line of the jouinv_emarks field, ignoring the remaining lines Expected result: Remark field on DB should print all the lines given at the time of placing the order on CS2K.

> 📎 **image-20260320-034153.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7c2db4f2-086a-444e-ad28-e01807ecefcb)（需 Jira 登入）
Testing was conducted on **10.34.103.18** **OCFA218** (CO AU environment) under Memo Number: **00000261**.

1.FE POS Remark total 4 lines.

> 📎 **image-20260320-034324.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/933c84d5-ab9e-42f3-90d9-1ea5dd6c4634)（需 Jira 登入）
2.Sales receipt can normal display the 4 lines remarks.

> 📎 **image-20260320-034402.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/2000145f-5caf-4e9c-bfae-8a50cffcba7e)（需 Jira 登入）
3.I found that the maximum field limit for the jouinv_remarks field is 40 in BE DB jouinv table.

And in the BE jouinv table, there is only one remarks field.

> 📎 **image-20260320-034859.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/920e8c3f-4428-4037-8492-8007c0dba14c)（需 Jira 登入）
4.But in FE DBSSE,there are total 8 remarks field.The maximum character limit for each field is 40.

> 📎 **image-20260320-040941.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d83da334-b936-47c7-bee7-b5673c5ea845)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260320-034153.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7c2db4f2-086a-444e-ad28-e01807ecefcb)
2. 📎 **image-20260320-034324.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/933c84d5-ab9e-42f3-90d9-1ea5dd6c4634)
3. 📎 **image-20260320-034402.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/2000145f-5caf-4e9c-bfae-8a50cffcba7e)
4. 📎 **image-20260320-034859.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/920e8c3f-4428-4037-8492-8007c0dba14c)
5. 📎 **image-20260320-040941.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d83da334-b936-47c7-bee7-b5673c5ea845)

## 相關資訊

- **Jira:** [BE-1237](https://ctil.atlassian.net/browse/BE-1237)