---
tags: [faq, fe, 交易流程]
component: "Front End v750.01R01A"
symptom: "The POS ver is V75.004.0903."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1606
resolved: 2025-02-24
fix-version: ""
---

# FE-1606: RIN01441233-Till 0 cannot print out dayend report and shows printer error, this issue also occurred while reprint dayend report

## 問題

The POS ver is V75.004.0903.
POS use laser printer.
the value of enbalecrystalreport is Y
The printer name config in db is the same as that in  windows printer list.
We copied kos.lprinter.dll and kosprinter.exe from till1 and replaced, but issue still.
After POS repaired, issue still.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-02-24
### Jira Comments (5 則)
**Sang** (2025-01-13):
@@pierre.shi Is this till day end print normal before Jan/12. When did this till upgrade to v75. please copy dal (from both Retdata6 and csplus folder) and t9 log and dbtrans.sdf
**Sang** (2025-01-13):
@@pierre.shi please check is POS configured window  printer same as window default printer
**pierre.shi** (2025-01-13):
We confirm that the POS configured laser printer is the same as that in windows printer list. and has been set as default printer.but issue still .
**pierre.shi** (2025-01-13):
even if we set the pdf printer as default printer, pos still popped up this error.
**Tovi Wang** (2025-01-14):
@@Sang @@pierre.shi @@Cy Lau  this issue should be fixed.Please refer to
internal Jira [🔗](https://ctil.atlassian.net/browse/FE-1608)

## 相關資訊

- Jira: [FE-1606](https://ctil.atlassian.net/browse/FE-1606)
- Fix Version: 未記錄
- 解決日期: 2025-02-24
