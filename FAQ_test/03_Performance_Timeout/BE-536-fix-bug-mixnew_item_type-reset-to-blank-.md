---
project: BE
issue_key: BE-536
issue_type: Bug PRD
status: Closed
tags:
- 03_performance_timeout
- backend-(chainstoreplus-7.0)
- be
- faq
- performance_timeout
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/BE-536
created: '2022-01-28'
resolved: '2022-01-28'
fix_version: ''
components: []
has_images: false
category: 03_Performance_Timeout
category_label: 效能與超時
quality: partial
title: 'BE-536: Fix bug “mixnew_item_type” reset to blank after Product Table has ended lookup [RIN00913903]'
---
# BE-536: Fix bug “mixnew_item_type” reset to blank after Product Table has ended lookup [RIN00913903]

## 問題描述

 

Update of BE programs (HKJC,A+O,COACH,bash,AIGLE

I have updated the programs in \\ds411\csms60\delivery\be\update.be7.220121  for HKJC/A+O/COACH/bash/AIGLE.

 

**Issue Fix/ Enhancement**

- Update prj_mx6008.dll program

- SOG ticket: RIN00913903

- Fix bug “mixnew_item_type” reset to blank after Product Table has ended lookup

- Issue Detail:

- In Mix & Match Maintenance MX6008, the Product type is - ALL

- Once clicking Problem Table/Member Table for selection

- Exit with no change

- Product Type will change from “-All Type” to “D-Discount Item Only”

- Reproduce Step:

- In Mix & Match Maintenance MX6008

- Click on either one promotion (e.g. DISC 10%_E) and go to “Conditions” Tab

- Product Type is -All Type

- Click any table (e.g. Product Table/Member Table/Card Promotion)

- Exit table without any selection/change

- Product Type will be incorrect changed from “-All Type” to “D-Discount Item Only” automatically



## 相關資訊

- **Jira:** [BE-536](https://ctil.atlassian.net/browse/BE-536)
- **解決方式:** Done