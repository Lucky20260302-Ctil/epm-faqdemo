---
project: FE
issue_key: FE-972
issue_type: Bug PRD
status: Closed
faq_score: 7.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-972"
created: 2021-05-11
resolved: 2024-05-04
resolution: Done
has_images: True
---

# FE-972: Staff purchase quota calculation logic with MM coupon

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 7.5
> **解決日期:** 2024-05-04
> **負責人:** Sang
> **組件:** Front End

## 問題描述

Currently the staff has available quota 2935.

The staff will have a 50% member discount, and further 40% discount MM coupon.

If the non - discount amount > quota, the POS will block this transaction, but actually the discount amount < available quota.

 

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/95570421-b758-4634-a98d-c19962c7c995)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/95570421-b758-4634-a98d-c19962c7c995)


## Jira Comments

> **Sang** (2022-06-16):
> 17. Staff Limit - Count Qty Exclude Cpn Qty, Check Limit after apply MM Coupons (KTS 220616 v750.02 Jira  )

## 相關資訊

- **Jira:** [FE-972](https://ctil.atlassian.net/browse/FE-972)
- **解決方式:** Done
- **標籤:** RIN00671843