---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-689
resolved: 2023-02-21
fix-version: ""
---

# BE-689: No data in a batch in Stock Replenishment Batch but sill able to execute Batch Validate

## 問題

Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)
Location: Stock Replenishment Batch Control Information (IC5000)
Reproduce steps:
1. 
2. 
3. 
Existing resu;t:
Pop up: Are you sure to proceed to Store Request Validation (IC5002)?, if Click OK, it will try to process the Validation (Ref: ChainStorePlus _ 99.mp4)
Expected resulr:
Should pop up: "No records within range" directly
Remark:
IC1002 also has the issue

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-02-21
### Jira Comments (1 則)
**Thomas** (2023-02-21):
It is normal, same as other Batch Process (such as Physical In/Out Batch Control (IC6000), please check

## 相關資訊

- Jira: [BE-689](https://ctil.atlassian.net/browse/BE-689)
- Fix Version: 未記錄
- 解決日期: 2023-02-21
