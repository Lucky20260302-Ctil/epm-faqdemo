---
project: FE
issue_key: FE-972
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-972
created: '2021-05-11'
resolved: '2024-05-04'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-972: Staff purchase quota calculation logic with MM coupon'
---
# FE-972: Staff purchase quota calculation logic with MM coupon

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