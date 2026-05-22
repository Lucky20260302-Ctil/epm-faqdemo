---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-683
resolved: 2023-03-03
fix-version: ""
---

# BE-683: Cannot select export file name in Export POS Master Data

## 問題

Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)
Location: Export POS Master Data (DI9008)
Reproduce steps:
1. 
2. 
Existing result:
Field of export file name show as dimmed & **<span style="color:#ff0000">no button</span>** can be clicked to select file name (Ref:image-2022-11-09-11-45-50-465.png, screenshot-1.png)
Remark:
Seems missing a Browse button next to Field of export file name

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-03-03
### Jira Comments (2 則)
**Sherman tse** (2023-02-17):
still missing "browse" button
**Thomas** (2023-02-21):
This is a technical issue, WEB application can't access the local client directory. Even if it can access, you are talking about download huge data, it will have a performance issue. Therefore, the output folder can't be changed.

## 相關資訊

- Jira: [BE-683](https://ctil.atlassian.net/browse/BE-683)
- Fix Version: 未記錄
- 解決日期: 2023-03-03
