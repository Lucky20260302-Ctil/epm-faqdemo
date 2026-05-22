---
project: MP
title: "MP-738: [MPOS-68] MPOS_3.29.4-20241204.1 Didn't show Line bind indicator(For JP Region)"
issue_key: MP-738
issue_type: Bug PRD
status: Closed
faq_score: 5.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, mp, data_sync, mpos, mpos-api]
jira_url: "https://ctil.atlassian.net/browse/MP-738"
created: 2024-12-13
resolved: 2025-06-05
resolution: Done
has_images: True
---

# MP-738: [MPOS-68] MPOS_3.29.4-20241204.1 Didn't show Line bind indicator(For JP Region)

## 問題描述


> 📎 **image-20241213-013926.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/391b238d-acad-4ecd-b064-cdff5c8bbdd6)（需 Jira 登入）

> 📎 **image-20241213-013940.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/78a0f3a0-8ed2-4551-8ee0-9d6e9517bc46)（需 Jira 登入）

> 📎 **image-20241213-013953.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9bdf29cb-2d00-4ac4-baf2-5b197c9b5f30)（需 Jira 登入）
Q1 , does the listing have the indicator ?(As I rmb , nope ?)
Q2 Details page 100% sure missed - owing to MPOS itself or API ?



## 附件截圖

1. 📎 **image-20241213-013926.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/391b238d-acad-4ecd-b064-cdff5c8bbdd6)
2. 📎 **image-20241213-013940.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/78a0f3a0-8ed2-4551-8ee0-9d6e9517bc46)
3. 📎 **image-20241213-013953.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9bdf29cb-2d00-4ac4-baf2-5b197c9b5f30)


## Jira Comments

> **Cy Lau** (2024-12-13):
> Investigation on 13-Dec

> **Cy Lau** (2024-12-13):
> \\ds411\share\POS_MPOS_Release\3.29.X\3.29.5-20241212.1b1   release note :  applied getMemberDefinitions When Result Count == 1 CompanyCode = "COACHJP" And Not using C360

> **Cy Lau** (2024-12-13):
> Testing Data : DB : .8       

> **Daniel Leung** (2024-12-16):
> new ipa on Pre-Coach : 3.29.5-20241216.1: -bug fix: passing correct parameter to member detail to trigger getMembers api

> **Daniel Leung** (2024-12-16):
> With new API and IPA, Line Bind label can be displayed.

> **Cy Lau** (2024-12-17):
> Recap for Release: MPOS API - 3.29.5-20241212.1b1 : \\ds411\share\POS_MPOS_Release\3.29.X\3.29.5-20241212.1b1   release note :  applied getMemberDefinitions When Result Count == 1 CompanyCode = "COACHJP" And Not using C360 MPOS - 3.29.5-20241216.1:   release note : Member Details Page: -bug fix: passing correct parameter to member detail to trigger getMembers api

> **Andrew_Au** (2025-02-21):
>   Please update the ticket status

> **Andrew_Au** (2025-02-21):
>  Please update the ticket status

> **Sherman tse** (2025-02-21):
> Verfied on QA test case attached  

> **Andrew_Au** (2025-02-21):
>  Please update the ticket status

## 相關資訊

- **Jira:** [MP-738](https://ctil.atlassian.net/browse/MP-738)
- **解決方式:** Done