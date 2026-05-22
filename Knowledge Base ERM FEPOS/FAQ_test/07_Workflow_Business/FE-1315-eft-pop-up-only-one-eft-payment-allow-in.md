---
project: FE
issue_key: FE-1315
issue_type: Bug QA
status: Closed
faq_score: 5.5
faq_category: 07_Workflow_Business
faq_category_label: 流程與業務
tags: [faq, fe, workflow_business, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1315"
created: 2023-11-20
resolved: 2023-12-14
resolution: Done
has_images: False
---

# FE-1315: [EFT] Pop up "Only one EFT payment Allow in single transaction" when non-EFT payment method selected first, then select EFT payment

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 流程與業務 | **FAQ 分數:** 5.5
> **解決日期:** 2023-12-14
> **負責人:** Sang
> **組件:** Front End

## 問題描述

Reproduce steps:

1. Select non-EFT payment method, e.g.: E-payment

2. Select EFT payment

3. Click on Tick

Existing result:

Pop up "Only one EFT payment Allow in single transaction" & not allow to process to further steps



## 相關資訊

- **Jira:** [FE-1315](https://ctil.atlassian.net/browse/FE-1315)
- **解決方式:** Done