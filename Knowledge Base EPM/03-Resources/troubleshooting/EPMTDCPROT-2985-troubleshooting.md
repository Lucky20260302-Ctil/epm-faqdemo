---
tags: [bug, jira, ext-tdc-uat, change-request]
component: Tender & RFQ
symptom: "1/ Even Tender Response is updated to align the value from EPRO per[Link:https://hktdc.atlassian.net/browse/EPRO-694] , Reason for No Offer is missing"
root-cause: ""
solution: ""
jira: EPMTDCPROT-2985
resolved: 2025-11-04
---

# EPMTDCPROT-2985: EPRO-698 [UAT] Incorrect PO Creation API

## 問題

[Link:https://hktdc.atlassian.net/browse/EPRO-698] 
1/ Even Tender Response is updated to align the value from EPRO per[Link:https://hktdc.atlassian.net/browse/EPRO-694] , Reason for No Offer is missing.
2/  The API call missing total Amount and Remark, which were provided in [Link:https://hktdc.atlassian.net/browse/EPRO-635]  , [Link:https://hktdc.atlassian.net/browse/EPRO-626?focusedCommentId=164561] 
Please also further check and fix. Thanks.
[Image]
[Image]
cc [accountid:5df204e72702bc0ec7e7af0b] , [accountid:712020:286ef455-0480-4b26-aad8-33ea563a2c14] , [accountid:712020:9d3711ef-d393-4f93-9a23-9f1aa6e398fa] 

```
{
	"finalCurrency": "HKD",
	"totalPOAmount": 350000,
	"hkdEquivalent": 350000,
	"attachments": [
		"attachment.png"
	],
	"poDescription": "MIS 20250910",
	"fmsSupplierId": "27632",
	"buyer": "dewang",
	"poCreatedDate": "2025-09-10 03:34:35",
	"siteName": "BILLING",
	"declaration": "Yes",
	"purchaseMethod": "Request for Quotation",
	"exemptionListItem": [],
	"purchaseMethodRefNum": "RFQ-25/26-ITS-00119",
	"noOfTenderersInvited": 3,
	"noOfReturnOffer": 1,
	"registeredSupplier": [
		{
			"tenderResponse": "Offer",
			"supplierName": "MIS2050910"
		},
		{
			"tenderResponse": "No return",
			"supplierName": "EPRO 581"
		},
		{
			"tenderResponse": "No offer",
			"supplierName": "MISC"
		}
	],
	"nonRegisteredSupplier": [],
	"selectionReason": "Only Compliant Offer",
	"poLineItem": [
		{
			"poLineNumber": "1",
			"prDetails": [
				{
					"prNumber": "2471",
					"prLineNumber": "1"
				}
			],
			"itemDescription": "PO LINE 1 FY2526",
			"quantity": 1,
			"uom": "Each",
			"currency": "HKD",
			"unitPrice": 110000,
			"lineTotal": 110000,
			"attachments": [
				"ATTACHMENT_EMAIL.msg"
			]
		},
		{
			"poLineNumber": "2",
			"prDetails": [
				{
					"prNumber": "2471",
					"prLineNumber": "2"
				}
			],
			"itemDescription": "PO LINE 2 FY2627",
			"quantity": 1,
			"uom": "Each",
			"currency": "HKD",
			"unitPrice": 120000,
			"lineTotal": 120000,
			"attachments": []
		},
		{
			"poLineNumber": "3",
			"prDetails": [
				{
					"prNumber": "2471",
					"prLineNumber": "3"
				}
			],
			"itemDescription": "PO LINE 3 FY2829",
			"quantity": 1,
			"uom": "Each",
			"currency": "HKD",
			"unitPrice": 120000,
			"lineTotal": 120000,
			"attachments": []
		}
	]
}
```

## 根因

Please also further check and fix. Thanks.
cc [accountid:5df204e72702bc0ec7e7af0b] , [accountid:712020:286ef455-0480-4b26-aad8-33ea563a2c14] , [accountid:712020:9d3711ef-d393-4f93-9a23-9f1aa6e398fa] 
	"finalCurrency": "HKD",
	"totalPOAmount": 350000,
	"hkdEquivalent": 350000,
	"attachments": [
		"attachment.png"
	"poDescription": "MIS 20250910",
	"fmsSupplierId": "27632",
	"buyer": "dewang",
	"poCreatedDate": "2025-09-10 03:34:35",
	"siteName": "BILLING",
	"declaration": "Yes",
	"purchaseMethod": "Request for Quotation",
	"exemptionListItem": [],

## 解法

```
{
	"finalCurrency": "HKD",
	"totalPOAmount": 350000,
	"hkdEquivalent": 350000,
	"attachments": [
		"attachment.png"
	],
	"poDescription": "MIS 20250910",
	"fmsSupplierId": "27632",
	"buyer": "dewang",
	"poCreatedDate": "2025-09-10 03:34:35",
	"siteName": "BILLING",
	"declaration": "Yes",
	"purchaseMethod": "Request for Quotation",
	"exemptionListItem": [],
	"purchaseMethodRefNum": "RFQ-25/26-ITS-00119",
	"noOfTenderersInvited": 3,
	"noOfReturnOffer": 1,
	"registeredSupplier": [
		{
			"tenderResponse": "Offer",
			"supplierName": "MIS2050910"
		},
		{
			"tenderResponse": "No return",
			"supplierName": "EPRO 581"
		},
		{
			"tenderResponse": "No offer",
			"supplierName": "MISC"
		}
	],
	"nonRegisteredSupplier": [],
	"selectionReason": "Only Compliant Offer",
	"poLineItem": [
		{
			"poLineNumber": "1",
			"prDetails": [
				{
					"prNumber": "2471",
					"prLineNumber": "1"
				}
			],
			"itemDescription": "PO LINE 1 FY2526",
			"quantity": 1,
			"uom": "Each",
			"currency": "HKD",
			"unitPrice": 110000,
			"lineTotal": 110000,
			"attachments": [
				"ATTACHMENT_EMAIL.msg"
			]
		},
		{
			"poLineNumber": "2",
			"prDetails": [
				{
					"prNumber": "2471",
					"prLineNumber": "2"
				}
			],
			"itemDescription": "PO LINE 2 FY2627",
			"quantity": 1,
			"uom": "Each",
			"currency": "HKD",
			"unitPrice": 120000,
			"lineTotal": 120000,
			"attachments": []
		},
		{
			"poLineNumber": "3",
			"prDetails": [
				{
					"prNumber": "2471",
					"prLineNumber": "3"
				}
			],
			"itemDescription": "PO LINE 3 FY2829",
			"quantity": 1,
			"uom": "Each",
			"currency": "HKD",
			"unitPrice": 120000,
			"lineTotal": 120000,
			"attachments": []
		}
	]
}
```

## 相關問題

- [EPRO-626](https://hktdc.atlassian.net/browse/EPRO-626)
- [EPRO-635](https://hktdc.atlassian.net/browse/EPRO-635)
- [EPRO-694](https://hktdc.atlassian.net/browse/EPRO-694)
- [EPRO-698](https://hktdc.atlassian.net/browse/EPRO-698)

