---
project: WEB
title: "WEB-332: Remove 1st and 2nd page in new customer creation flow"
issue_key: WEB-332
issue_type: Improvement
status: Closed
faq_score: 8.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, web, performance_timeout, ename]
jira_url: "https://ctil.atlassian.net/browse/WEB-332"
created: 2023-07-20
resolved: 2023-07-20
resolution: Done
has_images: False
---

# WEB-332: Remove 1st and 2nd page in new customer creation flow

## 問題描述

eName Program [ 3ca7665 / 8092e65 ]

- Remove 1st page & 2nd (QR code) page in new member creation flow.

- (After change) Total User click(s) before Enter Input Page: 1 click

- Program change to disable 1st page.

- Config change to disable 2nd page.

- Program Enhance on Log Handling

- Some logging function in API is not a ASYNC task >> may amplify problem when heavy API loading

- Program enhance for change logging function as ASYNC task.

- Enable Trace log for case investigation.

- Program Enhance on Connection String configuration.

- Program load the connection string for data insert for different region access >> may significantly affect the performance.

- Program enhance to load the connection string into cache.



## 相關資訊

- **Jira:** [WEB-332](https://ctil.atlassian.net/browse/WEB-332)
- **解決方式:** Done