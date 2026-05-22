---
project: BE
issue_key: BE-330
issue_type: Bug DEV
status: Closed
tags:
- 05_error_exception
- backend-(web)
- be
- error_exception
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-330
created: '2020-11-03'
resolved: '2022-06-15'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-330: Data concurrency handling'
---
# BE-330: Data concurrency handling

## 問題描述

Client A and Client B open same module in edit mode e.g. (MF1005)

Client A save record successfully.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/799ab9e2-7d67-4b8c-98e9-d6f816fb7015)（需 Jira 登入）
After long period of time, Client B save record display error.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/f0be7737-d8f4-4b13-a9f8-1ba606f60ec2)（需 Jira 登入）
Already handle data concurrency, please try again (8/9/2021)



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/799ab9e2-7d67-4b8c-98e9-d6f816fb7015)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/f0be7737-d8f4-4b13-a9f8-1ba606f60ec2)

## 相關資訊

- **Jira:** [BE-330](https://ctil.atlassian.net/browse/BE-330)
- **解決方式:** Done