---
project: FE
issue_key: FE-1384
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1384
created: '2024-05-09'
resolved: '2024-05-24'
fix_version: v750.05, v750.04R04A
components:
- Front End
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: complete
---
FE-1384: KMY incorrect PC 01 record with two member no

| 問題
啟用 dotnetpcd 後（v75），KMY 的 PC 01 記錄中 member no 被錯誤地同時寫入 jouinv_flight 與 jouinv_class 兩張表，導致資料不一致。

| 根因
dotnetpcd 模組啟用後，member no 的寫入邏輯未正確限制目標表，導致多餘的資料寫入 jouinv_class。

| 解法
修正程式使 member no 僅寫入 jouinv_flight 表，確保 posting 至 BE 時無錯誤。修復版本：v750.05 / v750.04R04A。

| 相關資訊
- Jira: [FE-1384](https://ctil.atlassian.net/browse/FE-1384)
- Fix Version: v750.05, v750.04R04A
- 解決日期: 2024-05-24
- 組件: Front End
- 負責人: Joy Li
- 附件: [image-20240509-041220.png](https://ctil.atlassian.net/rest/api/3/attachment/content/41210) | [image-20240513-024611.png](https://ctil.atlassian.net/rest/api/3/attachment/content/41302) | [pce2024050802.dat](https://ctil.atlassian.net/rest/api/3/attachment/content/41209)