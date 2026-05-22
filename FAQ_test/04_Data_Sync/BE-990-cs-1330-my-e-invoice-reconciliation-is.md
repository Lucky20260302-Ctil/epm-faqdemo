---
project: BE
title: "BE-990: [CS-1330] - MY E-invoice Reconciliation Issue"
issue_key: BE-990
issue_type: Bug PRD
status: Closed
faq_score: 5.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-990"
created: 2025-01-22
resolved: 2025-05-06
resolution: Done
has_images: True
---

# BE-990: [CS-1330] - MY E-invoice Reconciliation Issue

## 問題描述

we got callout from BDO side, for below Coach MY transaction at Jan-19, total amount send to BDO is incorrect, I've check the log on that day, CS2K do miss line item send to BDO. Log attached, could you please help to further check? Thanks

> 📎 **image-20250122-022554.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/6d719595-b2b7-477c-8578-a97b72d2880f)（需 Jira 登入）
1.OCF75-20192764

DB total amount: 1806

> 📎 **image-20250122-030815.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7932ee8a-6a0a-4b67-abf1-2693a8b53547)（需 Jira 登入）
2.OCF75-20192764

MY_Einvoice log total amount(BDO): 1521

Variance is 285,Missing the item CT743  285 amount.                       

> 📎 **image-20250122-030950.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/509636c8-ba7c-4c31-991e-69c070a45eb4)（需 Jira 登入）

> 📎 **image-20250122-031343.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/463ac844-d3bd-45b0-ae6f-71b0a1a8b2a0)（需 Jira 登入）
3.sqlp

> 📎 **image-20250123-045747.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/af2daf39-94fc-4538-8d2b-2bfb4e3f1bae)（需 Jira 登入）
cd table



## 附件截圖

1. 📎 **image-20250122-022554.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/6d719595-b2b7-477c-8578-a97b72d2880f)
2. 📎 **image-20250122-030815.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/7932ee8a-6a0a-4b67-abf1-2693a8b53547)
3. 📎 **image-20250122-030950.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/509636c8-ba7c-4c31-991e-69c070a45eb4)
4. 📎 **image-20250122-031343.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/463ac844-d3bd-45b0-ae6f-71b0a1a8b2a0)
5. 📎 **image-20250123-045747.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/af2daf39-94fc-4538-8d2b-2bfb4e3f1bae)


## Jira Comments

> **Tovi Wang** (2025-01-22):
>  log here.If need anything other logs,Please ping me here.Thanks!

> **Anson Cheung** (2025-01-22):
>  can you provide the records of: ‘jouinv’, ‘joudis’, ‘itmast’ of these two documents?

> **Tovi Wang** (2025-01-22):
>  After checked the DB & Einvoice log,Found Variance is 285,Missing the item CT743 285 amount.Description detials for your refrence.Please check why the 285 amount for item CT743 missing in the log?Please double check the send logic.Thanks!

> **Anson Cheung** (2025-01-22):
>  can you provide the result of these two sql? select top 1 rtrim(dbconfig_long_value) COLLATE Latin1_General_CI_AS from dbconfig where dbconfig_key='BDO_GWP_cat_filters'
> SELECT * FROM itmast WHERE itmast_item_no = 'CT743'

> **Tovi Wang** (2025-01-22):
>  FYI.

> **Anson Cheung** (2025-01-22):
>  can you help to get the result? Thanks. DECLARE @frdate nvarchar(20) = '20250101'
> DECLARE @todate nvarchar(20) = '20250120'
> DECLARE @divisionCode nvarchar(20) = '0200'
> 
> DECLARE @BDO_GWP_cat_filters NVARCHAR(MAX) = ''
>                                 select top 1 @BDO_GWP_cat_filters = rtrim(dbconfig_long_value) COLLATE Latin1_General_CI_AS from dbconfig where dbconfig_key='BDO_GWP_cat_filters'
> 
>                                 SELECT loctab_code 
>                                 INTO #ec_loctab
>                                 FROM loctab WITH (NOLOCK)
>                                 WHERE loctab_code like 'OCE%' OR loctab_type = 'E' OR loctab_depart_store = 'Y'
> 
> 								SELECT * INTO #jougic
> 								FROM jougic WITH (NOLOCK)
> 								WHERE jougic_date BETWEEN @frdate
> 										AND @todate
> 			

> **Tovi Wang** (2025-01-22):
>  FYI.Thanks!

> **Anson Cheung** (2025-01-22):
>  the sql result is normal, documents can return the correct amount.  Could you check if multiple pdc were posted? I suspect the data was incomplete during the first scan.

> **Tovi Wang** (2025-01-22):
>  Posting log here.Please check.

> **Anson Cheung** (2025-01-23):
> The issue can be confirmed as caused by the interface retrieving invoice while the data is still posting, resulting in incomplete data. An enhancement is needed.

> **Tovi Wang** (2025-01-23):
>   Many Thanks for your keep updating.May I know the about time of ETA for the enhancement?Thanks!

> **Tovi Wang** (2025-01-23):
> sqlpcd table

> **Tovi Wang** (2025-01-23):
> Another same issue memo OCF79-10112802 for your reference.Just only first line send to BDO.

> **Tovi Wang** (2025-01-23):
> Resend MY E-invoice to BDO for bellow 2 memo 1.OCF75 - 20192764 2.OCF79 - 10112802

> **Anson Cheung** (2025-01-23):
> Release:   \\ds411\public\anson\MY_eInvoice \MY_eInvoice_v1.0.0_20250123.zip Release notes: new appsettings.json 'scanDelayMin', default: 10  do not scan jouinv data created within the configured number of minutes('scanDelayMin') to prevent scanning incomplete data during posting

> **Tovi Wang** (2025-02-05):
>  Please help to testing this issue.Thanks!

> **Sherman tse** (2025-02-06):
> Verified on QA Attached test case  

> **Tovi Wang** (2025-04-07):
>  Coach team callout BDO receive incomplete sales amt data for bellow 2 sales memo. After checked the log,I just only find the first item sales data in log,But missing the second item sales data.Please help to double check and confirm the RCA?Thanks!   1. OCF77-20229270 2025-03-18 OCF79-10119181 2025-03-20 2.OCF77-20229270 2025-03-18 3.OCF79-10119181 2025-03-20

> **Anson Cheung** (2025-04-09):
>  This case has same cause with last callout. By config, program scans the memo not within 10 mins, but the posting is done after 18 mins. I suggest setting the  scanDelayMin  config to 20.

> **Andrew_Au** (2025-05-02):
>    Please update the ticket status

> **Tovi Wang** (2025-05-06):
> data patch done and will keep monitoring.Closed firstly.

## 相關資訊

- **Jira:** [BE-990](https://ctil.atlassian.net/browse/BE-990)
- **解決方式:** Done