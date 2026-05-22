---
project: FE
title: "FE-1566: [Coach][CRM milestone 2] No need to display 'Fail to connect CRM' when Member created by POS directly"
issue_key: FE-1566
issue_type: Bug QA
status: Closed
faq_score: 7.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end]
jira_url: "https://ctil.atlassian.net/browse/FE-1566"
created: 2024-11-20
resolved: 2024-11-21
resolution: Done
has_images: True
---

# FE-1566: [Coach][CRM milestone 2] No need to display "Fail to connect CRM" when Member created by POS directly

## 問題描述

[Coach][CRM milestone 2] No need to display "Fail to connect CRM" when Member created by POS directly

Reproduce steps:

1. Open member section

2. Click on Create new member to create a member

3. Click on “Purchase histoy“ & “Profile“

Existing result:

Pop up “Fail to connect CRM. Member profile is not available“

Expected result:

- Need to Pop up “Purchase histoy is not available“/ “ Profile is not available“ as POS dosen’t fail to connect CRM, it is just a member that is not exisitng in CRM only

> 📎 **image-20241120-090617.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/07a466e0-a67a-4759-a60e-d0111cb24333)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20241120-090617.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/07a466e0-a67a-4759-a60e-d0111cb24333)

## 相關資訊

- **Jira:** [FE-1566](https://ctil.atlassian.net/browse/FE-1566)
- **解決方式:** Done