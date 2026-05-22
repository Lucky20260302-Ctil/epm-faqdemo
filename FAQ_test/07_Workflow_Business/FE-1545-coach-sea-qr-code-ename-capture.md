---
project: FE
title: "FE-1545: Coach SEA QR Code eName Capture"
issue_key: FE-1545
issue_type: Change Request
status: Closed
faq_score: 6.0
faq_category: 07_Workflow_Business
faq_category_label: 流程與業務
tags: [faq, fe, workflow_business, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1545"
created: 2024-10-31
resolved: 2024-12-24
resolution: Done
has_images: False
---

# FE-1545: Coach SEA QR Code eName Capture

## 問題描述

According to Acxiom, **‘iv@used4tapstry=’** is the IV for CN coupon API. The IV **‘iv@test4tapstry=’** is for SEA QA test.

They will provide new IV and encrypted key for SEA PROD. 

Therefore, we need to enhance POS front end to make the IV key configurable. 

We would store the iv key in backend database. Frontend will retrieve this key and store in tblconfig automatically.



## 相關資訊

- **Jira:** [FE-1545](https://ctil.atlassian.net/browse/FE-1545)
- **解決方式:** Done