---
project: "MP"
issue_key: "MP-563"
issue_type: "Bug QA"
status: "Closed"
tags: [faq, mp]
jira_url: "https://ctil.atlassian.net/browse/MP-563"
created: "2022-10-01"
resolved: "2024-01-22"
fix_version: ""
components: [MPOS]
category: "05_Error_Exception"
---

MP-563: New member cannot online update BE

| 問題
新會員無法線上更新後端（BE），出現 API 資料格式錯誤。

| 根因
測試環境的 POS region 在 Windows registry 中設定錯誤，導致 API 資料格式不符。

| 解法
修正 Windows registry 中的 POS region 設定為正確值。

| 相關資訊
- Jira: [MP-563](https://ctil.atlassian.net/browse/MP-563)
- 解決日期: 2024-01-22
- 組件: MPOS
- 負責人: Cy Lau
- 附件: [image-2022-10-06-09-37-25-336.png](https://ctil.atlassian.net/rest/api/3/attachment/content/40482) | [image-2022-10-10-11-35-18-799.png](https://ctil.atlassian.net/rest/api/3/attachment/content/40485)