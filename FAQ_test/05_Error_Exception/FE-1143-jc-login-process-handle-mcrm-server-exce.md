---
project: FE
issue_key: FE-1143
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1143
created: '2022-08-15'
resolved: '2024-03-01'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1143: JC Login Process Handle MCRM Server Exception'
---
# FE-1143: JC Login Process Handle MCRM Server Exception

## 問題描述

When user Log-in POS, POS will validate NetWork connection. If POS can connect Web CAP API,  but when API connect to MCRM server and receive exception, POS have not handle it (trigger 'Unhandled exception,') and popup ' .. ran into a problem' message, then need to exit POS.



## 相關資訊

- **Jira:** [FE-1143](https://ctil.atlassian.net/browse/FE-1143)
- **解決方式:** Done