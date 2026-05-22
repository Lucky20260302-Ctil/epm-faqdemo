---
project: BE
issue_key: BE-786
issue_type: Bug DEV
status: Closed
tags:
- 05_error_exception
- backend-(web)
- be
- error_exception
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-786
created: '2023-08-02'
resolved: '2023-09-07'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-786: invalid blockvote account show previous account obtained successfully instead of empty'
---
# BE-786: invalid blockvote account show previous account obtained successfully instead of empty

## 問題描述

select the valid account cntBVAcc02

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e9fd658e-52c6-41c5-8430-45429a33a3df)（需 Jira 登入）

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d8fbc987-7d39-4169-8229-ab615beb3180)（需 Jira 登入）
then back, leave the page, and select an invalid account

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/bdb70679-9e3b-4542-aefb-babb47cb84da)（需 Jira 登入）
but the block vote account field remains cntBVAcc02 still.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/8bb198d1-7122-4cc7-92fb-27a3b18e7bac)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e9fd658e-52c6-41c5-8430-45429a33a3df)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d8fbc987-7d39-4169-8229-ab615beb3180)
3. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/bdb70679-9e3b-4542-aefb-babb47cb84da)
4. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/8bb198d1-7122-4cc7-92fb-27a3b18e7bac)

## 相關資訊

- **Jira:** [BE-786](https://ctil.atlassian.net/browse/BE-786)
- **解決方式:** Done