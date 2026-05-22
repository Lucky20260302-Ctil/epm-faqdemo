---
project: FE
issue_key: FE-1821
issue_type: Bug PRD
status: DEV Done
tags:
- 04_data_sync
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1821
created: '2025-11-28'
resolved: ''
fix_version: ''
components:
- Day End
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: complete
---
FE-1821: INC3314927 KSJ C309 Receipt Print performance issue

| 問題
韓國 CJ 店舖 C309 的收據列印速度異常緩慢，交易儲存過程中的「會員資料上傳（Member Data Upload）」步驟耗時過長。比對 C309 與 C318 的效能數據，C309 的中位數時間為 8.822 秒，明顯高於 C318 的 6.601 秒。

| 根因
系統組態 tblconfig.WebApiUpdateNewMember 已應用於 CS2000、CSPLUS、AXIOM CRM 等系統，可在建立新交易時抑制同步呼叫 Web API upsert 會員資料，改為非同步處理。然而，C360 及 Memberson CRM 尚未套用此優化，導致該等店舖在交易儲存時仍進行同步的會員資料上傳，拖慢整體收據列印效能。

| 解法
開發人員在 v750.04R13E1 版本中為 C360 及 Memberson CRM 新增支援非同步 Upsert Member（透過 Web API），當 tblconfig.WEBAPIUPDATENEWMEMBER 設為 'Y' 時，建立新會員備註時將採用非同步方式上傳，不再阻塞交易儲存流程。程式碼已提交至 v750.04R13E1、v750.04R16 及 v750.05R03 分支。

| 相關資訊
- Jira: [FE-1821](https://ctil.atlassian.net/browse/FE-1821)
- 組件: Day End
- 負責人: Sherman tse