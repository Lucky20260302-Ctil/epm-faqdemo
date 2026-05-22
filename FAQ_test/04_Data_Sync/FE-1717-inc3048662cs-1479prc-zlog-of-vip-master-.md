---
project: FE
issue_key: FE-1717
issue_type: Bug DEV
status: Closed
faq_score: 5.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, interface]
jira_url: "https://ctil.atlassian.net/browse/FE-1717"
created: 2025-06-24
resolved: 
resolution: 
has_images: False
---

# FE-1717: [INC3048662][[CS-1479]]PRC Zlog of VIP Master still send to FE

> **類型:** Bug DEV | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 5.0
> **負責人:** Joy Li
> **組件:** interface

## 問題描述

PRC Zlog of VIP Master still send to FE [📎附件](https://ctil.atlassian.net/rest/api/3/attachment/content/7a2e505a-8f19-47a0-aaa0-3d09a5a28087) 




## Jira Comments

> **Joy Li** (2025-06-26):
>    send log program should skip the member detail , bouns point and sales figure which member type is set to “NOT donwload“. But today CN is sending those member detail to FE via zlog.  could you please help to check the send log logic?

> **Cy Lau** (2025-06-26):
>  wait for Jerry logic trace ETA 1100

> **Jerry Wong** (2025-06-26):
>  set dbtmnlog_gen = ‘X' if member type is not download ‘Y’ where dbtmnlog_table_name in vip, vipfig, vipdef and viprgpts. During send zlog, only dbtmnlog_gen = ' ’ would be selected 

> **Andrew_Au** (2025-09-08):
>       Please ticket status

> **Tovi Wang** (2025-09-08):
> Should be same duplicate issue with internal Jira  .Will double confirm with     

> **Andrew_Au** (2025-09-14):
>       Please ticket status

> **Automation for Jira** (2025-10-08):
> Issue has been created since Days since: 105 Week since : 15 Issue due date difference Days since :  Weeks since: 

> **Andrew_Au** (2025-10-28):
>      Pending for a long time. Please update the status.

> **Tovi Wang** (2025-10-28):
>  Since we can’t reproduce this issue in our QA.So we are keep monitoring this issue in pro with Coach team.Hold on please.

> **Tovi Wang** (2025-10-29):
> This issue has not occurred again in Pro.Closed first.Keep monitoring in pro.

## 相關資訊

- **Jira:** [FE-1717](https://ctil.atlassian.net/browse/FE-1717)