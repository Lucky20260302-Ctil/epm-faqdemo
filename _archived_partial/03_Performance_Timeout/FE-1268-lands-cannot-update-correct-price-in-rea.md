---
project: FE
issue_key: FE-1268
issue_type: Bug QA
status: Closed
tags:
- 03_performance_timeout
- faq
- fe
- front-end-v760.02
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1268
created: '2023-06-16'
resolved: '2023-07-27'
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'FE-1268: [Lands] Cannot update correct price in real time when GOV member change as Public status'
---
# FE-1268: [Lands] Cannot update correct price in real time when GOV member change as Public status

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