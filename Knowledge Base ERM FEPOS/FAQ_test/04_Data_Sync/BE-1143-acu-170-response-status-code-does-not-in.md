---
project: BE
issue_key: BE-1143
issue_type: Task
status: Closed
faq_score: 4.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-1143"
created: 2025-07-04
resolved: 2025-07-04
resolution: Done
has_images: False
---

# BE-1143: [ACU-170] Response status code does not indicate success: 404 (Not Found) while processing async update for member

> **類型:** Task | **狀態:** Closed
> **分類:** 資料與同步 | **FAQ 分數:** 4.0
> **解決日期:** 2025-07-04
> **負責人:** Joy Li
> **組件:** Data Interface

## 問題描述

None


## Jira Comments

> **Joy Li** (2025-07-04):
> Software Release Note   Installation Prerequisites Back Office Release V70R3.101 must be installed before installing this release.   Release Media COACH_L4.0.0_V70R3.104.zip Web Folder – ChainStorePlus WEB Server update ChainStorePlusv7 R3.104 Servers Installation Guide v1.0.docx - This release note Test case of [ACU-170] CRM Async update.xlsx   Changes in This Release Web Server: [ACU-170] Response status code does not indicate success: 404 (Not Found) while processing async update for member Enhance the async update process logic to handle null value return of first name/ last name field during Member search   Impact modules: BEAPICRM.exe – CRM API module

> **Joy Li** (2025-07-04):
> released by Ken on 2025-05-20 with BE V70R3.104

## 相關資訊

- **Jira:** [BE-1143](https://ctil.atlassian.net/browse/BE-1143)
- **解決方式:** Done