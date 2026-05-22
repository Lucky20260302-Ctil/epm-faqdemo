---
project: BE
issue_key: BE-1035
issue_type: Improvement
status: Closed
faq_score: 4.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, api]
jira_url: "https://ctil.atlassian.net/browse/BE-1035"
created: 2025-03-21
resolved: 2025-05-02
resolution: Done
has_images: False
---

# BE-1035: [ACU-128]Improved Token Retrieval Mechanism

> **類型:** Improvement | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 4.0
> **解決日期:** 2025-05-02
> **負責人:** Anson Cheung
> **組件:** API

## 問題描述

- Improvement: Streamlining the token retrieval process by caching the token from ACIXOM will minimize delays, reducing the time from 5 seconds to 2-3 seconds.

- Pros: Within the token's expiry period, calls to ACIXOM will not be affected by token retrieval delays.

- Cons: The first call (without a cached token) will still experience delays.

- ETA: V1.07.08+ - Function ready.



## 相關資訊

- **Jira:** [BE-1035](https://ctil.atlassian.net/browse/BE-1035)
- **解決方式:** Done