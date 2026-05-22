---
project: BE
issue_key: BE-988
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- be
- error_exception
- faq
- polling
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-988
created: '2025-01-16'
resolved: '2025-02-21'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-988: [CS-1323] - 01-15 9 CN V75 pilot store can''t upload ACP data file to BE- RIN01442452'
---
# BE-988: [CS-1323] - 01-15 9 CN V75 pilot store can't upload ACP data file to BE- RIN01442452

## 問題描述

SOG call out 01-15 CN pilot store can’t upload sales to BE.

troubleshooting:

1.Check cs2kconnect.ini config is correct.cs2k log NOT have error and can normal find ACP data file.

2.Check sqlpcdossa & sqlpcdossb table,Just only find OC185,OC182,OC270 3 store’s acp file upload to BE.

> 📎 **image-20250116-010553.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/25cbca6e-d5d9-4fea-9079-73343b23fcff)（需 Jira 登入）
3.Check polling log also NOT have error and can find OC185 ACP file.



## 附件截圖

1. 📎 **image-20250116-010553.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/25cbca6e-d5d9-4fea-9079-73343b23fcff)

## 相關資訊

- **Jira:** [BE-988](https://ctil.atlassian.net/browse/BE-988)
- **解決方式:** Done