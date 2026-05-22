---
project: FE
issue_key: FE-1879
issue_type: Bug PRD
status: HOLD
tags:
- 03_performance_timeout
- faq
- fe
- front-end
- performance_timeout
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1879
created: '2026-02-05'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'FE-1879: [CS-2135][INC3430754]KSN237 Store said the till 1 & 2 also the new log update symbol there but after clicked it showing error “Execute.Error: Object reference not set to an instance of
  an object.”'
---
# FE-1879: [CS-2135][INC3430754]KSN237 Store said the till 1 & 2 also the new log update symbol there but after clicked it showing error “Execute.Error: Object reference not set to an instance of an object.”

## 問題描述

Trouble shotting:

1.Repaired cs2k program,issue still.

2.Checked T9 log found so many same error:

[20260205 16:35:16 -4755]: CheckNewLog - Start : Avail V.  Memory : 140731731.927
[20260205 16:35:16 -5014]: CheckNewLog - End True : Avail V.  Memory : 140731731.927
[20260205 16:35:19 -5921]: Unhanded Exception.Error: Object reference not set to an instance of an object.

> 📎 **image-20260205-083802.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/78004e85-3639-412d-8d22-f86332405531)（需 Jira 登入）

KSN237 till1 vedio:

> 📎 **video.mp4** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/201ea7f3-09a1-4f53-978c-597c8c70ad27)（需 Jira 登入）
 FE logs for your further checking:

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/f9ccc979-dd8f-49b7-8e55-0f6dbc3c5224)（需 Jira 登入）



## 附件截圖

1. 📎 **image-20260205-083802.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/78004e85-3639-412d-8d22-f86332405531)
2. 📎 **video.mp4** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/201ea7f3-09a1-4f53-978c-597c8c70ad27)
3. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/f9ccc979-dd8f-49b7-8e55-0f6dbc3c5224)

## 相關資訊

- **Jira:** [FE-1879](https://ctil.atlassian.net/browse/FE-1879)