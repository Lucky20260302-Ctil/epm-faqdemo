---
project: BE
title: "BE-987: [Coach][CRM] Enhancement of prevent value of vip_no_edm, vip_no_dm, vip_no_phone, vip_no_sms cannot be inserted"
issue_key: BE-987
issue_type: Improvement
status: Closed
faq_score: 6.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, api]
jira_url: "https://ctil.atlassian.net/browse/BE-987"
created: 2025-01-15
resolved: 2025-02-25
resolution: Done
has_images: True
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