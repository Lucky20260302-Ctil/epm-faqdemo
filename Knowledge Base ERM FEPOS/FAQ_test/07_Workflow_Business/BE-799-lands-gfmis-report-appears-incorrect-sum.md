---
project: BE
issue_key: BE-799
issue_type: Bug QA
status: Closed
faq_score: 6.5
faq_category: 07_Workflow_Business
faq_category_label: 流程與業務
tags: [faq, be, workflow_business, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-799"
created: 2023-09-01
resolved: 2023-09-07
resolution: Done
has_images: True
---

# BE-799: [Lands] GFMIS report appears incorrect sum of total price

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 流程與業務 | **FAQ 分數:** 6.5
> **解決日期:** 2023-09-07
> **負責人:** Sherman tse
> **組件:** Backend (Web)

## 問題描述

GFMIS report appears incorrect sum of total price:

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9ce4402e-dd87-47a2-a7a4-27686507c9f3)（需 Jira 登入）
Total price of Receipt Details displayed as 10980.8
It seems sum by colunm of joinv_tot_amt_fx- 1372.6*8 = 10980.8, instead, joupay_pay_amt_fx- 872.6+100+200+200 = 1372.6

 

Seems purchased specific items causing the issue

Items pusrchased in this order:

PHOTOCGEODA3
PHOTOCSVY
PHOTOCSVYA3
PHOTOCSVYCOLOR
PHOTOCSVYLSO
PHOTOCSVYLSOA3
100001
233575

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/64828169-b9b0-4526-8805-a4970dbe8fd5)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9ce4402e-dd87-47a2-a7a4-27686507c9f3)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/64828169-b9b0-4526-8805-a4970dbe8fd5)

## 相關資訊

- **Jira:** [BE-799](https://ctil.atlassian.net/browse/BE-799)
- **解決方式:** Done