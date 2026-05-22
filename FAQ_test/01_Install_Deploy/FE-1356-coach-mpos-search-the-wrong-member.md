---
project: FE
issue_key: FE-1356
issue_type: Bug PRD
status: Closed
tags:
- 01_install_deploy
- faq
- fe
- front-end
- install_deploy
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1356
created: '2024-03-05'
resolved: '2025-02-27'
fix_version: ''
components: []
has_images: false
category: 01_Install_Deploy
category_label: 安裝與部署
quality: partial
title: 'FE-1356: Coach MPOS search the wrong member'
---
# FE-1356: Coach MPOS search the wrong member

## 問題描述

Store J814 Called out below.

SA searches for customer by phone number -> **J814WJ00162846** (**correct**) information comes up -> tap on iphone screen -> information is converted to **JXXX0013893218** (**incorrect**), This is the Issue.

I have also checked the possible things in advance,

The phone number, customer ID and member ID are not the same.
The same situation occurs when searching on another staff member's device.
When I search for the phone number on a cash register or iPad, the correct J814WJ00162846 information is reflected.

We are aware that this is the case.
What are the possible errors and how can we correct them?

 

Callouted time January 25, 2024 5:31 PM



## 相關資訊

- **Jira:** [FE-1356](https://ctil.atlassian.net/browse/FE-1356)
- **解決方式:** Done