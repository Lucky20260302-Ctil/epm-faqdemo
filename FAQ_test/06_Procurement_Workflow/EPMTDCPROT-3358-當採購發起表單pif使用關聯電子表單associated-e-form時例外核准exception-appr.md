---
project: EPMTDCPROT
issue_key: EPMTDCPROT-3358
issue_type: ''
status: ''
tags:
- 06-procurement-workflow
- 06_procurement_workflow
- epm
- epmtdcprot
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-3358
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 06_Procurement_Workflow
category_label: 採購流程
quality: complete
---
EPMTDCPROT-3358: 

| 問題

當採購發起表單（PIF）使用關聯電子表單（associated e-Form）時，例外核准（exception approval）的驗證邏輯會錯誤地從原始關聯 PIF 繼承資料，導致例外核准原因無法取消選取，且該繼承問題同時影響開標團隊（opening team）的選擇，嚴重影響系統記錄與審計日誌。

| 根因

系統在處理關聯電子表單鏈時，部分記錄與驗證邏輯會從原始 PIF（例如 PIF#1287）傳遞至後續 PIF。即使採購員已在新 PIF 中更改詳細資料，這些從關聯 PIF 繼承的資料仍無法被覆蓋更新，導致例外核准驗證及開標團隊資料錯誤。

| 解法

修正例外核准原因的驗證邏輯，使其不再從關聯的採購發起電子表單中提取驗證資料；同步修正開標團隊電子表單驗證，不再檢查關聯 PIF 的資料。測試確認：例外核准原因正確顯示，開標團隊電子表單驗證不再從關聯 PIF 提取資料（Test Pass）。

| 相關資訊

- Jira: [EPMTDCPROT-3358](https://ctil.atlassian.net/browse/EPMTDCPROT-3358)
- Fix Version: 未標註
- 分類: 採購流程
- 專案: EPMTDCPROT | 附件: [74277](https://ctil.atlassian.net/rest/api/3/attachment/content/74277) | [74275](https://ctil.atlassian.net/rest/api/3/attachment/content/74275) | [74278](https://ctil.atlassian.net/rest/api/3/attachment/content/74278) | [74276](https://ctil.atlassian.net/rest/api/3/attachment/content/74276) | [74274](https://ctil.atlassian.net/rest/api/3/attachment/content/74274) |
