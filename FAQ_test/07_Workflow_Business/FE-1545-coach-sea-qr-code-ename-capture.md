---
project: FE
issue_key: FE-1545
issue_type: Change Request
status: Closed
tags:
- 07_workflow_business
- faq
- fe
- front-end
- workflow_business
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1545
created: '2024-10-31'
resolved: '2024-12-24'
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'FE-1545: Coach SEA QR Code eName Capture'
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