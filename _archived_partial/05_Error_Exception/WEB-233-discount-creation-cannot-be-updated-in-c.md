---
project: WEB
issue_key: WEB-233
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- epromo
- error_exception
- faq
- web
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/WEB-233
created: '2022-06-15'
resolved: '2022-06-28'
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'WEB-233: Discount creation cannot be updated in CS2K BE'
---
# WEB-233: Discount creation cannot be updated in CS2K BE

## 問題描述

Ticket: RIN01005316 
Region: Coach HK
Store: OC501
Error: Invalid Mix & Match Discount
Promotion: DISC HK2PIECES10OFF
Discount Discount Code: 2UNIT10OFF
Discount Description: buy 2 get 10% off
MM Portal UI Version: 15397
MM Portal API Version: 17170

<u>Case Summary</u>

- User created Discount '2UNIT10OFF' on MM Portal website on 2022-06-14.

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/c5873ee7-a9a4-4d68-a558-348da05c9fdd)（需 Jira 登入）
 

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/8bdb0b67-d2ed-47b2-a30a-d677d4c3c58a)（需 Jira 登入）
 

- However, 2UNIT10OFF can be updated in BE table 'mixdisc' but not in 'mixdisch'(header).

- It made user not able to re-save Promotion and shows error 'Invalid Mix & Match Discount'

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/6728dd00-b460-4187-aadc-edeb6009d6f7)（需 Jira 登入）
 

> 📎 **image** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/a4fd3653-2215-441e-9754-27c622779452)（需 Jira 登入）
<u>Workaround</u>

- Apply data patch to add the Discount Code into BE DB table 'mixdisch'



## 附件截圖

1. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/c5873ee7-a9a4-4d68-a558-348da05c9fdd)
2. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/8bdb0b67-d2ed-47b2-a30a-d677d4c3c58a)
3. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/6728dd00-b460-4187-aadc-edeb6009d6f7)
4. 📎 **image** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/a4fd3653-2215-441e-9754-27c622779452)

## 相關資訊

- **Jira:** [WEB-233](https://ctil.atlassian.net/browse/WEB-233)
- **解決方式:** Done