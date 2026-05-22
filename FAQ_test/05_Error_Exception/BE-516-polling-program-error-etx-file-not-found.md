---
project: "BE"
issue_key: "BE-516"
issue_type: "Bug PRD"
status: "Closed"
tags: [faq, be]
jira_url: "https://ctil.atlassian.net/browse/BE-516"
created: "2021-08-24"
resolved: "2021-08-24"
fix_version: "BE-V70R2.63"
components: [Backend (ChainStorePlus 7.0)]
category: "05_Error_Exception"
---

BE-516: Polling program --- Error “ETX file not found”

| 問題
Polling 排程在處理檔案時回傳「ETX file not found」錯誤，導致部分 sales memo 遺失未匯入 BE。

| 根因
Polling 任務在 ACP 檔案尚未完全上傳（STX/ETX 未就緒）時便開始處理，race condition 導致檔案不完整。

| 解法
修改 Polling 程式邏輯，確認 STX 與 ETX 皆已上傳完成後才開始處理檔案。已於 BE-V70R2.63 版本修復。

| 相關資訊
- Jira: [BE-516](https://ctil.atlassian.net/browse/BE-516)
- Fix Version: BE-V70R2.63
- 解決日期: 2021-08-24
- 組件: Backend (ChainStorePlus 7.0)
- 負責人: Joy Li