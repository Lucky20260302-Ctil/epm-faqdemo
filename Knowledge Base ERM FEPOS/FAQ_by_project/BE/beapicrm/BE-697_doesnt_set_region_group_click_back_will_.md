---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Env: [https://172.16.138.101/chainstoreplus](https://172.16.138.101/chainstoreplus)"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-697
resolved: 2023-03-03
fix-version: ""
---

# BE-697: Doesn't set Region group & Click Back will get stuck in MX3003

## 問題

Env: [https://172.16.138.101/chainstoreplus](https://172.16.138.101/chainstoreplus)
Location: MX3003
Reproduce steps:
1. 
2. 
3. 
4. 
Existing result:
no matter Click OK/ Cancel, it will pop "Please enter group code or delete the Region group", then "Discard changes?" would appear again
(Ref:ChainStorePlus _ 99 - ERM Company 99 - Google Chrome 2022-11-14 15-38-22)
*This action become a loop, users have to Click Enter by keyboard back to home page

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-03-03
### Jira Comments (3 則)
**Sherman tse** (2023-02-17):
@@Thomas @@Bobby should we remove this program from standard menu?
**Thomas** (2023-02-17):
Program fixed in our development environment, need to check after program updated.
This function is developed for ImagineX, you can keep it in standard menu
**Sherman tse** (2023-03-03):
Verified on 172.16.138.55
Close case

## 相關資訊

- Jira: [BE-697](https://ctil.atlassian.net/browse/BE-697)
- Fix Version: 未記錄
- 解決日期: 2023-03-03
