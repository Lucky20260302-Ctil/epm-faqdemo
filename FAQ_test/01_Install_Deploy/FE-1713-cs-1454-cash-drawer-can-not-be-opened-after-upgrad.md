---
project: FE
issue_key: FE-1713
issue_type: Bug PRD
status: Closed
tags:
- 01_install_deploy
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1713
created: '2025-06-11'
resolved: '2025-07-11'
fix_version: FE-75.004.1303.0002
components:
- Front End
has_images: false
category: 01_Install_Deploy
category_label: 安裝與部署
quality: complete
---
FE-1713: Cash drawer can not be opened after upgrade to V75 - MC region

| 問題
升級至 V75 版本後，所有收銀機的錢櫃（Cash Drawer）無法開啟。經排查發現 cah.ini 設定檔中的 COM Port 設定值從原本的 '1' 被自動變更為 '7'，導致錢櫃無法正常運作。此問題影響 MC 區域所有已升級的 POS 機台。

| 根因
V75 升級過程中，cah.ini 設定檔被兩個來源覆蓋：1) InstallationShield 在主要更新時使用 Z:\Tapestry\COMMON 路徑下的 cah.ini（預設 COM Port=7）；2) AdminUpdate.bat 從 Retdata6\inibak 備份資料夾複製 cah.ini。當備份資料夾不存在或 ini 設定不正確時，最終 cah.ini 的 COM Port 即被改為 7。

| 解法
1) 手動將 cah.ini 中的 COM Port 設定改回正確值（如 1）。2) 已於 FE-75.004.1303.0002 版本中修復，增強 AdminUpdate.bat 邏輯：若備份資料夾中不存在 cah.ini，則保留 CSPLUS 資料夾中的現有 cah.ini；若備份資料夾存在 cah.ini，則覆蓋至 CSPLUS 資料夾以還原原有設定。

| 相關資訊
- Jira: [FE-1713](https://ctil.atlassian.net/browse/FE-1713)
- Fix Version: FE-75.004.1303.0002
- 解決日期: 2025-07-11
- 組件: Front End
- 負責人: Joy Li
- 附件: [ac222b97-ef25-489b-b535-916a01f5fcdd.png](https://ctil.atlassian.net/rest/api/3/attachment/content/59514) | [AdminUpdate.bat](https://ctil.atlassian.net/rest/api/3/attachment/content/59387) | [AdminUpdate (3c8ee31d-efc6-4c84-9f04-9ab12b8224b1).bat](https://ctil.atlassian.net/rest/api/3/attachment/content/59529) | [AdminUpdate (563609df-3e9d-4377-99ee-60d5b0838a49).bat](https://ctil.atlassian.net/rest/api/3/attachment/content/59533) | [AdminUpdate (7f72979e-8f20-4c7a-a73f-39812f04e9b3).bat](https://ctil.atlassian.net/rest/api/3/attachment/content/59495)