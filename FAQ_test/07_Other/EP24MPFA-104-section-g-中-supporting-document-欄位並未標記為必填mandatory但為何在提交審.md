---
project: EP24MPFA
issue_key: EP24MPFA-104
issue_type: ''
status: ''
tags:
- 07-other
- 07_other
- ep24mpfa
- epm
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EP24MPFA-104
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 07_Other
category_label: 其他
quality: complete
---

EP24MPFA-104: 

## 症狀

Section G 中 Supporting Document 欄位並未標記為必填（Mandatory），但為何在提交審批時系統卻提示為必填？

## 根因

必填驗證邏輯與 UI 標記不一致：當使用者選擇「Not applicable」時，文件上傳應為非必填，但系統的提交驗證仍將其視為必填。Jocelynml_Chan 確認正確邏輯應為：選擇「Yes」時才為必填（Mandatory），選「Not applicable」時不應觸發必填驗證。根因為 yes/no 條件判斷反轉。

## 解法

修正 Section G Supporting Document 的必填驗證邏輯，使其與 UI 標記一致：僅在選擇「Yes」時才要求必須上傳文件，選擇「Not applicable」時不應觸發必填驗證。

## 相關資訊

- Jira: [EP24MPFA-104](https://ctil.atlassian.net/browse/EP24MPFA-104)
- Fix Version: 未標註
- 分類: 其他
- 專案: EP24MPFA
