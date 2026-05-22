---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "MPOS: When the price is 738.34 and the cash is 739. the original change should be 0.66, after roundi"
root-cause: "待提取"
solution: "### Jira Comments (3 則)"
jira: MP-816
resolved: 
fix-version: ""
---

# MP-816: MPOS NZ Rounding incorrect when change is ending in 6¢

## 問題

MPOS: When the price is 738.34 and the cash is 739. the original change should be 0.66, after rounding, it should be 0.70
Here is the same case in POS:

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (3 則)
**Daniel Leung** (2026-03-05):
new ipa uploaded to [🔗](https://ios.ctil.com/mpos/PreCoach/)  : 3.31.0-20260305.1 @@Joseph_Hu
**Joseph_Hu** (2026-03-05):
@@Daniel Leung @@Sherman tse After upgrade the version, I cannot register the MPOS.
**Daniel Leung** (2026-03-05):
@@Joseph_Hu sorry my bad, Please also update mpos api. Latest version uploaded to \\ds411\share\POS_MPOS_Release\3.31.X\3.31.0-20260305.1b1

## 相關資訊

- Jira: [MP-816](https://ctil.atlassian.net/browse/MP-816)
- Fix Version: 未記錄
- 解決日期: 未記錄
