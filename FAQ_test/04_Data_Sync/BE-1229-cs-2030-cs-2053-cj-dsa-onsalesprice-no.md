---
project: BE
issue_key: BE-1229
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- api
- be
- data_sync
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-1229
created: '2026-02-05'
resolved: '2026-02-26'
fix_version: ''
components: []
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-1229: [CS-2030] -[CS-2053]  CJ DSA OnSalesPrice not effective owing to ZeroLength Temp solution'
---
# BE-1229: [CS-2030] -[CS-2053]  CJ DSA OnSalesPrice not effective owing to ZeroLength Temp solution

## 問題描述

Temp Solution as Data patching with .BAT 

for case startDate = EndDate with 00:00:00.000




## Jira Comments

> **Cy Lau** (2026-02-05):
> Scenario :  both the  effective-from  and  effective-to  datetimes are identical. Because of this, PriceChecker returns a result with  no OnSalePricing . Current DateTime:  2026-02-03 16:34 fromDateTime:  2026-02-03 00:00:00 toDateTime:  2026-02-03 00:00:00 Although the  fromDateTime  is valid, it is immediately invalidated by the  toDateTime . The POS system currently handles cases where  fromDate = toDate  with a time of  00:00:00 , but  PriceChecker does not  handle this scenario. Before the latest version of PriceCheckerJP delivery,  Avoid using 00:00:00 when fromDate = toDate Use  23:59:59  for the  toDateTime  instead (as in the existing test case), ensuring the full day is covered. Yet, SAP dataset is not available for this changes, so schedule data patch on  itmprx_onsale_to_date_1

> **Cy Lau** (2026-02-05):
> Definintions :  itmprx_onsale_fr_date_1 OnSalePrice 1 effects from DateTime itmprx_onsale_to_date_1 OnSalePrice 1 effects up to DateTime(End) onsale_fr_date_2 OnSalesPrice 2 effects from DateTime onsale_to_date_2 OnSalePrice 2 effects up to DateTime(End) Zero-length effective period itmprx_onsale_fr_date_1 = itmprx_onsale_to_date_1, with 00:00:00 onsale_fr_date_2 = onsale_to_date_2 , with 00:00:00 Deliverables :  Please help to place in DS411 File structure:  File type Description check_patch_itmprx.bat batch Check any from Day before running date to future for zero-length effetive period requires: verify_zero_length.sql test_patch_itmprx.bat batch Test connectivity requires: verify_connectivity.sql run_patch_itmprx.bat batch Data patch for from Day before running date to future for zero-l

> **Automation for Jira** (2026-02-05):
> Issue has been created since Days since: 0 Week since : 0 Issue due date difference Days since :  Weeks since: 

> **Andrew_Au** (2026-02-23):
>   Please update the Jira ticket status

> **Sherman tse** (2026-02-23):
> Verified ok on QA with release: \\ds411\public\daniel\pricechecker\20260223.1_JP_fullset  

> **Joy Li** (2026-02-26):
> ken will release on 2026-02-27 with V70R3.145

## 相關資訊

- **Jira:** [BE-1229](https://ctil.atlassian.net/browse/BE-1229)
- **解決方式:** Done