---
project: BE
issue_key: BE-680
issue_type: Bug QA
status: Closed
faq_score: 5.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-680"
created: 2022-11-08
resolved: 2023-02-21
resolution: Done
has_images: False
---

# BE-680: Position of Aging code field is incorrect

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 5.0
> **解決日期:** 2023-02-21
> **負責人:** Ken Lam
> **組件:** Backend (Web)

## 問題描述

Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)

Location: 

Secondary > optional > Aging table maintenance (MF5008)

Existing result:

Field of inserting Aging code placed at incorrect position (under from date/ to date)

Expected result:

Field of inserting Aging code should be placed at first row (Ref: image-2022-11-08-13-50-45-890.png)



## 相關資訊

- **Jira:** [BE-680](https://ctil.atlassian.net/browse/BE-680)
- **解決方式:** Done