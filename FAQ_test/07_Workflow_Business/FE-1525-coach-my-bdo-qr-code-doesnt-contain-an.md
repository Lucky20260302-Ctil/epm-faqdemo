---
project: FE
title: "FE-1525: Coach MY BDO - QR code doesn't contain any information after identity="
issue_key: FE-1525
issue_type: Bug QA
status: Closed
faq_score: 6.5
faq_category: 07_Workflow_Business
faq_category_label: 流程與業務
tags: [faq, fe, workflow_business, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1525"
created: 2024-10-16
resolved: 2025-02-12
resolution: Done
has_images: True
---

# FE-1525: Coach MY BDO - QR code doesn't contain any information after identity=

## 問題描述

When I scan the QR code for E-Invoice, I get the basic URL:

[https://uat-microsite1.bdomiddleware.my/buyerportal/customer/login?identity=](https://uat-microsite1.bdomiddleware.my/buyerportal/customer/login?identity=) 

but after identity=, I should get the following: 

> 📎 **image-20241016-054311.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a7c40409-cde4-4c80-81c3-f3a11ef62964)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20241016-054311.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a7c40409-cde4-4c80-81c3-f3a11ef62964)

## 相關資訊

- **Jira:** [FE-1525](https://ctil.atlassian.net/browse/FE-1525)
- **解決方式:** Done