---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "Reproduce steps:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-635
resolved: 2023-02-14
fix-version: ""
---

# MP-635: Fail to add new member when inserted email address

## 問題

Reproduce steps:
1. 
2. 
Existing result:
Fail to add new member & pop up error: [999] This email has been registered (reg: image-2023-02-14-16-14-07-369.png)

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-02-14
### Jira Comments (2 則)
**Sherman tse** (2023-02-14):
config issue, close case
**Daniel Leung** (2023-02-15):
Deprecated config
ENABLEONLINEEMAILVALIDATION
should always set to N, will casue mPos email validation error

## 相關資訊

- Jira: [MP-635](https://ctil.atlassian.net/browse/MP-635)
- Fix Version: 未記錄
- 解決日期: 2023-02-14
