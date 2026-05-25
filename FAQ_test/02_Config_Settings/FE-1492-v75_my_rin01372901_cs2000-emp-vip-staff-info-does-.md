---
project: FE
issue_key: FE-1492
issue_type: Bug PRD
status: Closed
title: "FE-1492: V75_MY_RIN01372901_CS2000 EMP VIP staff info does not update in FE"
tags:
- 02_config_settings
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1492
created: '2024-08-29'
resolved: '2024-09-08'
fix_version: v750.04R04I
components:
- Front End
has_images: false
category: 02_Config_Settings
category_label: 配置與設定
quality: complete
---

FE-1492: V75_MY_RIN01372901_CS2000 EMP VIP staff info does not update in FE 

## 症狀

在 ONLINEMEMBERENQUIRY 設為 Y 的環境（如 KSG、KMY 等），EMP 員工 VIP 會員資料無法從 zlog 或 mastconv.dat 檔案更新至前端（FE）系統。即使成功匯入 Mastconv 檔案或推送 Zlog，前端的 VIP 員工資料仍維持舊值未更新。

## 根因

當 ONLINEMEMBERENQUIRY 配置設為 Y 時，系統會啟用線上會員查詢模式，但程式在處理 EMP 類型會員時存在邏輯缺陷，無法正確從 zlog/mastconv.dat 檔案中讀取並更新 EMP 會員資料至本地數據庫。

## 解法

臨時 Workaround：(1) 將 ONLINEMEMBERENQUIRY 設為 N；(2) 重新匯入 Mastconv 檔案或更新 Zlog 檔案；(3) 將 ONLINEMEMBERENQUIRY 恢復為 Y。正式修復版本：v750.04R04I（含 v750.04R04H 及 v750.05 的 DotNet Zupdated 程式修正）。

## 相關資訊

- Jira: [FE-1492](https://ctil.atlassian.net/browse/FE-1492)
- Fix Version: v750.04R04I
- 解決日期: 2024-09-08
- 組件: Front End
- 負責人: Sherman tse
