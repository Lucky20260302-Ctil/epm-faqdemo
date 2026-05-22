---
tags: [faq, fe, 會員_api]
component: "interface"
symptom: "Invalid field in CAR  sales files during 3/21-3/23"
root-cause: "待提取"
solution: "### Jira Comments (11 則)"
jira: FE-1659
resolved: 
fix-version: ""
---

# FE-1659: INC2874105 Invalid field in CAR sales files during 3/21-3/23 for KR OCF90 pilot store

## 問題

Invalid field in CAR  sales files during 3/21-3/23
Please help to find the root cause of this issue.this is for KR OCF90 pilot store.
1.@@Sang ’H’这一行为什么会有一串“NUL“是从哪里来的？客户输入的嘛还是怎样？
CC @@Cy Lau @@Bobby @@pierre.shi  FYI.
2.在TIll0 PC250321.DAT 和 M till PC250321.M file里也能发现。Please help to further checking.
Till0 PC file
M Till PC file

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (11 則)
**Tovi Wang** (2025-03-24):
@@Sang  03-21 to 03-23 CAR file for your further checking.
**Tovi Wang** (2025-03-24):
@@Sang 03-21 to 03-23 PC file for your further checking.
**Sang** (2025-03-24):
@@Tovi Wang Null position should be staff code
Please copy T9 and Dal log, check who do the day end
**Tovi Wang** (2025-03-24):
@@Sang From till0 PC  file & T9 log,Should be staff code 737494 do the dayend.
Dayendh table:
Till0 PC file:
T9 log:
DAL log:
**Sang** (2025-03-24):
@@Tovi Wang Please copy 21/3-23/3 dbtrans.sdf.
**Sang** (2025-03-24):
Program rollback from v75 to v72 21/3 @18:00.
**Tovi Wang** (2025-03-24):
@@Sang Yes,you are right.Program rollback from v75 to v72 due to other strange issue.
**Tovi Wang** (2025-03-24):
@@Sang  21/3-23/3 dbtrans.sdf for your further checking.
03-20 dayendh table is normal,dayendh_staff value also is normal.
**Sang** (2025-03-24):
@@Tovi Wang when did OCF90 upgrade to v75. Please get dbtrans.sdf before upgrade to v75
**Tovi Wang** (2025-03-24):
@@Sang 03-20 的dbtrans也在之前的zip file里面。please further checking.
**Tovi Wang** (2025-05-30):
Dear ALL,
he root cause is during OCF90 rollback from V75 to V72.re-import V72 Xconfig then issue fixed.Closed ticket first.

## 相關資訊

- Jira: [FE-1659](https://ctil.atlassian.net/browse/FE-1659)
- Fix Version: 未記錄
- 解決日期: 未記錄
