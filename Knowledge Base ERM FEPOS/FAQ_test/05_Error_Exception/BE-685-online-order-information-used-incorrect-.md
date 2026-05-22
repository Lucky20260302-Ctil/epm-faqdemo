---
project: BE
issue_key: BE-685
issue_type: Bug QA
status: Closed
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-685"
created: 2022-11-09
resolved: 2023-02-21
resolution: Done
has_images: False
---

# BE-685: Online Order Information used incorrect word limitation for member no. field

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.5
> **解決日期:** 2023-02-21
> **負責人:** Ken Lam
> **組件:** Backend (Web)

## 問題描述

Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)

Location: Online Order Information (OR0001)

Reproduce steps:

1. To Online Order Information

2. Click on Create

3. Click on "..." of  Member no. field

4. Select one of the member no. that are over 10 words

Existing result:

Field of Member no. rounded by red outline, if I click save, it will pop up an error that has word limiatation (Ref: screenshot-1.png)

 



## 相關資訊

- **Jira:** [BE-685](https://ctil.atlassian.net/browse/BE-685)
- **解決方式:** Done