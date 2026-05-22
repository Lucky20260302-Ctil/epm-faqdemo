---
project: FE
issue_key: FE-897
issue_type: Bug PRD
status: Closed
faq_score: 5.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, fe, performance_timeout, sales]
jira_url: "https://ctil.atlassian.net/browse/FE-897"
created: 2021-01-08
resolved: 2022-08-18
resolution: Done
has_images: False
---

# FE-897: Duplicated Transaction caused by out of memory 

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 5.5
> **解決日期:** 2022-08-18
> **負責人:** Sang
> **組件:** Sales

## 問題描述

Version : 7.1.0.02R14K

After checking the log files, this issue caused by out of memory . Once the POS is not enough memory to complete the transaction then it may happen wrongly load the last running sequence to complete the transaction again. 

please help to check it.

Thanks.



## 相關資訊

- **Jira:** [FE-897](https://ctil.atlassian.net/browse/FE-897)
- **解決方式:** Done