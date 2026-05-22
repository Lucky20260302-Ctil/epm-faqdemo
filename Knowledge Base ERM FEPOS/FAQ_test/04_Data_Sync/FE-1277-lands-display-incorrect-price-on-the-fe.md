---
project: FE
issue_key: FE-1277
issue_type: Bug QA
status: Closed
faq_score: 6.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, frontend]
jira_url: "https://ctil.atlassian.net/browse/FE-1277"
created: 2023-07-27
resolved: 2023-10-09
resolution: Done
has_images: True
---

# FE-1277: [Lands] Display incorrect price on the FE

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 6.0
> **解決日期:** 2023-10-09
> **負責人:** Sang
> **組件:** Frontend

## 問題描述

Item: 233575 (Hong Kong Guide)

Front end display this item as $128

But SQL display this item in column 1) jouinv_item_amt 2) jouinv_item_amt 3) jouinv_item_amt_fx display $0

 

Got dbmas & retdata6 for your reference: 

\\172.16.183.201\localuser\support\20230727\LandsD\Retdata6+dbmas

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e2fcc098-3ac4-416e-9b7e-45c8d937cd58)（需 Jira 登入）
 



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e2fcc098-3ac4-416e-9b7e-45c8d937cd58)


## Jira Comments

> **Sang** (2023-08-01):
> 5. Lands Production Type 'S' (Stock On Hand) Match to CSPLUS Stock Indicator 'B' (KTS 230803 V760.01R03E Jira  )

> **Sherman tse** (2023-10-09):
> Verified on UAT env Lands

## 相關資訊

- **Jira:** [FE-1277](https://ctil.atlassian.net/browse/FE-1277)
- **解決方式:** Done