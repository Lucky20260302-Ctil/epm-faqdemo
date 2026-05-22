---
tags: [faq, mp, 交易流程]
component: "Frontend"
symptom: "When entering decimal places with different payments, the price is rounded up incorrectly."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-503
resolved: 2021-12-08
fix-version: ""
---

# MP-503: MPOS price rounds incorrectly with decimal places

## 問題

When entering decimal places with different payments, the price is rounded up incorrectly.
Incident description:
1)MPOS price change after choosing Payment code
Also fail to edit price on MPOS
HD has troubleshooted:
1) 146.6 will become 146.7 automatically on MPOS
2) No such issue on PC POS
3) 移动支付=164.6, 付款界面跳转164.7，无法修改金额
4) User reset MPOS and issue still
Please see the example video at \\172.16.183.201\localuser\support\20210921\RIN00829121 or attached mp4.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2021-12-08
### Jira Comments (1 則)
**Nathan Chan** (2021-09-27):
Replicate steps have been attached in this thread as mp4.

## 相關資訊

- Jira: [MP-503](https://ctil.atlassian.net/browse/MP-503)
- Fix Version: 未記錄
- 解決日期: 2021-12-08
