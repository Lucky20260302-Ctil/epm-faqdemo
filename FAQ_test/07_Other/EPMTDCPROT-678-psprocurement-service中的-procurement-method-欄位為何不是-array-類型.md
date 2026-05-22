---
project: EPMTDCPROT
issue_key: EPMTDCPROT-678
tags: [faq, epm, epmtdcprot, 07-other]
jira_url: "https://ctil.atlassian.net/browse/EPMTDCPROT-678"
category: 07_Other
category_name: "其他"
---

EPMTDCPROT-678: 

| 問題

PS（Procurement Service）中的 Procurement Method 欄位為何不是 Array 類型，導致使用者只能選擇一個項目？

| 根因

Procurement Method 欄位的資料型別定義為單一值（Single Value）而非陣列（Array），導致前端只能綁定單選元件，使用者無法多選採購方式。

| 解法

將 Procurement Method 欄位的資料型別從單一值修改為 Enum（多選列舉型別），使前端可使用多選元件，允許使用者同時選擇多個採購方式。

| 相關資訊

- Jira: [EPMTDCPROT-678](https://ctil.atlassian.net/browse/EPMTDCPROT-678)
- Fix Version: 未標註
- 分類: 其他
- 專案: EPMTDCPROT
