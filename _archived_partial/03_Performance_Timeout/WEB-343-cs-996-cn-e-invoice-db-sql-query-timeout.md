---
project: WEB
issue_key: WEB-343
issue_type: Bug PRD
status: Closed
tags:
- 03_performance_timeout
- faq
- interface
- performance_timeout
- web
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/WEB-343
created: '2024-04-25'
resolved: '2024-04-25'
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'WEB-343: CS-996: CN E-invoice DB SQL Query timeout checking'
---
# WEB-343: CS-996: CN E-invoice DB SQL Query timeout checking

## 問題描述

Previously, it is null for joueinv_confirm_state, joueinv_red_confirm_uuid,joueinv_org_memo_no.

now it is blank, please kindly check whether there is program logic change.

and change it as the same logic. 

> 📎 **image-20240425-073308.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ee2aee37-424e-45bd-9d12-82bf6278a1d5)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20240425-073308.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ee2aee37-424e-45bd-9d12-82bf6278a1d5)

## 相關資訊

- **Jira:** [WEB-343](https://ctil.atlassian.net/browse/WEB-343)
- **解決方式:** Done
- **標籤:** 2024