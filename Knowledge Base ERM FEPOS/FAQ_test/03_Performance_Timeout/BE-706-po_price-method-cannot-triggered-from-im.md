---
project: BE
issue_key: BE-706
issue_type: Bug PRD
status: Closed
faq_score: 6.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-706"
created: 2022-11-25
resolved: 2022-12-30
resolution: Done
has_images: False
---

# BE-706: PO_Price Method cannot triggered from IM_price flag

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 6.5
> **解決日期:** 2022-12-30
> **負責人:** Jacky Lam
> **組件:** Backend (ChainStorePlus 7.0)

## 問題描述

Env: Prorunner UAT web & local Backend 

ACC: sx1                        PW: sx1

Location: Process > Purchase Order Maintenance (PO3000)

Precondition: One item fills in in Standard Cost/Retail Price in Item Master & Supplier Cost

Reproduce steps:

Expected

1. Purchase Order Information (PO3000) 

2. Create 

3. Fill in PO No.

4. Select Supplier 

5. Select Currency

6. **Select Price Method correspondingly**

7.  Should tirrgre list price on Manage Table on after select one item (same item)



## 相關資訊

- **Jira:** [BE-706](https://ctil.atlassian.net/browse/BE-706)
- **解決方式:** Done