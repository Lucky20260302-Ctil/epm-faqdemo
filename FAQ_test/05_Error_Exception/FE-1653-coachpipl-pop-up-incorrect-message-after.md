---
project: FE
title: "FE-1653: [Coach][PIPL] Pop up incorrect message after searching member with EXIT_PERMIT != 1"
issue_key: FE-1653
issue_type: Bug QA
status: Closed
faq_score: 7.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, mpos]
jira_url: "https://ctil.atlassian.net/browse/FE-1653"
created: 2025-03-19
resolved: 2025-03-21
resolution: Done
has_images: True
---

# FE-1653: [Coach][PIPL] Pop up incorrect message after searching member with EXIT_PERMIT != 1

## 問題描述

[Coach][PIPL] Pop up incorrect message after searching member with EXIT_PERMIT != 1

Testing data-mobile number( CN member with EXIT_PERMIT != 1 ): **21001203962**

Region: 10 (HK)

Reproduce steps:

1. To MPOS- member section

2. Search member by mobile no.

3. Pop up error message: Record not found

Expected result:

Need to pop up "This member does not consent to enquire out of border."

> 📎 **image-20250319-041441.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/e7622426-69c4-406a-915f-31d2ff98c245)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20250319-041441.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/e7622426-69c4-406a-915f-31d2ff98c245)

## 相關資訊

- **Jira:** [FE-1653](https://ctil.atlassian.net/browse/FE-1653)
- **解決方式:** Done