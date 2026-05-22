---
project: EPMTDCPROT
issue_key: EPMTDCPROT-1903
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
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-1903
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 06_Procurement_Workflow
category_label: 採購流程
quality: complete
---
EPMTDCPROT-1903: 

| 問題

在技術評估結果（Technical Assessment Result）中：(1) 評估為 Pass 的供應商未自動勾選 checkbox；(2) 評估為 Fail 的供應商的 checkbox 仍可被手動勾選，導致可錯誤選入不合格供應商。

| 根因

前端未根據技術評估結果動態控制 checkbox 的啟用/禁用狀態與自動勾選邏輯。Benson Xu 確認修正邏輯為：「Result為Pass的checkbox會自動勾選，如果有Result為Fail的Checkbox的狀態為不可選」。

| 解法

修改前端邏輯：進入表單時自動勾選所有 Result 為 Pass 的供應商 checkbox；Result 為 Fail 的供應商 checkbox 設為禁用狀態（滑鼠移上顯示禁用標識），不可選取。Gavin Zhou 確認 uat pass。

| 相關資訊

- Jira: [EPMTDCPROT-1903](https://ctil.atlassian.net/browse/EPMTDCPROT-1903)
- Fix Version: 未標註
- 分類: 採購流程
- 專案: EPMTDCPROT | 附件: [57907](https://ctil.atlassian.net/rest/api/3/attachment/content/57907) | [57908](https://ctil.atlassian.net/rest/api/3/attachment/content/57908) | [58445](https://ctil.atlassian.net/rest/api/3/attachment/content/58445) |
