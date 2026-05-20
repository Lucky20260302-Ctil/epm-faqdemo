---
tags: bug, jira, hotfix
component: Integration
symptom: "Reference to [Link:https://hktdc.atlassian.net/browse/EPRO-626], [Link:https://hktdc.atlassian.net/browse/EPRO-156]"
root-cause: ""
solution: ""
jira: EPMTDCPROT-3117
resolved: 2025-12-22
---

# EPMTDCPROT-3117: EPRO-781 [Phase 1 Hot Fix] Total Amount interfaced to FMS did not consider fee modification

## 問題

[Link:https://hktdc.atlassian.net/browse/EPRO-781] 
Reference to [Link:https://hktdc.atlassian.net/browse/EPRO-626], [Link:https://hktdc.atlassian.net/browse/EPRO-156]
 
[Image]

[Image]

[Image]


Fee quoted by AV Promotions Ltd. has been modified and approved.
The final quote should be  $7,626,368 instead of  $7,630,928 according to the approved fee modification.

## 根因

UAT Test Result ： The original quotation of Travel Expert Business Services Limited supplier was USD 2,340,000. Through the Fee Modification Request form, the price was modified to 234,000. The amount filled in the Award Recommendation is 234,000. Through the interface query, the transmitted data is 234,000, and the test is passed

## 解法

_See Jira ticket for resolution details._

## 相關問題

- [[EPRO-156]]
- [[EPRO-626]]
- [[EPRO-781]]

