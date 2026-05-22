---
project: FE
title: "FE-1911: [LCX] Redeem Qty=0 of gift code can be comfirmed when Gift Redeem items summary has other gift code Redeem Qty=1"
issue_key: FE-1911
issue_type: Bug QA
status: Closed
faq_score: 5.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1911"
created: 2026-03-27
resolved: 2026-04-21
resolution: Done
has_images: True
---

# FE-1911: [LCX] Redeem Qty=0 of gift code can be comfirmed when Gift Redeem items summary has other gift code Redeem Qty=1

## 問題描述

[LCX] Redeem Qty=0 of gift code can be comfirmed when Gift Redeem items summary has other gift code Redeem Qty=1

Specific condition:

Gift Redeem items summary has  gift code A Redeem Qty=1 and gift code B Redeem Qty=0

Existing result:

Still able to complete the redeem process cauing pc file has one more 19 line with 0 amount

> 📎 **image-20260327-091325.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/6a4f8e97-1006-480d-8bad-6d6cd33fdbc5)（需 Jira 登入）
PC file content:

> 📎 **image-20260327-091631.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/68b2ff43-dbd7-4968-81f8-6691bfa17dd2)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260327-091325.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/6a4f8e97-1006-480d-8bad-6d6cd33fdbc5)
2. 📎 **image-20260327-091631.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/68b2ff43-dbd7-4968-81f8-6691bfa17dd2)


## Jira Comments

> **Automation for Jira** (2026-03-30):
> Issue has been created since Days since: 2 Week since : 0 Issue due date difference Days since :  Weeks since: 

> **Sang** (2026-03-30):
>   Gift Redeem - Gift redeem Rule set gift item qty =0 and Multi Gift Set Write PCD Fixed (KTS 260330 FE-1911 v750.05R11). Program uploaded to \\ds411\share\POS_FE_Release_64\20260330 LCX v750.05R11  

> **Andrew_Au** (2026-04-16):
> Please update the ticket status

> **Sherman tse** (2026-04-21):
> Verifed on QA Close case

## 相關資訊

- **Jira:** [FE-1911](https://ctil.atlassian.net/browse/FE-1911)
- **解決方式:** Done