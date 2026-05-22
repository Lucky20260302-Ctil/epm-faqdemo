---
project: FE
issue_key: FE-1557
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1557
created: '2024-11-11'
resolved: '2024-11-18'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1557: [Coach][CRM milestone 2] Botton of Purchase history & Profile need  to be checkable & pop up fail to connect CRM'
---
# FE-1557: [Coach][CRM milestone 2] Botton of Purchase history & Profile need  to be checkable & pop up fail to connect CRM

## 問題描述

[Coach][CRM milestone 2] Botton of Purchase history & Profile need to be checkable & pop up fail to connect CRM

Situation: When POS fail to connect CRM, member can be found in backend DB

Reproduce steps:

1. Fail to connect CRM

2. Search member that Backedn DB has that member

Exisiting result:

Purchase history dimmed & Profile can be clicked but pop up “Member Profile is not available”

Expected result:

- Purchase history & Profile are checkable when POS fail to connect to CRM

- Both oh them can pop up “Fail to connect CRM. XXXXX is not available. “

> 📎 **image-20241111-013213.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/622182f8-53ea-48e3-b9a1-870f192c600f)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20241111-013213.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/622182f8-53ea-48e3-b9a1-870f192c600f)

## 相關資訊

- **Jira:** [FE-1557](https://ctil.atlassian.net/browse/FE-1557)
- **解決方式:** Done