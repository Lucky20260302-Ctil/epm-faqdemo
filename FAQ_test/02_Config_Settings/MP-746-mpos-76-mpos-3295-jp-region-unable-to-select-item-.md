---
project: MP
issue_key: MP-746
issue_type: Bug PRD
status: Closed
tags:
- 02_config_settings
- faq
- mp
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-746
created: '2025-02-17'
resolved: '2025-05-02'
fix_version: ''
components:
- Frontend
has_images: false
category: 02_Config_Settings
category_label: 配置與設定
quality: partial
---
MP-746: MPOS 3.29.5 - JP region -Unable to select item after deploy COACH_MPOSWebAPI_R3.29.5d

| 問題
JP 區域部署 COACH_MPOSWebAPI_R3.29.5d 後，若 Saleshub 已啟用，則無法在 MPOS 上選取商品。

| 根因
TblConfig 中的 mPosEncryptKey 設定值為 '0'（無效加密金鑰），導致 Saleshub 與 API 之間的通訊加密驗證失敗，商品選取功能無法正常運作。

| 解法
將 Xconfig 中 mPosEncryptKey 的值設定為正確的加密金鑰字串（如 f6brWp8kVPs4HYbIsoykeR5TCAdMmOuV），即可恢復正常。此為部署 patch 後的必要配置步驟。

| 相關資訊
- Jira: [MP-746](https://ctil.atlassian.net/browse/MP-746)
- 解決日期: 2025-05-02
- 組件: Frontend
- 負責人: Daniel Leung
- 附件: [202502141124040000.mp4](https://ctil.atlassian.net/rest/api/3/attachment/content/51676) | [image-2025-02-14-11-25-49-225.png](https://ctil.atlassian.net/rest/api/3/attachment/content/51675) | [image-20250217-031714.png](https://ctil.atlassian.net/rest/api/3/attachment/content/51691) | [image-20250217-085758.png](https://ctil.atlassian.net/rest/api/3/attachment/content/51777) | [MPOS logs MPOS-76_MPOS-77.zip](https://ctil.atlassian.net/rest/api/3/attachment/content/51677)