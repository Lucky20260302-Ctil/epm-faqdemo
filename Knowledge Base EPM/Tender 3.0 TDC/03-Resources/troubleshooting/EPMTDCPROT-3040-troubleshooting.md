---
tags: bug, jira, ext-tdc-uat, uat
component: Supplier Management
symptom: "If supplier selects “Others (Please specify)” in no offer response, the system should provide a free text field for them to input the reason.  That fi"
root-cause: ""
solution: ""
jira: EPMTDCPROT-3040
resolved: 2025-10-15
---

# EPMTDCPROT-3040: EPRO-742 [UAT] Missing field for supplier to state no offer reason if "Others(Please specify)" is selected

## 問題

[Link:https://hktdc.atlassian.net/browse/EPRO-742] 
If supplier selects “Others (Please specify)” in no offer response, the system should provide a free text field for them to input the reason.  That field is missing now.  Please check and fix.  Thanks.

[Image]

## 根因

If supplier selects “Others (Please specify)” in no offer response, the system should provide a free text field for them to input the reason.  That field is missing now.  Please check and fix.  Thanks.
As per mentioned in checkpoint meeting on 30 Sep, issue caused by label change.
Fixed and verified in UAT:
Text field is required when supplier choosing “Others(please specify)” as no offer reason.

## 解法

_See Jira ticket for resolution details._

## 相關問題

- [[EPRO-742]]

