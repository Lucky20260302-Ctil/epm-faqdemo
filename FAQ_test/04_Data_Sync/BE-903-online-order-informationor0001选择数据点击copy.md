---
project: BE
issue_key: BE-903
issue_type: Bug QA
status: Closed
faq_score: 6.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-903"
created: 2024-09-13
resolved: 2025-02-21
resolution: Done
has_images: True
---

# BE-903: Online Order Information(OR0001):选择数据点击Copy时，Order No,仍然能够输入数据，保存后，Order No.里输入的数据被强制更改

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 6.0
> **解決日期:** 2025-02-21
> **負責人:** ryan
> **組件:** Backend (Web)

## 問題描述

1、选择Order No.为‘‘00000001’’，click copy

2、在Order No.输入‘‘Q1’’

3、click Save button，

4、Order No.输入的Q1，被强制更改了

> 📎 **image-20240913-091924.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/fc084f12-42e8-4032-8249-0b71522c0d90)（需 Jira 登入）

> 📎 **image-20240913-092025.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/cf36636c-4bad-4dc6-bf47-3826252457cb)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20240913-091924.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/fc084f12-42e8-4032-8249-0b71522c0d90)
2. 📎 **image-20240913-092025.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/cf36636c-4bad-4dc6-bf47-3826252457cb)

## 相關資訊

- **Jira:** [BE-903](https://ctil.atlassian.net/browse/BE-903)
- **解決方式:** Done