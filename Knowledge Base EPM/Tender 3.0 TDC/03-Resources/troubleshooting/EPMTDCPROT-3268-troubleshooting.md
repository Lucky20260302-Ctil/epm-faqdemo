---
tags: bug, jira, production, production
component: Tender & RFQ
symptom: "No similar case was noticed during health check and other issued RFQ/Tenders in production site. Please investigate root cause."
root-cause: ""
solution: ""
jira: EPMTDCPROT-3268
resolved: 2025-12-30
---

# EPMTDCPROT-3268: EPRO 874 [Production] Incorrect checking on RFQ / Tender Period

## 問題

For Issuance of RFQ / Tender, no approval will be required if the RFQ / Tender period is sufficient according to the pre-set rules as below. The calculation of RFQ / Tender period should include the issuance and closing days. (reference: EPRO-81: [UAT] To update RFQ / Tender duration reminder and exception approval logicDone)
[Image]

For RTI-25/26-12/30-00008, it is a single envelope tender. The issuance date is 30 Dec 2025 and closing on 13 Jan 2026 (10 working days), but the system mandates user to go through approval for the issuance, which should NOT be required.
 
[Image]
[Image]
[Image]

No similar case was noticed during health check and other issued RFQ/Tenders in production site. Please investigate root cause.

## 根因

No similar case was noticed during health check and other issued RFQ/Tenders in production site. Please investigate root cause.
From Fanny: User accidentally clicked the button, will cancel the Jira

## 解法

_See Jira ticket for resolution details._

## 相關問題

- [[EPRO-81]]

