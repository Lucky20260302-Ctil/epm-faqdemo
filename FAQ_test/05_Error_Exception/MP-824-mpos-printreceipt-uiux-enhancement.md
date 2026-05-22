---
project: MP
issue_key: MP-824
issue_type: Improvement
status: Release
tags:
- 05_error_exception
- error_exception
- faq
- mp
- mpos
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-824
created: '2026-03-30'
resolved: ''
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'MP-824: MPOS PrintReceipt UIUX Enhancement'
---
# MP-824: MPOS PrintReceipt UIUX Enhancement

## 問題描述

The current printing UI only shows a generic loading state for too long, without clearly indicating:

- which processing stage is currently running,

- whether the request is still active,

- whether the request has failed,

- or what action the user should take next.

---

Introduce **stage-based status indicators** during receipt printing so that store users can understand exactly what the system is doing.

### Suggested Stages

1. **Preparing receipt**

2. **Sending print request**

3. **Waiting for print hub response**

4. **Printing receipt**

5. **Print completed** / **Print failed**

### UI Requirements

- Clearly display the **current processing stage**

- Show whether the operation is:

- in progress,

- retrying,

- completed,

- or failed

- Avoid indefinite generic loading animation without message update

### Expected Result

This improves transparency and reduces user anxiety during slow or unstable network conditions.



## 相關資訊

- **Jira:** [MP-824](https://ctil.atlassian.net/browse/MP-824)