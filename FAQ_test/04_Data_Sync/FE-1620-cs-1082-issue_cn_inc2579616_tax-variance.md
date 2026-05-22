---
project: FE
issue_key: FE-1620
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1620
created: '2025-02-03'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1620: [CS-1082] Issue_CN_INC2579616_Tax variance for OC183 – 10008908 (incorrect VAT & GST amount)'
---
# FE-1620: [CS-1082] Issue_CN_INC2579616_Tax variance for OC183 – 10008908 (incorrect VAT & GST amount)

## 問題描述

WECHAT Coupon -$100 counted as 2 time causing the incorrect GST amount

OC183- 10008908

Found log & data in \\172.16.183.201\localuser\support\^^DiscountVariance_2024\ 

POS Version Ver. 7.2.0.02R23E

> 📎 **image-20250203-025939.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/600a0488-2147-4de7-81f4-cf72d9947c1a)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250203-025939.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/600a0488-2147-4de7-81f4-cf72d9947c1a)


## Jira Comments

> **Sherman tse** (2025-02-03):
> I will try to reproduce the issue in our qa env later

> **Tovi Wang** (2025-02-05):
>   Many Thanks for your support.

> **Tovi Wang** (2025-02-06):
>  Could you help to take a look this VAT & TAX issue if can be covered in R10?Thanks!

> **pierre.shi** (2025-02-06):
> Hi Teams, this issue occurred again:OC131-00023592.

> **Sang** (2025-02-11):
>  I can’t re-produce OC183 – 10008908 case. Regarding OC131-00023592, please get all logs from OC131. thanks

> **Sang** (2025-02-11):
>      only one E-coupon found in db. But from NPOS log,  seems same coupon have  been applied two time.    Regarding OC131-00023592, please get all logs, dbtrans.sdf and dbmas or mastconv.dat also.  

> **pierre.shi** (2025-02-12):
> Hi    logs have been uploaded as attachment.

> **Sang** (2025-02-14):
>  please help to get one set of mastconv files to build dbmas. Thx

> **pierre.shi** (2025-02-14):
> Hi   dbmas has been uploaded as attachment.

> **Sang** (2025-02-17):
>  where is dbmas ?

> **pierre.shi** (2025-02-17):
> Hi   I have re-uploaded the dbmas again, maybe not successfully upload last time.

> **Sang** (2025-02-20):
>  Can’t find dbmas in attachment. Please upload again.

> **pierre.shi** (2025-02-24):
> Hi    dbmas has been uploaded. please follow onedrive path: 20250224-OC131dbmas

> **Ken Wang** (2025-02-25):
> The ticket pending for a long time. Please update the ticket status

> **Tovi Wang** (2025-03-03):
>   Could you got the Dbmas now?Let me know the update.Because same issue still happenning.Thanks!

> **Andrew_Au** (2025-03-21):
>     The ticket pending for a long time. Please update the ticket status

> **Tovi Wang** (2025-03-21):
>  May I know anything update please? CC     

> **Sang** (2025-05-15):
>  can’t re-produce in v7202.02R23 and v750.04R13  cc     

> **Tovi Wang** (2025-05-16):
>  So how do we replied to Coach team?Thanks! CC       

> **Tovi Wang** (2025-05-30):
> Dear ALL, Because can’t reproduce  in v7202.02R23 and v750.04R13，We will keep monitoring this issue with Coach team. Ticket hold on!

> **Andrew_Au** (2025-08-28):
>    The ticket hold for a long time. Could you confirm the ticket current status.

> **Tovi Wang** (2025-08-29):
> Coach Team Testing is passed, but not deployed to PRD yet,Closed first.

## 相關資訊

- **Jira:** [FE-1620](https://ctil.atlassian.net/browse/FE-1620)