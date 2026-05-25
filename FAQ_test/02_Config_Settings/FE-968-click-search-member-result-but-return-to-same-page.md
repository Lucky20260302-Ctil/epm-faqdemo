---
project: FE
issue_key: FE-968
issue_type: Bug QA
status: Closed
title: "FE-968: click search member result but return to same page"
tags:
- 02_config_settings
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-968
created: '2021-05-04'
resolved: '2022-07-12'
fix_version: v750.01R01A
components:
- Frontend
has_images: false
category: 02_Config_Settings
category_label: 配置與設定
quality: complete
---

FE-968: click search member result but return to same page

## 症狀

在會員查詢表單（Member Enquiry）中輸入條件搜尋會員後，點選搜尋結果中的會員，系統未將該會員資料帶入會員面板（Member Panel），而是停留在原查詢頁面。

## 根因

tblconfig 設定項 ValidateOnlineMember 預設值為 'N'，系統未對從會員查詢表單選擇的會員進行有效性驗證，導致無法正確傳遞會員資料至會員面板。

## 解法

將 tblconfig.ValidateOnlineMember 設定為 'Y'，系統將驗證所選會員是否有效且未過期，僅回傳符合條件的會員至會員面板。此修復包含於版本 v750.01R01A。

## 相關資訊

- Jira: [FE-968](https://ctil.atlassian.net/browse/FE-968)
- Fix Version: v750.01R01A
- 解決日期: 2022-07-12
- 組件: Frontend
- 負責人: howard
- 附件: [image-2021-05-04-16-24-44-125.png](https://ctil.atlassian.net/rest/api/3/attachment/content/37338)


## 相關截圖

<img src="/FAQ_test/attachments/FE-968/image-2021-05-04-16-24-44-125.png" style="max-width:100%;border-radius:6px;margin:4px 0">

