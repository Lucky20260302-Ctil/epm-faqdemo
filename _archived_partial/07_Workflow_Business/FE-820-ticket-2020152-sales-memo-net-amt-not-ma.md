---
project: FE
issue_key: FE-820
issue_type: Bug PRD
status: Closed
tags:
- 07_workflow_business
- enquiry
- faq
- fe
- sales
- workflow_business
symptom: ''
root_cause: ''
solution: Done
jira_url: https://ctil.atlassian.net/browse/FE-820
created: '2020-11-03'
resolved: '2022-06-15'
fix_version: ''
components: []
has_images: false
category: 07_Workflow_Business
category_label: 業務流程
quality: partial
title: 'FE-820: Ticket 2020152 Sales memo net amt not match with payment amount'
---
# FE-820: Ticket 2020152 Sales memo net amt not match with payment amount

## 問題描述

This issue is related to the Give Away and the MM coupon event below.

The mask items were separated when trigger the Giveaway event. Eventually , POS has assigned the wrong coupon discount to the item adjustment(INVTRX_MIXCOUPONREF_NET_AMT) after completed the payment.  

DB copied in \\172.16.183.201\localuser\support\20201030\BPSHKG24

Thanks.



## 相關資訊

- **Jira:** [FE-820](https://ctil.atlassian.net/browse/FE-820)
- **解決方式:** Done