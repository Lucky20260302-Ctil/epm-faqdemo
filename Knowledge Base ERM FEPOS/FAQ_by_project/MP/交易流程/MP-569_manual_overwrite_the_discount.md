---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "_（Jira 中無 description 內容）_"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-569
resolved: 2022-11-21
fix-version: ""
---

# MP-569: Manual overwrite the discount

## 問題

_（Jira 中無 description 內容）_

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2022-11-21
### Jira Comments (5 則)
**Andrew_Au** (2022-10-11):
Manual overwrite the discount show the wrong price. Please refer the screenshot and video.
**Cy Lau** (2022-10-11):
it should be a known bug as 550, it should be correct price when you go to the next page
The solution would be a lock removal , according to yan ,& joy, it should be a fix applied to some issue.
But will have a release to you if we remove the lock
**Cy Lau** (2022-10-17):
3.20.1-20221017
**Andrew_Au** (2022-10-19):
request select the reason code. the behavior not same as testing POS current setting.
**Andrew_Au** (2022-10-22):
Mpos reason show the reason/not show reason is directly check on the reason table, POS reason the reason/not show is check ->flag setting -> table records.  (Yeung / Sang : Please confirm which setting is correct ? 2 application behavior not the same)

## 相關資訊

- Jira: [MP-569](https://ctil.atlassian.net/browse/MP-569)
- Fix Version: 未記錄
- 解決日期: 2022-11-21
