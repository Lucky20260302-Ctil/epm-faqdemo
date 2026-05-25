---
project: FE
issue_key: FE-1866
issue_type: Bug PRD
status: Closed
title: "FE-1866: Unable to update customer email on CS2000 web"
tags:
- 05_error_exception
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1866
created: '2026-01-26'
resolved: ''
fix_version: BE-V70R3.142
components:
- Front End
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: complete
---

FE-1866: Unable to update customer email on CS2000 web

## 症狀

在 KS AU 區域的 CS2000 網頁版中，更新客戶電子郵件時系統顯示「cannot connect API, internal server error 500」錯誤，無法完成儲存。此問題僅發生於 KS ANZ 區域（40 及 41），其他區域（Coach MY、KS MY、AWS ANZ）正常。

## 根因

資料庫預存程序 spwSE9016M_UpdateMemberInfo 在 KS AU 區域缺少 @vip_comp_code 參數定義，導致 API 呼叫時傳遞的參數數量超出預存程序實際接受的參數，觸發「Procedure or function has too many arguments specified」錯誤。根本原因為該區域的 DB 預存程序版本過舊，未包含公司代碼欄位。

## 解法

將預存程序 spwSE9016M_UpdateMemberInfo 更新至最新版本以包含 @vip_comp_code 參數。Hot fix 已包含於 BE-V70R3.142 版本中，可透過標準 BE 升級流程套用。

## 相關資訊

- Jira: [FE-1866](https://ctil.atlassian.net/browse/FE-1866)
- Fix Version: BE-V70R3.142
- 組件: Front End
- 負責人: Jerry Wong
- 附件: [Apply SQL.txt](https://ctil.atlassian.net/rest/api/3/attachment/content/75255) | [image-20260126-080855.png](https://ctil.atlassian.net/rest/api/3/attachment/content/74689) | [image-20260126-081224.png](https://ctil.atlassian.net/rest/api/3/attachment/content/74691) | [image-20260129-050631.png](https://ctil.atlassian.net/rest/api/3/attachment/content/75254) | [image-20260129-051649.png](https://ctil.atlassian.net/rest/api/3/attachment/content/75256)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1866/image-20260126-080855.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1866/image-20260126-081224.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1866/image-20260129-050631.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1866/image-20260129-051649.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/FE-1866/image-20260129-072825.png" style="max-width:100%;border-radius:6px;margin:4px 0">

