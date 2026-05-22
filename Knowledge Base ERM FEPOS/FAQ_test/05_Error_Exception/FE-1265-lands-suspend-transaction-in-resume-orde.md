---
project: FE
issue_key: FE-1265
issue_type: Bug QA
status: Closed
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end-v760.02]
jira_url: "https://ctil.atlassian.net/browse/FE-1265"
created: 2023-06-09
resolved: 2023-11-16
resolution: Done
has_images: False
---

# FE-1265: [Lands] Suspend transaction in Resume Order cannot be deleted after day end

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.5
> **解決日期:** 2023-11-16
> **負責人:** Sang
> **組件:** front end v760.02

## 問題描述

Reproduce steps:

1. Save some orders into Resume Order as suspended  transaction

2. Make a day end

3. Go back to Resume Order 

Existng result:

Resume Order still save suspended  orders 



## 相關資訊

- **Jira:** [FE-1265](https://ctil.atlassian.net/browse/FE-1265)
- **解決方式:** Done