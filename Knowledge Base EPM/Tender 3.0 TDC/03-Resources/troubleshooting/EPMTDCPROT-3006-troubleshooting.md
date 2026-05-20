---
tags: bug, jira, ext-tdc-uat, uat
component: E-Form & Workflow
symptom: "Buyer cancelled PIF-24/25-07/30-00052 and used associated e-Form to create PIF-25/26-09/19-00703."
root-cause: ""
solution: ""
jira: EPMTDCPROT-3006
resolved: 2025-09-29
---

# EPMTDCPROT-3006: EPRO-725 [UAT] PR locked by other form can be chosen

## 問題

[Link:https://hktdc.atlassian.net/browse/EPRO-725] 
Buyer cancelled PIF-24/25-07/30-00052 and used associated e-Form to create PIF-25/26-09/19-00703.
[Image]
[Image]
1. PR should not be allowed to choose when locked by other Procurement Initiation form.
2. PR should be locked once buyer has chosen for a Procurement Initiation form, even the form is in draft status.
3. PR should be unlocked once a Procurement Initiation form was cancelled or rejected.
4. Validation massage to be modified: PR is locked by other form.

Please investigate the root cause.

## 根因

Please investigate the root cause.
When a pr is locked, a prompt will be given when it is selected. The locked pr cannot be selected again
After part 1 canceled, pr will be automatically unlocked, associated with the cancel form, pr can be automatically selected
If part I selects pr, even if it is in the draft state, pr will still be locked, and when creating a new part I, the same pr cannot be selected

## 解法

_See Jira ticket for resolution details._

## 相關問題

- [[EPRO-725]]

