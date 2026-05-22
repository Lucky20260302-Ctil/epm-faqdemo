---
project: FE
issue_key: FE-1670
issue_type: Bug PRD
status: Closed
tags:
- 02_config_settings
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1670
created: '2025-04-17'
resolved: ''
fix_version: ''
components:
- API
has_images: false
category: 02_Config_Settings
category_label: 配置與設定
quality: complete
---

FE-1670: Unable to send eReceipt - JP CS2K v75.004.1200.0001

## 症狀

在日本 Coach 店舖（JP CS2K v75.004.1200.0001）測試 CJ eReceipt 電子收據功能時，系統無法發送電子收據，前端呼叫 eReceiptRestfulService 時返回 HTTP Error 500.31「Failed to load ASP.NET Core runtime」錯誤，且後續出現 404 找不到服務的錯誤。

## 根因

根本原因有兩層：(1) Web 伺服器（apawiqwposweb21 及 apawiqwposweb22）未安裝 .NET 8 Hosting Bundle，導致 ASP.NET Core runtime 無法載入；(2) BEAPI 呼叫 eReceiptRestfulService 的路徑設定與實際部署環境不一致，導致 404 錯誤。

## 解法

於兩台 Web 伺服器上安裝 .NET 8 Hosting Bundle（位於 \\ds411\public\anson\eReceiptRestfulService），安裝後重新啟動 Application Pool。同時需確認 FEPOS 版本與 BEAPI 的 eReceipt 服務路徑設定與部署環境一致。測試通過後等待正式部署。

## 相關資訊

- Jira: [FE-1670](https://ctil.atlassian.net/browse/FE-1670)
- 組件: API
- 負責人: Tovi Wang
- 附件: [1EA47B32-111B-4DDD-85DE-3390C7E42E54-20250516-090909.png](https://ctil.atlassian.net/rest/api/3/attachment/content/57004) | [2B48D9C6-FADD-4C6C-A88A-E2E9213F42CA-20250516-083422.png](https://ctil.atlassian.net/rest/api/3/attachment/content/56987) | [7153572C-B977-4833-B8BC-B1F195FA98BF-20250516-090714.png](https://ctil.atlassian.net/rest/api/3/attachment/content/56989) | [A22286B1-275F-4BAD-AFCE-FBF97316FAA9-20250516-092625.png](https://ctil.atlassian.net/rest/api/3/attachment/content/56995) | [CS-1403.zip](https://ctil.atlassian.net/rest/api/3/attachment/content/55106)
