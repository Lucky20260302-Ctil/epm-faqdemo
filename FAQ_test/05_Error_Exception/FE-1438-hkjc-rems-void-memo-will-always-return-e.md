---
project: FE
issue_key: FE-1438
issue_type: Bug QA
status: Closed
faq_score: 7.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1438"
created: 2024-06-27
resolved: 2024-07-09
resolution: Done
has_images: True
---

# FE-1438: [HKJC] REMS void memo will always return error message even though API returned sucess

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.5
> **解決日期:** 2024-07-09
> **負責人:** Sang
> **組件:** Front End

## 問題描述

After voiding a transaction that has PP pay code (burn points), then the void transaction will return a failure message, even though the API returned a success. It is blocking our system from completing the void transaction.

> 📎 **Untitled.jpg** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a00a16ce-8cff-4a58-8865-669fcf608dd6)（需 Jira 登入）


## 附件截圖

1. 📎 **Untitled.jpg** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a00a16ce-8cff-4a58-8865-669fcf608dd6)

## 相關資訊

- **Jira:** [FE-1438](https://ctil.atlassian.net/browse/FE-1438)
- **解決方式:** Done