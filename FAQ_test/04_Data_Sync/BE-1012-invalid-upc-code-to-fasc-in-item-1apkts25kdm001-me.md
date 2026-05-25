---
project: BE
issue_key: BE-1012
issue_type: Bug PRD
status: Closed
title: "BE-1012: Invalid UPC Code to FASC in Item 1APKTS25KDM001 Mem Bdg K-Tee plain"
tags:
- 04_data_sync
- be
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1012
created: '2025-02-27'
resolved: '2025-03-21'
fix_version: ''
components:
- Backend (ChainStorePlus 7.0)
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: complete
---

BE-1012: Invalid UPC Code to FASC in Item 1APKTS25KDM001 Mem Bdg K-Tee plain

## 症狀

使用者在 Item Master Maintenance 連續建立商品時，前一個商品的尺寸類別（如 SML）會殘留並被帶入下一個應為不同尺寸類別（如 KDS）的商品，造成 edisku 資料表寫入錯誤尺寸，最終使 FASC 介面產出無效的 UPC 碼。

## 根因

Item Master Maintenance 程式在連續建立商品時，未正確清除/重置前一筆商品的尺寸類別欄位狀態，導致前次建立的商品尺寸類別殘留並污染下一個商品的資料。

## 解法

由 Jerry Wong 修復 Item Master Maintenance 程式邏輯，確保每次建立新商品時尺寸類別欄位正確重置，避免前次資料殘留。修復後已交付 HKJC 進行測試驗證。

## 相關資訊

- Jira: [BE-1012](https://ctil.atlassian.net/browse/BE-1012)
- 解決日期: 2025-03-21
- 組件: Backend (ChainStorePlus 7.0)
- 負責人: Jerry Wong
- 附件: [image-20250227-055449.png](https://ctil.atlassian.net/rest/api/3/attachment/content/52229) | [image-20250227-055520.png](https://ctil.atlassian.net/rest/api/3/attachment/content/52231) | [image-20250227-055611.png](https://ctil.atlassian.net/rest/api/3/attachment/content/52233) | [image-20250227-055627.png](https://ctil.atlassian.net/rest/api/3/attachment/content/52232) | [image-20250227-055738.png](https://ctil.atlassian.net/rest/api/3/attachment/content/52230)


## 相關截圖

<img src="/FAQ_test/attachments/BE-1012/image-20250227-055449.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/BE-1012/image-20250227-055520.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/BE-1012/image-20250227-055611.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/BE-1012/image-20250227-055627.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/BE-1012/image-20250227-055738.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

