---
project: FE
issue_key: FE-1692
issue_type: Bug DEV
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- fe
- front-end-v720.02
- front-end-v750.01r01a
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1692
created: '2025-05-12'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1692: [INC2936715]Till0 receipt 00053075 can''t be printed fully'
---
# FE-1692: [INC2936715]Till0 receipt 00053075 can't be printed fully

## 問題描述

[INC2936715]Till0 receipt 00053075 can't be printed fully.

正常应打出顾客联*1+店铺联*1且均有完整条码。但till0会时而出现问题，只会打出一张顾客联且无完整条码。

00053075 is incorrect,20006500 is correct:

> 📎 **20006500.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/2c08e1d8-ed35-4c2c-961e-fec0f842fa01)（需 Jira 登入）

> 📎 **00053075.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/3a1e252f-7c4c-4be0-a4ca-3028c393d910)（需 Jira 登入）
checked in T9, has error report while printing:

> 📎 **1111.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/383df1fc-b84d-45bf-90b8-14f5581b571b)（需 Jira 登入）
compare with till2, no related config find

> 📎 **compare2.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ed2b8d76-83a7-477e-b75b-4ac4519e143c)（需 Jira 登入）

> 📎 **compare1.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/88477c99-cb71-4e77-8730-cb2087113792)（需 Jira 登入）

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ac4c511a-4140-4e8c-9914-eb98aa5737d4)（需 Jira 登入）



## 附件截圖

1. 📎 **20006500.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/2c08e1d8-ed35-4c2c-961e-fec0f842fa01)
2. 📎 **00053075.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/3a1e252f-7c4c-4be0-a4ca-3028c393d910)
3. 📎 **1111.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/383df1fc-b84d-45bf-90b8-14f5581b571b)
4. 📎 **compare2.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ed2b8d76-83a7-477e-b75b-4ac4519e143c)
5. 📎 **compare1.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/88477c99-cb71-4e77-8730-cb2087113792)
6. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ac4c511a-4140-4e8c-9914-eb98aa5737d4)

## 相關資訊

- **Jira:** [FE-1692](https://ctil.atlassian.net/browse/FE-1692)