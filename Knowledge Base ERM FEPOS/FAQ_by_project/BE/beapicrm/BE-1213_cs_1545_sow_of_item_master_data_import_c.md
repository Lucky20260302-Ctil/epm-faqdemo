---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "Due to requirements from the legal team, we need to prevent unexpected item description updates that"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1213
resolved: 2026-01-08
fix-version: ""
---

# BE-1213: [CS-1545] SOW of Item Master Data Import Customization

## 問題

Due to requirements from the legal team, we need to prevent unexpected item description updates that could impact compliance. The standard SAP item master interface (itemmaster import) can inadvertently override product descriptions, Free Gift settings, and the Discount Control flag during data synchronization, potentially leading to unintended changes in item properties.
This customization allows users to lock item descriptions, Free Gift and Discount Control settings against update-mode imports, the system will help preserve original product description, Free Gift and Discount Control settings against accidental changes by the interface file.
** **
**NOTE: This change will apply to all regions and brands.**

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-01-08
### Jira Comments (5 則)
**Bobby** (2025-11-14):
@@Jerry Wong Please start the development.
**Jerry Wong** (2025-12-02):
# Release:
[\\DS411\csms60\delivery\coach\Item_Master_Data_Import_Customization_2025-12-02](file://DS411/csms60/delivery/coach/Item_Master_Data_Import_Customization_2025-12-02)
# Notes:
- 
- 
- 
- 
# Sources:
svn://sanyosvn.ctil.com/svn/cs2000/Trunk/BackEnd.Net(VS2017 FW 4.5.2 NEW)/CS2000BNV1_Prod
svn://sanyosvn.ctil.com/svn/cs2000/Trunk/BackEnd.Net(VS2017 FW 4.5.2 NEW)/CSDataInterface
**Automation for Jira** (2025-12-02):
Issue has been created since
Days since: 18
Week since : 2
Issue due date difference
Days since : 0
Weeks since: 0
**Cy Lau** (2026-01-05):
@@Jerry Wong  please review if the updates did being pushed to svn
**Sherman tse** (2026-01-08):
released

## 相關資訊

- Jira: [BE-1213](https://ctil.atlassian.net/browse/BE-1213)
- Fix Version: 未記錄
- 解決日期: 2026-01-08
