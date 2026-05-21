---
tags: [bug, jira, ext-tdc-uat, change-request]
component: Tender & RFQ
symptom: "Bidders who did not submit quotation / proposal or failed in technical assessment is available for buyer to select for issuing Post-Tender Clarificati"
root-cause: ""
solution: "failed in technical assessment, which both should not be selection values."
jira: EPMTDCPROT-2293
resolved: 2025-07-23
---

# EPMTDCPROT-2293: EPRO-243 [UAT] Only valid suppliers should be available for search for Create Post-Tender Clarification Issuance

## 問題

[Link:https://hktdc.atlassian.net/browse/EPRO-243] 
[UAT] Only valid suppliers should be available for search for Create Post-Tender Clarification Issuance
Issue
Bidders who did not submit quotation / proposal or failed in technical assessment is available for buyer to select for issuing Post-Tender Clarification.
[Image]

CMGRP did not submit tender and SA Solution failed in technical assessment, which both should not be selection values.

Expected Result
For Technical Clarification, only bidders that have submitted proposals will be shown as selection value.
For Fee Clarification (two envelope), only bidders that have submitted proposals and passed in technical assessment will be shown as selection values.
For Fee Clarification (single envelope), only bidders that have submitted quotations will be shown as selection values.

## 解法

failed in technical assessment, which both should not be selection values.

## 相關問題

- [EPRO-243](https://hktdc.atlassian.net/browse/EPRO-243)

