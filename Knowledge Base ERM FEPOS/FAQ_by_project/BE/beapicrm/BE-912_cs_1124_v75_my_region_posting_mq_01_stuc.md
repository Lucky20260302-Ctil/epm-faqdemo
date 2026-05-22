---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "_（Jira 中無 description 內容）_"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-912
resolved: 2024-10-18
fix-version: ""
---

# BE-912: [CS-1124] V75 - MY region Posting MQ_01 stuck

## 問題

_（Jira 中無 description 內容）_

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-10-18
### Jira Comments (1 則)
**Joy Li** (2024-10-18):
Tested by @@Andrew_Au
Released by @@Joy Li to COACH Team : BE_V70R3.70 (2024-10-18)
Reopen by PRD MY stuck issue
l   [CS-1124] V75 - MY region Posting MQ_01 stuck
n   RCA: When psterr table contain two error record which psterr_date, hh, mn, ss and ms is same, program fail to get the correct running sequence. Therefore posting will stuck if posting file need to insert new psterr record.
n   Resolve the program by check the insert key with psterr_date, hh, mn, ss and ms + psterr_seq.

## 相關資訊

- Jira: [BE-912](https://ctil.atlassian.net/browse/BE-912)
- Fix Version: 未記錄
- 解決日期: 2024-10-18
