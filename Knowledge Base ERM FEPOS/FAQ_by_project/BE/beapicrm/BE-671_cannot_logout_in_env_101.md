---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Env: [https://172.16.138.101/chainstoreplus/home](https://172.16.138.101/chainstoreplus/home)"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-671
resolved: 2022-11-07
fix-version: ""
---

# BE-671: Cannot logout in Env 101

## 問題

Env: [https://172.16.138.101/chainstoreplus/home](https://172.16.138.101/chainstoreplus/home)
ACC: P01    PW: P01

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2022-11-07
### Jira Comments (1 則)
**Ken Lam** (2022-11-07):
please make sure   **apiUrl** in
environment.ts ,
environment.prod.ts,
assets/config.json
is the same value.

## 相關資訊

- Jira: [BE-671](https://ctil.atlassian.net/browse/BE-671)
- Fix Version: 未記錄
- 解決日期: 2022-11-07
