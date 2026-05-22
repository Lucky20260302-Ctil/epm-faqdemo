---
project: BE
issue_key: BE-827
issue_type: Bug DEV
status: Closed
tags:
- 04_data_sync
- be
- data-interface
- data_sync
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-827
created: '2023-11-01'
resolved: '2023-11-10'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-827: bug fix EnterpriseSystemAPI StockAdjustment overwrite the origin value by accident'
---
# BE-827: bug fix EnterpriseSystemAPI StockAdjustment overwrite the origin value by accident

## 問題描述

incorrect:

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7c7a2b39-cbf1-4e42-a1a1-9804027ed618)（需 Jira 登入）
 

correct:

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ff482ede-7cc6-452e-b06a-6f75f0e26f73)（需 Jira 登入）
 



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7c7a2b39-cbf1-4e42-a1a1-9804027ed618)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ff482ede-7cc6-452e-b06a-6f75f0e26f73)


## Jira Comments

> **Sherman tse** (2023-11-01):
> Verified on QA env 

> **Sherman tse** (2023-11-10):
> Verified on UAT env

## 相關資訊

- **Jira:** [BE-827](https://ctil.atlassian.net/browse/BE-827)
- **解決方式:** Done