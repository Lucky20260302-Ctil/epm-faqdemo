---
project: FE
issue_key: FE-1667
issue_type: Bug DEV
status: Closed
tags:
- 03_performance_timeout
- faq
- fe
- front-end-v750.01r01a
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1667
created: '2025-04-09'
resolved: '2025-09-30'
fix_version: ''
components: []
has_images: true
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'FE-1667: [CS-1399]Issue_CS2000 change password'
---
# FE-1667: [CS-1399]Issue_CS2000 change password

## 問題描述

PRC region, POS v75 tested on OCF470 on 8th April, OCF121 on 9th April, with account lsun.

After change password on FE, it will not update to BE.  This issue only happens on force change password.

 changed password on OCF47 Till0 on 4.8. but BE still show below on 4.9.

 When update password in BE, Password Expiry Date will not change together. 

> 📎 **111.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/4a13cb09-025e-4322-8795-ba8f35319bc1)（需 Jira 登入）

> 📎 **222.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/9e0564c1-98dd-4676-ac18-f5333262e439)（需 Jira 登入）

> 📎 **333.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/4b4bf2d9-abc1-40cb-bb1c-80bddd50aea7)（需 Jira 登入）

Changed password on FE by below function.

> 📎 **444.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/5b7496bb-33bf-4f3c-beca-ba78b4d3152e)（需 Jira 登入）

 

Confirmed new password update to CS2000 BE around 14:15

 

 

15:00 HKT

### Change password expired date to 2025.04.07 on BE

### Login LSUN on OCF121 and show force to change password.

> 📎 **555.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/0fc85164-2771-497e-aab8-5fe52b822b44)（需 Jira 登入）

### Successfully login on OCF121

> 📎 **666.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/62870564-290e-4f51-8e26-25fb467a8c1e)（需 Jira 登入）

 



## 附件截圖

1. 📎 **111.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/4a13cb09-025e-4322-8795-ba8f35319bc1)
2. 📎 **222.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/9e0564c1-98dd-4676-ac18-f5333262e439)
3. 📎 **333.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/4b4bf2d9-abc1-40cb-bb1c-80bddd50aea7)
4. 📎 **444.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/5b7496bb-33bf-4f3c-beca-ba78b4d3152e)
5. 📎 **555.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/0fc85164-2771-497e-aab8-5fe52b822b44)
6. 📎 **666.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/62870564-290e-4f51-8e26-25fb467a8c1e)

## 相關資訊

- **Jira:** [FE-1667](https://ctil.atlassian.net/browse/FE-1667)
- **解決方式:** Done