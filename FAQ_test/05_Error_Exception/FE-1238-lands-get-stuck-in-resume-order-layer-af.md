---
project: FE
issue_key: FE-1238
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- fe
- front-end-v760.01r01a
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1238
created: '2023-05-10'
resolved: '2023-05-11'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1238: [Lands] Get stuck in Resume Order layer after inputed specific number'
---
# FE-1238: [Lands] Get stuck in Resume Order layer after inputed specific number

## 問題描述

Reproduce steps:

1. Apply a member  ID: [123456789012345678901234567890@ABC.COM](mailto:123456789012345678901234567890@ABC.COM)

2. Make suspand transaction

3. To  Resume order layer

4. Input 12345678 into serarch field & press Enter

Exsitng result:

Pop up an error & Get stuck in Resume Order layer after inputed 12345678

 

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7b3e416c-aa3d-45f6-9a3a-244fe6cbaff0)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7b3e416c-aa3d-45f6-9a3a-244fe6cbaff0)

## 相關資訊

- **Jira:** [FE-1238](https://ctil.atlassian.net/browse/FE-1238)
- **解決方式:** Done