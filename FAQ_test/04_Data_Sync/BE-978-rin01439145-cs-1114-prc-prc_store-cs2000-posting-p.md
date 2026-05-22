---
project: BE
issue_key: BE-978
issue_type: Bug PRD
status: Re Open
tags:
- 04_data_sync
- be
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/BE-978
created: '2025-01-06'
resolved: ''
fix_version: ''
components:
- Backend (ChainStorePlus 7.0)
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: complete
---
BE-978: PRC - PRC_Store - CS2000 - Posting : Posting Main terminated

| 問題
中國地區 POS 過帳（Posting）時，Posting Main 程序異常終止，錯誤訊息為「Cannot insert duplicate key row in object 'dbo.joupay' with unique index 'Ijoupa'」。PCD 檔案卡住導致後續過帳中斷，且該筆交易僅有 joupay 資料，缺少 jouinv 及 joudis 資料。此問題為週期性發生。

| 根因
多筆交易同時過帳時，因 joupay 表的唯一索引（Ijoupa）約束，psterr_seq 序號取得邏輯存在排序缺陷，加上共用資料庫連線（shared conn instance）引發的並行衝突，導致重複鍵值寫入失敗。Cy Lau 分析確認為 IC8006 的 psterr_seq 排序及 DLL_CSDBObj 共用連線問題。

| 解法
短期解法：移除卡住的 PCD 檔案，刪除錯誤的 joupay 紀錄後重新匯入 PCD 檔案。長期修復已包含於 Hot fix CY 250117 (v1.25.01.1700)：增加隨機延遲處理重試機制、修正 get_psterr_seq 排序邏輯避免重複序號、修正 pstlog_dbObj 共用連線問題改為新建連線。

| 相關資訊
- Jira: [BE-978](https://ctil.atlassian.net/browse/BE-978)
- 組件: Backend (ChainStorePlus 7.0)
- 負責人: Cy Lau
- 附件: [20250106.zip](https://ctil.atlassian.net/rest/api/3/attachment/content/49993) | [image-20250106-102908.png](https://ctil.atlassian.net/rest/api/3/attachment/content/49974) | [image-20250106-103131.png](https://ctil.atlassian.net/rest/api/3/attachment/content/49975) | [image-20250106-103225.png](https://ctil.atlassian.net/rest/api/3/attachment/content/49976) | [image-20250107-061807.png](https://ctil.atlassian.net/rest/api/3/attachment/content/50001)