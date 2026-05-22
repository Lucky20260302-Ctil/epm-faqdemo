---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "SHOWONHANDQTY_TRANSFER=Y, cannot show enable show the onhand qty column in transfer module."
root-cause: "待提取"
solution: "### Jira Comments (1 則)"
jira: FE-1165
resolved: 
fix-version: ""
---

# FE-1165: Transfer out show onhand QTY

## 問題

SHOWONHANDQTY_TRANSFER=Y, cannot show enable show the onhand qty column in transfer module.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (1 則)
**Andrew_Au** (2022-10-22):
set  SUPPRESSWRITEPCD=Y , should not write new member record to  PCD file.  Now MPOS still write the new member records send to BE.

## 相關資訊

- Jira: [FE-1165](https://ctil.atlassian.net/browse/FE-1165)
- Fix Version: 未記錄
- 解決日期: 未記錄
