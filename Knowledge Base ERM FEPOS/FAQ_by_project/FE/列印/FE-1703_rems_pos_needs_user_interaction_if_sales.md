---
tags: [faq, fe, 列印]
component: "Receipt Printing"
symptom: "Needs user interaction when A4 Sales Memo print more than one page. But Transfer Note does not have "
root-cause: "待提取"
solution: "### Jira Comments (6 則)"
jira: FE-1703
resolved: 
fix-version: ""
---

# FE-1703: REMS POS needs user interaction if sales memo print more than one page

## 問題

Needs user interaction when A4 Sales Memo print more than one page. But Transfer Note does not have such issue.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (6 則)
**Bobby** (2025-05-27):
1. 
The error message seems the printer is enabled manual print double side feature. I have checked the printer driver setting.
“Print on both sides manually” setting has already set to ‘None’. Pannie said she has tried to print multiple pages from Notepad to the printer, but it does not show this dialogue.
**Bobby** (2025-05-27):
You can select the HVLEVM-40324712 on 15/04/2025 for testing. When you print/reprint this memo, it will prompt a “Print on both side instruction” dialogue to ask user to resinsert the stock of pages into the input tray and press the printer button. to continue print the next page. The user said that the Transfer Note does not have issues when it exceeds one page.
**Sang** (2025-06-03):
@@Bobby @@Cy Lau
1.
**Andrew_Au** (2025-09-30):
@bobby Please update the status
**Automation for Jira** (2025-10-08):
Issue has been created since
Days since: 133
Week since : 19
Issue due date difference
Days since : 131
Weeks since: 18
**Andrew_Au** (2025-10-08):
@bobby Please update the status

## 相關資訊

- Jira: [FE-1703](https://ctil.atlassian.net/browse/FE-1703)
- Fix Version: 未記錄
- 解決日期: 未記錄
