---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "Email: Please follow up on INC1814512"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1124
resolved: 2022-06-29
fix-version: ""
---

# FE-1124: J812 Cash Denomination missing

## 問題

Email: Please follow up on INC1814512
<span style="color:#ff0000"> Reproduce step:</span>
1. Input Cash Denomination then click F1 confirm
2. Back to Cash Drawer Tender Count Input and re-enter cash denomination.
3. Click F10 Cancel without any change.
4. Then finish the day end process. The cash denomination will missing.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2022-06-29
### Jira Comments (4 則)
**Joy Li** (2022-06-21):
Data Copied at \\172.16.183.201\localuser\support\JIRA_DB\FE-1124\J812_cash_flow\
**Joy Li** (2022-06-22):
Sang release FE package
\\ds411\share\POS_FE_Release\20220622 Coach v720.02R16F Patch
**Joy Li** (2022-06-28):
\\ds411\share\POS_FE_Release\20220622 Coach v720.02R16F Patch
Test Fail:
I expect press Cancel Mean “Exit without change”……
why still keep denomination inside but shown 0 outside.
**Joy Li** (2022-06-29):
Re-test with new program release.
result postive.

## 相關資訊

- Jira: [FE-1124](https://ctil.atlassian.net/browse/FE-1124)
- Fix Version: 未記錄
- 解決日期: 2022-06-29
