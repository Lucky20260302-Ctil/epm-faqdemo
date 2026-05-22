---
tags: [faq, mp, 交易流程]
component: "MPOS"
symptom: "Unable enable open item"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: MP-561
resolved: 2024-07-26
fix-version: ""
---

# MP-561: Enable Open Item

## 問題

Unable enable open item
flag set as below
- 
- 
-

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-07-26
### Jira Comments (7 則)
**Andrew_Au** (2022-10-06):
attatched the FE open item screen.
**Cy Lau** (2022-10-07):
API config delivery - @@Cy Lau::check_mark:: 20221011
UI & flow - @@Cy Lau (Temp / base)
**Cy Lau** (2022-10-11):
SYSCON_OPEN_ITEM_MOD - Enable Open Item
ENABLEOPENITEMBARCODEINPUT - Allow barcode input
ENABLEOPENITEMDESCCHK - Must input product description
**Andrew_Au** (2022-10-19):
Not found the open item button
**Daniel Leung** (2022-10-27):
Added new config enableOpenItemMod, enableOpenItem no longer in use.
Open Item will be shown in SalesMemo sidemenu.
**Cy Lau** (2022-11-10):
@@Andrew_Au Please help to arrange retest
@@Daniel Leung Please check if the barcode option exists
**Andy Ko** (2022-11-15):
confirm for next release

## 相關資訊

- Jira: [MP-561](https://ctil.atlassian.net/browse/MP-561)
- Fix Version: 未記錄
- 解決日期: 2024-07-26
