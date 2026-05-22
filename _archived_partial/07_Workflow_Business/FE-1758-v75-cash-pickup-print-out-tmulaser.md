---
project: FE
issue_key: FE-1758
issue_type: Improvement
status: Open
tags:
- 07_workflow_business
- faq
- fe
- front-end
- workflow_business
symptom: ''
root_cause: ''
solution: ''
jira_url: https://ctil.atlassian.net/browse/FE-1758
created: '2025-09-29'
resolved: ''
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'FE-1758: V75 Cash Pickup Print Out - TMU/Laser'
---
# FE-1758: V75 Cash Pickup Print Out - TMU/Laser

## 問題描述

Create Cash Pickup - [Cash Pick up Header / Cash Pick up Detail]
b. Write PCD ("14")
c. Print Cash Pickup Memo (tblconfig.PRINTPICKUPREPORT='Y') 
d. Cash Balance Enquiry - Show / Print Till  Cash Pickup Report (Dbtran.sdf)
e. Cash Balance Enquiry - Show / Print All Till(s)  Cash Pickup Report (dbHist.SSE)
f. Till Day End / Re-do Day End- Print Till  Cash Pick up Report (Dbtran.sdf)
g. Consolidated Day End/Re-do Consolldated Day End - Print Consolidated Till(s)  Cash Pick up Report (till's dbtrans.sdf)



## 相關資訊

- **Jira:** [FE-1758](https://ctil.atlassian.net/browse/FE-1758)