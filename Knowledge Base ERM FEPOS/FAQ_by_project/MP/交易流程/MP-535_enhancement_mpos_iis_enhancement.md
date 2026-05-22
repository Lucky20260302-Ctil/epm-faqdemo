---
tags: [faq, mp, 交易流程]
component: "MPOS, MPOS API, MPOSPrint.exe"
symptom: "_（Jira 中無 description 內容）_"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-535
resolved: 2024-01-22
fix-version: ""
---

# MP-535: Enhancement - MPOS IIS Enhancement

## 問題

_（Jira 中無 description 內容）_

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-01-22
### Jira Comments (7 則)
**Joy Li** (2022-06-23):
PRD Log: Take J314 20/6 to 22/6 as example
Server Log: \\172.16.183.201\localuser\support\JIRA_DB\MP-535\IIS_Server_Log_J314.zip
IPA Log: \\172.16.183.201\localuser\support\JIRA_DB\MP-535\J314_2022-06-20-23_UI_Log.zip
FE MPOS print log: \\172.16.183.201\localuser\support\JIRA_DB\MP-535\J314_2022-06-20-23_Log.zip
**Joy Li** (2022-06-27):
Video from COACH: copied to folder \\172.16.183.201\localuser\support\JIRA_DB\MP-535\
**Steven Yuen** (2022-06-27):
Added J486_MPOSPrint_20220531.log
FE MPOS print log: \\172.16.183.201\localuser\support\JIRA_DB\MP-535\J486_2022-05-31_Log
**Joy Li** (2022-06-27):
J486 Server Log added
\\172.16.183.201\localuser\support\JIRA_DB\MP-535\J486_IIS_Log_20220601_to_20220627.zip
\\172.16.183.201\localuser\support\JIRA_DB\MP-535\J486_2022-05-31_Log\
**Joy Li** (2022-07-05):
QA J780 Log added
\\172.16.183.201\localuser\support\JIRA_DB\MP-535\QA_J780_log.zip
All server log + IPA Log
Test info:
Cloud API: 3.16.8   IPA: 3.16.4
FE: v72.0216.0501
Store code: J780
Transaction no. : MB000029/MB000030/MB000031
**Joy Li** (2022-07-05):
Comment from Yau:
Attached the payment time consumptions log for reference.
In normal case, MPOS use 9-12s to complete the payment (from "Click Payment" to Pop up "Memo No")
Please note that number of item per memo would affect the used time but not significant. But number of effective mix & match rules affect too.
[PRD_J486 payment analysis.pdf^](https://jira.tapestry.support/secure/attachment/612638/612638_PRD_J486+payment+analysis.pdf)
![](https://jira.tapestry.support/images/icons/link_attachment_7.gif)
[^](https://jira.tapestry.support/secure/attachment/612638/612638_PRD_J486+payment+analysis.pdf)
**Joy Li** (2022-07-08):
PRD J486 IPA log uploaded.
\\172.16.183.201\localuser\support\JIRA_DB\MP-535\J486%2dOC173_K%2d2022%2D07%2D03%2016%3A16%3A43%3A650688.txt

## 相關資訊

- Jira: [MP-535](https://ctil.atlassian.net/browse/MP-535)
- Fix Version: 未記錄
- 解決日期: 2024-01-22
