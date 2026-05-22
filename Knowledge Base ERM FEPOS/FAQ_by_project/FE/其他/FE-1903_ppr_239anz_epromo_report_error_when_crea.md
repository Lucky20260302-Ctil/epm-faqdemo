---
tags: [faq, fe, 其他]
component: "Service"
symptom: "Coach QA Team tried to create one COACH AU 20 QA coupon in ePromo, but after clicking save button, t"
root-cause: "待提取"
solution: "### Jira Comments (2 則)"
jira: FE-1903
resolved: 
fix-version: ""
---

# FE-1903: [PPR-239]ANZ ePromo - Report error when create the coupon

## 問題

Coach QA Team tried to create one COACH AU 20 QA coupon in ePromo, but after clicking save button, the error occurred, could you please help to check and fix?
User: CJ-RQ-1

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (2 則)
**Tovi Wang** (2026-03-20):
Hi @@Jerry Wong As we talked,Please help to take a look this error,Do we have any relates log for further checking?Please give me some advice,Thanks!
CC @@Joy Li @@Bobby @@Cy Lau
**Tovi Wang** (2026-03-20):
[1.QA](http://1.QA) AU DB missing the dbconfig item no 'EVR010B' in itmast table and itmsrch table.
2.This normal sample[.QA](http://reference.QA) SG DB  have the dbconfig item no 'BKL14' in itmast table and itmsrch table.

## 相關資訊

- Jira: [FE-1903](https://ctil.atlassian.net/browse/FE-1903)
- Fix Version: 未記錄
- 解決日期: 未記錄
