---
project: MP
issue_key: MP-811
issue_type: Bug QA
status: Test in Progress
tags:
- 05_error_exception
- error_exception
- faq
- mp
- mpos
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-811
created: '2026-02-12'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'MP-811: [ANZ] Insert value in Update_TimeStamp column for [dbTrans].[dbo].[NEW VIP]'
---
# MP-811: [ANZ] Insert value in Update_TimeStamp column for [dbTrans].[dbo].[NEW VIP]

## 問題描述

MPOS write new Member information to dbtrans.[New Vip] table have not update mandatory update_timestamp field, as POS help to execute upsert action for MPOS determinated by the update_timestamp field.

> 📎 **image-20260212-042327.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7207c0f7-3ffc-4901-8132-675346688cae)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260212-042327.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7207c0f7-3ffc-4901-8132-675346688cae)

## 相關資訊

- **Jira:** [MP-811](https://ctil.atlassian.net/browse/MP-811)