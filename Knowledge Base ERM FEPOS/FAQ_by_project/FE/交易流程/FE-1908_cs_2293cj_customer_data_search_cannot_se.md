---
tags: [faq, fe, 交易流程]
component: "Frontend"
symptom: "[https://jira.tapestry.support/browse/CS-2293](https://jira.tapestry.support/browse/CS-2293)"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1908
resolved: 2026-04-17
fix-version: ""
---

# FE-1908: [CS-2293]CJ_Customer data search_cannot see "membership available period" info

## 問題

[https://jira.tapestry.support/browse/CS-2293](https://jira.tapestry.support/browse/CS-2293)
Symptom:
When search customer data, we cannot see "member ship available period" info on POS.
**<Sample customer ID>**
J111WJ03887170
JXXX0011352497
**<Detail of issue>**
When store search following customer, one of customer already epxired and another customer still available membership period.
however both case, system did NOT show member ship available period as below.
please check this issue case, why we can not see that info.
J111WJ03887170
JXXX0011352497

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-04-17
### Jira Comments (21 則)
**Cy Lau** (2026-03-26):
Code checking : v750
So basically , it would come from <span style="color:#ff991f">**vipdef**</span>** **by <span style="color:#4c9aff">**BE Query**</span>
---
@@Joy Li  & support team , please check the Production Database about the vip stage expiry date field.
Please advise for both <span style="color:#4c9aff">“amt to next”</span> & <span style="color:#00b8d9">“stage expiry date“</span> are not shown for **JXXX0011352497 **in FEPOS, (~~zlog ? ~~BE Connection Issue ?)
@@Jerry Wong  please check agrex importing about any vip stage expiry date mapping
**Joy Li** (2026-03-27):
Hi @@Cy Lau 
in testing PC 172.16.13.61
search J101TJ00009102 but no stage Expiry Date is show.
Connect to 172.16.138.8\sqlexpress,40000 Backend
**Jerry Wong** (2026-03-27):
In CSDataInterface, it has importing vip_expiry_date, but no any vip stage expiry date in the import file config
**Cy Lau** (2026-03-27):
please make sure it is using CS2000 as membership
**Cy Lau** (2026-03-27):
……
**Cy Lau** (2026-03-27):
Video attached. 
In winMemberEnquiry no VipDef obtained
In winMemberEnquiryOnline , VipDef will be obtained
@@Sang  Please check
**Cy Lau** (2026-03-27):
Suspected Code :
CS2000 , does it mean OnlineMemberEnquiry = Y ?
**Cy Lau** (2026-03-27):
After tracing for the follow , v75 at least upon to 27 Mar 2026 code base , there’s no logic to fetch the vipdef dataset in MemberPanelViewModel ,
adding back the handling :
@@Sang  @@Joy Li  @@Andrew_Au  @@Sherman tse  
Please comment on this
**Automation for Jira** (2026-03-30):
Issue has been created since
Days since: 3
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2026-03-30):
@@Cy Lau @@Sherman tse Confirmed need to add code to handle. Fixed in v750.04R23
v750.04R23
1.
**Joy Li** (2026-04-02):
Hi @@Sang  @@Cy Lau 
Please apply on
- 
-
**Cy Lau** (2026-04-02):
@@Sang  please review suggested the fixing logic as below. Mainly around function **ProcessViPFound**
**Sang** (2026-04-02):
@@Cy Lau Already applied suggested logic in latest version R23. I will re-apply to previous versions as Joy requested
**Sang** (2026-04-02):
@@Joy Li  @@Sherman tse @@Cy Lau
v750.04R14D2 uploaded to \\ds411\share\POS_FE_Release_64\20260402 Coach v750.04R14D2
v750.04R14D1
1. 
v750.04R14D2
1.
**Cy Lau** (2026-04-02):
@@Joy Li  please verify if only cs2000 needs vipdef, since mpos api got reported for requiring others also
**Sang** (2026-04-02):
@@Cy Lau Only Coach JP need this information, and Coach JP Member information online retrieved from BE database (tblconfig.ONLINECRMSYSTEM='CS2000')
**Cy Lau** (2026-04-02):
@@Sang 
this the fix after TP QAQC & Support team reported issue
**Sang** (2026-04-02):
@@Cy Lau @@Cy Lau In FE UI, only Coach JP (IsCoachJP) Show Stage Information (VipDef), Coach JP (tblconfig.ONLINECRMSYSTEM='CS2000'). Further KS JP Member information (Vip master) and extra information (VipDef0 does not save in our BE DB ((tblconfig.ONLINECRMSYSTEM='C360').
**Sang** (2026-04-02):
@@Cy Lau@@Joy Li
**Joy Li** (2026-04-02):
@@Sherman tse 
Take J101TJ00009102        for testing
**Joy Li** (2026-04-17):
The issue is included in FE V75.004.2400.0000 which released on 2026-04-16.

## 相關資訊

- Jira: [FE-1908](https://ctil.atlassian.net/browse/FE-1908)
- Fix Version: 未記錄
- 解決日期: 2026-04-17
