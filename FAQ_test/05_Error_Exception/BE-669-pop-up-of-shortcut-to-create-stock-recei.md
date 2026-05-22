---
project: BE
issue_key: BE-669
issue_type: Bug QA
status: Closed
faq_score: 5.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-669"
created: 2022-11-04
resolved: 2024-04-27
resolution: Done
has_images: False
---

# BE-669: Pop up of shortcut to create stock receive (rc2000) still existing after click OK in Unauthorized Access  

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 5.0
> **解決日期:** 2024-04-27
> **負責人:** Jerry Wong
> **組件:** Backend (Web)

## 問題描述

Env: [https://172.16.138.101/chainstoreplus/rc2000](https://172.16.138.101/chainstoreplus/rc2000)

ACC: P01      PW: P01

Reproduce steps:

1. Enter into Stock Receive input against PO/DRV (rc2000)

2. Click OK in Unauthorized Access

Existing result:

Pop up of shortcut to create stock receive (rc2000) is  still existing in home page (Ref: image-2022-11-04-11-06-11-167.png)



## 相關資訊

- **Jira:** [BE-669](https://ctil.atlassian.net/browse/BE-669)
- **解決方式:** Done