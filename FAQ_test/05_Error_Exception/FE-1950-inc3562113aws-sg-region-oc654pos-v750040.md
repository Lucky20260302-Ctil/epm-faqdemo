---
project: FE
issue_key: FE-1950
issue_type: Bug DEV
status: Open
tags:
- 05_error_exception
- error_exception
- faq
- fe
- front-end-v750.01r01a
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1950
created: '2026-05-13'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1950: [INC3562113]AWS SG region, OC654,pos v75.004.0702.0000, search all member show: This Member Card is expired'
---
# FE-1950: [INC3562113]AWS SG region, OC654,pos v75.004.0702.0000, search all member show: This Member Card is expired

## 問題描述

[INC3562113]AWS SG region, OC654,pos v75.004.0702.0000, search all member show: This Member Card is expired

compared with OC595till0 by member code OC552XS00002558

OC595 can search normally, but OC654 shew error

> 📎 **OC552XS00002558_OC654.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/080336b5-348b-4257-a54e-4cac1361f762)（需 Jira 登入）

> 📎 **OC552XS00002558_OC5950.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9aa804b9-2465-498a-bc04-47e1b553b2ee)（需 Jira 登入）
Checked wa.log, no wa.log found after 8th May.

dbtrans.sdf and dbtbk07.sdf from OC654 has been attached

dbtrans.sdf from OC595till has been attached



## 附件截圖

1. 📎 **OC552XS00002558_OC654.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/080336b5-348b-4257-a54e-4cac1361f762)
2. 📎 **OC552XS00002558_OC5950.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9aa804b9-2465-498a-bc04-47e1b553b2ee)

## 相關資訊

- **Jira:** [FE-1950](https://ctil.atlassian.net/browse/FE-1950)