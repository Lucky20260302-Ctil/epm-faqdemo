---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "1."
root-cause: "待提取"
solution: "### Jira Comments (5 則)"
jira: BE-1214
resolved: 
fix-version: ""
---

# BE-1214: [INC3319642] PRC Posting OSS_B delay

## 問題

1.
2025-11-27 09:25:52 SOG callout OSS_B delay issue.
use csdata11_70
select top 100 * from pstlog with (nolock) where pstlog_date = '2025-11-27' and pstlog_node = 'OSS_B'
order by pstlog_date desc, pstlog_time DESC
select * from sqlpcdossb
---update sqlpcdossb set sqlpcd_post = 'E'  
where sqlpcd_post_ref like 'acp20251127091928.OCF85___0%'
2.Checked pstlog table found that the issue caused by stuck file acp20251127091928.OCF85___0 with follow error:
<span style="color:#ff5630">83	20251127	091003	OCF85	0	z25112606	27	 Load Data Failure</span>
<span style="color:#ff5630">已成功与服务器建立连接，但是在登录前的握手期间发生错误。 (provider: Shared Memory Provider, error: 0 - 管道已结束。)</span>	
I also can find follow error in PCDBAK file.@@Sang Please help to further checking the RCA.
CC @@Joy Li @@pierre.shi

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (5 則)
**Tovi Wang** (2025-11-28):
2025-11-27 OCF85 till0 FE logs here:
**Tovi Wang** (2025-12-01):
@@Sang Please help to take a look this Jira ticket RCA.Where come from for The PCD file error?
**Automation for Jira** (2025-12-02):
Issue has been created since
Days since: 4
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Sang** (2025-12-02):
@@Tovi Wang @@Joy Li 2025/11/27 09:10:03-09:10:08 CSPLUS try to update Z-files to local database (dbMas SSE), but fail to connect DBmas, and connecting resumed normal 09:10:08.  This PCD error record is one of z-update file failure record due to unknown issue . Since everything resume normal w/o re-start CSPLUS or window, the problem is not due to CSPLUS program or setting. It may due to network or other unknown environment impact.  Recommend to continuous monitor CSPLUS is operating under stable environment.
**Tovi Wang** (2025-12-02):
@@Sang  Thanks for your details update,Understood your point.
In our opinious,The Chinese error info should not write into PCD file,Because the Chinese error info can stuck the posting job.So could you help to removed the Chinese error info from PCD file?
The Chinese error info write into T9 log is OK.

## 相關資訊

- Jira: [BE-1214](https://ctil.atlassian.net/browse/BE-1214)
- Fix Version: 未記錄
- 解決日期: 未記錄
