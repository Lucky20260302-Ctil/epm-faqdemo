---
project: FE
issue_key: FE-1342
issue_type: Bug QA
status: Closed
faq_score: 6.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, fe, performance_timeout, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1342"
created: 2024-02-15
resolved: 2024-02-19
resolution: Done
has_images: True
---

# FE-1342: [Lands] Add a number of items & fill in ref no/ additional no., then pos pop up restart message

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 6.5
> **解決日期:** 2024-02-19
> **負責人:** Sang
> **組件:** Front End

## 問題描述

Reproduce steps:

1. Add items over 10 until scroll bar appear

2. Insert Ref no . & external ref. for an item

3. Scroll the item list

 

Existing result:

Your POS ran into a problem and need to restart. We’re just collecting some error info & pos would keep loading

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e76c5a69-c7d3-4455-bfdc-9e2bc1cd3d15)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e76c5a69-c7d3-4455-bfdc-9e2bc1cd3d15)

## 相關資訊

- **Jira:** [FE-1342](https://ctil.atlassian.net/browse/FE-1342)
- **解決方式:** Done