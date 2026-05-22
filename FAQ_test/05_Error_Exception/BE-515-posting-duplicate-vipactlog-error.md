---
project: BE
issue_key: BE-515
issue_type: Bug PRD
status: Closed
faq_score: 7.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-515"
created: 2021-08-18
resolved: 2021-08-24
resolution: Done
has_images: False
---

# BE-515: Posting - duplicate vipactlog error

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.5
> **解決日期:** 2021-08-24
> **負責人:** Joy Li
> **組件:** Backend (ChainStorePlus 7.0)

## 問題描述

- Posting program — Error “Cannot insert duplicate key in object vipactlog”

- The issue is caused by the new member records were creating at this same time in different posting nodes.

- Difficult to reproduce in QA.



## 相關資訊

- **Jira:** [BE-515](https://ctil.atlassian.net/browse/BE-515)
- **解決方式:** Done