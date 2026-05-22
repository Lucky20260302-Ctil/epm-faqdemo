---
project: FE
issue_key: FE-1271
issue_type: Bug QA
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- fe
- front-end-v720.02
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1271
created: '2023-06-30'
resolved: '2023-11-16'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1271: Open item applied an unusable coupon but still dislpay the unusable coupon'
---
# FE-1271: Open item applied an unusable coupon but still dislpay the unusable coupon

## 問題描述

Reproduce steps:

1. To sales memo page & set an Open item

2. Try to apply a unusable coupon

3. Pop up a dialog: XXX, this coupon can't be used in this coupon & click on OK

4. Back to payment page

Existing result:

Still dislpay the unusable coupon (as below screenshot)

 

Remark:

- Same issue also occur in deposit section

VM : 172.16.138.113

Version: 7.2.0.02R23B (build230628)

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/72edc9a5-fd5e-49bf-b6e4-084dbe05057f)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/72edc9a5-fd5e-49bf-b6e4-084dbe05057f)

## 相關資訊

- **Jira:** [FE-1271](https://ctil.atlassian.net/browse/FE-1271)
- **解決方式:** Done