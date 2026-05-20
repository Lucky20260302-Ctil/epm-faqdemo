---
tags: bug, jira
component: Tender & RFQ
symptom: "This has been clarified and fixed previously in [Link:https://hktdc.atlassian.net/browse/EPRO-299]"
root-cause: ""
solution: ""
jira: EPMTDCPROT-3041
resolved: 2025-10-15
---

# EPMTDCPROT-3041: EPRO-743 Number of Attendees should be a checking of maximum instead of minimum

## 問題

[Link:https://hktdc.atlassian.net/browse/EPRO-743] 
The number entered in RFQ / Tender Setting form about the number of attendees indicates the maximum number of attendees allowed to register, not minimum, for control in Briefing / Site Visit Registration form.
This has been clarified and fixed previously in [Link:https://hktdc.atlassian.net/browse/EPRO-299]
 
This issue is marked as high in severity because of the following:
1. It is a repeated issue;
2. This checking will affect external suppliers and cause interruption to our internal operation, i.e. we intended to control the number of supplier representatives but not the checking forces suppliers to register more representatives, which make it more difficult to control the briefing logistics and higher chance of bid rigging.

## 根因

2. This checking will affect external suppliers and cause interruption to our internal operation, i.e. we intended to control the number of supplier representatives but not the checking forces suppliers to register more representatives, which make it more difficult to control the briefing logistics and higher chance of bid rigging.
Verified in UAT:
Buyer set up to 2 attendees is allowed for briefing registration in Tender Setting”
Error message will pop and supplier cannot submit registration form if the total amount of attendees against the setting.

## 解法

_See Jira ticket for resolution details._

## 相關問題

- [[EPRO-299]]
- [[EPRO-743]]

