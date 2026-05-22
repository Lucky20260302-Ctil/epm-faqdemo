---
project: FE
issue_key: FE-1628
issue_type: Bug PRD
status: Closed
tags:
- 03_performance_timeout
- backend
- faq
- fe
- performance_timeout
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1628
created: '2025-02-19'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'FE-1628: CN Epromo 邮件approve失败'
---
# FE-1628: CN Epromo 邮件approve失败

## 問題描述

中国以下五个coupon遇到了无法邮件approve的问题。

COACHXY200

COACHXY300

COACHXY400

COACHXY500

COACHXY600

1.从DB看，Retail 这边（Caroline Zhang ）已经批了，现在等待Finance的批复。

> 📎 **image-20250219-123427.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/f990d3f1-cb7d-4770-9375-244da79183b7)（需 Jira 登入）

> 📎 **image-20250219-123502.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/556f02ef-d248-4f1b-87e4-8b68476b1e38)（需 Jira 登入）
2.但是昨天Finance确认已经通过邮件批复，且能找到对应发出的邮件。

> 📎 **image-20250219-123624.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a81d4cf5-ce0a-4540-9808-27bb9d2a11b7)（需 Jira 登入）
请帮忙查一下原因并修复这五个coupon。



## 附件截圖

1. 📎 **image-20250219-123427.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/f990d3f1-cb7d-4770-9375-244da79183b7)
2. 📎 **image-20250219-123502.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/556f02ef-d248-4f1b-87e4-8b68476b1e38)
3. 📎 **image-20250219-123624.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a81d4cf5-ce0a-4540-9808-27bb9d2a11b7)

## 相關資訊

- **Jira:** [FE-1628](https://ctil.atlassian.net/browse/FE-1628)