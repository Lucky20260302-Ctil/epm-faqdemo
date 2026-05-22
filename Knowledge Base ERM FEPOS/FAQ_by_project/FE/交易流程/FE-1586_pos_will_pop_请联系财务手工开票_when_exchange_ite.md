---
tags: [faq, fe, 交易流程]
component: "Front End v720.02"
symptom: "Original Sales memo:  OC37-20054018 on 8th Dec"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1586
resolved: 2024-12-24
fix-version: ""
---

# FE-1586: Pos will pop '请联系财务手工开票' when exchange items in other store

## 問題

Original Sales memo:  OC37-20054018 on 8th Dec
Exchange Sales memo: OC201-00032621 on 14th Dec:
the exchanged has been done normally and sales memo has been printed but pos popped 'Please contact the finance department for manual invoicing'.
Please help to check why pos popped 'Please contact the finance department for manual invoicing', and what should we do next.
logs link: Onedrive [20241216_FE-1586](https://ctil00046-my.sharepoint.com/:f:/g/personal/jason_wu_ctil00046_onmicrosoft_com/EiytitqFAypAsPSKyaL7yc4BparzJXQ6XTg-DEeTk4K-ng?e=CGKcwX)

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-12-24
### Jira Comments (4 則)
**Sang** (2024-12-16):
@@pierre.shi  For Coach China 百望 einvoice operation, if return memo was issued by Department store, PO should pop up alert message 請聯繫財務手工開票. Please check is the return item sold by department store.
Ref: Coach China 百望 einvoice (KTS 220531 v720.02R18, v750.02 Jira FE-1118)
**pierre.shi** (2024-12-16):
Hi@@Sang  yes, the return item is sold by another store.
what’s the logic? could you please describe it detailed？
thanks
**Sang** (2024-12-16):
@@pierre.shi the logic for Coach China 百望 einvoice operation: if return memo was issued by Department store, POS should pop up alert message 請聯繫財務手工開票. Details please refer to Jira FE-1118
**pierre.shi** (2024-12-18):
Hi @@Sang  thanks

## 相關資訊

- Jira: [FE-1586](https://ctil.atlassian.net/browse/FE-1586)
- Fix Version: 未記錄
- 解決日期: 2024-12-24
