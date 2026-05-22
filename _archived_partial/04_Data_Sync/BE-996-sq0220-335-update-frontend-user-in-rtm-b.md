---
project: BE
issue_key: BE-996
issue_type: Bug QA
status: Closed
tags:
- 04_data_sync
- backend-(chainstoreplus-7.0)
- be
- data_sync
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-996
created: '2025-01-26'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-996: [SQ0220-335] update frontend user in RTM backend, min length should be mandatory field'
---
# BE-996: [SQ0220-335] update frontend user in RTM backend, min length should be mandatory field

## 問題描述

update front end user in RTM back end, set "min length" empty, and set home store = home

click save button, user acct information update succ

expected;

according SRS, "min length should be a mandatory field

> 📎 **image-20250126-013659.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d5142c58-7140-47d1-b6be-4ea45087c8f4)（需 Jira 登入）

> 📎 **image-20250126-013718.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/fc73d825-b6d9-436b-8155-65d111c0077c)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250126-013659.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d5142c58-7140-47d1-b6be-4ea45087c8f4)
2. 📎 **image-20250126-013718.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/fc73d825-b6d9-436b-8155-65d111c0077c)

## 相關資訊

- **Jira:** [BE-996](https://ctil.atlassian.net/browse/BE-996)