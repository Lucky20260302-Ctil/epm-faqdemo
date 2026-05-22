---
project: FE
issue_key: FE-1268
issue_type: Bug QA
status: Closed
faq_score: 7.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, fe, performance_timeout, front-end-v760.02]
jira_url: "https://ctil.atlassian.net/browse/FE-1268"
created: 2023-06-16
resolved: 2023-07-27
resolution: Done
has_images: True
---

# FE-1268: [Lands] Cannot update correct price in real time when GOV member change as Public status

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 7.5
> **解決日期:** 2023-07-27
> **負責人:** Sang
> **組件:** front end v760.02

## 問題描述

Reproduce steps:

1. Add items into sales memo page

2. Apply a GOV member (GOV00002)

3. Remove the applied GOV member

Existing result:

Price displayed in sales memo page cannot update as Public price timely

Remark:

VM: 172.16.138.111   /   P@ssw0rd@09

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d0616252-7fcf-436d-9d1c-7282442b3531)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d0616252-7fcf-436d-9d1c-7282442b3531)

## 相關資訊

- **Jira:** [FE-1268](https://ctil.atlassian.net/browse/FE-1268)
- **解決方式:** Done