---
project: FE
issue_key: FE-1200
issue_type: Bug PRD
status: Closed
faq_score: 6.5
faq_category: 07_Workflow_Business
faq_category_label: 流程與業務
tags: [faq, fe, workflow_business, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1200"
created: 2022-12-20
resolved: 2023-11-16
resolution: Done
has_images: False
---

# FE-1200: MM Coupon Discount Calculation - Apply Rounding Method

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 流程與業務 | **FAQ 分數:** 6.5
> **解決日期:** 2023-11-16
> **負責人:** Yan Wong
> **組件:** Front End

## 問題描述

Sales Memo - apply rounding method on the net amount ( Gross Amt - Disc Amt) .

         Net amt = RND (Gross amt x (1- DIsc %))

ex:    Net Amt = 2950 x (1-15%) = 2507.5 --> 2507 ( Round down)

However in MM Coupon Module,  POS apply rounding method on MM Coupon discount amount first, then calculate net amt. 

          Net Amt = Gross Amt - RND ( Gross Amt x Disc %)

     ex:  Net Amt  = 2950 - RND(2950 x15%) = 2950 - Rnd(442.5 --> 442) = 2508

 

Thus getting different Result.

 

This bug occurred in v720.02R10+ caused by Fixing Multi Disc Perc MM Coupon Not based on Net/Net Amount cause negative value (KTS 210719 v720.01R10 Item 15, v750.01R01A)

 



## 相關資訊

- **Jira:** [FE-1200](https://ctil.atlassian.net/browse/FE-1200)
- **解決方式:** Done