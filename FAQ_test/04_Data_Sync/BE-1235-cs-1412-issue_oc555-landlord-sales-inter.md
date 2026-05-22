---
project: BE
title: "BE-1235: [CS-1412] Issue_OC555 Landlord sales interface logic is wrong"
issue_key: BE-1235
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-1235"
created: 2026-03-11
resolved: 2026-05-05
resolution: Done
has_images: True
---

# BE-1235: [CS-1412] Issue_OC555 Landlord sales interface logic is wrong

## 問題描述

When pay code is GIC in one transaction, the payment will be double.

 

In bellow case.

Total 20 GIC in this transaction, each one is 50 and total should be 1000.

> 📎 **image-20260311-063734.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/eba76107-9ea2-4137-9cc5-3fadb740d2ac)（需 Jira 登入）
But system will send 20000 to Landlord.

> 📎 **image-20260311-064045.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/fcfd49ec-1c4f-4618-bfdb-27db07e24f1c)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260311-063734.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/eba76107-9ea2-4137-9cc5-3fadb740d2ac)
2. 📎 **image-20260311-064045.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/fcfd49ec-1c4f-4618-bfdb-27db07e24f1c)

## 相關資訊

- **Jira:** [BE-1235](https://ctil.atlassian.net/browse/BE-1235)
- **解決方式:** Done