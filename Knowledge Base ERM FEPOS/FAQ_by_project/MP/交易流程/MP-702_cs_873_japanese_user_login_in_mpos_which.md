---
tags: [faq, mp, 交易流程]
component: "MPOS, MPOS API"
symptom: "The issue  caused by User input Japanese when logining MPOS,But login failed.And the failed login re"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-702
resolved: 2024-06-07
fix-version: ""
---

# MP-702: [CS-873] Japanese user login in MPOS which caused posting error

## 問題

The issue  caused by User input Japanese when logining MPOS,But login failed.And the failed login records need also posting.
Workaround:
1.Contact User NOT input Japanese when logining MPOS.
2.Long workaround:Need to enhance program to block Japanese when user logining MPOS.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-06-07
### Jira Comments (3 則)
**Joy Li** (2024-05-28):
@@Daniel Leung  @@Cy Lau  Please confirm me the change detail for this case.
ONly MPOS  IPA?
**Joy Li** (2024-06-04):
please help to handle and release on June 5. ETA to COACH is June 7
**Joy Li** (2024-06-07):
Test Case:

## 相關資訊

- Jira: [MP-702](https://ctil.atlassian.net/browse/MP-702)
- Fix Version: 未記錄
- 解決日期: 2024-06-07
