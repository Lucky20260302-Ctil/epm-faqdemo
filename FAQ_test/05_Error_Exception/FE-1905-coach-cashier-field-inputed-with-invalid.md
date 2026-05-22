---
project: FE
title: "FE-1905: [Coach] Cashier Field inputed with invalid sales lady ID can still pass to payment section"
issue_key: FE-1905
issue_type: Bug QA
status: Closed
faq_score: 7.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1905"
created: 2026-03-24
resolved: 2026-03-24
resolution: Done
has_images: True
---

# FE-1905: [Coach] Cashier Field inputed with invalid sales lady ID can still pass to payment section

## 問題描述

[Coach] Cashier Field inputed with invalid sales lady ID can still pass to payment section

Reproduce steps:

1. To POS

2. Input valid ID to fields of Sales Staff & Cashier

3. Add an item & stay at this status

4. To local DB > dbMas sse > TblSalady

5. Edit the salady_code that inputed in the Cashier field e.g.: origanal 20522 to 205199

6. back to POS, Click on Pay

Existing result:

Still able to process to payment section

Expected result:

Should have a checking for sales staff ID, 

- If invalid, Pop up Invalid sales staff ID, and stay in the current page

- If sales staff ID is valid, process to Payment page

> 📎 **image-20260324-020902.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/b41f8563-2acc-4efd-a766-682addf2ac2f)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260324-020902.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/b41f8563-2acc-4efd-a766-682addf2ac2f)

## 相關資訊

- **Jira:** [FE-1905](https://ctil.atlassian.net/browse/FE-1905)
- **解決方式:** Done