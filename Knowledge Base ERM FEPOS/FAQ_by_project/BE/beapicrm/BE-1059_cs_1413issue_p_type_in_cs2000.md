---
tags: [faq, be, beapicrm]
component: "API"
symptom: "Issue_Detail:"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1059
resolved: 2025-07-04
fix-version: ""
---

# BE-1059: [CS-1413]Issue_P type in CS2000

## 問題

Issue_Detail:
when API return a P type member，CS2000 should convert “P” to "C". but CS2000 didn't convert to this member to "C" and send "P" to Car
Induced by Async insertion workflow
The data was directly passed to FEPOS

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-07-04
### Jira Comments (3 則)
**Cy Lau** (2025-04-28):
20240424 1749
<u>**Program Release V1.07.18(Acxiom CRM)**</u>
Release:
- 
- 
- 
Notes:
Release notes:
- 
- 
Source code:
- 
-
**Andrew_Au** (2025-06-05):
@@Sherman tse  Please update the ticket status
**Joy Li** (2025-07-04):
released on 2025-04-26 BE-V70R3.101

## 相關資訊

- Jira: [BE-1059](https://ctil.atlassian.net/browse/BE-1059)
- Fix Version: 未記錄
- 解決日期: 2025-07-04
