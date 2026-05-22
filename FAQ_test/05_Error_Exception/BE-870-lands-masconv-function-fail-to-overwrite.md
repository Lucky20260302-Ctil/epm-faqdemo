---
project: BE
issue_key: BE-870
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- backend-(chainstoreplus-7.0)
- be
- error_exception
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-870
created: '2024-07-09'
resolved: '2024-07-10'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-870: [Lands] Masconv function fail to overwrite encrypted masconv'
---
# BE-870: [Lands] Masconv function fail to overwrite encrypted masconv

## 問題描述

[Lands] Masconv function fail to overwrite encrypted masconv

Reproduce steps:

1. Execute Masconv to export encrypted Masconv file

2. Execute Masconv again to overwrite encrypted Masconv file

Existing result:

Got stuck in Item Master during Masconv

> 📎 **image-20240709-061102.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/635fe286-126e-4ed6-a50c-9700b67b100a)（需 Jira 登入）
I tried to close the Export POS master data & execute again, it will pop up an error:

> 📎 **image-20240709-061309.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/539c9449-1bd4-4e5b-9111-cdae9057d6c7)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20240709-061102.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/635fe286-126e-4ed6-a50c-9700b67b100a)
2. 📎 **image-20240709-061309.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/539c9449-1bd4-4e5b-9111-cdae9057d6c7)

## 相關資訊

- **Jira:** [BE-870](https://ctil.atlassian.net/browse/BE-870)
- **解決方式:** Done