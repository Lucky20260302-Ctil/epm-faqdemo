---
project: BE
issue_key: BE-841
issue_type: Improvement
status: Closed
faq_score: 5.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-841"
created: 2024-04-15
resolved: 2024-05-24
resolution: Done
has_images: False
---

# BE-841: Colsiz_seq fully occupied and causes ITMEAN interface hang up

> **類型:** Improvement | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 5.5
> **解決日期:** 2024-05-24
> **負責人:** Joy Li
> **組件:** Backend (ChainStorePlus 7.0)

## 問題描述

Coach reports that the itmean import data interface process hang up. The root cause is the colsiz_seq is fully occupied. The workaround is to delete unused color & size seq. and find space for the new color & size record create. Tapestry requests a long term solution now.



## 相關資訊

- **Jira:** [BE-841](https://ctil.atlassian.net/browse/BE-841)
- **解決方式:** Done
- **標籤:** CS-924