---
project: BE
issue_key: BE-985
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- api
- be
- data_sync
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-985
created: '2025-01-15'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-985: Total amount duplicate when syncing memo OC65 - 20002034 to CN CRM side'
---
# BE-985: Total amount duplicate when syncing memo OC65 - 20002034 to CN CRM side

## 問題描述

1.2025-01-01 memo OC65-20002034 total amount should be 4555.00.

Memo OC65-20002034 was voided by OC65-20002036       

> 📎 **image-20250115-035232.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e47906bc-0fe0-4ef7-8f19-a71cc0360aa6)（需 Jira 登入）
2.But CRM side received the total amount is '9110'

> 📎 **image-20250115-035441.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/f6aa6868-69b7-469f-b9de-42024cf1158c)（需 Jira 登入）
3.I checked the CRM log,Can also find 2 same SKU.Please help to check the RCA why we send the same SKU twice to CRM?

> 📎 **Image20250115114420.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/2d515f36-c90b-4b8c-9ee9-c241d8571725)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250115-035232.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e47906bc-0fe0-4ef7-8f19-a71cc0360aa6)
2. 📎 **image-20250115-035441.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/f6aa6868-69b7-469f-b9de-42024cf1158c)
3. 📎 **Image20250115114420.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/2d515f36-c90b-4b8c-9ee9-c241d8571725)

## 相關資訊

- **Jira:** [BE-985](https://ctil.atlassian.net/browse/BE-985)