---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "Brand: Coach"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-776
resolved: 2024-09-04
fix-version: ""
---

# BE-776: CS-595:Chinese Character in store address

## 問題

Brand: Coach
Region: PRC/TW/JP
**Issue Detail:**
We have 40 characters limit on BE store address.
All Chinese, Korea and Japan character will count 1 in BE, BUT it will count as 2 characters when we printer receipt.
if we have Chinese character in address, it may over 40 when we print receipt. like below
it is allowed in BE, but it is not allowed in FE, it will has printing issue and no store information and no payment line.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-09-04
### Jira Comments (1 則)
**Joy Li** (2023-06-29):
Can we have length checking in address field?

## 相關資訊

- Jira: [BE-776](https://ctil.atlassian.net/browse/BE-776)
- Fix Version: 未記錄
- 解決日期: 2024-09-04
