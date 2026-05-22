---
project: FE
title: "FE-1123: [Coach] Item Sales Amount & Payment Amount Variance"
issue_key: FE-1123
issue_type: Bug PRD
status: Closed
faq_score: 9.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1123"
created: 2022-06-16
resolved: 2024-05-04
resolution: Done
has_images: True
---

# FE-1123: [Coach] Item Sales Amount & Payment Amount Variance

## 問題描述

**<u>Basic Information</u>**
Project: Coach Japan
Store: J432
Sales memo: 00021313
Sales date: 2022-06-12
VIP: JXXX0006681353
Promotion: LPE001C, LPP001B

**<u>Case Details</u>**

- Shop user would like to create sales memo J432-00021313 with Ecoupons.

- However, Sales Item Amount $(44,000+1,650+1,650) =$47,300 which means discount could not be shown effectively.

- Payment Amount is correct $40,700

- There is $6,600 variance between Sales Item Amount and Payment Amount

- Shop User discovered wrong data and voided sales memo #00021313 by #00021314. After that, user re-created sales memo #00021315

| **Sales Item** | **Payment** | **Variance** | 
| 47,300 | 40,700 | 6,600 | 

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/10e791ce-2cd3-432e-8ded-058285cdb1a0)（需 Jira 登入）

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/deaf1ef6-1130-4931-ba8b-d447e4f8b36c)（需 Jira 登入）
 
 
For more log and data, please refer to FTP \\172.16.183.201\localuser\support\JIRA_DB\FE-1123

- J432 dbMas

- J432 dbtrans.SDF



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/10e791ce-2cd3-432e-8ded-058285cdb1a0)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/deaf1ef6-1130-4931-ba8b-d447e4f8b36c)


## Jira Comments

> **Steven Yuen** (2022-06-30):
> Sang cannot reproduce the scenario and thus suggest to keep monitoring for more information. 

## 相關資訊

- **Jira:** [FE-1123](https://ctil.atlassian.net/browse/FE-1123)
- **解決方式:** Done