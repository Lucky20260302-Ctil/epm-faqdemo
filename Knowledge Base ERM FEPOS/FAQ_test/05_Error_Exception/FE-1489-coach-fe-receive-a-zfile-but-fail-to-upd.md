---
project: FE
issue_key: FE-1489
issue_type: Bug QA
status: Closed
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1489"
created: 2024-08-26
resolved: 2024-09-05
resolution: Done
has_images: True
---

# FE-1489: [Coach] FE receive a zfile but fail to update tblcoupon table

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.5
> **解決日期:** 2024-09-05
> **負責人:** Sang
> **組件:** Front End

## 問題描述

[Coach] FE receive a zfile but fail to update tblcoupon table

Here are 2 zupdate that received by POS but no new record added to tblcoupon table

> 📎 **image-20240826-020320.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7945feb7-3d03-4cee-87ff-af41f13edc13)（需 Jira 登入）

> 📎 **image-20240826-020243.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7915e83e-484d-4dff-b821-64c656ad81ba)（需 Jira 登入）

> 📎 **image-20240826-020543.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9ca02380-c1b9-4572-ba40-55b240456dad)（需 Jira 登入）

Only [dbMas].[dbo].[Mix Table] has new record of the coupon:

> 📎 **image-20240826-020437.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/1587497b-e8ab-44b3-9d9c-f92626d3b976)（需 Jira 登入）
But log can be found in the UD file

> 📎 **image-20240826-020836.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e394b53a-2987-4b21-b1fe-5fc19d898946)（需 Jira 登入）

VM:

172.16.138.60

.\sxd

Yan20201104@



## 附件截圖

1. 📎 **image-20240826-020320.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7945feb7-3d03-4cee-87ff-af41f13edc13)
2. 📎 **image-20240826-020243.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7915e83e-484d-4dff-b821-64c656ad81ba)
3. 📎 **image-20240826-020543.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9ca02380-c1b9-4572-ba40-55b240456dad)
4. 📎 **image-20240826-020437.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/1587497b-e8ab-44b3-9d9c-f92626d3b976)
5. 📎 **image-20240826-020836.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e394b53a-2987-4b21-b1fe-5fc19d898946)

## 相關資訊

- **Jira:** [FE-1489](https://ctil.atlassian.net/browse/FE-1489)
- **解決方式:** Done