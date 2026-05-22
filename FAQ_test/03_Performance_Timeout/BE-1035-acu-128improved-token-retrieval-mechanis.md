---
project: BE
issue_key: BE-1035
issue_type: Improvement
status: Closed
tags:
- 03_performance_timeout
- api
- be
- faq
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-1035
created: '2025-03-21'
resolved: '2025-05-02'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'BE-1035: [ACU-128]Improved Token Retrieval Mechanism'
---
# BE-1035: [ACU-128]Improved Token Retrieval Mechanism

## 問題描述

- Improvement: Streamlining the token retrieval process by caching the token from ACIXOM will minimize delays, reducing the time from 5 seconds to 2-3 seconds.

- Pros: Within the token's expiry period, calls to ACIXOM will not be affected by token retrieval delays.

- Cons: The first call (without a cached token) will still experience delays.

- ETA: V1.07.08+ - Function ready.



## 相關資訊

- **Jira:** [BE-1035](https://ctil.atlassian.net/browse/BE-1035)
- **解決方式:** Done