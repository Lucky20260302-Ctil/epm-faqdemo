---
tags: [bug, jira, ext-tdc-uat]
component: E-Form & Workflow
symptom: "For Declaration of Conflict of Interest e-Form RFQ-24/25-06/10-01564, Tim Lau as Level 6 approver raised a clarification question and selected Hermia "
root-cause: ""
solution: "Tim Lau cannot return the e-Form by clicking “Return” button before clarification"
jira: EPMTDCPROT-2255
resolved: 2025-07-07
---

# EPMTDCPROT-2255: EPRO-210 [UAT] Failed to return e-Form after clarification raised & answered

## 問題

[Link:https://hktdc.atlassian.net/browse/EPRO-210] 
For Declaration of Conflict of Interest e-Form RFQ-24/25-06/10-01564, Tim Lau as Level 6 approver raised a clarification question and selected Hermia Fu (Level 5) to respond.
Hermia cannot find related e-Form in her record to answer the clarification question (as there is no way to find her own completed approvals)
Ivan Lai (Requestor) has answered the question, but Tim Lau cannot approve the e-Form.
Tim Lau cannot return the e-Form by clicking “Return” button.
[Image]
[Image]
The same problem happened after bug fixing of [Link:https://hktdc.atlassian.net/browse/EPRO-148]

## 解法

Tim Lau cannot return the e-Form by clicking “Return” button before clarification

## 相關問題

- [EPRO-148](https://hktdc.atlassian.net/browse/EPRO-148)
- [EPRO-210](https://hktdc.atlassian.net/browse/EPRO-210)

