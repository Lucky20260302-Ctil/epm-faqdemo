---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "1.店铺在2024-11-11重装过POS后，每次打开POS的时候会有如下截图的小提示，点击‘确认’可以跳过。请检查确认如何能取消掉下面的小弹窗？是什么地方导致的这个issue？"
root-cause: "待提取"
solution: "### Jira Comments (4 則)"
jira: FE-1561
resolved: 
fix-version: ""
---

# FE-1561: RIN01416846 - OCF26 Till0 Open the POS will show the "TBLSALADY - 字段大小过长" this error

## 問題

1.店铺在2024-11-11重装过POS后，每次打开POS的时候会有如下截图的小提示，点击‘确认’可以跳过。请检查确认如何能取消掉下面的小弹窗？是什么地方导致的这个issue？
Troubleshooting in my side:
1.repaired POS program and reg reg,Issue still.
2.Checked the Tblsalady table in Dbsse and Dbtrans.sdf,Not found any abnormal.
3.Checked the AdoService log found bellow error.What’s this error?

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (4 則)
**Sang** (2024-11-15):
@@Tovi Wang What version?
**Tovi Wang** (2024-11-15):
@@Sang POS version: 72.0221.0102
**Tovi Wang** (2024-11-15):
@@Sang I has uploaded 2024-11-14 logs to OneDrive.Please help to check and fixed it.Thanks!
**Sang** (2024-11-15):
@@Tovi Wang @@Cy Lau  Is this v72 use vb6 print and tblsalady table contain double-byte characters

## 相關資訊

- Jira: [FE-1561](https://ctil.atlassian.net/browse/FE-1561)
- Fix Version: 未記錄
- 解決日期: 未記錄
