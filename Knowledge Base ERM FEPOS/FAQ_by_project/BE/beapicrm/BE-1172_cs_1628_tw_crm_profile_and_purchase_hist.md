---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "as per we talked this morning, please help to check below issue found in PRD for TW CRM verion(v75.0"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1172
resolved: 2025-09-11
fix-version: ""
---

# BE-1172: CS-1628 TW CRM - “Profile” and “Purchase History” Not Available For Current Version

## 問題

as per we talked this morning, please help to check below issue found in PRD for TW CRM verion(v75.004.1309.0000)
Issue 1: FE vbretail.ini config incorrectly
Issue 2: Member Purchase fail to show
Workaround:
1. 
1. 
Further Action:
FE: change ini value and program change to support Member Purchase by multi region (X-COUNTRY)
BE BEGWCRM: program change to support Member Purchase by multi region (X-COUNTRY)
Timeline:
- 
- 
-

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-09-11
### Jira Comments (3 則)
**Sherman tse** (2025-09-11):
Verified on QA
Test case attached
Issue involved: FE, MPOS IPA, MPOS API, webview
path:
FE: \\ds411\share\POS_FE_Release_64\20250904 Coach v750.04R14a
MPOS ipa: 3.30.6-20250908.1 PreCoach
MPOS API: \\ds411\share\POS_MPOS_Release\3.30.x\3.30.6-20250908.1
webview: \\ds411\public\daniel\acxiom\purchase history\v1.0.3
<span style="color:#4c9aff">**For web.config in MPOS API,  need to change version to 1.1.14 for SQLitePCLRaw.core**</span>
<span style="color:#4c9aff">**   <assemblyIdentity name="SQLitePCLRaw.core" publicKeyToken="1488e028ca7ab535" culture="neutral"/>**</span>
<span style="color:#4c9aff">**<bindingRedirect oldVersion="0.0.0.0-1.1.14" newVersion="1.1.14"/> **</span>
**Automation for Jira** (2025-09-11):
Issue has been created since
Days since: 9
Week since : 1
Issue due date difference
Days since : 
Weeks since:
**Joy Li** (2025-09-11):
released to Tapestry on 2025-09-11

## 相關資訊

- Jira: [BE-1172](https://ctil.atlassian.net/browse/BE-1172)
- Fix Version: 未記錄
- 解決日期: 2025-09-11
