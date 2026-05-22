---
project: BE
issue_key: BE-1217
issue_type: Bug DEV
status: Closed
faq_score: 6.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, backend-(chainstoreplus-7.0)]
jira_url: "https://ctil.atlassian.net/browse/BE-1217"
created: 2025-11-28
resolved: 2026-05-14
resolution: Done
has_images: True
---

# BE-1217: Discountvariance issue related to jouinv_exrate,jouinv_item_qty,jouinv_item_amt

> **類型:** Bug DEV | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 6.5
> **解決日期:** 2026-05-14
> **負責人:** Sang
> **組件:** Backend (ChainStorePlus 7.0)

## 問題描述

Discountvariance issue related to jouinv_exrate,jouinv_item_qty,jouinv_item_amt

KSG region, Pos V75.004.0702.0000

KSG729-00028561/00028562

00028561 is the original memo, 00028562 is the void memo.

checked in PCD file, the data is normally

> 📎 **c353ed00-afa9-43dc-a7dc-a7f0af2c2f8a.jpg** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/11e6d7c1-8c31-44ec-86b7-8638cb55b1a8)（需 Jira 登入）
but in BE, the value of the three fields are incorrect.

> 📎 **57dc1e04-c9ab-4b45-bfad-24e2f9c565bb.jpg** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/67262f42-bbc7-49b9-aff8-372e5ef28a63)（需 Jira 登入）

> 📎 **22ef1643-1743-49cf-9f1e-e8d9b76cbcfa.jpg** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e57da50f-3043-4372-ad0c-53dc99f7d10b)（需 Jira 登入）

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/b120cefa-3337-40aa-be4e-d1e2707e9232)（需 Jira 登入）
CC: @@Joy Li @@Tovi Wang 



## 附件截圖

1. 📎 **c353ed00-afa9-43dc-a7dc-a7f0af2c2f8a.jpg** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/11e6d7c1-8c31-44ec-86b7-8638cb55b1a8)
2. 📎 **57dc1e04-c9ab-4b45-bfad-24e2f9c565bb.jpg** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/67262f42-bbc7-49b9-aff8-372e5ef28a63)
3. 📎 **22ef1643-1743-49cf-9f1e-e8d9b76cbcfa.jpg** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e57da50f-3043-4372-ad0c-53dc99f7d10b)
4. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/b120cefa-3337-40aa-be4e-d1e2707e9232)

## 相關資訊

- **Jira:** [BE-1217](https://ctil.atlassian.net/browse/BE-1217)
- **解決方式:** Done