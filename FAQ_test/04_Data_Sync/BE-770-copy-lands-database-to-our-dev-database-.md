---
project: BE
issue_key: BE-770
issue_type: Task
status: Closed
faq_score: 4.5
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, administration]
jira_url: "https://ctil.atlassian.net/browse/BE-770"
created: 2023-06-21
resolved: 2023-07-07
resolution: Done
has_images: False
---

# BE-770: Copy LANDS database to our DEV database environment (172.16.138.128)

> **類型:** Task | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 4.5
> **解決日期:** 2023-07-07
> **負責人:** Andrew_Au
> **組件:** Administration

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