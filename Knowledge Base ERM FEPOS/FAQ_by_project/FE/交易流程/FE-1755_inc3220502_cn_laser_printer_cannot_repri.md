---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "AIO printer cannot reprint sales memo in till2 : Printing Error"
root-cause: "待提取"
solution: "### Jira Comments (9 則)"
jira: FE-1755
resolved: 
fix-version: ""
---

# FE-1755: [INC3220502] CN Laser printer cannot reprint sales memo in till2 : Printing Error

## 問題

AIO printer cannot reprint sales memo in till2 : Printing Error
Symptom:
AIO printer cannot reprint sales memo in till2
Troubleshooting:
1. 
2. 
3. 
4. 
5. 
Device information:
printer 10.34.63.10
till2: 10.42.69.194

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (9 則)
**Sang** (2025-09-29):
@@Tovi Wang  Seems encounter problem while loading crystal report library or docuement. Is this new POS setup? How about print out other Crystal Report such as deposit, transfer out ?
**Tovi Wang** (2025-09-29):
@@Sang Thanks for your quick action.这不是一家新店，该 till只在 2025-09-27 做过一笔销售，没有deposit和其它销售
**Sang** (2025-09-29):
@@Tovi Wang You mean this PC is first time print out crystal report memo ?
**Tovi Wang** (2025-09-29):
FE logs:
**Tovi Wang** (2025-09-29):
@@Sang yes,I think so.Then they met this issue and callout this issue to us.
**Sang** (2025-09-29):
@@Tovi Wang Please try re-install crystal report runtime library first
**Tovi Wang** (2025-09-29):
@@Sang Sure,Let me try it first.
**Tovi Wang** (2025-09-29):
After reinstall crystal report runtime library.Now till2 can reprint sales memo.
**Automation for Jira** (2026-01-08):
Issue has been created since
Days since: 100
Week since : 14
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1755](https://ctil.atlassian.net/browse/FE-1755)
- Fix Version: 未記錄
- 解決日期: 未記錄
