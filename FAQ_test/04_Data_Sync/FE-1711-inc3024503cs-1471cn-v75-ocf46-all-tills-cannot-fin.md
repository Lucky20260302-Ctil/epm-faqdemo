---
project: FE
issue_key: FE-1711
issue_type: Bug DEV
status: Closed
title: "FE-1711: CN v75 OCF46 All tills cannot find a member"
tags:
- 04_data_sync
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1711
created: '2025-06-11'
resolved: '2025-07-09'
fix_version: BE-V70R3.113
components:
- Front End v750.01R01A
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: complete
---

FE-1711: CN v75 OCF46 All tills cannot find a member

## 症狀

中國大陸 v75 店舖 OCF46 所有收銀機均無法搜尋到特定會員（OCF220C00027451，手機號碼 13161831983）。該會員在資料庫中顯示已過期，且透過 QR Code 掃描觸發自動建立會員時，使用 QR Code 內嵌的會員編號覆蓋了 POS 自動生成的編號。CRMBEAPI 返回 NullReferenceException 及型別對應錯誤。

## 根因

根本原因為 CRM BEAPI 無法正確處理 birth_day（生日）為 null 的會員資料。當透過 QR Code 搜尋會員並觸發自動建立新會員時，若 CRM 返回的會員資料中生日欄位為 null，BEAPI 的 upsert 邏輯無法處理 null 值，導致型別對應錯誤（Mapping types error）及 NullReferenceException，進而使前端無法找到該會員。

## 解法

Anson Cheung 修改 CRM BEAPI 的 upsert 邏輯，使其能正確處理 birth_day = null 的情況，將 null 值處理為 0（遵循與 FE POS 一致的生日處理規則，即 year=2999、2099 或大於等於當前年份均視為未定義生日）。修復版本：BE-V70R3.113，於 2025-07-09 發布。

## 相關資訊

- Jira: [FE-1711](https://ctil.atlassian.net/browse/FE-1711)
- Fix Version: BE-V70R3.113
- 解決日期: 2025-07-09
- 組件: Front End v750.01R01A
- 負責人: Anson Cheung
- 附件: [CRM-20250520.log](https://ctil.atlassian.net/rest/api/3/attachment/content/59377) | [CRM-20250524.log](https://ctil.atlassian.net/rest/api/3/attachment/content/59380) | [CRMBEAPI log (af413e45-1abe-45f8-a673-48ad39f19daf).zip](https://ctil.atlassian.net/rest/api/3/attachment/content/59379) | [image-20250611-033259.png](https://ctil.atlassian.net/rest/api/3/attachment/content/59356) | [image-20250611-033754.png](https://ctil.atlassian.net/rest/api/3/attachment/content/59355)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1711/image-20250611-033259.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1711/image-20250611-033754.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1711/image-20250611-034117.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1711/image-20250611-055925.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1711/image-20250611-061301.png" style="max-width:100%;border-radius:6px;margin:4px 0">

> 共 13 張截圖，[查看全部](/FAQ_test/attachments/FE-1711/)
