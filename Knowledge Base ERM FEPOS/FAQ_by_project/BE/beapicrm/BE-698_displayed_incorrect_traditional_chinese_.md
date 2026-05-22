---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-698
resolved: 2023-01-06
fix-version: ""
---

# BE-698: Displayed incorrect Traditional Chinese words

## 問題

env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)
Home page: Show **註銷** in Logout buttton (Ref: 1.png)
se8007: 自由&配搭促銷程式資料 (MX6008) > Click Create> 贈品處理 > **加光盤.冷** on Plus Disc./Cond. (Ref: 2.png)
mx5002: 銷售工作人員的密碼政策的信息的表 (MX5002) > Click Create > **限制行輓救最近使用的密碼時** on Restrict the resue recently used passwords times (Ref: 3.png)

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-01-06
### Jira Comments (2 則)
**Thomas** (2022-11-18):
Already fixed in development environment
**Sherman tse** (2022-12-02):
Tested on env 55, still has issue in mx5002 & Logout buttton
seems not deployed to 55 yet?
(ref: 20221202_55env.png)

## 相關資訊

- Jira: [BE-698](https://ctil.atlassian.net/browse/BE-698)
- Fix Version: 未記錄
- 解決日期: 2023-01-06
