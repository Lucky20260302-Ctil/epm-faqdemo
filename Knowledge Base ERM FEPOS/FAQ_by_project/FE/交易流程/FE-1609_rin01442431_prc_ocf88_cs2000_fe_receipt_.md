---
tags: [faq, fe, 交易流程]
component: "Front End v750.01R01A"
symptom: "PRC regrion,更新到v75以后，TMU打印机打印sales memo纸张长度过长，行间距过大，并且有数据夸行显示问题。"
root-cause: "待提取"
solution: "### Jira Comments (5 則)"
jira: FE-1609
resolved: 
fix-version: ""
---

# FE-1609: RIN01442431-PRC - OCF88  - CS2000 - FE : receipt length is too long after POS upgrade to V75

## 問題

PRC regrion,更新到v75以后，TMU打印机打印sales memo纸张长度过长，行间距过大，并且有数据夸行显示问题。

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (5 則)
**Sang** (2025-01-16):
@@pierre.shi please confirm tblconfig.TMU_PRINTER_REC_LINE_CHAR='42'
**pierre.shi** (2025-01-16):
Hi @@Sang the setting in opos is 42, and in dbtrans is 44.
**Sang** (2025-01-16):
@@pierre.shi ⁠It should be 42. Please set dbtrans value to 42.
**pierre.shi** (2025-01-16):
thanks @@Sang ,this issue is resolved.
**Andrew_Au** (2025-02-24):
Is a config settting issue.

## 相關資訊

- Jira: [FE-1609](https://ctil.atlassian.net/browse/FE-1609)
- Fix Version: 未記錄
- 解決日期: 未記錄
