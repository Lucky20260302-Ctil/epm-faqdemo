---
project: BE
issue_key: BE-1172
issue_type: Bug PRD
status: Closed
tags:
- 01_install_deploy
- be
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-1172
created: '2025-09-01'
resolved: '2025-09-11'
fix_version: 'CS2K_BE_V70R3.119, CS2k_FE_V75.004.1401.0000, MPOS API 3.30.6, MPOS IPA 3.30.6-20250908.1 '
components:
- Backend (ChainStorePlus 7.0)
has_images: false
category: 01_Install_Deploy
category_label: 安裝與部署
quality: complete
---

BE-1172: CS-1628 TW CRM - “Profile” and “Purchase History” Not Available For Current Version

## 症狀

台灣 CRM 版本（v75.004.1309.0000）升級後，POS 前端無法顯示會員「Profile」及「Purchase History」兩個功能。具體問題包括：(1) FE 端 vbretail.ini 設定檔內容不正確；(2) Member Purchase 功能無法顯示會員購買紀錄，因為程式未支援多區域（X-COUNTRY）情境。

## 根因

根因有二：(1) FE 端 vbretail.ini 設定檔部署時內容有誤，導致 POS 無法正確載入 CRM 相關配置；(2) 後端 BEGWCRM 及前端 Member Purchase 程式原本僅支援單一區域，當台灣 CRM 上線時需要同時處理多個區域嘅請求，但程式未做 multi-region 適配，導致無法正確傳遞 company code。

## 解法

短期 workaround：手動推送正確嘅 vbretail.ini 到 FE CSPLUS 資料夾，並手動修改 production 程式碼預設傳入 company code=14。長期修復：FE 端更新 ini 值及程式以支援 multi-region (X-COUNTRY)，BE BEGWCRM 同步更新支援多區域。Fix versions: CS2K_BE_V70R3.119、CS2k_FE_V75.004.1401.0000、MPOS API 3.30.6、MPOS IPA 3.30.6-20250908.1，已於 2025-09-11 發布至 Tapestry。

## 相關資訊

- Jira: [BE-1172](https://ctil.atlassian.net/browse/BE-1172)
- Fix Version: CS2K_BE_V70R3.119, CS2k_FE_V75.004.1401.0000, MPOS API 3.30.6, MPOS IPA 3.30.6-20250908.1 
- 解決日期: 2025-09-11
- 組件: Backend (ChainStorePlus 7.0)
- 負責人: Sherman tse
- 附件: [image-20250901-093357.png](https://ctil.atlassian.net/rest/api/3/attachment/content/64484) | [Test case of CS-1628 TW CRM - “Profile” and “Purchase History” Not Available For Current Version - FE.xlsx](https://ctil.atlassian.net/rest/api/3/attachment/content/64920) | [Test case of CS-1628 TW CRM - “Profile” and “Purchase History” Not Available For Current Version -mpos.xlsx](https://ctil.atlassian.net/rest/api/3/attachment/content/64921)
