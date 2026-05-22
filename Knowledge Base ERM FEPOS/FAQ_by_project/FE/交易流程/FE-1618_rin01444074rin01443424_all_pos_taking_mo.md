---
tags: [faq, fe, 交易流程]
component: "Front End v750.01R01A"
symptom: "In PRC region, after upgraded to V75, user submitted that it need to spend more than 40s in printing"
root-cause: "待提取"
solution: "### Jira Comments (6 則)"
jira: FE-1618
resolved: 
fix-version: ""
---

# FE-1618: [RIN01444074\RIN01443424]-All POS taking more than 30-40s to print a sales memo 

## 問題

In PRC region, after upgraded to V75, user submitted that it need to spend more than 40s in printing sales memo sometimes.
I checked the T9 logs and found that it cost one and a half mins between ‘save memo’ and 'compleate transaction', and no error popped up.
[20250119 15:45:59 -4723]: Save Memo STart:S.OCF33.30026006 : Avail V.  Memory : 140731742.765
[20250119 15:47:21 -5150]: CompleteTransaction.End()
[20250119 15:47:21 -5160]: Save Memo End:S.OCF33.30026006 : Avail V.  Memory : 140731768.496
[20250119 15:47:21 -5160]: Save Memo [30026006]: Success
Could you please help to check why it cost such more time?
In fact, in another memo, it  cost only 2s.
[20250119 15:58:28 -2605]: Save Memo STart:S.OCF33.30026007 : Avail V.  Memory : 140731754.996
[20250119 15:58:30 -8608]: CompleteTransaction.End()
[20250119 15:58:30 -8618]: Save Memo End:S.OCF33.30026007 : Avail V.  Memory : 140731747.394
[20250119 15:58:30 -8618]: Save Memo [30026007]: Success
The logs has been uploaded onto onedrive:[20250124_RIN01443424](https://ctil00046-my.sharepoint.com/:f:/g/personal/jason_wu_ctil00046_onmicrosoft_com/EtO4HyIiawFGrQkEPJg6CwEBVhgtUWVJdbNRLBwSFv_uEg?e=eHDfuR)

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (6 則)
**Sang** (2025-01-27):
@@pierre.shi
Upsert Member used 88 sec
**pierre.shi** (2025-02-06):
Hi @@Sang  there is an error 9999 from api reponse.
what may cause this issue?
**Cy Lau** (2025-02-09):
The error 9999 is owing to the restriction of the design with passing 
Response:{"successful":false,"data":{"errorType":"Exception","errorCode":9999,"errorMessage":"[\"The column '***vip_expiry_date***' is not allowed to update directly. You can update it by upgrade 'vip_type'.\",\"***vip_no_edm*** only accept 'Y'/'N'/NULL, given '0' !!!\"]","errorDetails":null,"errorDisplayMessage":"","errorDesc":"","message":"[\"The column 'vip_expiry_date' is not allowed to update directly. You can update it by upgrade 'vip_type'.\",\"vip_no_edm only accept 'Y'/'N'/NULL, given '0' !!!\"]"}}
vip_expiry_date:  shall not be updated.
vip_no_edm : invalid value from API
@@Anson Cheung  any updates for the POS_API upsert member ?
**Anson Cheung** (2025-02-10):
@@Cy Lau the value ‘1'/'0' of vip_no_edm/vip_no_dm/vip_no_phone/vip_no_sms from acxiom profile will be converted to ‘Y'/’N' in BEAPI v1.6.19, 
and vip_expiry_date direct update is allowed in BEAPI v1.6.20 by setting dbconfig beapi_allow_update_vip_expiry_date = 'Y'
**Andrew_Au** (2025-04-08):
@@pierre.shi Please update the ticket status
**pierre.shi** (2025-04-08):
Hi @@Andrew_Au please help to close the ticket.

## 相關資訊

- Jira: [FE-1618](https://ctil.atlassian.net/browse/FE-1618)
- Fix Version: 未記錄
- 解決日期: 未記錄
