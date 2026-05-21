---
tags: [bug, jira, uat]
component: Tender & RFQ
symptom: "MISC is awarded and PO565910 is created after the approval of award recommendation.  Please advise and fix the followings.  Thanks."
root-cause: ""
solution: "the followings.  Thanks."
jira: EPMTDCPROT-3087
resolved: 2025-11-04
---

# EPMTDCPROT-3087: EPRO-631 [UAT] Incorrect PO data from EPRO to FMS

## 問題

MISC is awarded and PO565910 is created after the approval of award recommendation.  Please advise and fix the followings.  Thanks.
1. PO number and status cannot be found in EPRO

[Image]
[Image]
[Image]
[Image]
1. Tender Response is incorrect for the awarded supplier (i.e. MISC). This leads to wrong no. return offer.
Per the API call, all tenderResponser are “No return”

 
1. Total Amount is not yet ready. Please advise the log# for totalAmount for each Supplier for PO Creation. Thanks.

[Link:https://hktdc.atlassian.net/browse/EPRO-156?focusedCommentId=154903#:~:text=%40Steve%20Wong%20(CTIL)%20%2D%20EXT%20%2C%20per%20checkpoint%20meeting%20on%2015%20Jul%2C%20please%20add%20parameter%20%E2%80%9CtotalAmount%E2%80%9D%20with%20value%20default%20as%20null%2C%20update%20to%20be%20added%20in%20Phase%202.]
 
1. PO Line Level Attachment Missing
Part name of each attachment in each PO line should be "poLineNumber.<poLineNumber>", such as poLineNumber.1 instead of poLineItem.1
cc [accountid:712020:9bb265cd-da44-4dea-9685-88966572d437]

[Image]

## 根因

[Link:https://hktdc.atlassian.net/browse/EPRO-156?focusedCommentId=154903#:~:text=%40Steve%20Wong%20(CTIL)%20%2D%20EXT%20%2C%20per%20checkpoint%20meeting%20on%2015%20Jul%2C%20please%20add%20parameter%20%E2%80%9CtotalAmount%E2%80%9D%20with%20value%20default%20as%20null%2C%20update%20to%20be%20added%20in%20Phase%202.]
1. PO Line Level Attachment Missing
Part name of each attachment in each PO line should be "poLineNumber.<poLineNumber>", such as poLineNumber.1 instead of poLineItem.1
cc [accountid:712020:9bb265cd-da44-4dea-9685-88966572d437]
{   "finalCurrency": "HKD",   "totalPOAmount": 900000,   "hkdEquivalent": 900000,   "status": null,   "attachments": [     "Scoresheet_3Round (6).xlsx"   ],   "poDescription": "631698",   "fmsSupplierId": "25630",   "buyer": "dewang",   "poCreatedDate": "2025-10-15 15:41:22",   "siteName": "BILLING",   "declaration": "Yes",   "purchaseMethod": "Tender",   "exemptionListItem": [],   "purchaseMethodRefNum": "Tender-25/26-ADM-00137",   "noOfTenderersInvited": 7,   "noOfReturnOffer": 3,   "registeredSupplier": [     {       "tenderResponse": "No return",       "reasonForNoOffer": null,       "remark": null,       "supplierName": "MIS Company Limited",       "totalAmount": null     },     {       "tenderResponse": "Disqualified",       "reasonForNoOffer": null,       "remark": null,       "supplierName": "Deloitte Advisory (Hong Kong) Limited",       "totalAmount": null     },     {       "tenderResponse": "No return",       "reasonForNoOffer": null,       "remark": null,       "supplierName": "ITTESTINGDEV20250926",       "totalAmount": null     },     {       "tenderResponse": "No return",       "reasonForNoOffer": null,       "remark": null,       "supplierName": "IDLE CASE",       "totalAmount": null     },     {       "tenderResponse": "No offer",       "reasonForNoOffer": "Not interested in this type of service",       "remark": null,       "supplierName": "Blue Bird Design & Project Ltd",       "totalAmount": null     },     {       "tenderResponse": "Offer",       "reasonForNoOffer": null,       "remark": null,       "supplierName": "Metadesign Limited",       "totalAmount": 1000200     },     {       "tenderResponse": "Disqualified",       "reasonForNoOffer": null,       "remark": null,       "supplierName": "Reliance Travel (HK) Ltd",       "totalAmount": null     }   ],   "nonRegisteredSupplier": [],   "selectionReason": "Lowest Compliant Offers",   "remark": null,   "poLineItem": [     {       "poLineNumber": "1",       "prDetails": [         {           "prNumber": "2456",           "prLineNumber": "9"         }       ],       "itemDescription": "MIS PR LINE9",       "quantity": 1,       "uom": "Each",       "currency": "HKD",       "unitPrice": 900000,       "lineTotal": 900000,       "attachments": []     }   ] }

## 解法

the followings.  Thanks.

## 相關問題

- [EPRO-156](https://hktdc.atlassian.net/browse/EPRO-156)

