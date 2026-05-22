---
project: BE
issue_key: BE-1029
issue_type: Bug PRD
status: Closed
tags:
- 03_performance_timeout
- be
- data-interface
- faq
- performance_timeout
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1029
created: '2025-03-18'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'BE-1029: [CS-1370] Landlord CHANGI CITY interface exported data is wrong'
---
# BE-1029: [CS-1370] Landlord CHANGI CITY interface exported data is wrong

## 問題描述

The landlord CHANGI CITY interface exported data from GentingHighlandsSalesUpload.exe is wrong / inconsistent.

 

For the attached sample data on 20250228, we found below incorrect points.

Hour 14 - Payment data in column 11-17 looks correct (the same as DB). The sales without tax (column 6) is consistent with the payment data. But the tax (column 7) looks incorrect, which should be 44.26 instead of 72.17.

Hour 17 - The payment data is not matching DB data. The total sales and tax (column 6 and 7) are wrong / inconsistent with both column 11-17 and DB.

Hour 21 - The payment data is missing 1 record. The total sales and tax are correct.

 

Also attached records exported from DB for comparing.

Quickly checked other exported data, all have similar behavior.

> 📎 **Image20250318165349.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/506a7dd1-023d-4892-9b52-103759a8214c)（需 Jira 登入）

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/6ec5f765-a98f-4d52-b419-3d10c45083d5)（需 Jira 登入）

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/09b84007-3a62-4510-9b38-aae070441abb)（需 Jira 登入）



## 附件截圖

1. 📎 **Image20250318165349.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/506a7dd1-023d-4892-9b52-103759a8214c)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/6ec5f765-a98f-4d52-b419-3d10c45083d5)
3. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/09b84007-3a62-4510-9b38-aae070441abb)

## 相關資訊

- **Jira:** [BE-1029](https://ctil.atlassian.net/browse/BE-1029)