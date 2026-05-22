---
project: MP
issue_key: MP-759
issue_type: Bug PRD
status: Closed
tags:
- 07_workflow_business
- faq
- mp
- mpos
- workflow_business
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-759
created: '2025-03-21'
resolved: '2025-05-02'
fix_version: ''
components: []
has_images: true
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'MP-759: [MPOS-84] MPOS V3.29.5 HK Region, for the print function should print directly instead pop-up window'
---
# MP-759: [MPOS-84] MPOS V3.29.5 HK Region, for the print function should print directly instead pop-up window

## 問題描述

during testing for HK MPOS, we found that for HK region, it will always pop-up below window after create transaction, and also for reprint & void function, it will also pop-up window ask to choose 'printer'. kindly help to check.

MPOS IPA: v3.29.5-20250212.1

MPOS API: R3.29.5d

Testing machine IP: 10.33.254.14(OCQ10) connect to apabiqwposweb23

> 📎 **image-20250321-051030.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a9937a5c-7da1-48a8-969c-34c141ae4378)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250321-051030.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a9937a5c-7da1-48a8-969c-34c141ae4378)

## 相關資訊

- **Jira:** [MP-759](https://ctil.atlassian.net/browse/MP-759)
- **解決方式:** Done