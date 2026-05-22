---
project: BE
issue_key: BE-1034
issue_type: SOW
status: Closed
tags:
- 01_install_deploy
- be
- data-interface
- faq
- install_deploy
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-1034
created: '2025-03-20'
resolved: '2025-05-12'
fix_version: ''
components: []
has_images: false
category: 01_Install_Deploy
category_label: 安裝與部署
quality: partial
title: 'BE-1034: [CS-1359]SOW of KS SEA CRM Sales Registration Enhancement'
---
# BE-1034: [CS-1359]SOW of KS SEA CRM Sales Registration Enhancement

## 問題描述

Currently Kate Spade SEA CRM sales registration interface, promotion code is not included in the JSON payload thus causing the issues of miscalculation for VIP upgrading in Loyalty system.

To overcome the issue, we need to enhance the Sales Registration Interface by including the promotion code in the payload sending to Memberson’s “Register Transaction” API. This change will be implemented on Kate Spade Singapore and Malaysia regions only.

Please refer to Teams Group: KS SEA CRM Memberson



## 相關資訊

- **Jira:** [BE-1034](https://ctil.atlassian.net/browse/BE-1034)
- **解決方式:** Done
- **標籤:** CR