---
project: EPMTDCPROT
issue_key: EPMTDCPROT-1101
issue_type: ''
status: ''
tags:
- 04-data-sync
- 04_data_sync
- epm
- epmtdcprot
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-1101
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: complete
---
EPMTDCPROT-1101: 

| 問題

呼叫 API 時，回傳的 supplierId 欄位顯示的是 MongoDB 的內部 _id（如 ObjectId），而非系統應回傳的供應商代碼（SupplierCode），導致 API 使用者無法正確識別供應商。

| 根因

API 回應的欄位映射（mapping）設定錯誤，後端將 supplierId 對應到資料庫的 _id 欄位（MongoDB 自動生成的內部識別碼），而非正確的 SupplierCode 欄位，導致回傳值與預期不符。

| 解法

修正 API 的欄位映射邏輯，將 supplierId 改為對應資料庫中的 SupplierCode 欄位。修正後，API 回傳的 supplierId 即為正確的供應商代碼，與系統其他模組一致。

| 相關資訊

- Jira: [EPMTDCPROT-1101](https://ctil.atlassian.net/browse/EPMTDCPROT-1101)
- Fix Version: 未標註
- 分類: 資料與同步
- 專案: EPMTDCPROT | 附件: [53585](https://ctil.atlassian.net/rest/api/3/attachment/content/53585) |
