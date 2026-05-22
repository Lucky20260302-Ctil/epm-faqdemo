---
tags: [faq, web, web服務]
component: "interface"
symptom: "Previously, it is null for joueinv_confirm_state, joueinv_red_confirm_uuid,joueinv_org_memo_no."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: WEB-343
resolved: 2024-04-25
fix-version: ""
---

# WEB-343: CS-996: CN E-invoice DB SQL Query timeout checking

## 問題

Previously, it is null for joueinv_confirm_state, joueinv_red_confirm_uuid,joueinv_org_memo_no.
now it is blank, please kindly check whether there is program logic change.
and change it as the same logic.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-04-25
### Jira Comments (1 則)
**Joy Li** (2024-04-25):
ChainStorePlus v7 Backend Release R3.56
Prerequisite
No CS2000 Back Office Release must be installed before install this release.
Release Media
COACH_L4.0.0_V70R3.56.zip
	APP Folder – ChainStorePlus APP Server update
	ChainStorePlusv7 R3.56 Servers Installation Guide v1.0.docx
Changes in This Release
ChainStorePlus APP Server
	[CS-996] CN E-invoice DB SQL Query timeout checking
	POSRedInvoicing
	Add config “sqlCmdTimeout" in appsetting.json file to control SQL timeout setting. (Default = 300 sec)
	SQL tuning for data selection
Impacted Modules
	E-Invoice interface program in APP Server

## 相關資訊

- Jira: [WEB-343](https://ctil.atlassian.net/browse/WEB-343)
- Fix Version: 未記錄
- 解決日期: 2024-04-25
