---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "1.  OCF29-10226739 on 2024-12-27,Missing first line issue"
root-cause: "待提取"
solution: "### Jira Comments (15 則)"
jira: BE-977
resolved: 
fix-version: ""
---

# BE-977: [CS-688] CN New DB version still have "Missing first line issue"

## 問題

1.  OCF29-10226739 on 2024-12-27,Missing first line issue
2.OCF501-20019776 missing first line issue. on 2024-12-28,Missing first line issue

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (15 則)
**Tovi Wang** (2024-12-31):
@@Cy Lau @@Joy Li  I am coping the posting log,Will upload here ASAP.
**Tovi Wang** (2025-01-02):
@@Cy Lau @@Joy Li Polling log here,Please help to further checking and long term solutions.Thanks!
**Tovi Wang** (2025-01-02):
@@Cy Lau OCF29-10226739
**Cy Lau** (2025-01-02):
May I kn the version they are using ?
with the jitter delay or not
**Tovi Wang** (2025-01-03):
Missing first line issue on 2025-01-01:
1.OC262 - 00006345, pce20250101190643.OC262___0,需要和Hyukie确认是否要重发CAR.
2.OCF44 -10044512,20250101, pce20250101171910.OCF44___1
3.OCF11 - 20031951,20250101,pce20250101132131.OCF11___2
4.OCF14 - 70038125,20250101,pce20250101112405.OCF14___7
5.OCF508 - 20022136,20250101,pce20250101153037.OCF508__2
6.OC295 - 00007612,20250101,pce20250101160407.OC295___0,需要和Hyukie确认是否要重发CAR
**Tovi Wang** (2025-01-07):
@@Cy Lau May I Know anything update for this issue?Because COACH Team are tracing me.Please in advance.Thanks!
CC @@Joy Li @@pierre.shi
**pierre.shi** (2025-01-17):
Hi Teams, this issue still occurs on V75.
RIN01443177 OCF88  10047101 20250116
**Tovi Wang** (2025-01-20):
Add 2 new call out case:
RIN01444203 OCF25 20159010 20250119
RIN01443881 OC127 00058397 20250118
**Tovi Wang** (2025-02-05):
@@Cy Lau @@Jason Wu Please help to investigate this issue in advance.Because it may cause CRM & CAR side data incorrect.
Add missing first line issue:
1.RIN01449569,OCF34 - 00074241
2.RIN01448874,OCF29- - 10230229
**Cy Lau** (2025-02-12):
For OCF501 :
For OCF29:
**Tovi Wang** (2025-02-13):
**pierre.shi** (2025-02-17):
Hi teams, this issue occurred again. POS ver 72.0221.0102
**Cy Lau** (2025-02-17):
When keep yelling for ocurred again,
I was keep asking about the version they are using : DLL*.dll
For IC8006 :
**Andrew_Au** (2025-02-27):
@@Tovi Wang  Please update the ticket status
**Tovi Wang** (2025-02-27):
Still keep monitoring.Will copy polling posting log to CY further checking when happening again.

## 相關資訊

- Jira: [BE-977](https://ctil.atlassian.net/browse/BE-977)
- Fix Version: 未記錄
- 解決日期: 未記錄
