---
tags: [faq, fe, 會員_api]
component: "API"
symptom: "Coach team callout there are so many  400,500,503 on 2025-04-06"
root-cause: "待提取"
solution: "### Jira Comments (4 則)"
jira: FE-1695
resolved: 
fix-version: ""
---

# FE-1695: [CLC2-789] Investigation on CJ LINE's Binding Issue of the POS API Create Member Failure

## 問題

Coach team callout there are so many  400,500,503 on 2025-04-06
While binding with an SA on Production, our attempts failed by receiving the **POS API Create Member Failure (503 Error)** at the following times. Some screenshots are provided below.
|  |  |  |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (4 則)
**Tovi Wang** (2025-05-15):
@@Cy Lau Please help to check. 04-06 Web22 BEAPI & IIS log for your further checking.
CC @@Joy Li
**Joy Li** (2025-05-21):
@@Anson Cheung  @@Cy Lau
event id  = f3b050fb1cf842269137a858143dccb8
Anson, May i know if the error “DB is locked“ is come from DB ?
**Anson Cheung** (2025-05-22):
@@Joy Li this message is caused by the sqlite file being locked when logging, there is an enhancement in later version.
**Andrew_Au** (2025-06-05):
@@Tovi Wang @@pierre.shi Please update the ticket status

## 相關資訊

- Jira: [FE-1695](https://ctil.atlassian.net/browse/FE-1695)
- Fix Version: 未記錄
- 解決日期: 未記錄
