---
project: BE
issue_key: BE-676
issue_type: Bug QA
status: Closed
faq_score: 5.5
faq_category: 07_Workflow_Business
faq_category_label: 流程與業務
tags: [faq, be, workflow_business, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-676"
created: 2022-11-07
resolved: 2022-11-25
resolution: Done
has_images: False
---

# BE-676: Supplier Code used incorrect words limitation

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 流程與業務 | **FAQ 分數:** 5.5
> **解決日期:** 2022-11-25
> **負責人:** Ken Lam
> **組件:** Backend (Web)

## 問題描述

Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)

ACC: sxd                          PW: sxd

Location: Process > Purchase Order Maintenance (PO3000)

Reproduce steps:

1. To Purchase Order Maintenance (PO3000)

2. Click Create

3. To Supplier Code

4. Select Supplier Code that are over 10 words e,g.:  CRIMSON_BRANDS

Existing result:

Field of Supplier is rounded by red outline, applied Text with Max Length = 10

 

Expected result:

Words limitation of Supplier Code should be 15 words



## 相關資訊

- **Jira:** [BE-676](https://ctil.atlassian.net/browse/BE-676)
- **解決方式:** Done