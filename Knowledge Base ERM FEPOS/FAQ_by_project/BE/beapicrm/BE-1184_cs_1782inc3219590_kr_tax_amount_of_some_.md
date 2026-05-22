---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "@@sang_ko @@Jerry Wong"
root-cause: "待提取"
solution: "### Jira Comments (10 則)"
jira: BE-1184
resolved: 
fix-version: ""
---

# BE-1184: [CS-1782][INC3219590] KR Tax amount of some transactions in OC858 & OC818 are wrong

## 問題

@@sang_ko @@Jerry Wong
Coach team call out that KR store some transactions missing jouinv_vat_amt value on 2025-08-31.
INC3219590,KR incorrect Tax issue on 2025-08-31
1.OC858 - 00012341
2.OC818-00022437
3.OC818-00022438

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (10 則)
**Tovi Wang** (2025-09-29):
@@Sang @@Jerry Wong Previously, CN had a tax issue (Jira FE-1514) that was already included in V75. Please check the log below to confirm if KR's tax issue will also be included in V75? Could you help check the RCA of KR tax issue and provide a long term workaround?Thanks!
CC @@Joy Li FYI.
FE logs:
 .
**Tovi Wang** (2025-09-30):
@@Sang May I know anything update for this one?Because Coach team are asking me the RCA.Thanks!
**Automation for Jira** (2025-10-09):
Issue has been created since
Days since: 9
Week since : 1
Issue due date difference
Days since : 
Weeks since:
**Sang** (2025-10-09):
@@Tovi WangOC818-00022438 was created on 2025-8-31. Please re-get dbtrans.sdf and all 8-31 logs
**Sang** (2025-10-09):
@@Tovi WangOC858-00012341 was created on 2025-8-31. Please re-get 8-31 dbtrans.sdf and all logs
**Tovi Wang** (2025-10-15):
@@Sang 08-31 log已经提供，因为08-31 dbtrans 已被覆盖，所以已经无法copy.
**Sang** (2025-10-15):
@@Sang Copy dbhist.sdf instead of dbtran.sdf
**Tovi Wang** (2025-10-22):
@@Joy Li @@Sang As talked in teams.Since OC858 & OC818 all are V72 version.Let us keep monitoring the Tax issue in V75 with Coach team.I has explained the deatils to Coach team.Hold on this ticket first.
**Andrew_Au** (2026-05-05):
@@Tovi Wang @@Joy Li  Should I change the ticket status to close? please confirm.
**Tovi Wang** (2026-05-07):
Not call out in V75.Can be closed.

## 相關資訊

- Jira: [BE-1184](https://ctil.atlassian.net/browse/BE-1184)
- Fix Version: 未記錄
- 解決日期: 未記錄
