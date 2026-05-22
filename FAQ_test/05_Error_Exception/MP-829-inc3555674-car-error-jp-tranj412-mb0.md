---
project: MP
issue_key: MP-829
issue_type: Bug PRD
status: Selected for Development (migrated)
tags:
- 05_error_exception
- error_exception
- faq
- mp
- mpos
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-829
created: '2026-04-24'
resolved: ''
fix_version: ''
components: []
has_images: true
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'MP-829: INC3555674 - CAR Error - JP-tran#J412-MB005013 Sum of item does not equal the payment sum 04/23'
---
# MP-829: INC3555674 - CAR Error - JP-tran#J412-MB005013 Sum of item does not equal the payment sum 04/23

## 問題描述

The correct total amount should be ‘27500' instead of '33000’ for memo J412-MB005013 on2026-04-23.The Coupon LPB001D 5500 amount NOT synced to the sales memo.

1.

> 📎 **image-20260424-021801.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/cd59cf9b-63c6-4414-981e-7cf03756e0dd)（需 Jira 登入）
2.FE POS:

> 📎 **image-20260424-021858.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/027f0b62-1a10-402b-a526-2b79a7577a71)（需 Jira 登入）
3.DB data for the sales memo:

> 📎 **image-20260424-022112.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/4fa8be19-01f3-4c5a-a91d-4172c0469dee)（需 Jira 登入）
4.

ALL Local IIS

POS version 75.004.1404.0000

MPOS version:3.30.3

> 📎 **image-20260424-023008.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/23f37c13-0f1d-4008-b96d-7ce2733445ff)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20260424-021801.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/cd59cf9b-63c6-4414-981e-7cf03756e0dd)
2. 📎 **image-20260424-021858.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/027f0b62-1a10-402b-a526-2b79a7577a71)
3. 📎 **image-20260424-022112.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/4fa8be19-01f3-4c5a-a91d-4172c0469dee)
4. 📎 **image-20260424-023008.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/23f37c13-0f1d-4008-b96d-7ce2733445ff)

## 相關資訊

- **Jira:** [MP-829](https://ctil.atlassian.net/browse/MP-829)