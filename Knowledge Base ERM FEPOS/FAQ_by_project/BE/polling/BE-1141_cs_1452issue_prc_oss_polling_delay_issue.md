---
tags: [faq, be, polling]
component: "polling"
symptom: "We have set below workaround, this issue has been solved temporary."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1141
resolved: 2025-07-03
fix-version: ""
---

# BE-1141: [CS-1452]Issue_PRC_OSS Polling Delay issue on 6.3

## 問題

We have set below workaround, this issue has been solved temporary.
1 Skip sending vip member to Zlog
2 move OCF25 to OCF9 to OSS-A
but we still have blow issue.
1 why VIP member still sending to FE by Zlog? we already stop download vip information on 3 years before.
2 too many stx files in OSS folder, you can find there is 4.18 stx files in OSS folder
![](https://jira.tapestry.support/secure/attachment/955051/955051_image-2025-06-04-18-39-29-506.png)
3 too many store in OSS_B, we have found OSS token only has 1 hour effective time.
![](https://jira.tapestry.support/secure/attachment/955050/955050_image-2025-06-04-18-50-31-852.png)
it will expired after 1 hour, if we have too many document waiting for polling, then like OCF88 OCF9 will never get change to finish polling.
4 generate Zlog job will block POSTAB table, on 6.3, we can find below error
![](https://jira.tapestry.support/secure/attachment/955048/955048_image-2025-06-04-19-04-54-143.png)
if POSTAB has been blocked, even not able to be access by SSMS, polling job will also be stopped.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-07-03
### Jira Comments (4 則)
**Sherman tse** (2025-06-30):
\\ds411\share\CYLau\SanyoCloud\UnitTest\20250627 Sanyo Unit Test
**Cy Lau** (2025-07-02):
\\ds411\share\CYLau\BE Compo\Coach\OSSPolling\2025_6_16_1215
adding configs in OSSPolling.exe.config
1. 
2. 
3. 
---
Overview:
**Sherman tse** (2025-07-03):
Verified on qa
test case attached
**Joy Li** (2025-07-03):
released on 2025-07-03 with V70R3.112
<u>**ChainStorePlus v7 Backend Release R3.112**</u>
**Software Release Note**
**Installation Prerequisites**
No CS2000 Back Office Release must be installed before install this release.
**Release Media**
COACH_L4.0.0_V70R3.112.zip
- 
- 
- 
-

## 相關資訊

- Jira: [BE-1141](https://ctil.atlassian.net/browse/BE-1141)
- Fix Version: 未記錄
- 解決日期: 2025-07-03
