---
project: BE
title: "BE-1001: CS-1333 OSS Enhancement for Polling"
issue_key: BE-1001
issue_type: Improvement
status: Closed
faq_score: 5.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, polling]
jira_url: "https://ctil.atlassian.net/browse/BE-1001"
created: 2025-02-11
resolved: 2025-05-02
resolution: Done
has_images: False
---

# BE-1001: CS-1333 OSS Enhancement for Polling

## 問題描述

- Use OSS native scanning mechanism instead of FTP’s

- In extreme conditions (all 855 tills have transaction every 3 mins) we need to take 87mins to handle one batch data uploading, which means we need 9 oss nodes.

- Considering about the real business, we propose to have oss main, N1 and N2 for whole CN.



## 相關資訊

- **Jira:** [BE-1001](https://ctil.atlassian.net/browse/BE-1001)
- **解決方式:** Done