---
project: FE
issue_key: FE-1126
issue_type: Improvement
status: Closed
faq_score: 6.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, fe, performance_timeout, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1126"
created: 2022-06-27
resolved: 2024-05-06
resolution: Done
has_images: False
---

# FE-1126: Enhance Coach Print Out Performance - Re-Get Member Name

> **類型:** Improvement | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 6.5
> **解決日期:** 2024-05-06
> **組件:** Front End

## 問題描述

Case Details:

when POS retrieve Member information which is new created in e-Name platform, POS will get a temporary  value '-' assign to Member Last Name and first name.  In order to print the correct member name in receipt, POS will retrieve member name again in printing receipt process.

 

Improvement:

. Change to retrieve member name in confirm create invoice if the member name is start with '-' or is ''

~~ Change to retrieve member name in printing process  if the member name in sales journal is start with '~~' or is ''

 



## 相關資訊

- **Jira:** [FE-1126](https://ctil.atlassian.net/browse/FE-1126)
- **解決方式:** Done