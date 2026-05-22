---
tags: [faq, be, beapicrm]
component: "Backend (V66)"
symptom: "[Coach][CRM milestone 2] Enhancement the Backend data sync function when program able to send order "
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-943
resolved: 2024-11-19
fix-version: ""
---

# BE-943: [Coach][CRM milestone 2] Enhancement for the Backend data sync function when program able to send order to crm but fail to send member 

## 問題

[Coach][CRM milestone 2] Enhancement the Backend data sync function when program able to send order to crm but fail to send member

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-11-19
### Jira Comments (2 則)
**Anson Cheung** (2024-11-13):
Approach:
If fail to send member, skip the send orders process and log crmlog_success= ‘N' to crmlog table. 
The orders logged crmlog_success = 'N’ will be rescan in next scheduled process.
**Sherman tse** (2024-11-19):
Verified on QA

## 相關資訊

- Jira: [BE-943](https://ctil.atlassian.net/browse/BE-943)
- Fix Version: 未記錄
- 解決日期: 2024-11-19
