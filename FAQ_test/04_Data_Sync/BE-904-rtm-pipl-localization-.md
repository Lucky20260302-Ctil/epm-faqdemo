---
project: BE
title: "BE-904: RTM PIPL Localization"
issue_key: BE-904
issue_type: SOW
status: Closed
faq_score: 5.0
faq_category: 04_Data_Sync
faq_category_label: 資料與同步
tags: [faq, be, data_sync, data-interface]
jira_url: "https://ctil.atlassian.net/browse/BE-904"
created: 2024-09-17
resolved: 2024-11-15
resolution: Done
has_images: False
---

# BE-904: RTM PIPL Localization 

## 問題描述

- RTM BJCH will migrate from HK server to China server.

- China should have its own MCRM (CN MCRM) for Membership data management.

- For Beijing Member (HKMemberIndicator = N), only profiles with consent to send data to HK will be included.

- HK MCRM: will filter the (‘Beijing’ and (IsConsentToHKInMCRM !=Y or IsConsentToThirdParty !=Y or IsConsentToProcessSensitiveInfo !=Y ))

- Display “Is Consent to HK” indicator in POS Member Profile screen. Refer to appendix W for the screen layout.

- The BJCH transaction data will be filtered out non-consent member to send data to HK Interim Datamart and End State Datamart. Refer to the System Interface Specification for the details.

- In addition to sending BJCH transaction data, a new interface to sending aggregate consent/non-consent member data in Json to End State Datamart. Refer to the System Interface Specification for the details.

- Add a Monthly Aggregate Turnover to summarize monthly turnover by total, consent and non-consent turnover sending to End State Datamart. 



## 相關資訊

- **Jira:** [BE-904](https://ctil.atlassian.net/browse/BE-904)
- **解決方式:** Done