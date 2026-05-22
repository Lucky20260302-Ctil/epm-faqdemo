---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "<u>COACH CS-856: Issue_Main UPC code issue</u>"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1339
resolved: 2024-11-29
fix-version: ""
---

# FE-1339: Label Printing for multi EAN handling

## 問題

<u>COACH CS-856: Issue_Main UPC code issue</u>
Testing FE DB: 172.16.138.180
ItmEan_Item_No = '80125'and ItmEan_Item_Col='FLI' and ItmEan_Item_Size = 'S'  <span style="color:#ff0000">>> have 2 EAN</span>
Label printing only get and print the smallest EAN. COACH reported that the last update EAS should be print >> 884830134087 in item 80125-FI-S should be print.
Could you please help?

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-11-29
### Jira Comments (2 則)
**Andrew_Au** (2024-11-29):
@@Joy Li  Can we change the status to Close
**Joy Li** (2024-11-29):
released in V75.0004.0301.0000
please close @@Andrew_Au

## 相關資訊

- Jira: [FE-1339](https://ctil.atlassian.net/browse/FE-1339)
- Fix Version: 未記錄
- 解決日期: 2024-11-29
