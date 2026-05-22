---
project: FE
issue_key: FE-1383
issue_type: Bug PRD
status: Closed
tags:
- 03_performance_timeout
- day-end
- faq
- fe
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1383
created: '2024-05-09'
resolved: '2024-05-24'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'FE-1383: [CS-939] day end issue caused by dbhist too large'
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