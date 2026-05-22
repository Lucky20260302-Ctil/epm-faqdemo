---
project: FE
issue_key: FE-1618
issue_type: Bug DEV
status: Closed
faq_score: 6.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, fe, error_exception, front-end-v750.01r01a]
jira_url: "https://ctil.atlassian.net/browse/FE-1618"
created: 2025-01-26
resolved: 
resolution: 
has_images: False
---

# FE-1618: [RIN01444074\RIN01443424]-All POS taking more than 30-40s to print a sales memo 

> **類型:** Bug DEV | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.0
> **負責人:** Anson Cheung
> **組件:** Front End v750.01R01A

## 問題描述

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



## 相關資訊

- **Jira:** [FE-1618](https://ctil.atlassian.net/browse/FE-1618)