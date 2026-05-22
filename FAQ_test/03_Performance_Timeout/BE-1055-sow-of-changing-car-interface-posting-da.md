---
project: BE
issue_key: BE-1055
issue_type: SOW
status: Closed
tags:
- 03_performance_timeout
- be
- data-interface
- faq
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-1055
created: '2025-04-22'
resolved: '2025-06-11'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'BE-1055: SOW of changing CAR Interface posting date time'
---
# BE-1055: SOW of changing CAR Interface posting date time

## 問題描述

Currently in CAR interface for transaction posting, POS will send data file to CAR and the posting datetime is using backend server datetime in Hong Kong time zone.

It causes a symptom that data datetime is not reflecting the corresponding region datetime especially for Japan and Korea since there is 1 hour time difference between Hong Kong time zones.

 

To resolve this issue, this solution is introduced that putting the transaction date and time into posting date and time fields inside the interface file for sending to CAR. The change will apply to Coach Japan, Coach Korea and Kate Spade Japan.



## 相關資訊

- **Jira:** [BE-1055](https://ctil.atlassian.net/browse/BE-1055)
- **解決方式:** Done
- **標籤:** CAR