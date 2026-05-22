---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "Coach team callout BDO receive incomplete sales amt data for bellow 2 sales memo."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1046
resolved: 2026-05-05
fix-version: ""
---

# BE-1046: [CS-1396]MY E-Invoice API data issue

## 問題

Coach team callout BDO receive incomplete sales amt data for bellow 2 sales memo.
After checked the log,I just only find the first item sales data in log,But missing the second item sales data.Please help to double check and confirm the RCA?Thanks!
1. 
OCF77-20229270 2025-03-18
OCF79-10119181 2025-03-20
2.OCF77-20229270 2025-03-18
3.OCF79-10119181 2025-03-20

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-05-05
### Jira Comments (7 則)
**Tovi Wang** (2025-04-08):
@@Anson Cheung  I remember there are interface enhance in Jira [🔗](https://ctil.atlassian.net/browse/BE-990) and the enhancement is already deployed to PRD.Could you help to double check and confirm if it is the same RCA with before?Log for your reference.Thanks!
**Anson Cheung** (2025-04-09):
@@Tovi Wang This case has same cause with  [🔗](https://ctil.atlassian.net/browse/BE-990). By config, program scans the memo not within 10 mins, but the posting is done after 18 mins. I suggest setting the **scanDelayMin **config to 20.
**Tovi Wang** (2025-04-09):
@@Anson Cheung Many Thanks for your double confirm.Can I directly updating the **scanDelayMin **config to 20 in AWS app server after Coach team approved it?
**Anson Cheung** (2025-04-09):
@@Tovi Wang yes
**Tovi Wang** (2025-04-10):
Sorry @@Anson Cheung,I have one more question.第一个 item 和第二个 item posting到DB的时间几乎一致，相差不到1秒。以这个sample来看，scanning job是从什么时候开始到什么时候结束呀？Coach Team 担心即使把**scanDelayMin** setting改到20，如果后面有的单子30分钟之后才posting到DB,会不会可能又发生类似的issue?谢谢！
**Anson Cheung** (2025-04-10):
@@Tovi Wang
scanning time is around 19:35 - 19:36. Note that the log time is 19:36:03.9085 doesn't mean all the records within this time always be scanned, there may be a latency. 
And yes, if the posting time is posted at 30 min after the jouinv create time, same issue will be occurred. You may discuss with Coach team to arrange a appropriate delay time.
**Automation for Jira** (2026-05-05):
Issue has been created since
Days since: 391
Week since : 55
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [BE-1046](https://ctil.atlassian.net/browse/BE-1046)
- Fix Version: 未記錄
- 解決日期: 2026-05-05
