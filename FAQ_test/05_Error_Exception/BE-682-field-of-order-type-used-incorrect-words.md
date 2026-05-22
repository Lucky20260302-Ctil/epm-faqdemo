---
project: BE
title: "BE-682: Field of Order Type used incorrect words limitation"
issue_key: BE-682
issue_type: Bug QA
status: Closed
faq_score: 6.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-682"
created: 2022-11-08
resolved: 2023-02-17
resolution: Done
has_images: False
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