---
project: FE
issue_key: FE-1942
issue_type: Bug QA
status: Closed
tags:
title: "FE-1942-imx-pop-up-object-reference-error-after-click-on-n"
- 05_error_exception
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1942
created: '2026-04-30'
resolved: '2026-05-05'
fix_version: ''
components:
- Front End
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

FE-1942: Pop up 'Object reference' error after click on New log update & complete payment

## 症狀

在 IMX 系統中，點選「New log update」或使用特定商品（CM00100419S6E4）完成付款後返回 Sales Memo 畫面時，彈出「Object reference」錯誤。

## 根因

error logging 模組在處理 exception 時，content 欄位為 null 導致 null reference 異常（KTS 260428 FE-1940 相關增強缺陷）。

## 解法

升級至 v750.05R14B，該版本修正了 error logging 對 null content 的處理邏輯，並一併修復 QueueBusting 中 New VIP EDM 的 null reference 問題。

## 相關資訊

- Jira: [FE-1942](https://ctil.atlassian.net/browse/FE-1942)
- 解決日期: 2026-05-05
- 組件: Front End
- 負責人: Sang
- 附件: [image-20260430-021506.png](https://ctil.atlassian.net/rest/api/3/attachment/content/85947)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1942/image-20260430-021506.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

