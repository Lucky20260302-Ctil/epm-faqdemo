---
project: FE
issue_key: FE-1033
issue_type: Bug PRD
status: Closed
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1033"
created: 2021-11-26
resolved: 2021-12-03
resolution: Done
has_images: False
---

# FE-1033: [RIN00888608][Coach CJ] FE checking for Invalid salesperson format 'AA'

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.5
> **解決日期:** 2021-12-03
> **負責人:** Sang
> **組件:** Front End

## 問題描述

Coach CJ reported invalid salesperson ‘AA’ / ‘aa’ with different format. It is failed to post sales memo due to this reason.

Normally, Coach CJ user will input salesperson code during sales memo creation. They may use another typing method.

 

Per discussion, please try reproduce scenario and apply checking on value of salesperson code. Thank you.

 



## 相關資訊

- **Jira:** [FE-1033](https://ctil.atlassian.net/browse/FE-1033)
- **解決方式:** Done