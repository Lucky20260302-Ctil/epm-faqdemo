---
project: FE
issue_key: FE-1672
issue_type: Change Request
status: Closed
tags:
- 03_performance_timeout
- faq
- fe
- front-end-v720.02
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1672
created: '2025-04-22'
resolved: '2025-04-29'
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'FE-1672: Print the store name and address on the receipt'
---
# FE-1672: Print the store name and address on the receipt

## 問題描述

The change details:

- Make change on POS v72.0207.3700

- Add a configuration setting ‘PRINTSHOPNAMEADDR=Y’ in tblConfig table to toggle the feature.

- If PRINTSHOPNAMEADDR=Y, print the location name, and location address under the ba&sh logo and align to the left. Skip the bank address line.

- Apply this config to Loc 10S02112.

 

Mockup Receipt. Will add some spacing between the logo and <u>销售单</u> heading.

> 📎 **image-20250422-022340.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/fe665b58-e767-4e91-8457-345616114e60)（需 Jira 登入）

 



## 附件截圖

1. 📎 **image-20250422-022340.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/fe665b58-e767-4e91-8457-345616114e60)

## 相關資訊

- **Jira:** [FE-1672](https://ctil.atlassian.net/browse/FE-1672)
- **解決方式:** Done