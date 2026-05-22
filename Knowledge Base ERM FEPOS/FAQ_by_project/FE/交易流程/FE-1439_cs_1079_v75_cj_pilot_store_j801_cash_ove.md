---
tags: [faq, fe, 交易流程]
component: "Day End"
symptom: "_（Jira 中無 description 內容）_"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1439
resolved: 2024-09-23
fix-version: ""
---

# FE-1439: [CS-1079] V7.5 CJ Pilot store J801 Cash Over short issue since May 9th

## 問題

_（Jira 中無 description 內容）_

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-09-23
### Jira Comments (10 則)
**Andrew_Au** (2024-06-28):
Affect the production version, support team need to do the data patch in daily suport.
**Andrew_Au** (2024-06-28):
Found V75 POS no value in dayendh_cash_phy_total_amt field.
**Andrew_Au** (2024-06-28):
@sang record type 94 missing write dayendh_cash_phy_total_amt field value
**Andrew_Au** (2024-06-28):
@sang A0 records missing in pcd file.
**Sang** (2024-07-03):
v750.04R04D
1. 
2.
**Sang** (2024-07-03):
**Sang** (2024-07-03):
**Sang** (2024-07-03):
**Sherman tse** (2024-07-05):
Verified on QA, Attached test case
**Andrew_Au** (2024-09-17):
@@Joy Li  Please update the ticket

## 相關資訊

- Jira: [FE-1439](https://ctil.atlassian.net/browse/FE-1439)
- Fix Version: 未記錄
- 解決日期: 2024-09-23
