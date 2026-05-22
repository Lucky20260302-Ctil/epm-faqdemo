---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "Todo:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-572
resolved: 2022-11-18
fix-version: ""
---

# MP-572: MPOS-After modify the discount as 50%, then the price will change to 0

## 問題

Todo:
Implement the changes from 3.20.x
---
test Info:
FE: v72.0219.0100
IPA: 3.19.1
API: 3.19.2(Local IIS and Cloud IIS)
Description: We try to modify the item price on MPOS, but after we change the discount as 50%, then it will change to 0. This happen to both local IIS and Cloud IIS. Please check the details in attach video. thanks

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2022-11-18
### Jira Comments (3 則)
**Daniel Leung** (2022-10-20):
API return error ORGCurrPrice value.
Reterned 0 ORGCurrPrice will cause percentage price override calculation error.
**Cy Lau** (2022-10-20):
Checked with API:
GetProducts function called :
items.Add(Shared.ConvertItemData2Product(item));
which missing fields
**Cy Lau** (2022-10-28):
The 50% solved on 3.19.2
But the lock removal not yet implement

## 相關資訊

- Jira: [MP-572](https://ctil.atlassian.net/browse/MP-572)
- Fix Version: 未記錄
- 解決日期: 2022-11-18
