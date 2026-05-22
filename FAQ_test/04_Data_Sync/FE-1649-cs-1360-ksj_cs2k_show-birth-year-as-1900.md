---
project: FE
issue_key: FE-1649
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1649"
created: 2025-03-14
resolved: 2025-10-03
resolution: Done
has_images: False
---

# FE-1649: [CS-1360] KSJ_CS2K_show birth year as 1900, when staff search customer

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 7.0
> **解決日期:** 2025-10-03
> **負責人:** Sherman tse
> **組件:** Front End

## 問題描述

When KSJ store staff search customer, even customer birth year info is exist in C360.

however customer search result on CS2K showing as birth year as 1900. 

CRM team confirmed this customer data in C360 and see this data has right birth date.

can you look into API logic?

 

#==< C360 >================================

 Customer No : 1209510912

 Name        : 佐川 愛実

 Kana Name   : サガワ マナミ

 Gender      : F

 Birthday    : 1994/07/01



## 相關資訊

- **Jira:** [FE-1649](https://ctil.atlassian.net/browse/FE-1649)
- **解決方式:** Done