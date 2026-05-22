---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "V67 and V7 both can be worked this format like mastconv.dat.01 , mastconv,dat.02 , mastconv.dat.03…."
root-cause: "待提取"
solution: "### Jira Comments (2 則)"
jira: BE-1152
resolved: 
fix-version: ""
---

# BE-1152: Ticket no. 2025059 v67 pos cannot use mastconv files to update pos data

## 問題

V67 and V7 both can be worked this format like mastconv.dat.01 , mastconv,dat.02 , mastconv.dat.03….and so on  as those data are exported from cs2000 backend .
But after migration ,  using CSP , the file format is changed like mastconv.dat.1 , mastconv.2 , mastconv.3 ….. mastconv.dat.100 , mastconv.dat.101 ….. ,
<span style="color:#ff5630">**>> Please check and confirm if we can generate the mastconv with mastconv.dat.01 , mastconv,dat.02 , mastconv.dat.03**</span>

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (2 則)
**Jerry Wong** (2025-07-29):
Release:
[\\DS411\csms60\delivery\imx\di9008-2025-07-29](file://DS411/csms60/delivery/imx/di9008-2025-07-29)
Note:
- 
- 
-
**Andrew_Au** (2025-10-08):
@@Joy Li @@Angela Chan Please update the status

## 相關資訊

- Jira: [BE-1152](https://ctil.atlassian.net/browse/BE-1152)
- Fix Version: 未記錄
- 解決日期: 未記錄
