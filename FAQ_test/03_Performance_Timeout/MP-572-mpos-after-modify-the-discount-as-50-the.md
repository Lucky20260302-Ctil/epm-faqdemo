---
project: MP
issue_key: MP-572
issue_type: Bug QA
status: Closed
tags:
- 03_performance_timeout
- faq
- mp
- mpos
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-572
created: '2022-10-20'
resolved: '2022-11-18'
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'MP-572: MPOS-After modify the discount as 50%, then the price will change to 0'
---
# MP-572: MPOS-After modify the discount as 50%, then the price will change to 0

## 問題描述

Todo:

Implement the changes from 3.20.x

---

test Info:

FE: v72.0219.0100

IPA: 3.19.1

API: 3.19.2(Local IIS and Cloud IIS)

Description: We try to modify the item price on MPOS, but after we change the discount as 50%, then it will change to 0. This happen to both local IIS and Cloud IIS. Please check the details in attach video. thanks 

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/05513004-79ba-49ad-8a9f-676813495713)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/05513004-79ba-49ad-8a9f-676813495713)

## 相關資訊

- **Jira:** [MP-572](https://ctil.atlassian.net/browse/MP-572)
- **解決方式:** Done