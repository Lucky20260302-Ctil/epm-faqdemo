---
project: BE
issue_key: BE-1226
issue_type: Bug QA
status: Closed
faq_score: 6.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-1226"
created: 2026-01-29
resolved: 
resolution: 
has_images: True
---

# BE-1226: After created multiple Credit Card, the range between "From Gift Cert" and "To Gift Cert" do not proceed properly

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 6.0
> **負責人:** Jerry Wong
> **組件:** Data Interface

## 問題描述

I created a sales memo with **10** quantity service item POS_KS_PGC, and another memo with 2 serivce item Amount 1000 and 1 service item Amount 800.

> 📎 **image-20260129-091802.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/ae40fa98-8529-4e03-ac77-d69a4e70744c)（需 Jira 登入）

> 📎 **image-20260129-091811.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9f723f51-5548-4e95-a9b6-116f78d53627)（需 Jira 登入）

Their Carlog is been like these.

|  | G | OC602 | 00048611 | 20251027 | I | 1 | **OC602000000486111** | **OC602000000486111** | **10** | 100 | 1000 | 402036 | 402036 | 1000 | 14 | 18 |  |  |  |  | 20251027 | 141800 |  |  |  | 
|  | P | OC602 | 00048611 | 20251027 | D | 1 | 123 | POS_KS_PGC |  |  |  | 6 | 1 | 10 | -1000 |  | 20251027 | 141800 |  |  |  |  |  |  |  | 
|  | G | OC602 | 00048611 | 20251027 | P | 1 | 0 | CSH | 1 | 1000 | 1000 |  | 0 |  |  |  |  |  |  |  |  |  |  | 20251027 | 141800 | 

|  | G | OC602 | 00048588 | 20251027 | I | 1 | **OC602000485881** | **OC602000485881** | **2** | 500 | 1000 | 402036 | 402036 | 1800 | 11 | 30 |  |  |  |  | 20251027 | 113000 |  |  |  | 
|  | G | OC602 | 00048588 | 20251027 | I | 2 | **OC602000485882** | **OC602000485882** | **1** | 800 | 800 | 402036 | 402036 | 1800 | 11 | 30 |  |  |  |  | 20251027 | 113000 |  |  |  | 
|  | P | OC602 | 00048588 | 20251027 | D | 1 |  | POS_CH_GIFTCER |  |  |  | 6 | 1 | 2 | -1000 |  | 20251027 | 113000 |  |  |  |  |  |  |  | 
|  | P | OC602 | 00048588 | 20251027 | D | 2 |  | POS_CH_GIFTCER |  |  |  | 6 | 2 | 1 | -800 |  | 20251027 | 113000 |  |  |  |  |  |  |  | 
|  | G | OC602 | 00048588 | 20251027 | P | 1 | 0 | CSH | 1 | 1800 | 1800 |  | 0 |  |  |  |  |  |  |  |  |  |  | 20251027 | 113000 | 



## 附件截圖

1. 📎 **image-20260129-091802.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/ae40fa98-8529-4e03-ac77-d69a4e70744c)
2. 📎 **image-20260129-091811.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9f723f51-5548-4e95-a9b6-116f78d53627)


## Jira Comments

> **Joseph_Hu** (2026-01-30):
> Confirmed with Bobby and Jerry, it’s not need to advised, so that’s not an issue.

## 相關資訊

- **Jira:** [BE-1226](https://ctil.atlassian.net/browse/BE-1226)
- **標籤:** CAR