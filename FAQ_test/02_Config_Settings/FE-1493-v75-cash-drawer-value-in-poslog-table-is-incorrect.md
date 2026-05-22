---
project: FE
issue_key: FE-1493
issue_type: Bug PRD
status: Closed
tags:
- 02_config_settings
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1493
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
FE-1493: V75 - Cash Drawer value in 'poslog' table is incorrect.

| 問題
V75 升級部署後，poslog 資料表中 Cash Drawer 的值記錄不正確。原本需要將 SYSCON_DRAWER 設定從 D 改為 W 才能正確記錄，但部署流程中難以識別正確設定值，導致 drawer 數值異常。

| 根因
SYSCON_DRAWER 設定值 D（connect to OPOS without feedback）與 W（connect to OPOS with feedback）在舊版程式中行為不同。V75 部署時若沿用 D 設定而未改為 W，POS 不會回寫正確的 drawer 反饋值至 poslog。

| 解法
開發團隊修改 V75 程式邏輯，使 SYSCON_DRAWER=D 的行為與 W 一致（connect to OPOS with feedback），無需再手動修改 config。修正版本：v750.04R04I。

| 相關資訊
- Jira: [FE-1493](https://ctil.atlassian.net/browse/FE-1493)
- Fix Version: v750.04R04I
- 解決日期: 2024-09-08
- 組件: Front End
- 負責人: Sherman tse