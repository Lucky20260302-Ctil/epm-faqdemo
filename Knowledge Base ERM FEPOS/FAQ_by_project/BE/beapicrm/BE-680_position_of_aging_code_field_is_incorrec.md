---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-680
resolved: 2023-02-21
fix-version: ""
---

# BE-680: Position of Aging code field is incorrect

## 問題

Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)
Location:
Secondary > optional > Aging table maintenance (MF5008)
Existing result:
Field of inserting Aging code placed at incorrect position (under from date/ to date)
Expected result:
Field of inserting Aging code should be placed at first row (Ref: image-2022-11-08-13-50-45-890.png)

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-02-21
### Jira Comments (1 則)
**Thomas** (2023-02-17):
This program UI is same as .NET version

## 相關資訊

- Jira: [BE-680](https://ctil.atlassian.net/browse/BE-680)
- Fix Version: 未記錄
- 解決日期: 2023-02-21
