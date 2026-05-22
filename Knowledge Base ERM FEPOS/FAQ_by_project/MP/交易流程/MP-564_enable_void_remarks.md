---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "cannot enable void remarks"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-564
resolved: 2024-07-28
fix-version: ""
---

# MP-564: Enable Void remarks

## 問題

cannot enable void remarks
-

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-07-28
### Jira Comments (6 則)
**Cy Lau** (2022-10-07):
API config delivery - @@Cy Lau ::check_mark:: 20221011
UI Remarks - @@Daniel Leung
**Cy Lau** (2022-10-13):
@@Andrew_Au
Please advise for the remark should be
1) single line with max 40 chars
OR
2) 9 lines with 40 chars by control
**Daniel Leung** (2022-10-13):
@@Andrew_Au
The current behavior of void remarks in Till0 will only concatenate all linebreak and save as a single string to db.
Is it necessary to enhance the multi-line remarks feature?
**Andrew_Au** (2022-10-19):
is blocked by cannot complete issue the sales memo
**Andy Ko** (2022-11-09):
after inputting the remarks into mpos, I am unable to see my full remark in the preview window.
**Cy Lau** (2022-11-09):
@@Andy Ko
Please define or explain "**Preview Window**"

## 相關資訊

- Jira: [MP-564](https://ctil.atlassian.net/browse/MP-564)
- Fix Version: 未記錄
- 解決日期: 2024-07-28
