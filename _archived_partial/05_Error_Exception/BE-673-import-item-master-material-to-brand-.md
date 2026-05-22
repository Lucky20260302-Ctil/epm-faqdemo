---
project: BE
issue_key: BE-673
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- backend-(chainstoreplus-7.0)
- be
- error_exception
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-673
created: '2022-11-04'
resolved: '2024-04-27'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-673: Import Item Master Material to Brand'
---
# BE-673: Import Item Master Material to Brand 

## 問題描述

Current BE program fail to auto create brand code

 CS2000 APP Server

- Import Data (as0003.out)

- Update “Material Code” to “Brand Code” in item master interface for Mix & Match Promotion.

- New brand code will be create automatically if not exist.

- A default supplier code ‘OC’ will assign to the new brand code.

- This customization applies to CJ only.



## 相關資訊

- **Jira:** [BE-673](https://ctil.atlassian.net/browse/BE-673)
- **解決方式:** Done