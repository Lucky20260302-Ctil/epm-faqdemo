---
project: BE
issue_key: BE-1228
issue_type: Bug PRD
status: Release
tags:
- 05_error_exception
- be
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1228
created: '2026-01-30'
resolved: ''
fix_version: ''
components:
- API
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

BE-1228: CJ DSA displays Retail Price instead of correct On Sale Price before scheduled price changes (observed on 1/23 and 1/29)

## 症狀

DSA (PriceChecker) 在排程價格變更前一天顯示 Retail Price，而非正確的 On Sale Price。例如：1/29 應顯示 ¥31,350，卻顯示 ¥104,500。POS 端正確，但 DSA 端錯誤。

## 根因

PriceChecker API 驗證 OnSalePricing 時，fromDateTime 與 toDateTime 皆為同日 00:00:00，導致有效期間長度為零，API 回傳無 OnSalePricing 的結果，DSA 因此顯示 Retail Price。POS 端能處理 fromDate = toDate + 00:00:00 情境，但 PriceChecker 未處理。

## 解法

方案一（無需程式變更）：將 toDateTime 改為 23:59:59 以涵蓋全日。方案二（需程式變更）：增強 PriceChecker API 邏輯，處理 fromDate = toDate 且時間為 00:00:00 的情境。

## 相關資訊

- Jira: [BE-1228](https://ctil.atlassian.net/browse/BE-1228)
- 組件: API
- 負責人: Daniel Leung
- 附件: [image (12).png](https://ctil.atlassian.net/rest/api/3/attachment/content/78979) | [image-20260130-073700.png](https://ctil.atlassian.net/rest/api/3/attachment/content/75560) | [image-20260130-073709.png](https://ctil.atlassian.net/rest/api/3/attachment/content/75561) | [image-20260130-073718.png](https://ctil.atlassian.net/rest/api/3/attachment/content/75559) | [image-20260130-073809.png](https://ctil.atlassian.net/rest/api/3/attachment/content/75564)


## 相關截圖

<img src="/FAQ_test/attachments/BE-1228/image (12" style="max-width:100%;border-radius:6px;margin:4px 0">.jpg)

<img src="/FAQ_test/attachments/BE-1228/image-20260130-073700.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/BE-1228/image-20260130-073709.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/BE-1228/image-20260130-073718.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/BE-1228/image-20260130-073809.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

> 共 7 張截圖，[查看全部](/FAQ_test/attachments/BE-1228/)
