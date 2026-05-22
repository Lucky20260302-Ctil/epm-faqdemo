---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "After updated from 7.5.0.0.5 to 7.5.0.0.5R3 , the search member having issue."
root-cause: "待提取"
solution: "### Jira Comments (4 則)"
jira: FE-1859
resolved: 
fix-version: ""
---

# FE-1859: [Ba&sh] After seearch member (Not exists in local DBMas) by BEDB connection (CS2000) cannot applied

## 問題

After updated from 7.5.0.0.5 to 7.5.0.0.5R3 , the search member having issue.
#1 The member could be fetched from backend
#2 The member cannot be applied for disc, msg nor coupon
#3 The interrupted member object could be applied on the FEPOS UI without any informations except VIP no.
---
After first investigation ,
- 
- 
Suspected in DC.GetMember function , certain object transformation or validation involve in RCA :
Joint log from DAL , DAL in csplus, T9, NPOS as below
[20260123 11:46:17 -8739]: Search Member Adv: Vipmas_vip_Code :M10C0196356-start
[20260123 11:46:17 -9276]: Search Member Adv: Vipmas_vip_Code :M10C0196356-Found, Get Details start
[20260123 11:46:17 -9276]: ProcessVipFound : M10C0196356-Found, Get Details Completed
[20260123 11:46:53 -2923]: DC.GetMember M10C0196356
[20260123 11:46:53 -7089]: Completed
[20260123 11:46:53 -7461]: doMsgCenterMsg- Start : Avail V.  Memory : 140731636.29
[20260123 11:46:53 -7461]: Getting Vip Message for:[M10C0196356]
[20260123 11:46:53 -7461]: Rendering VIP Message
[20260123 11:46:53 -7472]: Memo Summary
[20260123 11:46:53 -7472]: Has VIP: Y
[20260123 11:46:53 -7472]: VIP Code: M10C0196356
VIP Type:  
VIP Dis : 0
VIP Extra Disc : 0
VIP Limit : N
[20260123 11:46:53 -7472]: Is Tax Free : N
[20260123 11:46:53 -7483]: Card Promote Code :
[20260123 11:46:53 -7483]: +ve Item:101H24PAROO3-A0510 ^0 : 1
[20260123 11:46:53 -7519]: Get ECoupon Used Message
[20260123 11:46:53 -7664]: doMMCalculation.End() with 0:0:0:18
[20260123 11:46:53 -7674]: RunTime : 0h:0min:0.0.018s
[20260123 11:46:53 -8156]: Refresh UI
[20260123 11:46:53 -8202]: Update Task Message :最后销售单编号:00004613
[20260123 11:46:53 -8493]: doInputVip- End : Avail V.  Memory : 140731635.003
[20260123 11:46:55 -4824]: doMsgCenterMsg- End : Avail V.  Memory : 140731633.816
2026/01/23 11:46:53.414 DELETE FROM [TblEcoupon] WHERE Ecoupon_Vip_No='M10C0196356' : 32
2026/01/23 11:46:53.471 [DB: CeTrans]UpdateDataTableSelectedFields - pSingleTxn : True
2026/01/23 11:46:53.483 [DB: CeTrans]Update Data Table : 32
2026/01/23 11:46:53.491 Update CeTrans.TblEcoupon , No of Records : 32
2026/01/23 11:46:53.539 [DB: CeTrans]UpdateDataTableSelectedFields - pSingleTxn : True
2026/01/23 11:46:53.573 [DB: CeTrans]Update Data Table : 32
2026/01/23 11:46:53.579 Update CeTrans.TblEcoupon , No of Records : 32
2026/01/23 11:46:53.383 Keep Local Member Type: Update tblvipmas set vipmas_birth_date='1904/09/10' ,vipmas_type='U',vipmas_type_start_Date='2023/03/26' ,vipmas_new_Flag='N',vipmas_agegrp='01' Where Vipmas_Vip_code = 'M10C0196356'
2026/01/23 11:46:53.394 Refresh _DC.OnlineUpdateMemberECoupon
2026/01/23 11:46:53.491 Online Update Ecoupon for M10C0196356 Done
2026/01/23 11:46:53.581 Online/local Update Ecoupon for M10C0196356 Done
2026/01/23 11:46:53.663 OnlineUpdateMemberRgPts (M10C0196356) Global :* BP Bal :|T0.0
2026/01/23 11:46:53.669 onlineGet Member (M10C0196356) BP:**** Point Summary :E0.0|R0.0|B0.0
**** Group Summary
**** Grp + Expire Summary
2026/01/23 11:46:53.678 _DC.BackendDC.GetMemberEvents
2026/01/23 11:46:53.707 Online GetMemberEvents : M10C0196356 Done
2026/01/23 11:46:53.748 MixMatchPrice
2026/01/23 11:46:53.765 Trans Date:2026/01/23 Member : M10C0196356()  Disc,%: .0 Extra Disc,%: 0.0 Max Disc,%: .0
Total Amt : 3760 Misc Amt : 0 Memo Disc Amt :0
Net   Amt : 3760 Tax Amt : 0 Exempted :False
 Seq                  item  color   size    Qty      List Price      Curr Price        MM Price      Sell Price        Item Amt     NetAmt(-MD)  MMC Ref Amount         Tax Amt MM Evemt            
    1         101H24PAROO3  A0510      0      1        3,760.00        3,760.00        3,760.00        3,760.00        3,760.00        3,760.00        3,760.00            0.00

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (4 則)
**Cy Lau** (2026-01-23):
Comparing logs from 15-23 Jan , 
only starting from 21 - 23 Jan , there would be following searching logs when enquiry vips :
**Joy Li** (2026-01-23):
Confirm the issue is caused by config “<span style="color:#ff5630">**ONLINEMEMBERENQUIRY**</span><span style="color:#ff5630">“= N</span>
172.16.138.4 now can reproduce the issue by set ONLINEMEMBERENQUIRY=N
BE connect to .8 csdata18_70
cc @@Sherman tse  @@Cy Lau  @@Sang
**Sang** (2026-01-23):
@@Cy Lau @@Joy Li @@Sherman tse My understand BASH use local DB (Config 2, but fail to online get new created member from BE DB (jira FE-1846) in v750,05R03. We have fixed it in v750.05R04. Option 1 may be a workaround solution in v750,05R03 but increate BE DB and network loading.
1. 
2.ONLINEMEMBERENQUIRY ='N'
	- Use local DB to get Member Enquiry / search member
. 	- if search member not found and (tblconfig.ENABLEONLINEMEMBER), online connect BE DB to search Member
	  ( This function has bug in v750.05R03, and was fixed in v750.05R04
		12.Fix online member search from BE DB (tblconfig.EnableOnlineMember='Y') Function (KTS 260106 FE-1846 v750.05R04)
**Andrew_Au** (2026-05-05):
@@Sherman tse Please update the ticket status

## 相關資訊

- Jira: [FE-1859](https://ctil.atlassian.net/browse/FE-1859)
- Fix Version: 未記錄
- 解決日期: 未記錄
