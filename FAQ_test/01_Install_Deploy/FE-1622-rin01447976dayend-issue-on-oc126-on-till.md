---
project: FE
issue_key: FE-1622
issue_type: Bug DEV
status: Closed
tags:
- 01_install_deploy
- cs2kconnect
- faq
- fe
- front-end-v750.01r01a
- install_deploy
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1622
created: '2025-02-07'
resolved: '2025-02-24'
fix_version: ''
components: []
has_images: false
category: 01_Install_Deploy
category_label: 安裝與部署
quality: partial
title: 'FE-1622: [RIN01447976]dayend issue on OC126 on till1 after upgraded to V75'
---
# FE-1622: [RIN01447976]dayend issue on OC126 on till1 after upgraded to V75

## 問題描述

Hi Teams, OC126 often has dayend issue after upgraded to V75. 

We had store user not to shut down all PC on 6th Feb.

And found no dayendinfo in cs2000connect.log.

That caused the dayend inform not posted.

And it would be posted on the second day after the PC started.

It  can be found in the next day’s cs2Kconnect.log.



## 相關資訊

- **Jira:** [FE-1622](https://ctil.atlassian.net/browse/FE-1622)
- **解決方式:** Done