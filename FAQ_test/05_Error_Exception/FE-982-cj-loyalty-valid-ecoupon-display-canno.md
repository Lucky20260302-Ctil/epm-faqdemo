---
project: FE
issue_key: FE-982
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- fe
- frontend
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-982
created: '2021-06-15'
resolved: '2022-08-18'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-982: CJ Loyalty - valid eCoupon display cannot used in this memo message'
---
# FE-982: CJ Loyalty - valid eCoupon display cannot used in this memo message 

## 問題描述

Insert 1st eCoupon display cannot used in this memo message. Re-try another 2nd valid eCoupon will still display same message.

1. ) Apply coupon EC0000033 

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/0a5dcb44-06bc-44b5-b67d-84561bd88853)（需 Jira 登入）
2. ) Display can't be used in this meno

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/d1e5c584-8dad-47d7-96bc-e265df2b8022)（需 Jira 登入）
3.) Select another valid eCoupon EC0000030 

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ac7e3ab5-e8fe-494a-ac68-7092f9b874a8)（需 Jira 登入）
4.) Also display can't be used in this meno

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/de444d56-c755-49c4-a260-d06250330079)（需 Jira 登入）
5) After click OK, the eCoupon finally can be inserted. 

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/cbbc7e9e-aa60-4c15-8400-bc01f85596d0)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/0a5dcb44-06bc-44b5-b67d-84561bd88853)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/d1e5c584-8dad-47d7-96bc-e265df2b8022)
3. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ac7e3ab5-e8fe-494a-ac68-7092f9b874a8)
4. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/de444d56-c755-49c4-a260-d06250330079)
5. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/cbbc7e9e-aa60-4c15-8400-bc01f85596d0)

## 相關資訊

- **Jira:** [FE-982](https://ctil.atlassian.net/browse/FE-982)
- **解決方式:** Done