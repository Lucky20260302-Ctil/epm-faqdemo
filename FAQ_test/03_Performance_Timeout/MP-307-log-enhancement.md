---
project: MP
title: "MP-307: Log Enhancement"
issue_key: MP-307
issue_type: Bug QA
status: Closed
faq_score: 6.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, mp, performance_timeout, mpos-api]
jira_url: "https://ctil.atlassian.net/browse/MP-307"
created: 2020-11-10
resolved: 2021-07-20
resolution: Done
has_images: False
---

# MP-307: Log Enhancement

## 問題描述

Using IO Async to improve logging performance.

Some machine contain IO issue such as some low end machine and poor resource VM.

Use IO Async to improve this poor logging performance.

Known Issue:

Some time log is not in ascending order but we have time stamp for each log record.

 



## 相關資訊

- **Jira:** [MP-307](https://ctil.atlassian.net/browse/MP-307)
- **解決方式:** Done