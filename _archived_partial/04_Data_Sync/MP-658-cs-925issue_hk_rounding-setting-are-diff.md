---
project: MP
issue_key: MP-658
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- mp
- mpos-api
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-658
created: '2024-02-28'
resolved: '2024-07-12'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'MP-658: CS-925:Issue_HK_Rounding setting are different between POS and Mpos RIN01299427'
---
# MP-658: CS-925:Issue_HK_Rounding setting are different between POS and Mpos RIN01299427

## 問題描述

**Issue Detail**

\\172.16.183.201\localuser\support\JIRA_DB\

same item and same coupon, price should be 14458.5, it is 14459 on POS and 14458 on Mpos.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/5bec8a6f-a42d-4015-8303-b841aab48557)（需 Jira 登入）
 



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/5bec8a6f-a42d-4015-8303-b841aab48557)


## Jira Comments

> **Cy Lau** (2024-03-01):
> \\ds411\share\POS_MPOS_Release\3.28.X\3.28.1-20240301.1

## 相關資訊

- **Jira:** [MP-658](https://ctil.atlassian.net/browse/MP-658)
- **解決方式:** Done