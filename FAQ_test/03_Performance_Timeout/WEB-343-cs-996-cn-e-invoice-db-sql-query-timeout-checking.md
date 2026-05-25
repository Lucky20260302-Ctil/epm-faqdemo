---
project: WEB
issue_key: WEB-343
issue_type: Bug PRD
status: Closed
title: "WEB-343: CS-996: CN E-invoice DB SQL Query timeout checking"
tags:
- 03_performance_timeout
- faq
- web
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/WEB-343
created: '2024-04-25'
resolved: '2024-04-25'
fix_version: BE-V70R3.56
components:
- interface
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: complete
---

WEB-343: CS-996: CN E-invoice DB SQL Query timeout checking

## 症狀

CN E-invoice 電子發票 DB SQL 查詢發生逾時（timeout），導致發票資料處理異常。

## 根因

SQL 查詢效能不佳，資料選取邏輯無 timeout 控制機制，預設無上限等待導致查詢卡死。

## 解法

1) 於 appsettings.json 新增 sqlCmdTimeout 設定（預設 300 秒）；2) 進行 SQL tuning 優化資料選取效能。已於 BE-V70R3.56 版本修復。

## 相關資訊

- Jira: [WEB-343](https://ctil.atlassian.net/browse/WEB-343)
- Fix Version: BE-V70R3.56
- 解決日期: 2024-04-25
- 組件: interface
- 負責人: Joy Li
- 附件: [image-20240425-073308.png](https://ctil.atlassian.net/rest/api/3/attachment/content/40811)


## 相關截圖

<img src="/FAQ_test/attachments/WEB-343/image-20240425-073308.png" style="max-width:100%;border-radius:6px;margin:4px 0">

