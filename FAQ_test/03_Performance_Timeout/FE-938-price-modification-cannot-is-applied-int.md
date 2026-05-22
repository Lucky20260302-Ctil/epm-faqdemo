---
project: FE
issue_key: FE-938
issue_type: Bug PRD
status: Closed
tags:
- 03_performance_timeout
- faq
- fe
- front-end
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-938
created: '2021-03-19'
resolved: '2022-08-18'
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'FE-938: Price Modification cannot is applied into item with negative quantity (sales return)'
---
# FE-938: Price Modification cannot is applied into item with negative quantity (sales return)

## 問題描述

AH1S-TILL0
172.16.199.243,40000

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/415658b7-83a4-4e86-8c2b-f52874183b4d)（需 Jira 登入）
When get return item price without memo no., sales memo will not found or cannot found any valid price from history, current price will be use.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9c8e2b2d-25f4-4791-b5ce-add57a0e21d3)（需 Jira 登入）
If Shift +F1 to change price, it will display following message.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/8625d2dc-f5d3-444f-bdad-f9b206cbd725)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/415658b7-83a4-4e86-8c2b-f52874183b4d)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9c8e2b2d-25f4-4791-b5ce-add57a0e21d3)
3. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/8625d2dc-f5d3-444f-bdad-f9b206cbd725)

## 相關資訊

- **Jira:** [FE-938](https://ctil.atlassian.net/browse/FE-938)
- **解決方式:** Done