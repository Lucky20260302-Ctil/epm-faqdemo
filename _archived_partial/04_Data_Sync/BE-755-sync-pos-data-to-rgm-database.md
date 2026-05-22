---
project: BE
issue_key: BE-755
issue_type: Task
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
jira_url: https://ctil.atlassian.net/browse/BE-755
created: '2023-06-06'
resolved: '2023-11-10'
fix_version: ''
components: []
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-755: Sync POS data to RGM database'
---
# BE-755: Sync POS data to RGM database

## 問題描述

**Task:**

create a program for daily schedule task to sync data to RGM database.

**Data mapping and structure:**

data mapping and field structure according to the attachments.

Blue labeled table need to sync to RGM.

field CREATED_BY and MODIFIED_BY will be assigned to a fixed string from LANDS.

field CREATE_AT and MODIFIED_AT fill it if there is data field mapped otherwise fill by GETDATE().

field RECORD_ID is auto-increment.

table RGM Manual Receipt Registration and RGM Mechanised Receipt Registration insert once only at the beginning of year, the data is provided by Lands. Or maybe they will request to add a UI for data input. At this moment, not decided yet.

**Lands POS** **10.77.227.30** **UAT database info:**

login: csuser

pw: csuser

**DB server 10.77.227.30 remote desktop login:**
Administrator
P@ssw0rd1234#
**Lands UAT RGM database info:**
The PMSS DB server 10.77.227.30 in UAT platform has the access to the OSS_RGM database of the HKMS 2.0 UAT site, using the following info: 
    SqlInstance = "10.109.74.101,1433" 
    SqlDB = "OSS_RGM" 
    SqlUser = "poss1gUser" 
    SqlPWD = "Shn1sfqmsu@"



## 相關資訊

- **Jira:** [BE-755](https://ctil.atlassian.net/browse/BE-755)
- **解決方式:** Done