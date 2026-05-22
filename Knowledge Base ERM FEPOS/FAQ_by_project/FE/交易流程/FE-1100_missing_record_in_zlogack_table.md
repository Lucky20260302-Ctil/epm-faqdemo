---
tags: [faq, fe, 交易流程]
component: "Frontend"
symptom: "_（Jira 中無 description 內容）_"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1100
resolved: 2024-05-04
fix-version: ""
---

# FE-1100: Missing record in zlogack table

## 問題

_（Jira 中無 description 內容）_

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-05-04
### Jira Comments (1 則)
**Sang** (2022-03-03):
'KTS 220301
'1. Zupdate Library Enhance logic to handle Upload PCD acknowledge
' '97' Acknowledge PCD
' '83' Data eror PCD
' '81' resend PCD
'97 20220303 124229 S13 0 z22021601 2 0 2
'83 20201010 124229 S13 0 z22021602 0000003 Non-Numeric Field TblVipmas - Vipmas_Expiry_date
'83 20201010 124229 S13 0 z22021602 0000005 Non-Numeric Field TblVipmas - Vipmas_Expiry_date
'97 20220303 124229 S13 0 z22021602 33 2 35
' 95/96 filename no match
'97 20220303 124243 S13 0 z22021683 4 1 0
'83 20201010 124243 S13 0 z22021683 0000004 tblSysCon - 96 File Name (z2202168) - not Match 95 Syscon_Host_Log_Name
'Z220216.84 - 96 total record count diff
'97 20220303 124243 S13 0 z22021684 8 0 66
'Z220216.86 - Has 95, Remove 96
'97 20220303 124243 S13 0 z22021686 42 0 0
'81 S13 z22021533 0 DATA ERROR
'2. Extended Mastconv,dat daily backup files to 9999 (MAyymmdd.####)

## 相關資訊

- Jira: [FE-1100](https://ctil.atlassian.net/browse/FE-1100)
- Fix Version: 未記錄
- 解決日期: 2024-05-04
