---
tags: [faq, be, polling]
component: "polling"
symptom: "MO region 3 stores OC09, OC515, OC17 PCD failed to upload due to error 'payment type not found'"
root-cause: "待提取"
solution: "### Jira Comments (4 則)"
jira: BE-1011
resolved: 
fix-version: ""
---

# BE-1011: [RIN01457238][RIN01457099]MO region 3 stores OC09, OC515, OC17 PCD failed to upload due to error "payment type not found"

## 問題

MO region 3 stores OC09, OC515, OC17 PCD failed to upload due to error "payment type not found"
@@Cy Lau @@Bobby@@Jason Wu  PC file for your further checking.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (4 則)
**Jason Wu** (2025-02-26):
@@Tovi Wang  Please also help to copy the posting log & the Dbtbk.
**Tovi Wang** (2025-02-26):
@@Jason Wu DBtbk here
Because  app server very slow.I am trying to copy posting log.
**Jason Wu** (2025-02-26):
@@Tovi Wang It should caused by the loctab_curr changed to USD by user dyu in 25/2 3p.m.
**Tovi Wang** (2025-02-26):
Issue fixed now.Please help to calarify the RCA.

## 相關資訊

- Jira: [BE-1011](https://ctil.atlassian.net/browse/BE-1011)
- Fix Version: 未記錄
- 解決日期: 未記錄
