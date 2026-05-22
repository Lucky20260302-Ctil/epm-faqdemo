---
project: FE
issue_key: FE-1728
issue_type: Bug QA
status: Closed
tags:
- 07_workflow_business
- faq
- fe
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1728
created: '2025-07-11'
resolved: '2025-07-31'
fix_version: ''
components:
- Front End
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
---
FE-1728: Laser Day End report still display 按金單數量 when no deposit transaction in that day

| 問題
Laser模式的日結報表中，即使當天沒有任何按金（deposit）交易，報表上仍會顯示「按金單數量」的區段。此問題發生在SYSCON_DEP_MOD設為-1的設定下。TMU模式則無此問題，僅Laser模式受影響。

| 根因
Laser日結報表的PrintAgent在產生報表時，未正確根據當天實際交易情況判斷是否應顯示按金單數量區段。無論是否有按金交易，該區段都會被列印出來，此為PrintAgent程式邏輯缺陷，未對無交易情況進行條件判斷。

| 解法
更新PrintAgent程式至v750.04R13E版本（路徑：\\ds411\share\POS_FE_Release_64\20250711 Coach v750.04R13E\PrintAgent）。更新後，Laser模式的日結報表會根據當天是否有按金交易來決定是否顯示按金單數量區段。

| 相關資訊
- Jira: [FE-1728](https://ctil.atlassian.net/browse/FE-1728)
- 解決日期: 2025-07-31
- 組件: Front End
- 負責人: Sang
- 附件: [image-20250711-103328.png](https://ctil.atlassian.net/rest/api/3/attachment/content/61708)