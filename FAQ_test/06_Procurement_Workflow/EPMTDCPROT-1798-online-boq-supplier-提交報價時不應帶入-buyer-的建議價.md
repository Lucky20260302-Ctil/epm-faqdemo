---
project: EPMTDCPROT
issue_key: EPMTDCPROT-1798
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
jira_url: https://ctil.atlassian.net/browse/EPMTDCPROT-1798
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: 06_Procurement_Workflow
category_label: 採購流程
quality: partial
---
EPMTDCPROT-1798: Online BOQ supplier 提交報價時不應帶入 buyer 的建議價

| 問題

Online BOQ 的 supplier 在提交報價時，e-form 上已預先填入 buyer 在 PS e-form 設定的數值。Supplier 看到的 BOQ 應為空白自行填寫，不應把 buyer 端設定的建議價帶過來。

| 根因

先前系統設計是將 buyer e-form 的數值直接帶入 supplier 的 BOQ form。根據 Steve 的要求，需取消此 default 建議價功能（Comment by Michael Ren: 「之前是帶過來的，現在按照Steve要求，取消default 建議價」）。

| 解法

取消 BOQ form 的 default 建議價傳遞，讓 supplier 提交報價時看到空白欄位自行填寫。

| 相關資訊

- Jira: [EPMTDCPROT-1798](https://ctil.atlassian.net/browse/EPMTDCPROT-1798)
- Fix Version: 未標註
- 分類: 採購流程
- 專案: EPMTDCPROT
