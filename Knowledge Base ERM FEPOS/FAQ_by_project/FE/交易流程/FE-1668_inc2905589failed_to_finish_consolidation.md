---
tags: [faq, fe, 交易流程]
component: "Front End v750.01R01A"
symptom: "PRC region, POS V75, while doing dayend, it popped up error: Database not exist."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1668
resolved: 2025-06-05
fix-version: ""
---

# FE-1668: [INC2905589]failed to finish consolidation,  it popped up error: Database not exist.

## 問題

PRC region, POS V75, while doing dayend, it popped up error: Database not exist.
PC and RP file has been generated but no RC file.
no dayend report and  consolidation report printed.
checked in logs, it only showed :Database not exist. in T9 logs.
on the next day ,can finish consolidation without any error.
This issue occurred on 8th and 9th April.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-06-05
### Jira Comments (4 則)
**Sang** (2025-04-10):
@@Tovi Wang @@pierre.shi @@Jason Wu
Please check SSE DBtrans.MDF, properly missing table(s).  This Error may due to prepare M-POS Dayend report / data but fail to get data from dbtrans (SSE).    Drop dbtrans (SSE), and re-start CSPLUS to re-create a new one.
**pierre.shi** (2025-04-14):
Hi@@Sang on the day I re-created the dbtrans on 10th April, it could finish consolidation normally that day. but on the next several days ,this issue occurred again.
The pos ver on OC189 is  75.004.0903.0000.
but when did the consolidation, the date format is YYYY-MM-DD or YYYY-DD-MM.
If need any more logs ,please inform me.
**Andrew_Au** (2025-06-05):
@@Tovi Wang @@pierre.shi Please update the ticket status
**pierre.shi** (2025-06-05):
Hi @@Andrew_Au  please help to close this ticket.

## 相關資訊

- Jira: [FE-1668](https://ctil.atlassian.net/browse/FE-1668)
- Fix Version: 未記錄
- 解決日期: 2025-06-05
