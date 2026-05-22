---
project: BE
issue_key: BE-1031
issue_type: Improvement
status: Closed
faq_score: 5.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, api]
jira_url: "https://ctil.atlassian.net/browse/BE-1031"
created: 2025-03-19
resolved: 2025-05-02
resolution: Done
has_images: False
---

# BE-1031: [ACU-121][Acxion]Do not repeat call for 3 times when receive 400 error from CRM 

> **類型:** Improvement | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 5.0
> **解決日期:** 2025-05-02
> **負責人:** Anson Cheung
> **組件:** API

## 問題描述

Check whether current program will repeat call for 3 times if there is return error from CRM API:

1. If there is no response from API call, then try for 3 times.

2. If there is error return from API, program should not call API again.

HTTPStatusCode : 400,404, 500 no need to trigger the retry



## 相關資訊

- **Jira:** [BE-1031](https://ctil.atlassian.net/browse/BE-1031)
- **解決方式:** Done