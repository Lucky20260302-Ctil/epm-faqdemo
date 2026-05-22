---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "_（Jira 中無 description 內容）_"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-902
resolved: 2022-08-18
fix-version: ""
---

# FE-902: Agile New Member Expire Date

## 問題

_（Jira 中無 description 內容）_

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2022-08-18
### Jira Comments (1 則)
**Sang** (2021-01-19):
AIGLE - Permanent New Member Expiry Date
Config:
1. tblconfig.CompanyCode = "AIGLE"
2. tblconfig.NVIPPerExpDate = "12"
3. tblconfig.NewVIPExpiredInYearEnd = "Y+01"
Test Case :
POS Date        New VIP Expire Date
2020-12-29	2021-12-31-->2022-01-31
2021-01-18	2021-12-31-->2022-01-31
2021-01-31	2021-12-31-->2022-01-31
2021-02-01	2021-12-31-->2022-01-31-->2023-01-31
2021-02-28	2021-12-31-->2022-01-31-->2023-01-31
2021-12-12	2021-12-31-->2022-01-31-->2023-01-31
2021-12-31 	2021-12-31-->2022-01-31-->2023-01-31

## 相關資訊

- Jira: [FE-902](https://ctil.atlassian.net/browse/FE-902)
- Fix Version: 未記錄
- 解決日期: 2022-08-18
