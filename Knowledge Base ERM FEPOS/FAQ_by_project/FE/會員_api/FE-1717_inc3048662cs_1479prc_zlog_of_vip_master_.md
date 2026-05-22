---
tags: [faq, fe, 會員_api]
component: "interface"
symptom: "PRC Zlog of VIP Master still send to FE"
root-cause: "待提取"
solution: "### Jira Comments (10 則)"
jira: FE-1717
resolved: 
fix-version: ""
---

# FE-1717: [INC3048662][[CS-1479]]PRC Zlog of VIP Master still send to FE

## 問題

PRC Zlog of VIP Master still send to FE

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (10 則)
**Joy Li** (2025-06-26):
@@Cy Lau
send log program should skip the member detail , bouns point and sales figure which member type is set to “NOT donwload“.
But today CN is sending those member detail to FE via zlog.  could you please help to check the send log logic?
**Cy Lau** (2025-06-26):
@@Joy Li wait for Jerry logic trace ETA 1100
**Jerry Wong** (2025-06-26):
@@Joy Li set dbtmnlog_gen = ‘X' if member type is not download ‘Y’ where dbtmnlog_table_name in vip, vipfig, vipdef and viprgpts. During send zlog, only dbtmnlog_gen = ' ’ would be selected
**Andrew_Au** (2025-09-08):
@@pierre.shi @@Tovi Wang @@Joy Li  Please ticket status
**Tovi Wang** (2025-09-08):
Should be same duplicate issue with internal Jira [🔗](https://ctil.atlassian.net/browse/BE-1146).Will double confirm with @@Joy Li @@pierre.shi
**Andrew_Au** (2025-09-14):
@@pierre.shi @@Tovi Wang @@Joy Li  Please ticket status
**Automation for Jira** (2025-10-08):
Issue has been created since
Days since: 105
Week since : 15
Issue due date difference
Days since : 
Weeks since:
**Andrew_Au** (2025-10-28):
@@pierre.shi @@Tovi Wang @@Joy Li Pending for a long time. Please update the status.
**Tovi Wang** (2025-10-28):
@@Andrew_Au Since we can’t reproduce this issue in our QA.So we are keep monitoring this issue in pro with Coach team.Hold on please.
**Tovi Wang** (2025-10-29):
This issue has not occurred again in Pro.Closed first.Keep monitoring in pro.

## 相關資訊

- Jira: [FE-1717](https://ctil.atlassian.net/browse/FE-1717)
- Fix Version: 未記錄
- 解決日期: 未記錄
