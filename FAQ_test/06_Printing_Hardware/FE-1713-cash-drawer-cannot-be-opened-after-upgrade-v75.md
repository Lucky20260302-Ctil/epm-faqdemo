---
project: ERM FEPOS
issue_key: FE-1713
issue_type: Bug PRD
status: Closed
tags: [faq, erm_fepos]
jira_url: "https://ctil.atlassian.net/browse/FE-1713"
created: 2025-06-11
resolved: 2025-07-11
fix_version: "FE-75.004.1303.0002"
components: [Front End]
---

# FE-1713: [CS-1454] Cash drawer can not be opened after upgrade to V75 - MC region

## 問題

升級至 V75 版本後，MC 區域所有收銀機的錢櫃（Cash Drawer）無法開啟。經排查發現 cah.ini 檔案中的 COM Port 設定在升級過程中被自動從正確值（如 COM1）更改為預設值 COM7。

## 根因

升級過程中，InstallationShield 或 AdminUpdate.bat 會覆蓋 CSPLUS 資料夾下的 cah.ini 檔案。若備份資料夾（inibak）中存在 cah.ini，AdminUpdate.bat 會將其覆蓋到 CSPLUS 目錄；若備份資料夾不存在 cah.ini，則 InstallationShield 會使用預設 COM7 設定，導致錢櫃無法正常開啟。

## 解法

手動將 cah.ini 中的 COM Port 設定恢復為正確值（可參考 inibak 備份資料夾中的 cah.ini.bak）。此問題已於 FE-75.004.1303.0002 版本修正，升級腳本會保留原有 COM Port 設定。

## 相關資訊

- **Jira：** [FE-1713](https://ctil.atlassian.net/browse/FE-1713)
- **Fix Version：** FE-75.004.1303.0002
- **解決日期：** 2025-07-11
- **組件：** Front End
- **附件截圖：** [image-20250611-072631.png](https://ctil.atlassian.net/rest/api/3/attachment/content/59389) [image-20250611-072816.png](https://ctil.atlassian.net/rest/api/3/attachment/content/59388) [image-20250611-072936.png](https://ctil.atlassian.net/rest/api/3/attachment/content/59386) [image-20250611-073007.png](https://ctil.atlassian.net/rest/api/3/attachment/content/59391) [image-20250612-063415.png](https://ctil.atlassian.net/rest/api/3/attachment/content/59454) [image-20250612-095859.png](https://ctil.atlassian.net/rest/api/3/attachment/content/59494)
