---
project: FE
issue_key: FE-1375
issue_type: SOW
status: Closed
faq_score: 5.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, fe, data_sync, cs2kconnect, mqpolling]
jira_url: "https://ctil.atlassian.net/browse/FE-1375"
created: 2024-04-30
resolved: 2024-06-07
resolution: Done
has_images: False
---

# FE-1375: Alibaba Cloud OSS

> **類型:** SOW | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 5.0
> **解決日期:** 2024-06-07
> **負責人:** Bobby
> **組件:** CS2kconnect, MQPolling

## 問題描述

*** FTP and OSS will run parallel in pilot *** 

Front End: [FE-1388]

cs2kconnect 

- pc file upload

- zlog download

- tranffic file upload

Back End :

CS2000 Main Program  (App Sever)

- polling point create OSS folder

- zlog send to OSS folder

- offpolling (pick up pos files from oss folder)

OSS polling (New program in MQ Server) 

- Two New OSS table (sqlpcdXX, sqlpcdXXN1)

- new posting task for new node

- Access OSS folder to get record and insert to sqlpcdXX



## 相關資訊

- **Jira:** [FE-1375](https://ctil.atlassian.net/browse/FE-1375)
- **解決方式:** Done