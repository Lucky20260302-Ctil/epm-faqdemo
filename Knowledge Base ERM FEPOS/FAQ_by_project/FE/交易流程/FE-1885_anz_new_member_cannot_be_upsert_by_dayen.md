---
tags: [faq, fe, 交易流程]
component: "Day End"
symptom: "Here is the normal created flow:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1885
resolved: 2026-05-05
fix-version: ""
---

# FE-1885: [ANZ] New Member cannot be upsert by Dayend or transaction

## 問題

Here is the normal created flow:
The config：
MPOS has created the new Member
BE has no this record even once the “Day-end” is proceed.
Here is the log

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-05-05
### Jira Comments (5 則)
**Sang** (2026-02-12):
@@Joseph_Hu Please advise testing VM IP, user id and password
**Joseph_Hu** (2026-02-12):
@@Sang
172.16.138.103
id .\sxd
pwd Yan20201104@
402036
China123
**Sang** (2026-02-12):
@@Cy Lau @@Joseph_Hu @@Sherman tse MPOS write new Member information to dbtrans.[New Vip] table have not update mandatory update_timestamp field.
**Sang** (2026-03-02):
@@Sherman tse  Program uploaded to \\ds411\share\POS_FE_Release_64\20260302 Coach ANZ v750.04R21
15. Day End handle MPOS O/S Upsert Member with Upload_status is Null(KTS 2601302 v750.04R21, v750.05R09)
**Automation for Jira** (2026-03-02):
Issue has been created since
Days since: 18
Week since : 2
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1885](https://ctil.atlassian.net/browse/FE-1885)
- Fix Version: 未記錄
- 解決日期: 2026-05-05
