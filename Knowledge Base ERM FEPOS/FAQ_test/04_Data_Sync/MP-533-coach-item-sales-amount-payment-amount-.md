---
project: MP
issue_key: MP-533
issue_type: Bug PRD
status: Closed
faq_score: 8.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, mp, data_sync, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-533"
created: 2022-06-17
resolved: 2024-07-11
resolution: Done
has_images: True
---

# MP-533: [Coach] Item Sales Amount & Payment Amount Variance

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 8.5
> **解決日期:** 2024-07-11
> **負責人:** Cy Lau
> **組件:** MPOS

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