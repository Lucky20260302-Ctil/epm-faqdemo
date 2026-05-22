---
project: FE
issue_key: FE-1760
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1760
created: '2025-09-30'
resolved: '2025-11-03'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1760: [BASH] Pop up a .net error during processing dayend action'
---
# FE-1760: [BASH] Pop up a .net error during processing dayend action

## 問題描述

[BASH] Pop up a .net error during processing dayend action

Version: 7.5.0.05 (build250918)

Reproduce steps:

1. Open POS

2. Process dayend 

3. Print out 1 dayend report

Existing result:

Pop up .net error as below

> 📎 **image-20250930-042016.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/09c4a20c-8aa4-4bbf-830a-0b61ffc9691d)（需 Jira 登入）
**VM:**

172.16.138.4

acc:  .\sxd

pw:   AOtesting..

**POS Login:**
acc: 99999
pw: 9999



## 附件截圖

1. 📎 **image-20250930-042016.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/09c4a20c-8aa4-4bbf-830a-0b61ffc9691d)

## 相關資訊

- **Jira:** [FE-1760](https://ctil.atlassian.net/browse/FE-1760)
- **解決方式:** Done