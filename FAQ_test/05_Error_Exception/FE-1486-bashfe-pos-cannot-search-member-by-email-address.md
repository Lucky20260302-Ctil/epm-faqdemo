---
project: FE
issue_key: FE-1486
issue_type: Bug QA
status: Closed
tags:
title: "FE-1486-bashfe-pos-cannot-search-member-by-email-address"
- 05_error_exception
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1486
created: '2024-08-20'
resolved: '2024-08-20'
fix_version: ''
components:
- Front End
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

FE-1486: POS cannot search member by Email address

## 症狀

BASH POS 無法透過 Email 地址搜尋會員，但 VPN 連線及 DB 連線均正常。

## 根因

Email 搜尋功能查詢的是 vipemail 資料表而非 vip 資料表，導致查無結果。

## 解法

修正搜尋邏輯，從正確的 vipemail 表查詢 Email 對應的會員資料。

## 相關資訊

- Jira: [FE-1486](https://ctil.atlassian.net/browse/FE-1486)
- 解決日期: 2024-08-20
- 組件: Front End
- 負責人: Sang
- 附件: [Dbtrans.sdf](https://ctil.atlassian.net/rest/api/3/attachment/content/44889) | [image-20240820-030631.png](https://ctil.atlassian.net/rest/api/3/attachment/content/44888) | [vbretail.ini](https://ctil.atlassian.net/rest/api/3/attachment/content/44887)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1486/image-20240820-030631.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1486/screenshot-link_att.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

