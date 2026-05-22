---
project: FE
title: "FE-793: ticket:2020141 sales memo, discrepancy found in posted data"
issue_key: FE-793
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, frontend, sales]
jira_url: "https://ctil.atlassian.net/browse/FE-793"
created: 2020-10-06
resolved: 2020-11-11
resolution: Done
has_images: True
---

# FE-793: ticket:2020141 sales memo, discrepancy found in posted data

## 問題描述

I can reproduce that will miss an item adjustment record in db and PCD when trigger the MM BPSAL-HK20901A(giveaway: buy 7 ,free 4).

db copied in \\172.16.183.201\localuser\support\20201006\bpshkg29 

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/1dc2bd1c-88fd-44f1-a40b-a8cb39cb7fb4)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/1dc2bd1c-88fd-44f1-a40b-a8cb39cb7fb4)

## 相關資訊

- **Jira:** [FE-793](https://ctil.atlassian.net/browse/FE-793)
- **解決方式:** Done