---
project: FE
issue_key: FE-1680
issue_type: Bug QA
status: Closed
tags:
title: "FE-1680-coachcrm-r12a-havent-call-upsert-api-after-issue-a"
- 02_config_settings
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1680
created: '2025-04-25'
resolved: '2025-04-29'
fix_version: ''
components:
- Front End
has_images: false
category: 02_Config_Settings
category_label: 配置與設定
quality: complete
---

FE-1680: R12A haven't call upsert api after issue an order with new member created by POS

## 症狀

POS 建立新會員並完成交易後，系統未呼叫 upsert API 將新會員資料同步至後端 CRM（Acxiom），僅呼叫了 coupon 查詢 API（queryCustomerCoupons）。此問題發生於 v750.04R12A 版本。

## 根因

參數 tblconfig.WEBAPIUPDATENEWMEMBER 未設定為 Y。此設定於 v750.04R11A 版本新增，用於控制是否在建立交易時透過 Web API 進行 Acxiom 會員 Upsert。當設定值為 N（預設值）時，系統不會主動呼叫 upsert API。

## 解法

將 xconfig 中的 tblconfig.WEBAPIUPDATENEWMEMBER 設定為 Y 即可啟用 upsert API 呼叫。相關設定還包含 tblconfig.WEBAPIUPDATENEWMEMBERATDAYEND（控制日結時是否呼叫 upsert API）。

## 相關資訊

- Jira: [FE-1680](https://ctil.atlassian.net/browse/FE-1680)
- 解決日期: 2025-04-29
- 組件: Front End
- 負責人: Sang
- 附件: [image-20250425-064220.png](https://ctil.atlassian.net/rest/api/3/attachment/content/55726)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1680/image-20250425-064220.png" style="max-width:100%;border-radius:6px;margin:4px 0">

