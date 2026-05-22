---
tags: [faq, fe, 系統服務]
component: "DTUTIL"
symptom: "[Dtutil] Transafer Delivery note printed as veritical, it shoule be landscape"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1900
resolved: 2026-03-17
fix-version: ""
---

# FE-1900: [Dtutil] Transafer Delivery note printed as veritical, it shoule be landscape

## 問題

[Dtutil] Transafer Delivery note printed as veritical, it shoule be landscape
Applied with v4.27 KOS.LPrinter.dll
VM: 172.16.138.131
.\sxd
Yan20201104@
C:\DTUTIL2

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-03-17
### Jira Comments (5 則)
**Automation for Jira** (2026-03-16):
Issue has been created since
Days since: 2
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2026-03-16):
@@Sherman tse Please try updated program KOS.Lprinter.exe , uploaded to \\ds411\share\POS_FE_Release\20260316 DTUT Print DN
**Sang** (2026-03-16):
@@Sherman tse @@Bobby Upgrade SanyoPos.Report.dll to v720.02R28 Change DN report layout to Portrait. Program uploaded to \\ds411\share\POS_FE_Release\20260316 DTUT Print DN
**Sherman tse** (2026-03-17):
Verified OK on QA
Print out using vertical mode finally
**Sherman tse** (2026-03-17):
@@Sherman tse

## 相關資訊

- Jira: [FE-1900](https://ctil.atlassian.net/browse/FE-1900)
- Fix Version: 未記錄
- 解決日期: 2026-03-17
