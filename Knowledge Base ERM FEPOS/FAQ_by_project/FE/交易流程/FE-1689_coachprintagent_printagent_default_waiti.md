---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "[Coach][PrintAgent] PrintAgent default waiting Time not enough, x32TMUPrint.exe would occur timeout"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1689
resolved: 2025-09-30
fix-version: ""
---

# FE-1689: [Coach][PrintAgent] PrintAgent default waiting Time not enough, x32TMUPrint.exe would occur timeout 

## 問題

[Coach][PrintAgent] PrintAgent default waiting Time not enough, x32TMUPrint.exe would occur timeout
Currently,POS call PrintAgent waiting Time,
      a. Memo - 10 Sec
      b. Enquiry Report - 30 Sec
      c. DayEnd report - 60 Sec
Suggest to make config configurable, so that we can adjust it to ideal waiting time

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-09-30
### Jira Comments (2 則)
**Sherman tse** (2025-05-12):
Enhancement completed by Yeung
Close case
**Automation for Jira** (2025-09-30):
Issue has been created since
Days since: 144
Week since : 20
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [FE-1689](https://ctil.atlassian.net/browse/FE-1689)
- Fix Version: 未記錄
- 解決日期: 2025-09-30
