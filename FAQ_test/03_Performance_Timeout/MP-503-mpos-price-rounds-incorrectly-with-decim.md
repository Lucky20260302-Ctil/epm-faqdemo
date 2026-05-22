---
project: MP
issue_key: MP-503
issue_type: Bug PRD
status: Closed
tags:
- 03_performance_timeout
- faq
- frontend
- mp
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/MP-503
created: '2021-09-23'
resolved: '2021-12-08'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'MP-503: MPOS price rounds incorrectly with decimal places'
---
# MP-503: MPOS price rounds incorrectly with decimal places

## 問題描述

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



## 相關資訊

- **Jira:** [MP-503](https://ctil.atlassian.net/browse/MP-503)
- **解決方式:** Done