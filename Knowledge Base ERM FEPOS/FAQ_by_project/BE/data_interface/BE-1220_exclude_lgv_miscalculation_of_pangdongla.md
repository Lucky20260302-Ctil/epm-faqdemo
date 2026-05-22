---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "Hi Lein,"
root-cause: "待提取"
solution: "### Jira Comments (1 則)"
jira: BE-1220
resolved: 
fix-version: ""
---

# BE-1220: Exclude LGV miscalculation of Pangdonglai interface & modify Not export logic 

## 問題

Hi Lein,
As to confirm, we will make the below fixing on **both existing** Pangdonglai interface for OC331 and the **new** interface for OC334.
Bug fix covered:
1. 
1. 
As-Is: NOT sending when c_qtty = 0
To-Be: NOT sending when c_amount = 0
case 1: if +ve sales amount is 0 and -ve one is not 0 -> only export -ve payload
case 2: if +ve sales amount is not 0 and -ve one is 0 -> only export +ve payload
case 3: if +ve sales amount is not 0 and -ve one is not 0 -> export +ve & -ve payload
case 4: if +ve sales amount is 0 and -ve one is 0 -> Not expo

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (1 則)
**Jerry Wong** (2025-12-04):
# Release:
[\\DS411\csms60\delivery\coach\Coach_Pangdonglai-2025-12-04](file://DS411/csms60/delivery/coach/Coach_Pangdonglai-2025-12-04)
# Notes:
- 
- 
- 
# Sources:
[http://172.16.138.42:3000/ERM/Coach_Pangdonglai/commits/branch/Coach_Pangdonglai_OC331/](http://172.16.138.42:3000/ERM/Coach_Pangdonglai/commits/branch/Coach_Pangdonglai_OC331/)

## 相關資訊

- Jira: [BE-1220](https://ctil.atlassian.net/browse/BE-1220)
- Fix Version: 未記錄
- 解決日期: 未記錄
