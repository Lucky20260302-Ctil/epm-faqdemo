---
project: BE
issue_key: BE-506
issue_type: Bug PRD
status: Closed
faq_score: 9.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-506"
created: 2021-07-27
resolved: 2021-07-27
resolution: Done
has_images: False
---

# BE-506: member sync program update

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 9.5
> **解決日期:** 2021-07-27
> **負責人:** Joy Li
> **組件:** Backend (ChainStorePlus 7.0)

## 問題描述

APP Server Program Change

- Update member sync relative program (prj_cr4002.dll)

- Enhance program to avoid record total loss when SQL select timeout

- Unable to reproduce

- Enhance program to handle large amount vip data sync

- The SQL selection will process in piece to avoid JOB Server memory lack.



## 相關資訊

- **Jira:** [BE-506](https://ctil.atlassian.net/browse/BE-506)
- **解決方式:** Done