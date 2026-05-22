---
project: MP
title: "MP-702: [CS-873] Japanese user login in MPOS which caused posting error"
issue_key: MP-702
issue_type: Bug PRD
status: Closed
faq_score: 7.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, mp, error_exception, mpos, mpos-api]
jira_url: "https://ctil.atlassian.net/browse/MP-702"
created: 2024-05-28
resolved: 2024-06-07
resolution: Done
has_images: True
---

# MP-702: [CS-873] Japanese user login in MPOS which caused posting error

## 問題描述

The issue  caused by User input Japanese when logining MPOS,But login failed.And the failed login records need also posting.

Workaround:
1.Contact User NOT input Japanese when logining MPOS.
2.Long workaround:Need to enhance program to block Japanese when user logining MPOS.

> 📎 **image-20240528-084347.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/1f57eba4-5ce0-46b8-ad49-b8207c00e548)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20240528-084347.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/1f57eba4-5ce0-46b8-ad49-b8207c00e548)

## 相關資訊

- **Jira:** [MP-702](https://ctil.atlassian.net/browse/MP-702)
- **解決方式:** Done