---
project: MP
issue_key: MP-793
issue_type: Bug PRD
status: Closed
tags:
- 05_error_exception
- faq
- mp
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/MP-793
created: '2025-08-19'
resolved: '2025-09-02'
fix_version: 3.29.6-20250827.1, 3.30.5-20250827.1
components:
- MPOS
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
---
MP-793: CJ mPOS Prod_ J317 the transaction disappears if it`s not connected to SalesHub

| 問題
mPOS 在輸入交易但尚未完成時，使用者切換至其他應用程式（如 iPhone Safari 開啟 eNameCapture），返回 mPOS 後已輸入的交易資料全部消失。需保持「Connected to SalesHub」狀態才能避免問題發生。

| 根因
mPOS 在重新連線至 SalesHub 的過程中存在 UI 層級 Bug，重新連線時未保留當前交易資料，導致畫面中已輸入的交易資訊被清空。

| 解法
升級至 Hot Fix 版本 3.29.6-20250827.1 或 3.30.5-20250827.1。此修復已於 2025-09-02 發布至 COACH。短期規避方案：確保交易過程中保持與 SalesHub 連線，避免在未完成交易前切換至其他應用程式。

| 相關資訊
- Jira: [MP-793](https://ctil.atlassian.net/browse/MP-793)
- Fix Version: 3.29.6-20250827.1, 3.30.5-20250827.1
- 解決日期: 2025-09-02
- 組件: MPOS
- 負責人: Daniel Leung
- 附件: [image-20250827-083816.png](https://ctil.atlassian.net/rest/api/3/attachment/content/64279) | [J317.zip](https://ctil.atlassian.net/rest/api/3/attachment/content/63711) | [Test case of [MPOS-115][INC3149444]CJ mPOS Prod_ J317 the transaction disappears if it`s not connected to SalesHub.xlsx](https://ctil.atlassian.net/rest/api/3/attachment/content/64493) | [video_574897147062255875-Ub70KESy.mov](https://ctil.atlassian.net/rest/api/3/attachment/content/63710)