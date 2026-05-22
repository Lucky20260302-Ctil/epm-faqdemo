---
project: BE
issue_key: BE-770
issue_type: Task
status: Closed
tags:
- 04_data_sync
- administration
- be
- data_sync
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-770
created: '2023-06-21'
resolved: '2023-07-07'
fix_version: ''
components: []
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-770: Copy LANDS database to our DEV database environment (172.16.138.128)'
---
# BE-770: Copy LANDS database to our DEV database environment (172.16.138.128)

## 問題描述

Due to the RGM data sync development.

Could you copy LANDS RGM database to our DEV database(172.16.138.128)? So @@Jerry Wong  can develop, and test based on the database.

The database info is below:

**Lands UAT RGM database info:**
The PMSS DB server 10.77.227.30 in UAT platform has the access to the OSS_RGM database of the HKMS 2.0 UAT site, using the following info:
    SqlInstance = "10.109.74.101,1433"
    SqlDB = "OSS_RGM"
    SqlUser = "poss1gUser"
    SqlPWD = "Shn1sfqmsu@"

**Lands POS** **10.77.227.30** **UAT database info:**

login: csuser

pw: csuser

**DB server 10.77.227.30 remote desktop login:**
Administrator
P@ssw0rd1234#



## 相關資訊

- **Jira:** [BE-770](https://ctil.atlassian.net/browse/BE-770)
- **解決方式:** Done