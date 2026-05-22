---
project: FE
issue_key: FE-1653
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- fe
- mpos
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1653
created: '2025-03-19'
resolved: '2025-03-21'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1653: [Coach][PIPL] Pop up incorrect message after searching member with EXIT_PERMIT != 1'
---
# FE-1653: [Coach][PIPL] Pop up incorrect message after searching member with EXIT_PERMIT != 1

## 問題描述

[Coach][PIPL] Pop up incorrect message after searching member with EXIT_PERMIT != 1

Testing data-mobile number( CN member with EXIT_PERMIT != 1 ): **21001203962**

Region: 10 (HK)

Reproduce steps:

1. To MPOS- member section

2. Search member by mobile no.

3. Pop up error message: Record not found

Expected result:

Need to pop up "This member does not consent to enquire out of border."

> 📎 **image-20250319-041441.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e7622426-69c4-406a-915f-31d2ff98c245)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250319-041441.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e7622426-69c4-406a-915f-31d2ff98c245)

## 相關資訊

- **Jira:** [FE-1653](https://ctil.atlassian.net/browse/FE-1653)
- **解決方式:** Done