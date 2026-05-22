---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Store J814 Called out below."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1356
resolved: 2025-02-27
fix-version: ""
---

# FE-1356: Coach MPOS search the wrong member

## 問題

Store J814 Called out below.
SA searches for customer by phone number -> **J814WJ00162846** (**correct**) information comes up -> tap on iphone screen -> information is converted to **JXXX0013893218** (**incorrect**), This is the Issue.
I have also checked the possible things in advance,
The phone number, customer ID and member ID are not the same.
The same situation occurs when searching on another staff member's device.
When I search for the phone number on a cash register or iPad, the correct J814WJ00162846 information is reflected.
We are aware that this is the case.
What are the possible errors and how can we correct them?
Callouted time January 25, 2024 5:31 PM

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-02-27
### Jira Comments (2 則)
**Andrew_Au** (2025-02-21):
@jason Please update the ticket status
**Andrew_Au** (2025-02-24):
@@Jason Wu  Who know the ticket status ?

## 相關資訊

- Jira: [FE-1356](https://ctil.atlassian.net/browse/FE-1356)
- Fix Version: 未記錄
- 解決日期: 2025-02-27
