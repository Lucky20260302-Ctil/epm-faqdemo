---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "HKJC reported the v72 POS often show below message, the pc is using Win 11, attached the requested l"
root-cause: "待提取"
solution: "### Jira Comments (7 則)"
jira: FE-1831
resolved: 
fix-version: ""
---

# FE-1831: RTM POS memory low message (HKJC)

## 問題

HKJC reported the v72 POS often show below message, the pc is using Win 11, attached the requested logs for investigation
![](file:///C:/Users/ANGELA~1/AppData/Local/Temp/msohtmlclip1/01/clip_image002.gif)

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (7 則)
**Automation for Jira** (2025-12-12):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2025-12-12):
Found Memory Low alert, but user have not select quick reload
**Sang** (2025-12-12):
Remind user to use ‘quick reload’ function
**Angela Chan** (2025-12-12):
@@Sang
user also reported another issue about this POS today, attached please find the screen capture, if it is same reason, I will reply her together, thanks
**Sang** (2025-12-12):
@@Angela Chan Any other shop have similar problem?  please inform JC if POS popup this memory low alert message select ‘Yes’ to quick reload POS
**Sang** (2025-12-12):
tblconfig setting
SSE Dbhist: LOCALSERVERDATASOURCE
SSE dbMas : POSMASTERSERVER
2025/12/08 11:06:43 Get Register Key Info01.STLEVG.0.72.0107.5008.LASER.2025/12/02.ENG.
2025/12/08 11:07:02 [DB: SSE]DB Connect Failure: Data Source=IT0091625DTC\SQLEXPRESS,40000;Initial Catalog=DBHist;Persist Security Info=True;User ID=STLEVG;Password=STLEVG
Err: A network-related or instance-specific error occurred while establishing a connection to SQL Server. The server was not found or was not accessible. Verify that the instance name is correct and that SQL Server is configured to allow remote connections. (provider: TCP Provider, error: 0 - The remote computer refused the network connection.)
**Sang** (2025-12-15):
@@Bobby Compare memory recovery of v72 POS  operated under Window 10 & Window 11
**Window 10 – 2025/11/30**
Line   50: [30/11/2025 10:32:41 -8871]: CheckNewLog - Start : Avail V.  Memory : 1409.028
Line 5014: [30/11/2025 21:38:44 -9607]: DoSelectMenu :080101 : Avail V.  Memory : 807.846
STLEVG.00320229 - STLEVG.00320256 : 28 Nos.
**Window 11 – 2025/12/10**
Line   50: [10/12/2025 11:02:49 -5240]: CheckNewLog - Start : Avail V.  Memory : 1300.812
Line 4829: [10/12/2025 21:02:02 -0572]: DoSelectMenu :080101 : Avail V.  Memory : 204.595
Update Task Message :Last Memo No. : 00320390
Update Task Message :Last Memo No. : 00320409
Created Sales Memo – 19 Nos.

## 相關資訊

- Jira: [FE-1831](https://ctil.atlassian.net/browse/FE-1831)
- Fix Version: 未記錄
- 解決日期: 未記錄
