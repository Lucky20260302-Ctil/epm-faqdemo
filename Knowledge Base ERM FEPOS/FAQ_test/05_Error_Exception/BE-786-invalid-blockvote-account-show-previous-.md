---
project: BE
issue_key: BE-786
issue_type: Bug DEV
status: Closed
faq_score: 5.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-786"
created: 2023-08-02
resolved: 2023-09-07
resolution: Done
has_images: True
---

# BE-786: invalid blockvote account show previous account obtained successfully instead of empty

> **類型:** Bug DEV | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 5.0
> **解決日期:** 2023-09-07
> **負責人:** Sherman tse
> **組件:** Backend (Web)

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