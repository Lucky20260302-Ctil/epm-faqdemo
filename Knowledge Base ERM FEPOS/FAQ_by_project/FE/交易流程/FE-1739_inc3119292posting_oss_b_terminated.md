---
tags: [faq, fe, 交易流程]
component: "Front End v750.01R01A"
symptom: "[INC3119292]Posting OSS_B terminated."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1739
resolved: 2025-09-08
fix-version: ""
---

# FE-1739: [INC3119292]Posting OSS_B terminated

## 問題

[INC3119292]Posting OSS_B terminated.
Checked that line34 was seperated in two lines.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-09-08
### Jira Comments (9 則)
**Joy Li** (2025-07-30):
Please help to copy WA log too @@pierre.shi
**pierre.shi** (2025-07-30):
Hi@@Joy Li wa log has been uploaded.
**Automation for Jira** (2025-07-31):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2025-07-31):
@@Joy Li @@pierre.shi @@Bobby  @@Cy Lau Member name (WA log) return from Acxiom contains LF, this LF carried to DB and write PCD ‘34’. Please consider validate data from third party in web API or client write PCD side.
**Andrew_Au** (2025-08-27):
@@Joy Li @@pierre.shi Pending for a long time. Please update the ticket status
**Andrew_Au** (2025-09-08):
@@pierre.shi @@Joy Li @@Tovi Wang Please update the ticket status
**pierre.shi** (2025-09-08):
@@Andrew_Au please help to close
**Automation for Jira** (2025-09-08):
Issue has been created since
Days since: 40
Week since : 5
Issue due date difference
Days since : 
Weeks since:
**Tovi Wang** (2025-09-15):
@@Joy Li @@pierre.shi  [FYI.CN](http://FYI.CN) posting terminate issue details.

## 相關資訊

- Jira: [FE-1739](https://ctil.atlassian.net/browse/FE-1739)
- Fix Version: 未記錄
- 解決日期: 2025-09-08
