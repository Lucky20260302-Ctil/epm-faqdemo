---
project: FE
title: "FE-1383: [CS-939] day end issue caused by dbhist too large"
issue_key: FE-1383
issue_type: Bug PRD
status: Closed
faq_score: 7.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, fe, performance_timeout, day-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1383"
created: 2024-05-09
resolved: 2024-05-24
resolution: Done
has_images: False
---

# FE-1383: [CS-939] day end issue caused by dbhist too large

## 問題描述

After issue sales memo, FE will insert record in jouprint table.

Since the table will not purge, the size of dbhist.sdf is increased. Then cause day end issue.

Program will change:

>> Clear dbhist.sdf 's  jouprint table while day end 



## 相關資訊

- **Jira:** [FE-1383](https://ctil.atlassian.net/browse/FE-1383)
- **解決方式:** Done
- **標籤:** coach75