---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "2025-01-11 CN update a large master file and price "
root-cause: "待提取"
solution: "### Jira Comments (10 則)"
jira: BE-981
resolved: 
fix-version: ""
---

# BE-981: [CS-1326]RIN01441036] - CN Zlog issue again on 2025-01-11

## 問題

2025-01-11 CN update a large master file and price 
Cause zlog generate to 88 up
又有zlog issue
Since they already changed to internal end point last wed
Should not have such issue

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (10 則)
**Tovi Wang** (2025-01-14):
@@Cy Lau log here,please check.
**Cy Lau** (2025-01-15):
88+ files (98?), sending to OSS with del if exist
about 1-2 secords per action
each file send to all tills in stores
@@Tovi Wang  Please help to check the polling point (storecode_____tillno) folder number
**Tovi Wang** (2025-01-15):
@@Cy Lau total 885 polling folders.
**Cy Lau** (2025-01-16):
with knowing 885 as polling folders,
98 files to be deployed / re-deployed:
For a happy flow :
885 * 98 * (1/2/3) seconds :
at least needs 1 day 0 hours 5 minutes 30 seconds to finish the deployment
**Tovi Wang** (2025-01-16):
@@Cy Lau  I found a error  “System.Net.WebException: The remote server returned an error: (403) Forbidden.” in FatalFile.log for your reference.
**Cy Lau** (2025-01-16):
i think shall be wrong config and it is 11-Jan already
**Andrew_Au** (2025-02-24):
@@Tovi Wang Can I close the ticket ?
**Andrew_Au** (2025-03-26):
@@Tovi Wang @@pierre.shi  Please update the ticket status
**Andrew_Au** (2025-04-08):
@@Tovi Wang @@pierre.shi  Please update the ticket status
**Tovi Wang** (2025-04-08):
@@Andrew_Au  We has updated the RCA to Coach team.Please closed this one.

## 相關資訊

- Jira: [BE-981](https://ctil.atlassian.net/browse/BE-981)
- Fix Version: 未記錄
- 解決日期: 未記錄
