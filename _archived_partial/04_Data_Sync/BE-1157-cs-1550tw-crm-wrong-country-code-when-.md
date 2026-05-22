---
project: BE
issue_key: BE-1157
issue_type: Bug QA
status: Closed
tags:
- 04_data_sync
- api
- be
- data_sync
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-1157
created: '2025-08-11'
resolved: '2025-10-02'
fix_version: ''
components: []
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-1157: [CS-1550]TW CRM - Wrong Country Code when sending API Call'
---
# BE-1157: [CS-1550]TW CRM - Wrong Country Code when sending API Call

## 問題描述

Hi [Joy Li](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Joy_Li) (CC:[Tovi Wang](https://jira.tapestry.support/secure/ViewProfile.jspa?name=Tovi_Wang) ,[Abdulqadir Boxwala](https://jira.tapestry.support/secure/ViewProfile.jspa?name=aboxwala%40tapestry.com) ) , as per we talked today, kindly check the CRM logic for AWS region(SG MY TW KR), when we send the request to Axciom, the Country code was hardcode as CN.

{
  "path": "[https://apiqa.cdp.coach.com.cn/v2/cdp/profile/search"](https://apiqa.cdp.coach.com.cn/v2/cdp/profile/search%22),
  "header": [
   

{       "Key": "Accept",       "Value": [         "application/json"       ]     }

,
   

{       "Key": "X-Country-Code",       "Value": [         "CN"       ]     }

,
   

{       "Key": "Authorization",       "Value": [         "Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJwb3NfdWF0X3R3IiwidXNlcklkIjoiMTgxIiwibmFtZSI6InBvc191YXRfdHciLCJpZCI6IkFULTEtZUloSEtVZC1oLW1mMWVqd0d2dFpzYWd3RTFreEhNQ2oiLCJjbGllbnRJZCI6ImNkcCIsInJvbGVDb2RlcyI6IklOVEVSRkFDRSIsImV4cCI6MTc1NDY0NzY4Mn0.fb-Tp6UY8nZLNqYw3PKj4htYVdYKINqhJB-F3u4QOsVle476KDGvmP3Ls112O0qscSUvmLUpiilk7p_ORMrshXtVqA7KIg0q3XwfK0yyOOM1vQVib15SRmPILwm8AbalOi4W_ySecAM9H1_VMSQ_Fm8oXbZf_6hCCfAm0NhglfA"       ]     }

  ],
  "body": "{"pageSize":"100","pageNum":0,"queryCondition":{"operationType":"AND","subQueryConditions":[

{"key":"mobile","value":"0920250808","valueType":"STRING","operationType":"EQUALS"}

]}}"
}




## Jira Comments

> **Sherman tse** (2025-10-02):
> verified on QA

> **Automation for Jira** (2025-10-02):
> Issue has been created since Days since: 52 Week since : 7 Issue due date difference Days since :  Weeks since: 

## 相關資訊

- **Jira:** [BE-1157](https://ctil.atlassian.net/browse/BE-1157)
- **解決方式:** Done