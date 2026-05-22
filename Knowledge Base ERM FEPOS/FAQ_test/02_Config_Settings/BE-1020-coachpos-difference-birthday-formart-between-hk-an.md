---
project: "BE"
issue_key: "BE-1020"
issue_type: "Bug QA"
status: "Closed"
tags: [faq, be]
jira_url: "https://ctil.atlassian.net/browse/BE-1020"
created: "2025-03-03"
resolved: "2025-04-29"
fix_version: ""
components: [MPOS]
category: "02_Config_Settings"
---

BE-1020: Difference birthday formart between HK and CN

| 問題
Coach POS 在香港（HK）與中國（CN）顯示會員生日格式不一致：HK 僅顯示月份（如「July」），CN 顯示完整日期（如「2021/07/06」），使用者無法確認哪種格式為正確設定。

| 根因
生日顯示格式由 tblconfig 中的 ShowFullBirthday 參數控制。設定為 'Y' 時顯示完整日期格式 'yyyy/MM/dd'，設定為 'N' 時僅顯示月份。HK 與 CN 的此參數設定不同導致格式差異。

| 解法
依各區域需求調整 tblconfig.ShowFullBirthday 參數：若需顯示完整生日設為 'Y'（yyyy/MM/dd），若僅顯示月份則設為 'N'。此為 POS 前端設定，無需程式修改。

| 相關資訊
- Jira: [BE-1020](https://ctil.atlassian.net/browse/BE-1020)
- 解決日期: 2025-04-29
- 組件: MPOS
- 負責人: Sang
- 附件: [image-20250303-101748.png](https://ctil.atlassian.net/rest/api/3/attachment/content/52400)