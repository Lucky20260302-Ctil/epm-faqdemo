---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-676
resolved: 2022-11-25
fix-version: ""
---

# BE-676: Supplier Code used incorrect words limitation

## 問題

Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)
ACC: sxd                          PW: sxd
Location: Process > Purchase Order Maintenance (PO3000)
Reproduce steps:
1. 
2. 
3. 
4. 
Existing result:
Field of Supplier is rounded by red outline, applied Text with Max Length = 10
Expected result:
Words limitation of Supplier Code should be 15 words

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2022-11-25
### Jira Comments (2 則)
**Thomas** (2022-11-18):
Already fixed in development environment
**Sherman tse** (2023-01-05):
Verified on 101
Close case

## 相關資訊

- Jira: [BE-676](https://ctil.atlassian.net/browse/BE-676)
- Fix Version: 未記錄
- 解決日期: 2022-11-25
