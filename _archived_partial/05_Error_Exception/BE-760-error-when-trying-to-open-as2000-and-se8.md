---
project: BE
issue_key: BE-760
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- backend-(web)
- be
- error_exception
- faq
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-760
created: '2023-06-13'
resolved: '2023-06-23'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-760: error when trying to open AS2000 and SE8008'
---
# BE-760: error when trying to open AS2000 and SE8008

## 問題描述

cannot open AS2000 and SE8008

 

 Updated db by below sql script

DELETE FROM gldata.dbo.enqdic WHERE enqdic_progid = 'AS2000' and enqdic_seq > 5;

update gldata.dbo.enqdic set enqdic_field = 'interlog_comp_date' , enqdic_unique_key = 'interlog_comp_date' WHERE enqdic_progid = 'SE8008' and enqdic_seq = 1;

DELETE FROM gldata.dbo.enqdic WHERE enqdic_progid = 'SE8008' and enqdic_seq > 7;



## 相關資訊

- **Jira:** [BE-760](https://ctil.atlassian.net/browse/BE-760)
- **解決方式:** Done