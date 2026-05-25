---
project: BE
issue_key: BE-1193
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- be
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1193
created: '2025-10-29'
resolved: ''
fix_version: ''
components:
- Data Interface
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

BE-1193: ANZ POS - AU 20 Web sales import error - Exchange rate not found

## 症狀

匯入 ANZ POS AU 20 Web sales 檔案時，系統拋出「Exchange rate not found」錯誤，導致匯入失敗。即使先前成功匯入的檔案，重新匯入也出現相同錯誤。

## 根因

貨幣代碼（currency code）設定不正確，導致系統無法匹配對應的匯率資料。

## 解法

修正貨幣代碼設定，確保 paytab 幣別（如 AUD）與系統匯率表一致後即可正常匯入。

## 相關資訊

- Jira: [BE-1193](https://ctil.atlassian.net/browse/BE-1193)
- 組件: Data Interface
- 負責人: Tovi Wang
- 附件: [image-20251029-084549.png](https://ctil.atlassian.net/rest/api/3/attachment/content/67692) | [image-20251029-085423.png](https://ctil.atlassian.net/rest/api/3/attachment/content/67695) | [WEB_SALES_20251023000001_OCA213.TXT](https://ctil.atlassian.net/rest/api/3/attachment/content/67693) | [WEB_SALES_20251029000001_OCA213.TXT](https://ctil.atlassian.net/rest/api/3/attachment/content/67694) | [WEB_SALES_20251029000002_OCA213.TXT](https://ctil.atlassian.net/rest/api/3/attachment/content/67696)


## 相關截圖

![[../attachments/BE-1193/image-20251029-084549.png]]

![[../attachments/BE-1193/image-20251029-085423.png]]

![[../attachments/BE-1193/screenshot-link_att.jpg]]

