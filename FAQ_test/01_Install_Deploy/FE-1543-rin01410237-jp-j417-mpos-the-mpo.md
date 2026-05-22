---
project: FE
issue_key: FE-1543
issue_type: Bug PRD
status: Closed
faq_score: 6.5
faq_category: 01_Install_Deploy
faq_category_label: 安裝與部署
tags: [faq, fe, install_deploy, mpos]
jira_url: "https://ctil.atlassian.net/browse/FE-1543"
created: 2024-10-29
resolved: 
resolution: 
has_images: False
---

# FE-1543: RIN01410237 - JP - J417  - Mpos : the mpos will register double sales

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 安裝與部署 | **FAQ 分數:** 6.5
> **負責人:** Cy Lau
> **組件:** MPOS

## 問題描述

Store user has some problem with mpos
Symptom:

1. the mpos will register double sales

Device & Network Information:
PC name: LPOS
IP Address:[http://172.24.90.211:5631](http://172.24.90.211:5631)

Software Version:
IIS: Cloud
IIS Version:72.0225.0004
MPOS Version:3.25.1

MA000865
MA000864

Troubleshooting:

1. other user's mpos also has appeared this issue
2.only MA000865 receipt was printed out, but user said there are also cases where two duplicate receipts are printed out
3.user will cancel one of the transactions when appear this issue
4.the issue doesn't occur very often, but users want to know if there are any ways to improve it
==================================
用户在mpos做一笔销售时，会出现两笔相同的销售记录，小票单号不一致，纸质小票有时候只会打出来一张（后生成的小票号），也可能会两张一起打出来
其他店员的mpos也出现过类似情况，每当出现这种情况他们都会通过cancel掉一张重复的来对应
虽然这个问题发生的频率不高，但是用户想知道有没有改善方法



## 相關資訊

- **Jira:** [FE-1543](https://ctil.atlassian.net/browse/FE-1543)