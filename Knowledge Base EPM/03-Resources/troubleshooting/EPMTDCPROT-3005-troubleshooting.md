---
tags: [bug, jira, ext-tdc-uat]
component: E-Form & Workflow
symptom: "PIF-25/26-09/19-00703"
root-cause: ""
solution: ""
jira: EPMTDCPROT-3005
resolved: 2025-09-29
---

# EPMTDCPROT-3005: EPRO-726 [UAT] Exceptional Approval is auto-checked without reason

## 問題

[Link:https://hktdc.atlassian.net/browse/EPRO-726] 
PIF-25/26-09/19-00703
[Image]
1. upon system checking, the exception approval conditions should be identified and the exception approval checkbox should be auto-checked with indication of reasons.


Please investigate root cause.

## 根因

1. upon system checking, the exception approval conditions should be identified and the exception approval checkbox should be auto-checked with indication of reasons.
Please investigate root cause.
This bug was caused by selecting "Single Envelope", which led to the Technical Assessment Panel Members not being set, resulting in the Exception Approval being automatically checked and no reason being displayed. Now the bug has been fixed. Selecting Single Envelope will not automatically check Exception Approval

## 解法

_See Jira ticket for resolution details._

## 相關問題

- [EPRO-726](https://hktdc.atlassian.net/browse/EPRO-726)

