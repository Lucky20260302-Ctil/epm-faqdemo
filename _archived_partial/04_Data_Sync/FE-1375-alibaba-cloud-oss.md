---
project: FE
issue_key: FE-1375
issue_type: SOW
status: Closed
tags:
- 04_data_sync
- cs2kconnect
- data_sync
- faq
- fe
- mqpolling
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1375
created: '2024-04-30'
resolved: '2024-06-07'
fix_version: ''
components: []
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1375: Alibaba Cloud OSS'
---
# FE-1375: Alibaba Cloud OSS

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