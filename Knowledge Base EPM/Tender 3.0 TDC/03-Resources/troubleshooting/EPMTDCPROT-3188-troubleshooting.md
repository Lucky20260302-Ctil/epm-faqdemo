---
tags: bug, jira, uat-phase1-hotfixbatch3, hotfix
component: Authentication & Login
symptom: "1. Pico International (HK) Ltd clicked the link in invitation email, it was asked to reset password. Why?"
root-cause: ""
solution: ""
jira: EPMTDCPROT-3188
resolved: 2026-01-22
---

# EPMTDCPROT-3188: EPRO-775 [Phase 1 Hot Fix] Error is shown and no re-direction after resetting password

## 問題

[Link:https://hktdc.atlassian.net/browse/EPRO-775] 
1. Pico International (HK) Ltd clicked the link in invitation email, it was asked to reset password. Why?
2. Upon reset of password, no email notification is sent to Pico.

[Image]
1. Upon login, the below error message popped up
2. Pico was not directed to the appropriate offer response e-form (there is no NDA requirement and briefing is set as optional)

## 根因

Phase2 Test Result ： When approving the tender setting form, the data of part 1 can be seen，test fail

## 解法

_See Jira ticket for resolution details._

## 相關問題

- [[EPRO-775]]

