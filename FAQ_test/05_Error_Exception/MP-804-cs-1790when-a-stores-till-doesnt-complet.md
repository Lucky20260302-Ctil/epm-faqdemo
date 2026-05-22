---
project: MP
issue_key: MP-804
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, mp, error_exception, frontend]
jira_url: "https://ctil.atlassian.net/browse/MP-804"
created: 2025-10-22
resolved: 
resolution: 
has_images: True
---

# MP-804: [CS-1790]When a store's Till doesn't complete Dayend, there is no prompt on Till 0

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.0
> **負責人:** Tovi Wang
> **組件:** Frontend

## 問題描述

Symptom:
When a store's Till doesn't complete Dayend, there is no prompt on Till 0

Troubleshooting:
When upgrading to V75 in the Outlet store, it was found that when the dayend of a certain till is not completed, there will be no prompt on Tile 0 indicating that the till has not completed its dayend.
The store will only discover the missing sales of a certain till when it needs to complete the total dayend of Tile 0 and print the total dayend report.
Attached is the error prompting missing data from certain sub-till, but no message will show up in v75 POS.

As per suggestion from sanyo team, please create JIRA ticket for checking. Thanks!

若店铺某台Till没有完成或者是某台Till完成日结，但该Till的数据没有反映到Till0的这两种情况下，V72版本无论在那种情况Till0提示该Till没有完成日结（如下方V72截图一样）。
但outlet升级到V75后上述的两种情况，均没有出现如V72一样的提示。店铺需要在完成日结后，才会发现某台Till的销售没有在总日结报告上。

> 📎 **image-20251022-020516.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/8ff96664-06db-42a1-8f18-b7e6d3bf2e43)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20251022-020516.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/8ff96664-06db-42a1-8f18-b7e6d3bf2e43)

## 相關資訊

- **Jira:** [MP-804](https://ctil.atlassian.net/browse/MP-804)