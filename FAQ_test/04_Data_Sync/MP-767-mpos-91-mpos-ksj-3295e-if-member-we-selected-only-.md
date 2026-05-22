---
project: MP
issue_key: MP-767
issue_type: Bug PRD
status: Closed
tags:
- 04_data_sync
- faq
- mp
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-767
created: '2025-04-14'
resolved: '2025-06-04'
fix_version: BE-V70R3.106
components:
- MPOS
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: partial
---
MP-767: MPOS KSJ 3.29.5e, if member we selected only have 'Home phone no', will cause posting error

| 問題
在 KSJ 地區的 MPOS v3.29.5e 版本中，若選擇的會員僅有「住家電話」（Home Phone No）而無手機號碼，則該筆交易無法成功 posting 到後端資料庫。系統日誌顯示 Text Length Overflow、Invalid occupation code 等多項錯誤，導致 Sales Memo 遺失。

| 根因
MQPolling.exe 在處理含有特定 VIP 名稱（由住家電話搜尋回傳）的訊息並產生 PCD 檔案時，發生編碼處理異常，導致 PCD 格式錯誤。當 sqlpcd polling 發生錯誤時，系統切換至 PCD 檔案流程，但 PCD 產出過程中的 encoding handling 不足，造成資料欄位長度溢位及格式錯誤。

| 解法
在 MQPolling.exe 版本 2025.5.22.1523 中修復：(1) 修正 sqlpcd_till length exception 問題；(2) 當 sqlpcd polling 發生錯誤需切換至 PCD 檔案時，加入 encoding handling。Release：\\ds411\share\POS_BE_Component_Release\250522 Coach_KSJ_MQPolling。僅適用於 KSJ 地區。

| 相關資訊
- Jira: [MP-767](https://ctil.atlassian.net/browse/MP-767)
- Fix Version: BE-V70R3.106
- 解決日期: 2025-06-04
- 組件: MPOS
- 負責人: Joy Li
- 附件: [8a6e12d2-1c1f-47fa-8120-594cbde9f439.png](https://ctil.atlassian.net/rest/api/3/attachment/content/56836) | [image (4).png](https://ctil.atlassian.net/rest/api/3/attachment/content/56880) | [image-20250414-100452.png](https://ctil.atlassian.net/rest/api/3/attachment/content/54948) | [image-20250414-100612.png](https://ctil.atlassian.net/rest/api/3/attachment/content/54946) | [image-20250414-100855.png](https://ctil.atlassian.net/rest/api/3/attachment/content/54947)