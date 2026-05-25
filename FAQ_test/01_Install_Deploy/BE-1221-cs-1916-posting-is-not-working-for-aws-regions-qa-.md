---
project: BE
issue_key: BE-1221
issue_type: Bug PRD
status: Closed
title: "BE-1221-cs-1916-posting-is-not-working-for-aws-regions-qa-"
tags:
- 01_install_deploy
- be
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1221
created: '2025-12-24'
resolved: '2026-02-26'
fix_version: BE-V70R3.134a
components:
- Posting
has_images: false
category: 01_Install_Deploy
category_label: 安裝與部署
quality: complete
---

BE-1221: POSTING is not working for AWS regions - QA Env

## 症狀

在 QA 環境中，所有區域（包括 JP 及 TW）的 Posting 功能無法正常運作。數據已經成功輪詢（polling）至 sqlpcda 資料表，但無論透過 Tidal 排程或手動從 Job Server 執行 Posting，數據均未能成功過帳。日誌顯示錯誤訊息「The network path was not found」。

## 根因

CSDataInterface 使用了舊版／不同版本的 Common DLL，與 CS2KBNV1 Object（被 Polling 和 Posting 共同使用）產生版本衝突。由於 DLL 不相容，Posting 程序在嘗試寫入檔案時無法找到正確的網絡路徑。

## 解法

為 CSDataInterface 建立獨立的安裝目錄（OBJ/CSDataInterface），避免與其他模組共用相同目錄下的 DLL。同時更新相關的 cmd 腳本（Standard Data Interface.cmd 及 Standard Data Interface (Onsale Price).cmd），呼叫路徑指向新的獨立目錄。修正版本：BE-V70R3.134a。

## 相關資訊

- Jira: [BE-1221](https://ctil.atlassian.net/browse/BE-1221)
- Fix Version: BE-V70R3.134a
- 解決日期: 2026-02-26
- 組件: Posting
- 負責人: Joy Li
- 附件: [image-20251224-012714.png](https://ctil.atlassian.net/rest/api/3/attachment/content/71641) | [image-20251224-012754.png](https://ctil.atlassian.net/rest/api/3/attachment/content/71642) | [image-20260119-030005.png](https://ctil.atlassian.net/rest/api/3/attachment/content/73718) | [image-20260119-031225.png](https://ctil.atlassian.net/rest/api/3/attachment/content/73716) | [image-20260119-031425.png](https://ctil.atlassian.net/rest/api/3/attachment/content/73717)


## 相關截圖

<img src="/FAQ_test/attachments/BE-1221/image-20251224-012714.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/BE-1221/image-20251224-012754.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/BE-1221/image-20260119-030005.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/BE-1221/image-20260119-031225.png" style="max-width:100%;border-radius:6px;margin:4px 0">

<img src="/FAQ_test/attachments/BE-1221/image-20260119-031425.jpg" style="max-width:100%;border-radius:6px;margin:4px 0">

