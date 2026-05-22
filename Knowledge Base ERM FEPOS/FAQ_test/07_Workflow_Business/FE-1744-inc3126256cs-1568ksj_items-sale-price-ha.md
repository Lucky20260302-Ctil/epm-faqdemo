---
project: FE
issue_key: FE-1744
issue_type: Bug DEV
status: Closed
faq_score: 5.5
faq_category: 07_Workflow_Business
faq_category_label: 流程與業務
tags: [faq, fe, workflow_business, front-end-v720.02]
jira_url: "https://ctil.atlassian.net/browse/FE-1744"
created: 2025-08-07
resolved: 
resolution: 
has_images: True
---

# FE-1744: [INC3126256][CS-1568]KSJ_item's sale price has variance between POS and receipt

> **類型:** Bug DEV | **狀態:** Closed
> **分類:** 流程與業務 | **FAQ 分數:** 5.5
> **負責人:** Sang
> **組件:** Front End v720.02

## 問題描述

C309-00117534

Item SKU: KM471 001
sale price displaying on POS: 25,696 JPY(Tax in)
sale price showing on receipt: 23,361 JPY(with out Tax )
consumption tax rate: 10%
User think the sales price on receipt should be 23,360 JPY instead of 23,361 JPY, since 25,696/1.1=23,360

1.C309-00117534 in DB

> 📎 **image-20250807-064956.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/bfb435ca-06c2-4cda-b23a-d9667e44ceb8)（需 Jira 登入）
2.Troubleshooting excel details for your reference.

> 📎 **image-20250807-065145.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/47677829-9c8e-49c4-b14f-262582738aac)（需 Jira 登入）
3. FE & receipt capture: [📎附件](https://ctil.atlassian.net/rest/api/3/attachment/content/6faf94b5-cc47-4488-95cc-87e29d05b9a7) 



## 附件截圖

1. 📎 **image-20250807-064956.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/bfb435ca-06c2-4cda-b23a-d9667e44ceb8)
2. 📎 **image-20250807-065145.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/47677829-9c8e-49c4-b14f-262582738aac)

## 相關資訊

- **Jira:** [FE-1744](https://ctil.atlassian.net/browse/FE-1744)