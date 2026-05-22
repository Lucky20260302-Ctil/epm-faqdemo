---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "Symptom:"
root-cause: "待提取"
solution: "### Jira Comments (2 則)"
jira: MP-832
resolved: 
fix-version: ""
---

# MP-832: INC3550023 - Exchange memo NOT linked to Original sales memo

## 問題

Symptom:
Store callout when doing Exchange memo OC516-MA013763，Input the Original sales memo OC16-30038860.But Original sales memo not diplayed in PC file and BE DB.Please help to double check the MPOS UI log to find the [RCA.Is](http://RCA.Is) it store mis-operation or other issue?Thanks!
1.From MPOS UI log,We can see the return item CCY30 records.
2026-04-20 19:37:19.574 +08:00 [INF] Result:退貨
2026-04-20 19:37:19.574 +08:00 [INF] SecurityController.GetSecurityTitle?secCode:SAL00005.End(),3ms
2026-04-20 19:37:28.037 +08:00 [INF] SecurityController.SecurityChecking?secCode:SAL00005;userCode:604082.Start()
2026-04-20 19:37:29.348 +08:00 [INF] Result:True
2026-04-20 19:37:29.348 +08:00 [INF] SecurityController.SecurityChecking?secCode:SAL00005;userCode:604082.End(),1306ms
2026-04-20 19:37:49.933 +08:00 [INF] SalesMemosController.GetReturnPrice?memoLoc:OC16;memoNo:30038860;itemNo:CCY30;color:B4YTH;size:;inseam:;isTaxEampt:False
2.Original sales memo is OC16-30038860
3.Exchange sales memo is OC516-MA013763

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (2 則)
**Tovi Wang** (2026-04-29):
@@Joy Li @@Daniel Leung  ALL log here.
**Tovi Wang** (2026-05-13):
查询MPOS log确认，user在2026-04-20 19:37:49 第一次return时，确实选了原始单小票OC16-30038860。但没有创建exchange memo.
然后user在2026-04-20 19:41:18 第二次return时，没有选择原始单小票且创建了exchange memo OC516-MA013763

## 相關資訊

- Jira: [MP-832](https://ctil.atlassian.net/browse/MP-832)
- Fix Version: 未記錄
- 解決日期: 未記錄
