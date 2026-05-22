---
project: BE
issue_key: BE-1146
issue_type: Bug PRD
status: Design
tags:
- 04_data_sync
- be
- data_sync
- faq
- polling
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1146
created: '2025-07-10'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-1146: [CS-1479] Issue_PRC_Member update information will send to FE by Zlog file'
---
# BE-1146: [CS-1479] Issue_PRC_Member update information will send to FE by Zlog file

## 問題描述

Issue Detail

Conformed in Current CS2000 version C/B/V/A member information update will be send to FE by Zlog

> 📎 **image-20250710-014939.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/8377f192-648a-456f-9ff9-fb9513776d51)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250710-014939.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/8377f192-648a-456f-9ff9-fb9513776d51)


## Jira Comments

> **Tovi Wang** (2025-07-10):
>     Internal Jira here.Please help to further checking.If need other info please ping me.Thanks!

> **Joy Li** (2025-07-14):
>  i checked that current send log program will send member master which member type should eb “NOT downlaod”. May i know if you need the log for checking>? cc   

> **Jerry Wong** (2025-07-14):
>  I need the log, and also what is the Date modified of the prj_di8004.dll

> **Automation for Jira** (2025-07-14):
> Issue has been created since Days since: 4 Week since : 0 Issue due date difference Days since :  Weeks since: 

> **Jerry Wong** (2025-07-14):
>  the vip type is “NOT downlaod” = ‘Y' is also not update dbtmnlog_gen to 'X’ when send log in QA?

> **Joy Li** (2025-07-14):
> i remember that we tested in QA beofre. it should work in QA.

> **Jerry Wong** (2025-07-14):
>  QA and prod are same version?

> **Tovi Wang** (2025-07-21):
>    May I know anything update for this case?Which version?FE version or BE version?

> **Jerry Wong** (2025-07-21):
>  Can I have the data of dbtmnlog, vip and viptyp which is supposed not in the Zlog but sent to FE?  I want to insert to my local db and do the test in my envionment

> **Tovi Wang** (2025-07-22):
>  Follow dbtmnlog data for your further checking.Thanks! select * from dbtmnlog where dbtmnlog_date >= '2025-07-01' and dbtmnlog_record_key in (select vip_no from vip where vip_type in ('C','V')) and dbtmnlog_gen = 'Y'  

> **Tovi Wang** (2025-08-26):
>  May I know if anything new found for this issue?Please help to share the investigate progress.Thanks! CC    

> **Andrew_Au** (2025-10-08):
>    Please update the status

> **Tovi Wang** (2025-10-09):
> Duplicate with  ,Let us follow up this issue in  ,Please closed this one first.

## 相關資訊

- **Jira:** [BE-1146](https://ctil.atlassian.net/browse/BE-1146)