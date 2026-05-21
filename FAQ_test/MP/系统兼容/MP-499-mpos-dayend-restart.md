---
tags: [faq, MP, bug]
component: "MPOS"
symptom: "When FE POS does day-end while MPOS sits idle on login page, MPOS continues showing old POS date and till number instead of updating"
root-cause: "MPOS had no mechanism to detect that POS date had changed after day-end. The shop config was cached and never refreshed until manual restart."
solution: "MPOS now detects POS date changes and forces a restart with error message, ensuring shop config is refreshed. Fixed in v3.13.0."
jira: MP-499
resolved: 2021-09-21
fix-version: "v3.13.0"
---

# MP-499: MPOS Doesn't Restart After POS Day End (Shows Old Date/Till Number)

## 問題

When FE POS does day-end while MPOS sits idle on login page, MPOS continues showing old POS date and till number instead of updating

## 根因

MPOS had no mechanism to detect that POS date had changed after day-end. The shop config was cached and never refreshed until manual restart.

## 解法

MPOS now detects POS date changes and forces a restart with error message, ensuring shop config is refreshed. Fixed in v3.13.0.

## 相關資訊

- Jira: [MP-499](https://ctil.atlassian.net/browse/MP-499)
- Fix Version: v3.13.0
- 解決日期: 2021-09-21
