---
project: BE
issue_key: BE-692
issue_type: Bug QA
status: Closed
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-692"
created: 2022-11-11
resolved: 2023-02-16
resolution: Done
has_images: False
---

# BE-692: Pop api error after click Save in On Sale Price Maintenance - Page Mode (MF2003)

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.5
> **解決日期:** 2023-02-16
> **負責人:** Ken Lam
> **組件:** Backend (Web)

## 問題描述

Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)

Location: On Sale Price Maintenance - Page Mode (MF2003)

Reproduce step:

1. To On Sale Price Maintenance - Page Mode (MF2003)

2. Click Create

3. Click Save directly (no need to insert other details)

Existing result:

Pop api error after click Save

Save failed : Object reference not set to an instance of an object.



## 相關資訊

- **Jira:** [BE-692](https://ctil.atlassian.net/browse/BE-692)
- **解決方式:** Done