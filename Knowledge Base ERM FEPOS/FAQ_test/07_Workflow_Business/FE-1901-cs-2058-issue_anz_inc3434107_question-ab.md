---
project: FE
issue_key: FE-1901
issue_type: Bug PRD
status: Closed
faq_score: 6.0
faq_category: 07_Workflow_Business
faq_category_label: 流程與業務
tags: [faq, fe, workflow_business, day-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1901"
created: 2026-03-17
resolved: 2026-03-25
resolution: Done
has_images: False
---

# FE-1901: [CS-2058] Issue_ANZ_INC3434107_Question about Day END Cash Balancing

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 流程與業務 | **FAQ 分數:** 6.0
> **解決日期:** 2026-03-25
> **負責人:** Sherman tse
> **組件:** Day End

## 問題描述

 Will jump 2 rows if  type "Enter" instead of 1 row in CASH Denomination

Troubleshooting:

1. DAY END> Cash Drawer Tender Count Input>CASH> CASH Denomination

2.E.g. Enter quantity of 5 cents for 5, then we tick "Enter", it jump to 20cents instead of next row (10 cents).  



## 相關資訊

- **Jira:** [FE-1901](https://ctil.atlassian.net/browse/FE-1901)
- **解決方式:** Done