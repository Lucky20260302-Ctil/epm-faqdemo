---
project: MP
title: "MP-537: [Coach] Item Sales Amount & Payment Amount Variance (J420)"
issue_key: MP-537
issue_type: Bug PRD
status: Closed
faq_score: 9.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, mp, data_sync, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-537"
created: 2022-06-28
resolved: 2024-07-11
resolution: Done
has_images: True
---

# MP-537: [Coach] Item Sales Amount & Payment Amount Variance (J420)

## 問題描述

**<u>Basic Information</u>**
Project: Coach Japan
Store: J420
POS Version: 72.0214.0000
Mpos Version: 3.14.1
Sales memo: MA001271 voided by MA001279, Re-create MA001280
Sales date: 2022-06-10
VIP: JXXX0006404868
Promotion: LPE001C, LPP001B 
**This is the same issue with MP-533**

**<u>Case Details</u>**

1. Shop user would like to create sales memo J432-MA001271 with Ecoupons (LPE001C, LPP001B).

2. By selecting LPE001C, sales amount will be deducted by 15%, $42,900*0.85 = $36,465.

3. However, MA000608 is showing $42,900which means discount could not be applied effectively.

4. FE POS: Payment Amount is correct $36,465

5. There is $6,435 variance between Sales Item Amount and Payment Amount

6. Customer confirmed actual payment is $31,425

7. Shop user voided MA001271 by MA001279, and re-created MA001280 with correct final price on the same day.

Refer to BE DB table Joudis, the record of LPE001C is missing for MA0012871 and MA001279 while MA001280 is showing correct record. 

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/947067f3-c234-4eef-b5dc-7f07a14208ad)（需 Jira 登入）
 

**<u>Support Document</u>**
Log Record: \\172.16.183.201\localuser\support\JIRA_DB\MP-537

- J420 dbHist

- J420 dbMas

- J420 2022-06-10 Log



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/947067f3-c234-4eef-b5dc-7f07a14208ad)

## 相關資訊

- **Jira:** [MP-537](https://ctil.atlassian.net/browse/MP-537)
- **解決方式:** Done