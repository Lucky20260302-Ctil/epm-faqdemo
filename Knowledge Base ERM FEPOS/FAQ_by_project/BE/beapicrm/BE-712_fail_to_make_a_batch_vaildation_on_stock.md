---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Env: [https://172.16.138.101/chainstoreplus/login](https://172.16.138.101/chainstoreplus/login)"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-712
resolved: 2024-04-27
fix-version: ""
---

# BE-712: Fail to make a batch vaildation on Stock Replenishment (IC5000)

## 問題

Env: [https://172.16.138.101/chainstoreplus/login](https://172.16.138.101/chainstoreplus/login)
ACC: sx1                   PW: sx1
Reproduce steps:
1. 
2. 
3. 
Exisitng result:
Fail to make a batch vaildation & Pop an error as attachment (Ref:image-2023-01-17-10-31-22-444.png)
Remark:
Same function on Remote control: 101 env works fine

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-04-27
### Jira Comments (2 則)
**Ken Lam** (2023-01-17):
1. Please confirm CSDATA[ companyCode ].dbo.dbconfig.dbconfig_key have 'txt_path_web' and dbconfig_value is correct.
2.Please confirm that the setting of txt_path_web is the correct file directory
**Ken Lam** (2023-01-17):
No error pops up when the correct file directory is created

## 相關資訊

- Jira: [BE-712](https://ctil.atlassian.net/browse/BE-712)
- Fix Version: 未記錄
- 解決日期: 2024-04-27
