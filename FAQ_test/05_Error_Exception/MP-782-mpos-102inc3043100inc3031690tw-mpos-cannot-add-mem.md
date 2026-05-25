---
project: MP
issue_key: MP-782
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- faq
- line-app
- member
- mp
- mpos
- qr-code
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-782
created: '2025-06-20'
resolved: '2025-07-09'
fix_version: MPOS API 3.29.6
components:
- MPOS
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

MP-782:   TW MPOS - Cannot add member through scanning QR code from LINE app

## 症狀

台灣 V75 MPOS 試點門市 OC705 使用 LINE App 掃描 QR Code 加入會員時，系統彈出「Invalid QR Code」錯誤，無法成功加入會員。此問題可在 QA 環境重現，影響 MPOS API v3.29.5 及之前版本。

## 根因

MPOS 3.29 開始支援 Member QR Code 的 Dynamic Token 功能，但因向後兼容性處理不完整，MPOS API 將所有 QR Code 一律以 Dynamic Token 方式驗證，導致非 ACIXOM 類型的 QR Code 被拒絕為 Invalid。FEPOS 可在 UI 層判斷 OnlineMemberType 再決定是否做 Dynamic Token 驗證，但 mPOS 完全依賴 MPOS API，差異未妥善處理。

## 解法

限制 Dynamic Token 驗證僅在 OnlineMemberType == ACIXOM 時執行。修復版本：MPOS API 3.29.6（2025-07-08 發布），Patch 版本：3.29.5-20250620.1-b1。

## 相關資訊

- Jira: [MP-782](https://ctil.atlassian.net/browse/MP-782)
- Fix Version: MPOS API 3.29.6
- 解決日期: 2025-07-09
- 組件: MPOS


## 相關截圖

![[../attachments/MP-782/image-20250620-071426.jpg]]

![[../attachments/MP-782/image-20250620-071458.jpg]]

![[../attachments/MP-782/image-20250620-072518.jpg]]

![[../attachments/MP-782/image-20250620-073623.jpg]]

