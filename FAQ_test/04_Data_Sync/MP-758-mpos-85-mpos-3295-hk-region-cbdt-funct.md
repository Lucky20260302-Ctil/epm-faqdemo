---
project: MP
title: "MP-758: [MPOS-85] MPOS 3.29.5 - HK Region, CBDT function not working in MPOS"
issue_key: MP-758
issue_type: Bug PRD
status: Closed
faq_score: 6.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, mp, data_sync, mpos]
jira_url: "https://ctil.atlassian.net/browse/MP-758"
created: 2025-03-19
resolved: 2025-05-02
resolution: Done
has_images: True
---

# MP-758: [MPOS-85] MPOS 3.29.5 - HK Region, CBDT function not working in MPOS

## 問題描述

Neil callout HK region, For the customer not allow cross-border will pop-up message as below in MPOS.

MPOS IPA: v3.29.5-20250212.1

MPOS API: R3.29.5d

Testing machine IP: 10.33.254.14(OCQ10) connect to apabiqwposweb23

Log already uploaded. Testing customer phone no: 17781482669

> 📎 **image-20250319-080856.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/bc5941da-45e3-40b4-88aa-0960db976363)（需 Jira 登入）

> 📎 **image-20250319-080921.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/98d9eb99-b0f5-4e40-9c42-994005f98cd1)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250319-080856.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/bc5941da-45e3-40b4-88aa-0960db976363)
2. 📎 **image-20250319-080921.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/98d9eb99-b0f5-4e40-9c42-994005f98cd1)


## Jira Comments

> **Tovi Wang** (2025-03-19):
> HK OCQ10 03-19 MPOS log for your further checking. CC         

> **Daniel Leung** (2025-03-20):
>  \\ds411\share\POS_MPOS_Release\3.30.x\3.30.1-20250320.1 please test

> **Daniel Leung** (2025-04-02):
>  Please also test \\ds411\share\POS_MPOS_Release\3.29.X\3.29.5-20250402.1b2 for 3.29.5

> **Sherman tse** (2025-04-03):
> Verified on QA test case attached   

## 相關資訊

- **Jira:** [MP-758](https://ctil.atlassian.net/browse/MP-758)
- **解決方式:** Done