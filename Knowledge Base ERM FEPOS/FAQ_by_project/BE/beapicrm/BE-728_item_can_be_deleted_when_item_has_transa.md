---
tags: [faq, be, beapicrm]
component: "Backend (Web)"
symptom: "Item can be deleted in item master when item has transaction."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-728
resolved: 2023-04-06
fix-version: ""
---

# BE-728: Item can be deleted when item has transaction

## 問題

Item can be deleted in item master when item has transaction.
Expected result:
Item cannot be deleted in item master when item has transaction.
Remark:
.net version has no issue (Ref: image-2023-03-22-15-37-24-813.png)
*Transaction from Sales Memo Journal Enquiry (SE7011)

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2023-04-06
### Jira Comments (1 則)
**Sherman tse** (2023-04-06):
Verified on 172.16.138.55
Close case

## 相關資訊

- Jira: [BE-728](https://ctil.atlassian.net/browse/BE-728)
- Fix Version: 未記錄
- 解決日期: 2023-04-06
