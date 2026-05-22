---
tags: [faq, be, beapicrm]
component: "API"
symptom: "Update PO: /api/v1/pos/"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1038
resolved: 2025-03-27
fix-version: ""
---

# BE-1038: [API] ponumber如果入了invalid value會timeout

## 問題

Update PO: /api/v1/pos/
`"poNumber": "2025032566ABC"`
Ponumber 入了一個DB沒有的value, 會導致return timeout

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-03-27
### Jira Comments (1 則)
**Sherman tse** (2025-03-27):
created in incorrect project
close case

## 相關資訊

- Jira: [BE-1038](https://ctil.atlassian.net/browse/BE-1038)
- Fix Version: 未記錄
- 解決日期: 2025-03-27
