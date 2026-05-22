---
project: BE
issue_key: BE-682
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
jira_url: https://ctil.atlassian.net/browse/BE-682
created: '2022-11-08'
resolved: '2023-02-17'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'BE-682: Field of Order Type used incorrect words limitation'
---
# BE-682: Field of Order Type used incorrect words limitation

## 問題描述

Env: [https://172.16.138.101/chainstoreplus/](https://172.16.138.101/chainstoreplus/)

Location: Online Order Information (OR0001)

Reproduce step:

1. To Online Order Information (OR0001)

2. Insert a word into Order Type field

3. Tab Enter

Existing result:

Pop up Invalid Format : Expected Text with Max Length = 0 (Ref: image-2022-11-08-15-38-05-262.png)
 
image-2022-11-08-15-37-58-685.png)

Expected result:

Words limitation of Order Type field should be more than one word



## 相關資訊

- **Jira:** [BE-682](https://ctil.atlassian.net/browse/BE-682)
- **解決方式:** Done