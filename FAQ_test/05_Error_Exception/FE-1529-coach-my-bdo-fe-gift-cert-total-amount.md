---
project: FE
title: "FE-1529: Coach MY BDO FE - gift cert total amount calculation error"
issue_key: FE-1529
issue_type: Bug QA
status: Closed
faq_score: 7.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1529"
created: 2024-10-18
resolved: 2024-10-19
resolution: Done
has_images: True
---

# FE-1529: Coach MY BDO FE - gift cert total amount calculation error

## 問題描述

@@Cy Lau @@Andrew_Au @@Sang @@Joy Li 

In FE (7.5.0.04R07 Build 241004), I created a gift cert issuance memo that has 3 lines:

> 📎 **image-20241018-033559.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9da0df1b-323c-4208-b498-b7c9b57ba2b2)（需 Jira 登入）
The total amount here is correct so far. But in the PCD file the total amount becomes 1400.00:

> 📎 **image-20241018-033658.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/0f8c8095-5ba4-436c-b066-67226df7e933)（需 Jira 登入）
This is causing problems in BE posting and potentially problems for the e-invoice interface.



## 附件截圖

1. 📎 **image-20241018-033559.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9da0df1b-323c-4208-b498-b7c9b57ba2b2)
2. 📎 **image-20241018-033658.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/0f8c8095-5ba4-436c-b066-67226df7e933)

## 相關資訊

- **Jira:** [FE-1529](https://ctil.atlassian.net/browse/FE-1529)
- **解決方式:** Done