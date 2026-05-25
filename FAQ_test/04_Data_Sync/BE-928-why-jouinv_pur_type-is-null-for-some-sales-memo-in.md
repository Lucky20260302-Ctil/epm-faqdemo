---
project: BE
issue_key: BE-928
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- be
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-928
created: '2024-10-30'
resolved: '2025-01-10'
fix_version: ''
components:
- Backend (ChainStorePlus 7.0)
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: complete
---

BE-928: Why jouinv_pur_type is null for some sales memo in CN DB

## 症狀

Coach 中國資料庫中，部分銷售備忘錄（deposit、void、return memo）的 jouinv_pur_type（購買類型）欄位為 NULL，導致報表或數據分析時無法識別購買類型。

## 根因

兩個原因：(1) 用戶直接結算 Deposit 而未修改任何項目時，POS 會跳過 Sales UI 直接進入付款頁面，因此從未寫入 Purchase Type。(2) 在 v72 版本中若 tblconfig.DotnetPCD='N'，VB6 PCD Library 無法寫入 Purchase Type 欄位。

## 解法

(1) 直接結算 Deposit 時，POS 自動寫入 tblconfig.PURCHASETYPE_DEFAULT 定義的預設購買類型值。(2) 升級至 V75 後自動使用 dotnetPCD，解決 VB6 PCD 無法寫入的問題。修正版本：v750.05、v750.04R10（KTS 250106）。

## 相關資訊

- Jira: [BE-928](https://ctil.atlassian.net/browse/BE-928)
- 解決日期: 2025-01-10
- 組件: Backend (ChainStorePlus 7.0)
- 負責人: Sang
- 附件: [DBhist.zip](https://ctil.atlassian.net/rest/api/3/attachment/content/49936) | [image-20241030-083418.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47555) | [image-20241030-084428.png](https://ctil.atlassian.net/rest/api/3/attachment/content/47556) | [image-20250106-081040.png](https://ctil.atlassian.net/rest/api/3/attachment/content/49940) | [image-20250106-083950.png](https://ctil.atlassian.net/rest/api/3/attachment/content/49954)


## 相關截圖

![[../attachments/BE-928/image-20241030-083418.jpg]]

![[../attachments/BE-928/image-20241030-084428.jpg]]

![[../attachments/BE-928/image-20250106-081040.jpg]]

![[../attachments/BE-928/image-20250106-083950.jpg]]

![[../attachments/BE-928/image-20250106-084112.jpg]]

