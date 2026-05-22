---
project: WEB
issue_key: WEB-383
issue_type: Change Request
status: Closed
tags:
- 05_error_exception
- beapicrm
- error_exception
- faq
- web
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/WEB-383
created: '2025-01-15'
resolved: '2025-07-23'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'WEB-383: [ACU-81] Birthday is not set as null for 1900/2999-1-1 member'
---
# WEB-383: [ACU-81] Birthday is not set as null for 1900/2999-1-1 member

## 問題描述

Convert as null if birthday is "1900-1-1 or 2999-1-1" when sending member data to CRM.

### 

> 📎 **image-20250115-020313.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/00494c65-5d7c-4849-9d3a-f9b8d05bcb04)（需 Jira 登入）

> 📎 **image-20250115-020329.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/05e470a4-acac-47ce-86a4-e8b5e03b0cc3)（需 Jira 登入）

> 📎 **image-20250115-020337.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/8f20fdc5-42d9-4761-9aef-ab1c38294aa9)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250115-020313.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/00494c65-5d7c-4849-9d3a-f9b8d05bcb04)
2. 📎 **image-20250115-020329.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/05e470a4-acac-47ce-86a4-e8b5e03b0cc3)
3. 📎 **image-20250115-020337.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/8f20fdc5-42d9-4761-9aef-ab1c38294aa9)

## 相關資訊

- **Jira:** [WEB-383](https://ctil.atlassian.net/browse/WEB-383)
- **解決方式:** Done