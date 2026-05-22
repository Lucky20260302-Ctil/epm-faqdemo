---
project: FE
issue_key: FE-820
issue_type: Bug PRD
status: Closed
faq_score: 7.0
faq_category: 07_Workflow_Business
faq_category_label: 流程與業務
tags: [faq, fe, workflow_business, enquiry, sales]
jira_url: "https://ctil.atlassian.net/browse/FE-820"
created: 2020-11-03
resolved: 2022-06-15
resolution: Done
has_images: False
---

# FE-820: Ticket 2020152 Sales memo net amt not match with payment amount

> **類型:** Bug PRD | **狀態:** Closed
> **分類:** 流程與業務 | **FAQ 分數:** 7.0
> **解決日期:** 2022-06-15
> **負責人:** Sang
> **組件:** Enquiry, Sales

## 問題描述

This issue is related to the Give Away and the MM coupon event below.

The mask items were separated when trigger the Giveaway event. Eventually , POS has assigned the wrong coupon discount to the item adjustment(INVTRX_MIXCOUPONREF_NET_AMT) after completed the payment.  

DB copied in \\172.16.183.201\localuser\support\20201030\BPSHKG24

Thanks.



## 相關資訊

- **Jira:** [FE-820](https://ctil.atlassian.net/browse/FE-820)
- **解決方式:** Done