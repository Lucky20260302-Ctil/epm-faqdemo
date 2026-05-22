---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "[BASH] Member searching behavior become different after applied BASH release for fixing member issue"
root-cause: "待提取"
solution: "### Jira Comments (6 則)"
jira: FE-1851
resolved: 
fix-version: ""
---

# FE-1851: [BASH] Member searching behavior become different after applied BASH release for fixing member issue

## 問題

[BASH] Member searching behavior become different after applied BASH release for fixing member issue
Reproduce steps:
1. 
2. 
3. 
4. 
5. 
Coach C360 behavior:
- 
C360 set up applied with BASH behavior:
- 
*no config changed
VM: 172.16.138.103
.\sxd
Yan20201104@

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (6 則)
**Automation for Jira** (2026-01-12):
Issue has been created since
Days since: 2
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sherman tse** (2026-02-24):
@@Sang 
172.16.138.103
.\sxd
Yan20201104@
**Sang** (2026-02-26):
@@Sherman tse @@Joy Li @@Cy Lau
CLPLUS tblconfig.OnlineRetrieveFirstMemOnly
	'Y' - Online retreive Temp Member - Get first Match one only
	Default "Y'
In v750.04 handle this feature (OnlineRetrieveFirstMemOnly='Y') has bug thus show a list of members for SA to select. v750.05 fixed this problem. Refer to development note, this value should be 'N' for C360
**Sherman tse** (2026-02-26):
When ONLINECRMSYSTEM= C360, POS would auto change value of OnlineRetrieveFirstMemOnly to N
Enhancement will be handled later
**Sang** (2026-02-27):
@@Sherman tse Program uploaded to \\ds411\share\POS_FE_Release_64\20260227 v750.05R09 - BASH IMX SPH AO
**Andrew_Au** (2026-05-05):
@@Sherman tse Please update the ticket status

## 相關資訊

- Jira: [FE-1851](https://ctil.atlassian.net/browse/FE-1851)
- Fix Version: 未記錄
- 解決日期: 未記錄
