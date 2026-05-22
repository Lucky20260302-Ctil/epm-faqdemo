---
project: FE
issue_key: FE-1047
issue_type: Bug PRD
status: Closed
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, msmq]
jira_url: "https://ctil.atlassian.net/browse/FE-1047"
created: 2021-12-29
resolved: 2022-08-18
resolution: Done
has_images: False
---

# FE-1047: MSMQ recovery steps for DB and APP server connection fail

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.5
> **解決日期:** 2022-08-18
> **負責人:** Terence Tsang
> **組件:** MSMQ

## 問題描述

when DB sever and APP server connection fail, the pcd files will be write in MSMQ program folder. 

>> Need to handle auto re-post 

>> Log for such case.



## 相關資訊

- **Jira:** [FE-1047](https://ctil.atlassian.net/browse/FE-1047)
- **解決方式:** Done