---
project: FE
issue_key: FE-1502
issue_type: SOW
status: Closed
tags:
- 04_data_sync
- data_sync
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1502
created: '2024-09-17'
resolved: '2024-11-15'
fix_version: ''
components: []
has_images: false
category: 04_Data_Sync
category_label: 資料同步
quality: partial
title: 'FE-1502: RTM PIPL Localization'
---
# FE-1502: RTM PIPL Localization

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

- **Jira:** [FE-1502](https://ctil.atlassian.net/browse/FE-1502)
- **解決方式:** Done