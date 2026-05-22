---
project: FE
issue_key: FE-1308
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 07_Workflow_Business
faq_category_label: 流程與業務
tags: [faq, fe, workflow_business, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1308"
created: 2023-11-02
resolved: 2024-03-05
resolution: Done
has_images: False
---

# FE-1308: Double BP redeem for member

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 流程與業務 | **FAQ 分數:** 7.0
> **解決日期:** 2024-03-05
> **負責人:** Sang
> **組件:** Front End

## 問題描述

Will duplicate the redeem record for the member.

 

Re-produce procedure:

1. Sales Memo  Tab1 and Tab2 - both select Member A

2. Sales Memo Tab1 Redeem BP as Cash Disc Amt Coupon

3. sales Memo Tab1 - Commit Payment

4. Sales Memo Tab2 - Select cash payment, commit payment, BP Redeem record duplicated in SM tab2



## 相關資訊

- **Jira:** [FE-1308](https://ctil.atlassian.net/browse/FE-1308)
- **解決方式:** Done