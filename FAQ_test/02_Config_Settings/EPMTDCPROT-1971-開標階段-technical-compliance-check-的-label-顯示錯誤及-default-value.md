---
project: EPMTDCPROT
issue_key: EPMTDCPROT-1971
issue_type: ''
status: ''
tags:
- 02-config-settings
- 02_config_settings
- epm
- epmtdcprot
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-1971
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 02_Config_Settings
category_label: 配置與設定
quality: complete
---

EPMTDCPROT-1971: 開標階段 Technical Compliance Check 的 label 顯示錯誤及 default value 預設為 disqualify

## 症狀

開標階段有多個 label 問題：(1) Upload sample e-form 顯示「NotReply」應改為「No Response」與 technical compliance check 一致；(2) User update clean version 時系統也顯示錯誤 label；(3) Technical compliance check form 的 compliance 狀態預設全部為 disqualify，應預設為空白。

## 根因

每個 supplier 的 compliance default value 皆設為 false，導致系統預設選取 disqualify。Benson Xu 確認問題後指出：「每一個supplier的compliance的default value都是false，所以默認就選了disqualify了。麻煩william把originalTechnicalFolderZip有數據的compliance的default value set 為 null」。

## 解法

(1) 修正 label 顯示：將「NotReply」改為「No Response」；(2) 將 compliance 的 default value 從 false 改為 null，使 technical compliance check form 預設為空白而非 disqualify。

## 相關資訊

- Jira: [EPMTDCPROT-1971](https://ctil.atlassian.net/browse/EPMTDCPROT-1971)
- Fix Version: 未標註
- 分類: 設定與配置
- 專案: EPMTDCPROT
