---
project: FE
issue_key: FE-1390
issue_type: Bug QA
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1390
created: '2024-05-16'
resolved: '2024-06-12'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1390: HKJC burn points should not allow decimals'
---
# FE-1390: HKJC burn points should not allow decimals

## 問題描述

When inputting amount for burn points, the lowest value should be 1, but currently the system allows decimal:

> 📎 **image-20240516-092229.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/06dfb621-1831-4361-a820-6c261e9303c0)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20240516-092229.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/06dfb621-1831-4361-a820-6c261e9303c0)


## Jira Comments

> **Andy Ko** (2024-05-21):
>  I tested inputting 1.50 for BP amount , and it rounded to 2. Is this based on the rounding flag in config?

> **Sang** (2024-05-23):
> Burn Point not accept decimal, auto round down to dollar  (KTS 240516 Jira FE-1390 v750.01R02A)

## 相關資訊

- **Jira:** [FE-1390](https://ctil.atlassian.net/browse/FE-1390)
- **解決方式:** Done