---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "It can be re-produced by Initial Configuration setup disable Tax function (syscon_Gst_Function=0) an"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1106
resolved: 2022-07-12
fix-version: ""
---

# FE-1106: Fail to write tax information in auto enable tax Rate POS instance. 

## 問題

It can be re-produced by Initial Configuration setup disable Tax function (syscon_Gst_Function=0) and effective tax rate was setup in dbmas.[tblVatRate]. When POS startup and detect effective tax rate in [tblvatRate], it will auto enable tax feature and set DB syscon_Gst_Function=-1. But when write complete transaction to database, POS have not get new gst function enable status and write 0 Gst to DB. This problem remains until POS Re-start.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2022-07-12

## 相關資訊

- Jira: [FE-1106](https://ctil.atlassian.net/browse/FE-1106)
- Fix Version: 未記錄
- 解決日期: 2022-07-12
