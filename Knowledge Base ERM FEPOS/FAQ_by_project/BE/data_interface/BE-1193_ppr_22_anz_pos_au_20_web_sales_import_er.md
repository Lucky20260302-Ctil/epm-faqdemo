---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "Coach QA team callout when import follow ecom sales file,then pop out 'Exchange rate not found’ erro"
root-cause: "待提取"
solution: "### Jira Comments (1 則)"
jira: BE-1193
resolved: 
fix-version: ""
---

# BE-1193: [PPR-22] - ANZ POS - AU 20 Web sales import error - Exchange rate not found

## 問題

Coach QA team callout when import follow ecom sales file,then pop out 'Exchange rate not found’ error ,can you check below error?
I used the same format before to import, it was inserted successfully.
but this time it is not working.
Troubleshooting:
1.2025-10-23 有一个正常导入的文件，没有error.
2.之前可以正常导入的文件
3.现在重新导入之前正常导入的文件，也是有同样的error
[4.AU](http://4.AU) 20 region AU paytab is 'AUD'

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (1 則)
**Tovi Wang** (2025-10-29):
incorrect currency code setting.issue fixed

## 相關資訊

- Jira: [BE-1193](https://ctil.atlassian.net/browse/BE-1193)
- Fix Version: 未記錄
- 解決日期: 未記錄
