---
project: FE
issue_key: FE-1615
issue_type: Bug DEV
status: Closed
faq_score: 6.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, fe, performance_timeout, front-end-v750.01r01a]
jira_url: "https://ctil.atlassian.net/browse/FE-1615"
created: 2025-01-24
resolved: 
resolution: 
has_images: False
---

# FE-1615: RIN01443671- loading member cost more time in V75

> **類型:** Bug DEV | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 6.5
> **負責人:** Anson Cheung
> **組件:** Front End v750.01R01A

## 問題描述

OCF120C00054040
1.From "input vip data in POS" to "CRM response vip data",spend31 s.
2.from "Start upsert CRM member" to "API response member data to POS" ,spend 9 s

Total spend about 40 s.



## 相關資訊

- **Jira:** [FE-1615](https://ctil.atlassian.net/browse/FE-1615)