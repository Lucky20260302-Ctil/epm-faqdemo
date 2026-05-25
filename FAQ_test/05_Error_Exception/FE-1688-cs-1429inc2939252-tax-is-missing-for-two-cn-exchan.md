---
project: FE
issue_key: FE-1688
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1688
created: '2025-05-08'
resolved: '2025-05-30'
fix_version: FE-V75.04R13A
components:
- Frontend
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

FE-1688: Tax is missing for two CN exchange transactions

## 症狀

CN 門店 V75 在進行換貨交易時，jouinv_vat_value 與 jouinv_gst_per 欄位未寫入 DB，導致兩筆 CN 換貨交易缺少稅額資料。

## 根因

換貨交易在計算品項稅額時存在程式缺陷：當換貨備註非免稅（NOT Tax Free）時，系統未正確計算並寫入對應的 VAT/GST 稅額欄位至 DB。

## 解法

已於 v750.04R13A 版本修正，換貨交易將正確計算品項稅額。若需緊急處理，可先透過 DB 資料補丁手動補入稅額資料。

## 相關資訊

- Jira: [FE-1688](https://ctil.atlassian.net/browse/FE-1688)
- Fix Version: FE-V75.04R13A
- 解決日期: 2025-05-30
- 組件: Frontend
- 負責人: Sherman tse
- 附件: [image-20250508-051310.png](https://ctil.atlassian.net/rest/api/3/attachment/content/56308) | [image-20250508-051353.png](https://ctil.atlassian.net/rest/api/3/attachment/content/56309) | [image-20250508-052251.png](https://ctil.atlassian.net/rest/api/3/attachment/content/56310) | [image-20250508-053444.png](https://ctil.atlassian.net/rest/api/3/attachment/content/56311) | [image-20250508-054241.png](https://ctil.atlassian.net/rest/api/3/attachment/content/56314)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1688/image-20250508-051310.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1688/image-20250508-051353.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1688/image-20250508-052251.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1688/image-20250508-053444.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1688/image-20250508-054241.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

> 共 7 張截圖，[查看全部](/FAQ_test/attachments/FE-1688/)
