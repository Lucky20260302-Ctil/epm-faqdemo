---
project: FE
issue_key: FE-1870
issue_type: Task
status: Re Open
tags:
- 05_error_exception
- error_exception
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1870
created: '2026-01-28'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1870: [CS-2024] Issue_ANZ_INC3405075_Search with Name but fail. (C360 use first name / last name)'
---
# FE-1870: [CS-2024] Issue_ANZ_INC3405075_Search with Name but fail. (C360 use first name / last name)

## 問題描述

In FE POS, only have Member Name, not have first name / last name.
When searching member info by Name, POS request body call to C360 with empty input.

> 📎 **image-20260128-085801.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/f49c62bf-e74c-4421-8130-07de473a3197)（需 Jira 登入）
request body：

> 📎 **image-20260306-082119.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9b790dfe-6f52-4bab-99d4-f49b8faa12b3)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260128-085801.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/f49c62bf-e74c-4421-8130-07de473a3197)
2. 📎 **image-20260306-082119.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9b790dfe-6f52-4bab-99d4-f49b8faa12b3)

## 相關資訊

- **Jira:** [FE-1870](https://ctil.atlassian.net/browse/FE-1870)