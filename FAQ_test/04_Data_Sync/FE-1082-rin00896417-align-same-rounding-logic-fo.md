---
project: FE
issue_key: FE-1082
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- fe
- frontend
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1082
created: '2022-01-28'
resolved: '2022-07-12'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1082: [RIN00896417] Align same Rounding logic for both parts in FE dayend report'
---
# FE-1082: [RIN00896417] Align same Rounding logic for both parts in FE dayend report

## 問題描述

**<u>Issue</u>**
User reflected that different amount is showing in two parts of FE dayend report.
By further checking, Properly one is based on 35000 (Round down 35000.90), and the other is based 35001 (rounding 35000.90).

**<u>Request</u>**
Client would like to align both parts by applying same Rounding logic. 

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/16587f59-be16-4929-b200-30e23661f30a)（需 Jira 登入）
 



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/16587f59-be16-4929-b200-30e23661f30a)

## 相關資訊

- **Jira:** [FE-1082](https://ctil.atlassian.net/browse/FE-1082)
- **解決方式:** Done