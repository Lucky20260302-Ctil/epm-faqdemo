---
project: BE
issue_key: BE-516
issue_type: Bug PRD
status: Closed
faq_score: 7.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-516"
created: 2021-08-24
resolved: 2021-08-24
resolution: Done
has_images: False
---

# BE-516: Polling program --- Error “ETX file not found”

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 7.5
> **解決日期:** 2021-08-24
> **負責人:** Joy Li
> **組件:** Backend (ChainStorePlus 7.0)

## 問題描述

- Polling program — Error “ETX file not found”

- From daily support case, we found that there are some sales memo is missing in BE. After checking, we found that those file are missing because polling task is processing before acp file is uploaded. Therefore, polling task will return “ETX file not found”. Program is changed to process the file if STX and ETX is uploaded.

- Difficult to reproduce in QA.



## 相關資訊

- **Jira:** [BE-516](https://ctil.atlassian.net/browse/BE-516)
- **解決方式:** Done