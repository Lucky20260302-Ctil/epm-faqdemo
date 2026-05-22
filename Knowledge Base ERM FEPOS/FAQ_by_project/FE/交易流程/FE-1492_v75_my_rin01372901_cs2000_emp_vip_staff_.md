---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "<span style='color:#ff5630'>RCA:</span>"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1492
resolved: 2024-09-08
fix-version: ""
---

# FE-1492: V75_MY_RIN01372901_CS2000 EMP VIP staff info does not update in FE [cs-1112]

## 問題

<span style="color:#ff5630">RCA:</span>
<span style="color:#ff5630">If ONLINEMEMBERENQUIRY = Y (such as KSG, KMY.....), the program fail to update member data from zlog / mastconv.dat file.</span>
<span style="color:#ff5630">Program change is request to handle the case of EMP member.</span>
Temp workaround:
1.Firstly,Need to disable ONLINEMEMBERENQUIRY,set the config setting is 'N'.
2.Secondly,update new Zlog file or reimport Mastconv file for issue tills.
3.Finally,Need to enable ONLINEMEMBERENQUIRY,set the config setting is 'Y'.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-09-08
### Jira Comments (1 則)
**Sang** (2024-08-29):
1.

## 相關資訊

- Jira: [FE-1492](https://ctil.atlassian.net/browse/FE-1492)
- Fix Version: 未記錄
- 解決日期: 2024-09-08
