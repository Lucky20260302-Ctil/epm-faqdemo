---
tags: [faq, mp, 系統兼容]
component: "Backend"
symptom: "_（Jira 中無 description 內容）_"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-653
resolved: 2023-06-09
fix-version: ""
---

# MP-653: LandsD day end checking popup error

## 問題

_（Jira 中無 description 內容）_

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-06-09
### Jira Comments (4 則)
**Hans Wong** (2023-06-09):
@@Johnny Cheung please help Andrew to see what's the problem.
**Johnny Cheung** (2023-06-09):
The path should be "D:\ChainStorePlus-LandsD\csms70\Obj" instead of "D:\ChainStorePlus\csms70\Obj" inside the script, right?
**Andrew_Au** (2023-06-09):
Please ignore the error. I missied pass the program id in command line
**Johnny Cheung** (2023-06-09):
Missing program ID, it should be run "csplus_dayendvalidation99.exe IC9000 99 sx1" instead of "csplus_dayendvalidation99.exe 99 sx1"

## 相關資訊

- Jira: [MP-653](https://ctil.atlassian.net/browse/MP-653)
- Fix Version: 未記錄
- 解決日期: 2023-06-09
