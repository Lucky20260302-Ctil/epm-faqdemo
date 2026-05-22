---
project: FE
issue_key: FE-1896
issue_type: Bug QA
status: Closed
faq_score: 7.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1896"
created: 2026-03-06
resolved: 2026-04-21
resolution: Done
has_images: True
---

# FE-1896: [LCX] The 43rd pcd record format incorrect in Line 17 in gift redeem module

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 7.0
> **解決日期:** 2026-04-21
> **負責人:** Sherman tse
> **組件:** Front End

## 問題描述

[LCX] The 43rd pcd record format incorrect in Line 17 in gift redeem module

- Existing Content of The 43rd pcd value in line 17: 0.00

pcdtmn_redm_tot_point

> 📎 **image-20260306-101656.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a6a931ce-7966-42df-a630-94a0a66d4020)（需 Jira 登入）
- SQL DB require  interspec scale of total point is 1

> 📎 **image-20260306-101402.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9d98a739-cf85-40b7-99bd-14842301ecd2)（需 Jira 登入）
Tested in LCX UAT side only X.0 and X accepted and can be posted into BEDB

Issue cause BE application has error of invalid numeric format

> 📎 **image-20260306-103630.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/68238622-fbed-45db-9e13-bba06e7c6f20)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260306-101656.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a6a931ce-7966-42df-a630-94a0a66d4020)
2. 📎 **image-20260306-101402.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9d98a739-cf85-40b7-99bd-14842301ecd2)
3. 📎 **image-20260306-103630.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/68238622-fbed-45db-9e13-bba06e7c6f20)

## 相關資訊

- **Jira:** [FE-1896](https://ctil.atlassian.net/browse/FE-1896)
- **解決方式:** Done