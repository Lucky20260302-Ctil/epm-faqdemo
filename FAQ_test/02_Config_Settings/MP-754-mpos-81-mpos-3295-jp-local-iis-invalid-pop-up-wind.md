---
project: MP
issue_key: MP-754
issue_type: Bug PRD
status: Closed
tags:
- 02_config_settings
- faq
- mp
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-754
created: '2025-03-05'
resolved: '2025-10-09'
fix_version: ''
components:
- MPOS
has_images: false
category: 02_Config_Settings
category_label: 配置與設定
quality: complete
---

MP-754: MPOS 3.29.5 - JP Local IIS, invalid pop-up window for Void function

## 症狀

在日本 Local IIS 環境的 MPOS v3.29.5 版本中，執行 Void Sales Memo（作廢銷售單）操作時，系統會錯誤地彈出 e-Receipt 列印提示視窗，而非直接列印作廢單據。正常行為應是 Void 操作直接印出小票，只有正常銷售才彈出 e-Receipt 提示。Cloud IIS 環境無此問題。

## 根因

MPOS API 伺服器上的 dbCoachLocal.db 資料庫中，printReceiptFlow 參數預設值為 0，此設定會使所有列印操作（包括 Void）都觸發列印彈窗。正確應設為 1，使系統直接列印後發送 e-Receipt，且 Void 操作不彈窗。Local IIS 環境未正確配置此參數。

## 解法

前往 MPOS API 伺服器 → 開啟 IIS → 選擇使用中的 API → 點擊 Explore → 在資料夾中找到 dbCoachLocal.db → 將 printReceiptFlow 參數設為 1。正式修復版本為 3.30.2-20250314.1。

## 相關資訊

- Jira: [MP-754](https://ctil.atlassian.net/browse/MP-754)
- 解決日期: 2025-10-09
- 組件: MPOS
- 負責人: Daniel Leung
- 附件: [dbCoachLocal.db](https://ctil.atlassian.net/rest/api/3/attachment/content/52542) | [image-20250305-032154.png](https://ctil.atlassian.net/rest/api/3/attachment/content/52491) | [image-20250305-032254.png](https://ctil.atlassian.net/rest/api/3/attachment/content/52492) | [image-20250305-032417.png](https://ctil.atlassian.net/rest/api/3/attachment/content/52493) | [image-20250305-033347.png](https://ctil.atlassian.net/rest/api/3/attachment/content/52494)
