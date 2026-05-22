---
project: FE
issue_key: FE-1933
issue_type: Task
status: Closed
tags:
- 05_error_exception
- error_exception
- faq
- fe
- front-end
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-1933
created: '2026-04-17'
resolved: '2026-04-17'
fix_version: ''
components: []
has_images: false
category: 05_Error_Exception
category_label: 報錯與異常
quality: partial
title: 'FE-1933: [CS-2413] Issue_PRC_INC3527055_Posting  OSS_A/ OSS_B/ OSS_C file time delay'
---
# FE-1933: [CS-2413] Issue_PRC_INC3527055_Posting  OSS_A/ OSS_B/ OSS_C file time delay

## 問題描述

**Issue RCA:**

- During the FE POS day-end process, day-end records (by till) are posted to the BE day-end related tables (dayendh and dayendp).

- As part of this posting, the BE posting task automatically generates the day-end consolidation records in the same BE tables and performs the consolidation calculations.

- In parallel, FE POS Till 0 also generates and uploads Till 0 and consolidation day-end records.

- This results in a duplicate error when the consolidation day-end records are posted.

- While this duplicate error does not impact day-end checking or data correctness, it does negatively affect posting performance, leading to delays.

 

**Enhancement Plan:**

- A new configuration will be introduced in FE POS to control the generation of day-end consolidation records.

- With the new configuration **“dec” – Day End Consolidation** set to **Y**, till 0 will skip the generation of day-end consolidation records (record types **94** and **95**).

- This change will eliminate the duplicate posting scenario and improve overall posting performance.



## 相關資訊

- **Jira:** [FE-1933](https://ctil.atlassian.net/browse/FE-1933)
- **解決方式:** Done