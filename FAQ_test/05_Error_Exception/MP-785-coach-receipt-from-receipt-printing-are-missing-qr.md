---
project: MP
issue_key: MP-785
issue_type: Bug QA
status: Closed
title: "MP-785: Receipt from receipt printing are missing QR code & order number"
tags:
- 05_error_exception
- faq
- mp
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-785
created: '2025-07-10'
resolved: '2025-07-16'
fix_version: ''
components:
- Frontend
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

MP-785: Receipt from receipt printing are missing QR code & order number

## 症狀

Coach 品牌使用 receipt printing（收據列印）功能時，列印出的收據缺少 QR code 與訂單號碼，但使用 normal reprint（一般重新列印）則正常顯示。

## 根因

CustomerReceipt（客戶收據）報表佈局未與 Sales Memo（銷售備忘錄）佈局對齊，導致 receipt printing 路徑下 eInvoice QR code 未被包含在列印範圍內。

## 解法

修正 CustomerReceipt 報表列印邏輯，將 eInvoice QR code 列印區塊與 Sales Memo Layout 對齊。（KTS 250710 MP-785/FE-1715，適用版本 v750.04R13E / v750.04R14 / v750.05）

## 相關資訊

- Jira: [MP-785](https://ctil.atlassian.net/browse/MP-785)
- 解決日期: 2025-07-16
- 組件: Frontend
- 負責人: Sherman tse
- 附件: [image-20250710-040457.png](https://ctil.atlassian.net/rest/api/3/attachment/content/61626) | [image-20250710-041037.png](https://ctil.atlassian.net/rest/api/3/attachment/content/61627)


## 相關截圖

<img src="/FAQ_test/attachments/MP-785/image-20250710-040457.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/MP-785/image-20250710-041037.png" style="max-width:100%;border-radius:6px;margin:4px 0">

