---
project: FE
issue_key: FE-1839
issue_type: Bug DEV
status: Open
tags:
- 05_error_exception
- error_exception
- faq
- fe
- front-end-v750.01r01a
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1839
created: '2025-12-29'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1839: [INC3353418]When they are processing a CMB payment bill, it firstly pop out a error ''CBM 付款 失败，已取消一个任务''. Then user try repay and it become successful.'
---
# FE-1839: [INC3353418]When they are processing a CMB payment bill, it firstly pop out a error 'CBM 付款 失败，已取消一个任务'. Then user try repay and it become successful.

## 問題描述

PRC region, OCF506, till0, POSv75

When processing a CMB payment bill, it firstly pop out a error 'CBM 付款 失败，已取消一个任务'.
Then user try repay and it become successful.

such as sales memo:00026610

> 📎 **image-20251229-083651.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e64c5347-9d1b-47f3-994c-60db7ebdf280)（需 Jira 登入）

> 📎 **image-20251229-083719.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/dae3a38c-fede-47d1-9745-1cddbfc782cc)（需 Jira 登入）
Checked in log. it shew error info in T9 log

> 📎 **6942d530-d693-45ae-9e37-e337468c6e44.jpg** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/f0d5b24b-c0f3-4af4-9a44-2d860ba90ca8)（需 Jira 登入）

below is the cmb log

> 📎 **8e374759-fb99-4eae-9ce4-e3408dd283df.jpg** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/c374eba6-d3a9-4ea2-bcfa-007fedadb221)（需 Jira 登入）
FE and cmb logs have been attached.



## 附件截圖

1. 📎 **image-20251229-083651.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e64c5347-9d1b-47f3-994c-60db7ebdf280)
2. 📎 **image-20251229-083719.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/dae3a38c-fede-47d1-9745-1cddbfc782cc)
3. 📎 **6942d530-d693-45ae-9e37-e337468c6e44.jpg** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/f0d5b24b-c0f3-4af4-9a44-2d860ba90ca8)
4. 📎 **8e374759-fb99-4eae-9ce4-e3408dd283df.jpg** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/c374eba6-d3a9-4ea2-bcfa-007fedadb221)

## 相關資訊

- **Jira:** [FE-1839](https://ctil.atlassian.net/browse/FE-1839)