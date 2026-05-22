---
project: BE
issue_key: BE-675
issue_type: Bug QA
status: Closed
faq_score: 5.5
faq_category: 07_Workflow_Business
faq_category_label: 流程與業務
tags: [faq, be, workflow_business, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-675"
created: 2022-11-07
resolved: 2024-04-27
resolution: Done
has_images: False
---

# BE-675: Field of P.O. No. with no any words filled in should be rounded by red color after click save

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 流程與業務 | **FAQ 分數:** 5.5
> **解決日期:** 2024-04-27
> **負責人:** Ken Lam
> **組件:** Backend (Web)

## 問題描述

Env: [https://172.16.138.101/chainstoreplus/po3000](https://172.16.138.101/chainstoreplus/po3000)

Location: Process > Purchase Order Maintenance (PO3000)

Reproduce steps:

1. To  Purchase Order Maintenance (PO3000)

2. Click Save directly

3. Pop up Please Enter P.O. No. dialog

4. Click OK 

Existing result:

Field of P.O. No. with no any words filled-in but no red outline rounded for reminder



## 相關資訊

- **Jira:** [BE-675](https://ctil.atlassian.net/browse/BE-675)
- **解決方式:** Done