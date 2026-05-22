---
project: BE
issue_key: BE-934
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
jira_url: https://ctil.atlassian.net/browse/BE-934
created: '2024-11-06'
resolved: '2024-12-03'
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-934: MF0001 Show the wrong retail'
---
# BE-934: MF0001 Show the wrong retail

## 問題描述

Once we create the onsales record, it make the MF0001 show the work price record. Please refer below showshort.

> 📎 **image-20241106-014409.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/00960989-0590-456e-9519-909161485a02)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20241106-014409.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/00960989-0590-456e-9519-909161485a02)


## Jira Comments

> **Andrew_Au** (2024-11-06):
>      

> **Andrew_Au** (2024-11-06):
> 

> **Andrew_Au** (2024-11-06):
>  

> **Bobby** (2024-11-06):
> Since the Additional Retail Price page shows the On Sale Price Record in Item Master Maintenance. We need to filter the On Sale Price Record by the following logic. select * from itmprx where (isnull(itmprx_onsale_disc_1,'') = ‘' and isnull(itmprx_onsale_disc_2,'') = '' and itmprx_sell_price_bx = 0) or (itmprx_sell_price_bx <> 0)

> **Jerry Wong** (2024-11-08):
> Prorunner Backend Web Release \\ds411\CSMS70\delivery\prorunner\UAT\Backend (Web)\2024-11-07 Prorunner Backend .Net Release \\ds411\CSMS70\delivery\prorunner\UAT\BackEnd.Net\2024-11-07 Lands Backend Web Release \\ds411\CSMS70\delivery\lands\UAT\Backend (Web)\2024-11-07 Lands Backend .Net Release \\ds411\CSMS70\delivery\lands\UAT\Backend.Net\2024-11-07

> **Cy Lau** (2024-12-02):
>   Please state the source patch / control on  BackEnd.Net

> **Cy Lau** (2024-12-02):
> Current state treat as  Not include Coach

> **Andrew_Au** (2024-12-03):
> Updated the web application and .net application to Prorunner production environment.

> **Jerry Wong** (2024-12-03):
>   Prorunner Backend API https://git.e-tendering.com/erm1/chainstoreplus-enterprise-management-system/chainstoreplus-backend-api/-/tree/Prorunner-2024-10-04-OR0005-Update?ref_type=heads Lands Backend API https://git.e-tendering.com/erm1/chainstoreplus-enterprise-management-system/chainstoreplus-backend-api/-/tree/2024/11/06-Fix-BE-934-MF0001-Show-the-wrong-retail?ref_type=heads

## 相關資訊

- **Jira:** [BE-934](https://ctil.atlassian.net/browse/BE-934)
- **解決方式:** Done