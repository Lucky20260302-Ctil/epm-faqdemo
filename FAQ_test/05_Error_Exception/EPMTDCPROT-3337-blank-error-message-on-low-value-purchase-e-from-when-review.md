---
project: EPMTDCPROT
issue_key: EPMTDCPROT-3337
issue_type: ''
status: ''
tags:
- 05-error-exception
- 05_error_exception
- epm
- epmtdcprot
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-3337
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

EPMTDCPROT-3337: Blank error message on low value purchase e-from when review and validate

## 症狀

在 Low Value Purchase e-form 點擊 Review & Validate 時，出現空白的錯誤訊息「Index was out of range」，原因是什麼？

## 根因

根據 Comment (William Qiu)：觸發原因是當 Random Supplier 的數量多於 Shortlist Supplier 的數量時，系統在進行索引操作時超出範圍，拋出 ArgumentOutOfRangeException，但前端未正確顯示錯誤訊息內容，僅顯示空白。

## 解法

修正 Low Value Purchase e-form 的後端邏輯，處理 Random Supplier 數量大於 Shortlist Supplier 數量的邊界條件，避免 Index out of range 異常；同時確保前端能正確顯示錯誤訊息內容。

## 相關資訊

- Jira: [EPMTDCPROT-3337](https://ctil.atlassian.net/browse/EPMTDCPROT-3337)
- Fix Version: 未標註
- 分類: 錯誤與異常
- 專案: EPMTDCPROT


## 相關截圖

<img src="/FAQ_test/attachments/EPMTDCPROT-3337/image-20260119-035524.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-3337/image-20260506-084956.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/EPMTDCPROT-3337/image-20260506-085022.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

