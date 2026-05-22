---
project: MP
issue_key: MP-764
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- mp
- mpos-api
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-764
created: '2025-04-02'
resolved: '2025-04-03'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'MP-764: [Coach][PIPL] Pop up 999 error message after searching member with EXIT_PERMIT=1 by mobile number'
---
# MP-764: [Coach][PIPL] Pop up 999 error message after searching member with EXIT_PERMIT=1 by mobile number

## 問題描述

Reproduce steps:

1. To member section

2. Input mobile number for searching a member with EXIT_PERMIT=1

*Testing data:

13761555153

Existing result:

Pop up 999 error message

Expected result:

Need to display the member details

> 📎 **image-20250402-023200.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/15227209-6be1-4ada-a92e-05008b9fc854)（需 Jira 登入）
Testing version:

3.30.1-20250320.1



## 附件截圖

1. 📎 **image-20250402-023200.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/15227209-6be1-4ada-a92e-05008b9fc854)

## 相關資訊

- **Jira:** [MP-764](https://ctil.atlassian.net/browse/MP-764)
- **解決方式:** Done