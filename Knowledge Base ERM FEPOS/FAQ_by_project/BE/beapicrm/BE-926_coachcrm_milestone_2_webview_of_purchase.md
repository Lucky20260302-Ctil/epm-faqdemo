---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "[Coach][CRM milestone 2] Webview of Purchase history pop up network error"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-926
resolved: 2024-11-01
fix-version: ""
---

# BE-926: [Coach][CRM milestone 2] Webview of Purchase history pop up network error

## 問題

[Coach][CRM milestone 2] Webview of Purchase history pop up network error
When Config of 3P Module Config in vbretail.ini use IP name as domin, webview pop up fail to connect network error:
[3P Module Config]
InstallationPath="[https://erm-coach-be7.sanyoextended.com/BEGWCRM_CN"](https://erm-coach-be7.sanyoextended.com/BEGWCRM_CN%22)
*Works fine if Config of 3P Module Config use IP address as domin:
[3P Module Config]
InstallationPath="[https://172.16.138.8/BEGWCRM_CN](https://172.16.138.8/BEGWCRM_CN)"
Front end Config location: C:\Program Files\CSPLUS\vbretail.ini

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-11-01
### Jira Comments (1 則)
**Sherman tse** (2024-11-01):
DNS issue occured in QA env  only
Close case

## 相關資訊

- Jira: [BE-926](https://ctil.atlassian.net/browse/BE-926)
- Fix Version: 未記錄
- 解決日期: 2024-11-01
