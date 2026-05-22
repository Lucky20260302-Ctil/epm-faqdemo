---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "J317 called out when I visited the store. They have experienced the issue after version upgraded(Ver"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-793
resolved: 2025-09-02
fix-version: ""
---

# MP-793: [MPOS-115][INC3149444]CJ mPOS Prod_ J317 the transaction disappears if it`s not connected to SalesHub

## 問題

J317 called out when I visited the store. They have experienced the issue after version upgraded(Ver 3.30.3) on 8/6.
Issue:
When a transaction is entered into the mPOS but not yet completed, and the user temporarily accesses another site (e.g., eNameCapture from an iPhone), upon returning to the mPOS screen, the entered information disappears.
According to the store, it seems like it requires to "Connected to SalesHub" in order to avoid this issue. They need to understand what caused disconnection from SalesHub.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-09-02
### Jira Comments (13 則)
**Tovi Wang** (2025-08-19):
@@Daniel Leung Please help to take a look this issue if anything abnormal.Thanks!
Recorder time: 2025-08-18 13:01
CC @@Joy Li @@pierre.shi
**Daniel Leung** (2025-08-19):
@@Tovi Wang  Seems a UI bug while mpos doing reconnection to salesHub
**Tovi Wang** (2025-08-19):
@@Daniel Leung Please help to double confirm it and provide the hot fix for it.Thanks!
**Tovi Wang** (2025-08-20):
@@Daniel Leung Could you help to double confirm it?Thanks!
**Daniel Leung** (2025-08-20):
@@Tovi Wang Yes it is a UI bug, will release a hot fix within today
**Daniel Leung** (2025-08-20):
@@Tovi Wang @@Joy Li  @@Sherman tse hot fix uploaded to [🔗](https://ios.ctil.com/mpos/PreCoach/) 
3.30.3-20250819.1
3.29.6-20250820.1
**Tovi Wang** (2025-08-20):
@@Daniel Leung Thanks for your double confirm.
@@Joy Li @@Sherman tse Please help to arrange the testing and released ETA.
**Daniel Leung** (2025-08-27):
@@Daniel Leung @@Joy Li
**Joy Li** (2025-08-27):
Hi @@Sherman tse 
Please test the issue in below IPA
- 
-
**Joy Li** (2025-08-27):
JP current MPOS IPA version: update to 2025-08-27
**Sherman tse** (2025-09-02):
Verified on QA
test case attached
with ipa version 3.29.6-20250827.1
3.30.5-20250827.1
**Automation for Jira** (2025-09-02):
Issue has been created since
Days since: 13
Week since : 1
Issue due date difference
Days since : 
Weeks since:
**Joy Li** (2025-09-02):
released to COACH on 2025-09-02

## 相關資訊

- Jira: [MP-793](https://ctil.atlassian.net/browse/MP-793)
- Fix Version: 未記錄
- 解決日期: 2025-09-02
