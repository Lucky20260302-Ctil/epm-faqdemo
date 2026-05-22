---
project: BE
issue_key: BE-1220
issue_type: Bug PRD
status: Open
tags:
- 04_data_sync
- be
- data-interface
- data_sync
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1220
created: '2025-12-04'
resolved: ''
fix_version: ''
components: []
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'BE-1220: Exclude LGV miscalculation of Pangdonglai interface & modify Not export logic'
---
# BE-1220: Exclude LGV miscalculation of Pangdonglai interface & modify Not export logic 

## 問題描述

Hi Lein,

 

As to confirm, we will make the below fixing on **both existing** Pangdonglai interface for OC331 and the **new** interface for OC334.

 

Bug fix covered:

 

1. Currently LGV is miscalculated that excluding more amount as expected. so will correct the calculation logic of LGV exclusion.

 

2. New request from Lein (not a program bug) that to add checking in export program that NOT sending the request to landlord if the accumulated amount "c_amount" is 0.

As-Is: NOT sending when c_qtty = 0

To-Be: NOT sending when c_amount = 0 

 

case 1: if +ve sales amount is 0 and -ve one is not 0 -> only export -ve payload

case 2: if +ve sales amount is not 0 and -ve one is 0 -> only export +ve payload

case 3: if +ve sales amount is not 0 and -ve one is not 0 -> export +ve & -ve payload

case 4: if +ve sales amount is 0 and -ve one is 0 -> Not expo



## 相關資訊

- **Jira:** [BE-1220](https://ctil.atlassian.net/browse/BE-1220)