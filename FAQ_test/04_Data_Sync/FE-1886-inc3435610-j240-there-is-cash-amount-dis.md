---
project: FE
title: "FE-1886: [INC3435610] J240 There is cash amount discrepancy in dayend report."
issue_key: FE-1886
issue_type: Bug PRD
status: Open
faq_score: 5.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1886"
created: 2026-02-11
resolved: 
resolution: 
has_images: True
---

# FE-1886: [INC3435610] J240 There is cash amount discrepancy in dayend report.

## 問題描述

Morning sang ko,Store callout that there is cash amount 173,300 discrepancy in RC report.

I have one quick question,May I confirm that under what circumstances would such a discrepancy occur in the RC report?

INC3435610

 

1.RC report:

> 📎 **image-20260211-092205.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/226e4048-eebe-4035-8e95-2dfbbfc219a7)（需 Jira 登入）
2.The cash flow 173,300 is come from Till0 which entered by store user.

Till0 RP:

> 📎 **image-20260211-092236.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/0fecbb4e-24dd-47d4-9e40-f29979362839)（需 Jira 登入）

> 📎 **image-20260211-092303.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/4d01078b-c64b-45ba-82c7-9af7cee49aa8)（需 Jira 登入）
3.From T9 log we can see that cashier id 488188 entered the cash flow amount 173,300

> 📎 **image-20260211-092427.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/8d4b86ec-0f16-4333-9571-57c4a4dabfe6)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260211-092205.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/226e4048-eebe-4035-8e95-2dfbbfc219a7)
2. 📎 **image-20260211-092236.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/0fecbb4e-24dd-47d4-9e40-f29979362839)
3. 📎 **image-20260211-092303.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/4d01078b-c64b-45ba-82c7-9af7cee49aa8)
4. 📎 **image-20260211-092427.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/8d4b86ec-0f16-4333-9571-57c4a4dabfe6)


## Jira Comments

> **Tovi Wang** (2026-02-12):
>  SOG team provided All the logs and files.Please further checking. CC     

> **Sang** (2026-02-12):
>    J240 have 3 tills. Please copy Till 1 and Till 2 dbtrans (Dbtbk08.1.sdf and Dbtbk08.2.sdf) and Dbtbk09.sdf from Till 0.

> **Sang** (2026-02-12):
>  Please copy Till 1 (Dbtbk08.1.sdf) and Till 2 (Dbtbk08.2.sdf if available)  dbtrans and Dbtbk09.sdf from Till 0.

> **pierre.shi** (2026-02-12):
> Hi    dbtbk has been uploaded as attachment. Please help to check.

> **Sang** (2026-02-12):
>       J240 has Till 0-2, in Till 0 found till 2026.02.08 dbtrans (dbtbk02.02.sdf),  Total Cash Flow show in RC report is 173300+93300+173300 = 439,900.   But Till 2 backup dbtrans (dbtbk08.2.sdf) actually is a copy of Till 0 2026.02.08 dbtrans.  Please find out why ?

## 相關資訊

- **Jira:** [FE-1886](https://ctil.atlassian.net/browse/FE-1886)