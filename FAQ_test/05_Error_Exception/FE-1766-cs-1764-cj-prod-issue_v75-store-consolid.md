---
project: FE
issue_key: FE-1766
issue_type: Bug PRD
status: Closed
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1766"
created: 2025-10-03
resolved: 2025-10-16
resolution: Done
has_images: False
---

# FE-1766: [CS-1764] CJ Prod issue_V7.5 store consolidated dayend missing sub till data

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.5
> **解決日期:** 2025-10-16
> **負責人:** Sherman tse
> **組件:** Front End

## 問題描述

related SOG ticket:

INC3224817 (store: J841, missing date: 9/29-9/30 of Till 2)

INC3224738  (store: J724, missing date: 9/29-9/30 of Till 2)

INC3223640  (store: J721, missing date: 9/29-9/30 of Till 2 & 3)

INC3229180  (store: J853, missing date: 10/2 of Till 2)

Symptom:

Till 2 sales data cannot reflected on consolidation dayend report

Tested by Joy (use 29/9 as example):

1. re-do dayend consolidation → still missing Till 2 sales data on the report

2. rename dbtbk29. sdf and re-do dayend consolidation → still missing Till 2 sales data on the report

3. copy dbtbk29.sdf manually from Till 2 to Till 0 and re-do dayend consolidation → Till 2 sales data can be reflected on consolidation dayend report, also worked for 30/9



## 相關資訊

- **Jira:** [FE-1766](https://ctil.atlassian.net/browse/FE-1766)
- **解決方式:** Done