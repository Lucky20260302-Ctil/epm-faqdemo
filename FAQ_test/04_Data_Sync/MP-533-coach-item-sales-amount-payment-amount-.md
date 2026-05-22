---
project: MP
issue_key: MP-533
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- mp
- mpos
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-533
created: '2022-06-17'
resolved: '2024-07-11'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'MP-533: [Coach] Item Sales Amount & Payment Amount Variance'
---
# MP-533: [Coach] Item Sales Amount & Payment Amount Variance

## 問題描述

**<u>Basic Information</u>**
Project: Coach Japan
Store: J441
POS Version: 72.0214.0000
Mpos Version: 3.14.1
Sales memo: MA000608
Sales date: 2022-06-16
VIP: JXXX0005222852
Promotion: LPE001C, LPP001A

**<u>Case Details</u>**

- Shop user would like to create sales memo J432-MA000608 with Ecoupons (LPE001C, LPP001A).

- By selecting LPE001C, sales amount will be deducted by 15%, $40,700*0.85 = $31,425.

- However, MA000608 is showing $40,700 which means discount could not be applied effectively.

- FE POS: Payment Amount is correct $40,700

- There is $6,105 variance between Sales Item Amount and Payment Amount

- Customer confirmed actual payment is $31,425

| **Sales Item** | **Payment** | **Variance** | 
| 40,700 | 31,425 | 6,105 | 

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d8ec6d8d-4fdb-404c-ad53-b0359128d729)（需 Jira 登入）
FTP: \\172.16.183.201\localuser\support\JIRA_DB\MP-533



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d8ec6d8d-4fdb-404c-ad53-b0359128d729)

## 相關資訊

- **Jira:** [MP-533](https://ctil.atlassian.net/browse/MP-533)
- **解決方式:** Done