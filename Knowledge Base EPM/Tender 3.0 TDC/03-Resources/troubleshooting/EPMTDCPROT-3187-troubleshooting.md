---
tags: bug, jira, uat-phase1-hotfixbatch3, hotfix
component: UI/UX
symptom: "No need to show parent e-form in the approval page."
root-cause: ""
solution: "3 Test Result ： When approving the rfq setting form, the data of part 1 can be seen，test fail"
jira: EPMTDCPROT-3187
resolved: 2026-04-13
---

# EPMTDCPROT-3187: EPRO-787 [Phase 1 Hot Fix] No need to show parent e-form in the approval page

## 問題

[Link:https://hktdc.atlassian.net/browse/EPRO-787] 
No need to show parent e-form in the approval page.
E.g. below is the approval page of Issuance of RFQ / Tender e-form, and the parent e-form (RFQ Setting) was also displayed.
[Image]
There was related discussion before.
[Link:https://hktdc.atlassian.net/browse/EPRO-712] asked for display of full reg e-form as per the full reg response checking e-form.
For other forms, if there is no parent e-form showed in the request e-form, no need to show in the corresponding approval page.

## 根因

[Link:https://hktdc.atlassian.net/browse/EPRO-712] asked for display of full reg e-form as per the full reg response checking e-form.
For other forms, if there is no parent e-form showed in the request e-form, no need to show in the corresponding approval page.
HotFix 3 Test Result ： When approving the rfq setting form, the data of part 1 can be seen，test fail
UAT Test Result: When approving Issuance of RFQ/Tender, no data from the parent form will appear，test pass
The data of the parent form cannot be seen when approval Issuance of RFQ/Tender，batch 3 test pass

## 解法

3 Test Result ： When approving the rfq setting form, the data of part 1 can be seen，test fail

## 相關問題

- [[EPRO-712]]
- [[EPRO-787]]

