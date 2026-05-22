---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "**Issue Detail**"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1569
resolved: 2025-02-12
fix-version: ""
---

# FE-1569: [CS-1148] Issue_KR_not able to return items sold from other store RIN01369752 RIN01390154 RIN01388455 CS-1119

## 問題

**Issue Detail**
not able to return item （**this item was not sold in same store**）in KR region
e.g.
OC825 try to return item C3916 B4/BK, original sales memo is OC807 00038691.
after we input qty and return sales memo OC807 00038691, it will show not able to find item C3916 B4/BK in this sales memo.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-02-12
### Jira Comments (4 則)
**Joy Li** (2024-11-25):
@@Andrew_Au  @@Joseph_Hu 
Please arrange testing  on FE current version V75.004.0702.XXXX or V75.004.0902.0000
**Sang** (2024-11-26):
@@Joseph_Hu @@Andrew_Au  Please get DAL and T9, check is it fail to connect backend DB at the moment.
**Andrew_Au** (2024-11-26):
@@Joy Li We will test the version  v75.004.0702.000 and V750040902.001. Is that correct test this 2 version of the POS  ?
**Andrew_Au** (2025-02-12):
@@Joseph_Hu Please update the ticket status.

## 相關資訊

- Jira: [FE-1569](https://ctil.atlassian.net/browse/FE-1569)
- Fix Version: 未記錄
- 解決日期: 2025-02-12
