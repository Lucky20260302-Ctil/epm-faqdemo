---
project: FE
issue_key: FE-1829
issue_type: Bug QA
status: Closed
tags:
- 05_error_exception
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1829
created: '2025-12-11'
resolved: '2025-12-17'
fix_version: ''
components:
- Front End
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
---
FE-1829: Fail to print out Replenishment after clicked Save for Send to host

| 問題
AO站點點擊「Save for Send to host」後無法列印Replenishment報表，彈出錯誤顯示路徑異常（C:\RETDATA6\C:\RETDATA6\Replenishment.rpt）

| 根因
程式中Replenishment.rpt的檔案路徑被重複串接，形成C:\RETDATA6\C:\RETDATA6\...的無效路徑，導致報表檔案無法被找到並列印

| 解法
修正程式中報表檔案路徑的串接邏輯，並重新上傳修正後的Replenishment.rpt至終端。修正包含於v75.05R03

| 相關資訊
- Jira: [FE-1829](https://ctil.atlassian.net/browse/FE-1829)
- 解決日期: 2025-12-17
- 組件: Front End
- 負責人: Sherman tse
- 附件: [image-20251211-040626.png](https://ctil.atlassian.net/rest/api/3/attachment/content/70535) | [image-20251211-090209.png](https://ctil.atlassian.net/rest/api/3/attachment/content/70600)