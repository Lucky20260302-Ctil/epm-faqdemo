---
project: BE
issue_key: BE-685
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
jira_url: https://ctil.atlassian.net/browse/BE-685
created: '2022-11-09'
resolved: '2023-02-21'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-685: Online Order Information used incorrect word limitation for member no. field'
---
# BE-685: Online Order Information used incorrect word limitation for member no. field

## 問題描述

Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)

Location: Online Order Information (OR0001)

Reproduce steps:

1. To Online Order Information

2. Click on Create

3. Click on "..." of  Member no. field

4. Select one of the member no. that are over 10 words

Existing result:

Field of Member no. rounded by red outline, if I click save, it will pop up an error that has word limiatation (Ref: screenshot-1.png)

 



## 相關資訊

- **Jira:** [BE-685](https://ctil.atlassian.net/browse/BE-685)
- **解決方式:** Done