---
project: FE
issue_key: FE-1749
issue_type: Bug PRD
status: Closed
title: "FE-1749-cs-1628-tw-crm-profile-and-purchase-history-not-av"
tags:
- 01_install_deploy
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1749
created: '2025-09-01'
resolved: '2025-09-16'
fix_version: BE-V70R3.119a
components:
- Front End
has_images: false
category: 01_Install_Deploy
category_label: 安裝與部署
quality: complete
---

FE-1749: CS-1628 TW CRM - “Profile” and “Purchase History” Not Available For Current Version - FE

## 症狀

台灣 CRM 版本升級後，POS 前端無法顯示會員「Profile」及「Purchase History」功能。FE 端 vbretail.ini 設定檔配置不正確，且 Member Purchase 功能在 multi-region 環境下無法正確顯示購買紀錄。

## 根因

根因有兩個層面：(1) FE vbretail.ini 部署時設定錯誤，導致 CRM 相關功能無法啟用；(2) 前端程式在讀取 crm_api_config 時錯誤使用了 dbconfig_long_value 欄位而非 dbconfig_value 欄位（Daniel Leung 在 comments 中指出此錯誤），導致多區域設定無法正確載入，Member Purchase 無法傳遞正確嘅 region code 及 company 資訊。

## 解法

短期 workaround：手動推送正確 ini 檔案到 FE CSPLUS 目錄，並手動修改 production code 預設 company=14。正式修復：修正 crm_api_config 讀取欄位從 dbconfig_long_value 改為 dbconfig_value，FE 程式增加 multi-region 支援（傳遞 region code + tblconfig.crm_api_config）。同時需更新 MPOS API web.config 中 SQLitePCLRaw.core 版本至 1.1.14。Fix version: BE-V70R3.119a，已於 2025-09-16 發布。

## 相關資訊

- Jira: [FE-1749](https://ctil.atlassian.net/browse/FE-1749)
- Fix Version: BE-V70R3.119a
- 解決日期: 2025-09-16
- 組件: Front End
- 負責人: Daniel Leung
- 附件: [image-20250901-094129.png](https://ctil.atlassian.net/rest/api/3/attachment/content/64486) | [purchaseHistory_region_string.xlsx](https://ctil.atlassian.net/rest/api/3/attachment/content/64807) | [Test case of CS-1628 TW CRM - “Profile” and “Purchase History” Not Available For Current Version - FE.xlsx](https://ctil.atlassian.net/rest/api/3/attachment/content/64918) | [Test case of CS-1628 TW CRM - “Profile” and “Purchase History” Not Available For Current Version -mpos.xlsx](https://ctil.atlassian.net/rest/api/3/attachment/content/64919)


## 相關截圖

<img src="/FAQ_test/attachments/FE-1749/image-20250901-094129.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

