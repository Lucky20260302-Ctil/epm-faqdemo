---
tags: [bug, jira, ext-tdc-uat]
component: Tender & RFQ
symptom: "1/ Manually Created PO"
root-cause: ""
solution: "issues below,"
jira: EPMTDCPROT-3023
resolved: 2025-10-03
---

# EPMTDCPROT-3023: EPRO-724 [FMS] Tender Quotation Form Configuration

## 問題

[Link:https://hktdc.atlassian.net/browse/EPRO-724] 
1/ Manually Created PO
There are renaming of Tender Response “No offer” and new Tender Response “Disqualified”, looks like the validation is based on the description of Tender Response, please kindly help to check and fix issues below,
a/ Total Amount is now mandotory when Tender Reponse is “No offer” and newly added “Disqualified” for Tender, Request for Quotation and Branch Office Purchase Purchase Method Type
Total Amount is only mandotory when Tender Reponse is “Offer” for Tender, Request for Quotation and Branch Office Purchase Purchase Method Type. Please check and fix for both Registered Supplier and Non-registered supplier
[Image]
[Image]
b/ Reason for No Offer is not mandatory when Tender Response is “No offer”
Reason for No Offer should be mandatory when Tender Response is “No offer”. Please check and fix for both Registered Supplier and Non-registered supplier
[Image]
2/ API created PO
As current Total Amount is editable. If I try to remove the Total Amount and save, “Field must be entered” is shown, which is correct. However, it keep popping that I cannot fill in the Total Amount again even using F4, please kindly help to check and fix. Thanks.
[Image]
[Image]

## 根因

There are renaming of Tender Response “No offer” and new Tender Response “Disqualified”, looks like the validation is based on the description of Tender Response, please kindly help to check and fix issues below,
a/ Total Amount is now mandotory when Tender Reponse is “No offer” and newly added “Disqualified” for Tender, Request for Quotation and Branch Office Purchase Purchase Method Type
Total Amount is only mandotory when Tender Reponse is “Offer” for Tender, Request for Quotation and Branch Office Purchase Purchase Method Type. Please check and fix for both Registered Supplier and Non-registered supplier
b/ Reason for No Offer is not mandatory when Tender Response is “No offer”
Reason for No Offer should be mandatory when Tender Response is “No offer”. Please check and fix for both Registered Supplier and Non-registered supplier
2/ API created PO
As current Total Amount is editable. If I try to remove the Total Amount and save, “Field must be entered” is shown, which is correct. However, it keep popping that I cannot fill in the Total Amount again even using F4, please kindly help to check and fix. Thanks.

## 解法

issues below,

## 相關問題

- [EPRO-724](https://hktdc.atlassian.net/browse/EPRO-724)

