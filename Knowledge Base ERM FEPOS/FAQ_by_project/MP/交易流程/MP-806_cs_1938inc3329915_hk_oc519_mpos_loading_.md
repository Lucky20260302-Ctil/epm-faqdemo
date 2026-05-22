---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "The related sales memo number is OC519-MA000019 on 2025-12-17, the video record time as follow, tota"
root-cause: "待提取"
solution: "### Jira Comments (11 則)"
jira: MP-806
resolved: 
fix-version: ""
---

# MP-806: [CS-1938][INC3329915] HK OC519 MPOS loading for 1 min when generated all the payment

## 問題

The related sales memo number is OC519-MA000019 on 2025-12-17, the video record time as follow, total takes 1min40s, please check and help to advise.
@@Cy Lau @@Daniel Leung Please help to take a look this case.Where exactly did that one minute spent when MPOS doing the payment?Thanks!
CC @@Joy Li @@pierre.shi
MPOS log as follow:
Video as follow:

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (11 則)
**Tovi Wang** (2025-12-23):
POS version: 75.004.1100.0010
Cloud MPOS version: 3.29.5
**Cy Lau** (2025-12-23):
So it should be complaining about taking about 1 mins for complete transaction.
Yet the log ain’t in a complete form,
please copy all DAL log from 20251216-20251216 , also retdata6 logs etc
@@Daniel Leung  please check the log once @@Tovi Wang  obtaining enough information.
**Tovi Wang** (2025-12-23):
@@Cy Lau The user said that this performance did not meet their expectations and needs to identify the RCA and resolve it .Let me re-copy all the MPOS relates logs.
**Tovi Wang** (2025-12-23):
@@Cy Lau @@Daniel Leung  Except UI logs which store Not upload.2025-12-17 ALL the MPOS log here.Please help to further checking.Thanks!
**Daniel Leung** (2025-12-23):
@@Tovi Wang Please also upload UI log if store uploaded
**Tovi Wang** (2025-12-24):
@@Daniel Leung Sure,I will copy it once store uploaded the UI log.If need other logs?
**Tovi Wang** (2025-12-30):
@@Daniel Leung 2025-12-17 UI logs here.Please help to further checking.Thanks!
**Tovi Wang** (2026-01-07):
@@Daniel Leung  May I know anything founding for this case?MPOS UI log also provided in last week.Thanks!
**Daniel Leung** (2026-03-25):
According to the video, the complete Transaction action took 30s in stead of one minute. And I believe it's caused by DB issue. Multiple DB failures were found.@@Tovi Wang
**Andrew_Au** (2026-05-05):
@@Tovi Wang @@Joy Li Please update the ticket status
**Tovi Wang** (2026-05-07):
Hold on please.Waiting store double confirm and feedback the result.

## 相關資訊

- Jira: [MP-806](https://ctil.atlassian.net/browse/MP-806)
- Fix Version: 未記錄
- 解決日期: 未記錄
