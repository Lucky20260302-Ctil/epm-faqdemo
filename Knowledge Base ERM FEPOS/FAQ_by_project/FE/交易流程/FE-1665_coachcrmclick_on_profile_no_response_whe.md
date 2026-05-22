---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "[Coach][CRM]Click on Profile no response when member who is not existing in CRM"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1665
resolved: 2025-03-31
fix-version: ""
---

# FE-1665: [Coach][CRM]Click on Profile no response when member who is not existing in CRM

## 問題

[Coach][CRM]Click on Profile no response when member who is not existing in CRM
Testing  data: OC1350C00015385 (not existing in CRM but existing in backend DB)
Reproduce steps:
1. 
2. 
3. 
4. 
Existing result:
- 
- 
BEAPI return jsondata with null

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-03-31
### Jira Comments (4 則)
**Sherman tse** (2025-03-31):
Issue set as close, fixed by beapi
**Sherman tse** (2025-03-31):
Issue reopen, beapi return null , fepos still has the issue
**Sang** (2025-03-31):
@@Sherman tse Fixed in v750.04R11A. source code uploaded to
1. 
2. 
3.
**Sherman tse** (2025-03-31):
Verified on QA
member with no membership number , and click on profile & purchase history, then pop up Profile not availble

## 相關資訊

- Jira: [FE-1665](https://ctil.atlassian.net/browse/FE-1665)
- Fix Version: 未記錄
- 解決日期: 2025-03-31
