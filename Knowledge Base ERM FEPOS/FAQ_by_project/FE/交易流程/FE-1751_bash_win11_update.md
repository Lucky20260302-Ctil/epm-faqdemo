---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Fail to go payment screen."
root-cause: "待提取"
solution: "### Jira Comments (14 則)"
jira: FE-1751
resolved: 
fix-version: ""
---

# FE-1751: BASH  win11  update

## 問題

Fail to go payment screen.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (14 則)
**Cy Lau** (2025-09-15):
# **Does KB5064401 include KB5064081?**
No, **KB5064401** and **KB5064081** are **separate updates**:
- 
- 
These updates serve **different components** of the system and are **not nested** within each other.
There are **known issues** with Microsoft Access and **ADO-based VBA code** after installing **KB5064081**:
- 
-
**Cy Lau** (2025-09-15):
The update **KB5064081** introduces changes that **break compatibility** with legacy Access components, particularly:
# ❌ **Affected DLLs**
1. 
2. 
# ⚠️ **Uninstalling KB5064081**
- 
- 
# 🧩 **DLL Restoration Strategy**
If you **cannot uninstall KB5064081**, you may try:
1. 
2. 
3. 
(Get-Item "C:\Windows\SysWOW64\msjtes40.dll").VersionInfo.FileVersion
(Get-Item "C:\Windows\SysWOW64\vbajet32.dll").VersionInfo.FileVersion
**Cy Lau** (2025-09-15):
Partical solution for furture windows updates :
`Microsoft.Jet.OLEDB.4.0` to `Microsoft.ACE.OLEDB.12.0`
# 🔄 Key Differences & Impacts
# ✅ **Compatibility**
- 
- 
- 
# ⚠️ **Deployment Impact**
- 
- 
# 🧠 **Code Changes**
Most ADO.net  code remains the same, but you need to update the **connection string**:
Dim conn As New OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=C:\yourfile.mdb;")
to
Dim conn As New OleDbConnection("Provider=Microsoft.ACE.OLEDB.12.0;Data Source=C:\yourfile.mdb;")
# 🧪 **Behavioral Differences**
- 
- 
- 
# 🧰 Recommendations
1. 
2. 
3.
**Joy Li** (2025-09-15):
- 
- 
-
**Joy Li** (2025-09-15):
@@Joy Li
- 
- 
-
**Joy Li** (2025-09-15):
Log is copied from store PC
**Cy Lau** (2025-09-15):
Firt Investigation on the Log and eventLog :
EventLog :
# ⚠️ **Error Description**
The application `Retail60.EXE` crashed due to an **unhandled exception**:
# **Exception Type**:
`System.ArgumentOutOfRangeException`
# **Cause**:
The error occurred in the method:
System.Windows.Threading.DispatcherTimer.set_Interval(System.TimeSpan)
This suggests that the application tried to set a timer interval to an invalid value (e.g., negative or zero), which is not allowed.
# **Stack Trace Highlights**:
- 
- 
- 
- 
This indicates the crash happened during a tooltip display operation, likely triggered by a UI interaction, and the timer interval used for showing the tooltip was invalid.
1. 
2. 
3. 
4. 
T9:
It is strongly having a win11 machine in order to do the testing
**Joy Li** (2025-09-15):
@@Sang Could you please check the issue below? Will same issue in V75 ?
**Sang** (2025-09-15):
@@Joy Li ‘10S02109’ use Ver. 7.2.0.02R07ZH.  Please try 20250915 BASH v720.02R07ZV Patch - Beta + \\ds411\share\POS_FE_Release\20250422 BASH v720.02R07ZU Full
**Sang** (2025-09-16):
@@Cy Lau Testing Report:
1. 
2.
**Sang** (2025-09-16):
@@Cy Lau 32-bit and 64-bit 2016 engine cannot co-exist
**Automation for Jira** (2025-09-18):
Issue has been created since
Days since: 3
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2025-09-22):
@@Joy Li I have copied [\\ds411\share\POS_FE_Release_64\20250918](file://ds411/share/POS_FE_Release_64/20250918) BASH v750.05 Beta to 172.16.138.60 csplus folder, v75.05 can startup normal.   Please start V75.04 in BASH machine first, if it can run normally, then upgrade to v750.05 by copying files.
**Joy Li** (2025-09-23):
@@Sherman tse  @@Andrew_Au 
Please found the mastconv, dbtrans, dbhist and RP files for testing. Thanks.

## 相關資訊

- Jira: [FE-1751](https://ctil.atlassian.net/browse/FE-1751)
- Fix Version: 未記錄
- 解決日期: 未記錄
