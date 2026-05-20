---
tags: bug, jira, tdc-hotfix, hotfix
component: User Management
symptom: "Referring to one of the issues in [Link:https://hktdc.atlassian.net/browse/EPRO-415]"
root-cause: ""
solution: "环境test， Email link跳转到 uat环境，并且无法通过email login"
jira: EPMTDCPROT-3116
resolved: 2025-11-28
---

# EPMTDCPROT-3116: EPRO-784 [Phase 1 Hot Fix] Approval Delegation Issues (Duplicate emails and no approval access)

## 問題

Referring to one of the issues in [Link:https://hktdc.atlassian.net/browse/EPRO-415]
Delegator and Delegator-to Person received duplicate emails for role assignment and approval request.
The below video shows totally 4 emails sent to Bonnie Cheung (delegator) and Gladys Ching (delegated-to person) about role assignment, 2 for each person.

The link to approval request in Delegated-to Person is invalid with error message.
The below video shows totally 4 emails sent to Bonnie Cheung (delegator) and Gladys Ching (delegated-to person) for approval request of Award Recommendation, 1 to delegator and 3 to delegated-to person. When Gladys clicked links in both approval request emails, error messages popped up.
Delegated-to Person cannot see the approval request in Pending Approvals, either Approval page or Delegated Approval page.
[Image]
[Image]
Only the delegator (Bonnie Cheung) can access the approval request of Award Recommendation.
[Image]

## 解法

环境test， Email link跳转到 uat环境，并且无法通过email login

## 相關問題

- [[EPRO-415]]

