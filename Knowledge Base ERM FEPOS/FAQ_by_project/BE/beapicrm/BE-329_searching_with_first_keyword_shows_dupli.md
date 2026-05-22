---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "<u>Case 1</u>"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-329
resolved: 2021-01-15
fix-version: ""
---

# BE-329: Searching with first keyword shows duplicate results

## 問題

<u>Case 1</u>
Search first keyword using "exchange", it return duplicated results start from the wording "exchange".
<u>Case 2</u>
Search keyword using "TAX" , the duplicated results only appear start from the first wording "TAX",  compared other results e.g. VAT **TAX** Rate (MX2000) is display once at normal.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2021-01-15
### Jira Comments (1 則)
**Thomas** (2020-11-04):
This is a known bug and already fixed, will be updated in next release (4/11/2020)

## 相關資訊

- Jira: [BE-329](https://ctil.atlassian.net/browse/BE-329)
- Fix Version: 未記錄
- 解決日期: 2021-01-15
