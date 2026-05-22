---
project: BE
issue_key: BE-987
issue_type: Improvement
status: Closed
tags:
- 03_performance_timeout
- api
- be
- faq
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-987
created: '2025-01-15'
resolved: '2025-02-25'
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'BE-987: [Coach][CRM] Enhancement of prevent value of vip_no_edm, vip_no_dm, vip_no_phone, vip_no_sms cannot be inserted'
---
# BE-987: [Coach][CRM] Enhancement of prevent value of vip_no_edm, vip_no_dm, vip_no_phone, vip_no_sms cannot be inserted

## 問題描述

Situation:

When upsert a member from CRM with expiry_date that is not same with backend DB, backend DB would not allow to update the value of  ip_no_edm, vip_no_dm, vip_no_phone, vip_no_sms

> 📎 **image-20250115-094443.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/8c4d08cb-0326-4bd2-ae41-f7463a3d94ac)（需 Jira 登入）

Solution:

Add a flag to control for coach company



## 附件截圖

1. 📎 **image-20250115-094443.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/8c4d08cb-0326-4bd2-ae41-f7463a3d94ac)

## 相關資訊

- **Jira:** [BE-987](https://ctil.atlassian.net/browse/BE-987)
- **解決方式:** Done