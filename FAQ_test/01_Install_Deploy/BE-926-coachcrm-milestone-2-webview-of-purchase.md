---
project: BE
issue_key: BE-926
issue_type: Bug QA
status: Closed
faq_score: 8.5
faq_category: 01_Install_Deploy
faq_category_label: 安裝與部署
tags: [faq, be, install_deploy, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-926"
created: 2024-10-25
resolved: 2024-11-01
resolution: Done
has_images: False
---

# BE-926: [Coach][CRM milestone 2] Webview of Purchase history pop up network error

> **類型:** Bug QA | **狀態:** Closed
> **分類:** 安裝與部署 | **FAQ 分數:** 8.5
> **解決日期:** 2024-11-01
> **負責人:** Daniel Leung
> **組件:** Backend (Web)

## 問題描述

[Coach][CRM milestone 2] Webview of Purchase history pop up network error

When Config of 3P Module Config in vbretail.ini use IP name as domin, webview pop up fail to connect network error:

[3P Module Config]
InstallationPath="[https://erm-coach-be7.sanyoextended.com/BEGWCRM_CN"](https://erm-coach-be7.sanyoextended.com/BEGWCRM_CN%22)

*Works fine if Config of 3P Module Config use IP address as domin:

[3P Module Config]
InstallationPath="[https://172.16.138.8/BEGWCRM_CN](https://172.16.138.8/BEGWCRM_CN)" 

Front end Config location: C:\Program Files\CSPLUS\vbretail.ini



## 相關資訊

- **Jira:** [BE-926](https://ctil.atlassian.net/browse/BE-926)
- **解決方式:** Done