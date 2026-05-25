---
project: FE
issue_key: FE-1643
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1643
created: '2025-03-07'
resolved: '2025-05-02'
fix_version: ''
components:
- Front End
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: complete
---

FE-1643: CN Member can't be created by QR code scanning or mobile number inputting

## 症狀

Coach 中國（CN）會員透過微信小程序註冊後，在 POS 端使用 QR Code 掃描或輸入手機號碼查詢會員時，會員資料可顯示但無法指派會員卡，點擊 Confirm 按鈕後出現錯誤，導致無法完成會員建立。

## 根因

BEAPI 在處理 CN 會員建立時，VIP 編號（vip no.）生成失敗，導致會員卡無法正確指派，進而使 Confirm 操作失敗。

## 解法

將 BEAPI 更新至 V1.7.5 版本（2025/03/07 發布），該版本修復了 VIP 編號生成失敗的問題。程式路徑：\\ds411\public\samuel\beapi\v1.7.5_20250307。

## 相關資訊

- Jira: [FE-1643](https://ctil.atlassian.net/browse/FE-1643)
- 解決日期: 2025-05-02
- 組件: Front End
- 負責人: Anson Cheung
- 附件: [image-20250307-063356.png](https://ctil.atlassian.net/rest/api/3/attachment/content/52698) | [QA web21_beapi_apilog_20250307.sqlite](https://ctil.atlassian.net/rest/api/3/attachment/content/52699) | [QA web22_beapi_apilog_20250307.sqlite](https://ctil.atlassian.net/rest/api/3/attachment/content/52697)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1643/image-20250307-063356.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

