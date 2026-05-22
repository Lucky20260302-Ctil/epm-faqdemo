---
project: BE
issue_key: BE-1001
issue_type: Improvement
status: Closed
tags:
- 03_performance_timeout
- be
- faq
- performance_timeout
- polling
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-1001
created: '2025-02-11'
resolved: '2025-05-02'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'BE-1001: CS-1333 OSS Enhancement for Polling'
---
# BE-1001: CS-1333 OSS Enhancement for Polling

## 問題描述

- Use OSS native scanning mechanism instead of FTP’s

- In extreme conditions (all 855 tills have transaction every 3 mins) we need to take 87mins to handle one batch data uploading, which means we need 9 oss nodes.

- Considering about the real business, we propose to have oss main, N1 and N2 for whole CN.



## 相關資訊

- **Jira:** [BE-1001](https://ctil.atlassian.net/browse/BE-1001)
- **解決方式:** Done