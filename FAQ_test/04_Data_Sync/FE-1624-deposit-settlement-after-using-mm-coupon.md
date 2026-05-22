---
project: FE
title: "FE-1624: Deposit Settlement After Using MM Coupons get negative net amount"
issue_key: FE-1624
issue_type: Bug PRD
status: Closed
faq_score: 6.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1624"
created: 2025-02-11
resolved: 2025-04-14
resolution: Done
has_images: True
---

# FE-1624: Deposit Settlement After Using MM Coupons get negative net amount

## 問題描述


> 📎 **image-20250211-055530.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/1c705922-dd38-44aa-980a-74a24e1a944f)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250211-055530.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/1c705922-dd38-44aa-980a-74a24e1a944f)


## Jira Comments

> **Sang** (2025-02-14):
> Re-produce Steps: Create Desposit (Ex. $1500), Paid $1400 Deposit, Balance Amt $100  Settle Deposit Net Amt To be Paid $100 ($1500-$1400) Apply MM Coupons, Deduct $200- from Purchase amt $1500. Net Amt = $1300 = $1500-$200 Net Amt to be Paid -$100 = $1300 (Net Amt)-$1400 (Deposit Amt)

> **Andrew_Au** (2025-02-24):
>   Please test this issue. Is that alread in the lastest version of POS 7.5

> **Andrew_Au** (2025-04-07):
>  Please update the ticket status

> **Andrew_Au** (2025-04-09):
>  Please update the ticket status

> **Sherman tse** (2025-04-09):
> Verified on QA with 7.5.0.04R12 (Build 250403) When MM coupon discount deduct amount high that settle deposit amount, pos would pop up “After deduct MM coupon discount, Net amount less than deposit amount, please re-input MM coupon“

## 相關資訊

- **Jira:** [FE-1624](https://ctil.atlassian.net/browse/FE-1624)
- **解決方式:** Done