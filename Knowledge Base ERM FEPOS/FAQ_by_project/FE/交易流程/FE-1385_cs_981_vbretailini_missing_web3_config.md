---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "vbretail.ini missing web3 config"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1385
resolved: 2024-05-24
fix-version: ""
---

# FE-1385: [CS-981] vbretail.ini missing Web3 config 

## 問題

vbretail.ini missing web3 config
only change in installation package
2024-05-22:
Already added missing [3P Module Config] added in  FE package.
Please test. The link should be like this
~~QA: "~~~~[https://qacs2000web.coach.com/3PModule](https://qacs2000web.coach.com/3PModule)~~~~"~~
~~PRD: "~~~~[https://cs2000web.coach.com/3PModule](https://qacs2000web.coach.com/3PModule)~~~~"~~
KSG 32 & KMY 33
QA: "[https://](https://qacs2000web.coach.com/3PModule)<span style="color:#ff5630">qa</span>[ksjcs2000.katespade.com](http://ksjcs2000.katespade.com)[/3PModule](https://qacs2000web.coach.com/3PModule)"
PRD: "[https://](https://qacs2000web.coach.com/3PModule)[ksjcs2000.katespade.com](http://ksjcs2000.katespade.com)[/3PModule](https://qacs2000web.coach.com/3PModule)"

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-05-24
### Jira Comments (5 則)
**Andy Ko** (2024-05-13):
@@Joy Li what should I add here? please clarify.
**Joy Li** (2024-05-22):
@@Andy Ko Please test
**Joy Li** (2024-05-23):
\\172.16.183.201\localuser\coach\POSPATCH\V75\Setup_75.004.0302.0004.zip
**Andy Ko** (2024-05-23):
actual value for PRD:
[3P Module Config]
InstallationPath="[https://apawipwposwebvip01.coach.com/3PModule](https://apawipwposwebvip01.coach.com/3PModule)"
expected: PRD: "[https://cs2000web.coach.com/3PModule](https://qacs2000web.coach.com/3PModule)"
**Joy Li** (2024-05-24):
@@Andy Ko  Please provide me test report. Thanks.

## 相關資訊

- Jira: [FE-1385](https://ctil.atlassian.net/browse/FE-1385)
- Fix Version: 未記錄
- 解決日期: 2024-05-24
