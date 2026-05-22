---
project: MP
issue_key: MP-499
issue_type: Task
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- mp
- mpos
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-499
created: '2021-09-02'
resolved: '2021-09-21'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'MP-499: mPOS doesn''t restart (POS day end with mPOS idle)'
---
# MP-499: mPOS doesn't restart (POS day end with mPOS idle)

## 問題描述

When the staff stays on the login page in MPOS and do day end in front end POS, the MPOS UI would not update the latest POS date and till number.

After bug fixing, MPOS would pop up an error message box and help the user to restart MPOS to update the shop config.

 



## 相關資訊

- **Jira:** [MP-499](https://ctil.atlassian.net/browse/MP-499)
- **解決方式:** Done