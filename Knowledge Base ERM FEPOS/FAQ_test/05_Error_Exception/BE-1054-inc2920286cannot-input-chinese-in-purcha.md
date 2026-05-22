---
project: BE
issue_key: BE-1054
issue_type: Bug DEV
status: Closed
faq_score: 5.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, frontend]
jira_url: "https://ctil.atlassian.net/browse/BE-1054"
created: 2025-04-22
resolved: 2025-06-05
resolution: Done
has_images: True
---

# BE-1054: [INC2920286]cannot input Chinese in purchase-bank info

> **類型:** Bug DEV | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 5.0
> **解決日期:** 2025-06-05
> **負責人:** Sang
> **組件:** Frontend

## 問題描述

PRC POSv75,银行信息界面，持卡人姓名一栏，无法输入中文，强制锁定英文输入。只能将中文复制到持卡人姓名一栏。（这个问题在测试机上也可以重现）

在V72中银行卡-持卡人姓名一栏是可以输入中文的。

> 📎 **持卡人1.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/06f21455-04b7-4fab-bdef-77f74e1aab12)（需 Jira 登入）

> 📎 **持卡人2.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/83f75dcf-4f37-4d5f-89e1-f3efa5312d45)（需 Jira 登入）


## 附件截圖

1. 📎 **持卡人1.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/06f21455-04b7-4fab-bdef-77f74e1aab12)
2. 📎 **持卡人2.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/83f75dcf-4f37-4d5f-89e1-f3efa5312d45)

## 相關資訊

- **Jira:** [BE-1054](https://ctil.atlassian.net/browse/BE-1054)
- **解決方式:** Done