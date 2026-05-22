---
project: BE
issue_key: BE-681
issue_type: Bug QA
status: Closed
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-681"
created: 2022-11-08
resolved: 2023-02-16
resolution: Done
has_images: False
---

# BE-681: Cannot display other possible options after click "X" in Selection list of specific data

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.5
> **解決日期:** 2023-02-16
> **負責人:** Ken Lam
> **組件:** Backend (Web)

## 問題描述

Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)

Location: Selection list of specific data

e.g.: Payment Type Code Maintenance (MF0009)

Reproduce steps:

1. To Payment Type Code Maintenance (MF0009)

2. Click Create

3. Click "..." for location selection

4. Select "P02"

5. Click "..." again for location selection

6. Click "X" in Location code>=

Existing result:

Cannot display other possible options e.g.: display option P01

(Ref: ChainStorePlus _ 99 - ERM Company 99 - Google Chrome 2022-11-08 15-11-52)

 

Remark: Other tabs seems also have same issue



## 相關資訊

- **Jira:** [BE-681](https://ctil.atlassian.net/browse/BE-681)
- **解決方式:** Done