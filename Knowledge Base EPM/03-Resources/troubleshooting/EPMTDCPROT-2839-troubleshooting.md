---
tags: bug, jira, ext-tdc-uat, uat
component: Tender & RFQ
symptom: "MISC is awarded and PO565910 is created after the approval of award recommendation.  Please advise and fix the followings.  Thanks."
root-cause: ""
solution: "the followings.  Thanks."
jira: EPMTDCPROT-2839
resolved: 2025-11-04
---

# EPMTDCPROT-2839: EPRO-631 [UAT] Incorrect PO data from EPRO to FMS

## 問題

[Link:https://hktdc.atlassian.net/browse/EPRO-631] 
MISC is awarded and PO565910 is created after the approval of award recommendation.  Please advise and fix the followings.  Thanks.
1. PO number and status cannot be found in EPRO

[Image]
[Image]
[Image]
[Image]
1. Tender Response is incorrect for the awarded supplier (i.e. MISC). This leads to wrong no. return offer.
Per the API call, all tenderResponser are “No return”
2. Total Amount is not yet ready. Please advise the log# for totalAmount for each Supplier for PO Creation. Thanks.

[Link:https://hktdc.atlassian.net/browse/EPRO-156] 
1. PO Line Level Attachment Missing
Part name of each attachment in each PO line should be "poLineNumber.<poLineNumber>", such as poLineNumber.1 instead of poLineItem.1
cc [accountid:712020:9bb265cd-da44-4dea-9685-88966572d437]

[Image]
[Image]

## 解法

the followings.  Thanks.

## 相關問題

- [[EPRO-156]]
- [[EPRO-631]]

