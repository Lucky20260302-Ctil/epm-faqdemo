---
project: BE
issue_key: BE-800
issue_type: Bug QA
status: Closed
tags:
- 04_data_sync
- backend-(web)
- be
- data_sync
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-800
created: '2023-09-01'
resolved: '2023-10-09'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-800: [Lands] GFMIS report doesn''t dsiplay creadit card (inserted by manual) payment method'
---
# BE-800: [Lands] GFMIS report doesn't dsiplay creadit card (inserted by manual) payment method

## 問題描述

GFMIS report doesn't dsiplay creadit card (inserted by manual) payment method:

Highlighted part should be displayed Mastercard

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9fedfc65-bb66-4164-bb6a-fa6b9a1b9225)（需 Jira 登入）
Payment method of that record paid by Mastercard, the method is made by manual card, means mastercard's card details inserted by user.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/332b93d4-0672-4200-86f7-3e9d85466a14)（需 Jira 登入）


## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9fedfc65-bb66-4164-bb6a-fa6b9a1b9225)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/332b93d4-0672-4200-86f7-3e9d85466a14)


## Jira Comments

> **Hans Wong** (2023-09-07):
> There are only 4 types for LANDS. Cash, Cheque, Credit card and SVF (Wechat/Ali Pay). The criteria is below: CASE
> WHEN paytab.paytab_chg_flag='Y' THEN 'Cash' WHEN paytab.paytab_chg_flag='2' THEN 'Octopus' WHEN paytab.paytab_chg_flag='L' THEN 'Cheque'
> WHEN (paytab.paytab_chg_flag='A' AND UPPER(paytab_s9000_type) IN ('VISA','MASTERCARD','JCB','AMEX','UNIONPAY'))
> OR (paytab.paytab_chg_flag='C' AND UPPER(paytab_code) IN ('018','022')) THEN 'Credit card'
> WHEN paytab.paytab_chg_flag='A' AND UPPER(paytab_s9000_type) IN ('ALIPAY','WECHAT PAY')
> OR (paytab.paytab_chg_flag='C' AND UPPER(paytab_code) IN ('WEC')) THEN 'SVF'
> END

> **Sherman tse** (2023-09-18):
> Verified on QA env 172.16.138.55

> **Sherman tse** (2023-10-09):
> Verified on UAT env Lands

## 相關資訊

- **Jira:** [BE-800](https://ctil.atlassian.net/browse/BE-800)
- **解決方式:** Done