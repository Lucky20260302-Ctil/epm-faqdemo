---
project: EPRO
issue_key: ''
issue_type: Functional Requirement
status: Specified
tags:
- epro
- functional-requirement
- spec
title: 'FR-RTR-002: Purchase Requisition (“PR”)'
quality: complete
category_label: Pre-Tender
created: '2026-05-22'
---

## 需求描述

- **3.3** Purchase Requisition (“PR”)
    - **3.3.1** PR creation shall remain on FMS. When Internal Users chose “RFQ / Tender” flow on the Platform, they shall be required to enter a valid PR number generated on FMS. The Platform shall be able to identify if a PR was approved before allowing the Internal Users to proceed. If the PR was not approved in FMS, a warning message shall be popped up with suitable reminder.
    - **3.3.2** Despite the input nature of PR Information in FMS, all information entered by Internal Users, including but not limited to the following, shall be transferred from FMS to corresponding field in the Platform for preparation of RFQ / tender invitation:
- **3.4** Preparation of RFQ / Tender Invitations
    - **3.4.1** Selective information brought from FMS shall be editable by Internal Users before issuing invitations (the edit record shall remain on the Platform and edited information may not need to synchronise back to corresponding PR in FMS). The attachments of the PR included in FMS shall be transferred to the Platform, of which Internal Users shall be allowed to choose which attachment(s) to send out for RFQ / tender invitations.
    - **3.4.2** Information brought forward from FMS shall be mapped and auto-filled at corresponding fields on the Platform for issuance preparation. Checking on mandatory fields as required by HKTDC shall be applied. The Platform shall allow Internal Users to group multiple PR lines from FMS into a single quotation item line with customized quotation item description before issuing RFQ / tender invitation since a procurement item might be split into different PR lines in FMS according to financial years or budget codes, etc.
## 驗收標準

Before initiating the sourcing process, the requestor from either the User Division/Department or the Purchasing Division/Department must complete the Procurement Strategy (PS) e-form and obtain approval at the project's initial stage.
The requestor is required to fill the associated Purchase Request (PR) from FMS in Procurement Categories sub-section under each Sourcing section of PS e-Form as outlined in FR-RTR-001 Procurement Strategy (PS).
The selected line items from the PR will automatically fill the Requisition Item(s) sub-section within the Sourcing section of the PS e-Form. These selected line items will remain locked until the procurement process is either finished or awarded. If the linked RFQ / Tender is discarded or terminated, the PR and selected line items can then be unlocked for use in other PS e-Form.
Selective information imported from FMS will be editable by the requestor before issuing invitations.
If a suggested supplier is specified in the line item of the PR from FMS, the Platform will require that supplier to be included in the bidder/tenderer list for the RFQ / Tender exercise.
The edit record will be remained on the Platform, and any edited information may not need to synchronize back to the corresponding PR in the FMS.
The attachments from the PR included in the FMS will be transferred to the Platform, allowing the requestor to select which attachment(s) to send out with the RFQ / Tender invitations.
Information imported from FMS will be mapped and automatically filled into the corresponding fields on the Platform for the preparation of issuance. The selected line items from the PR will automatically fill the Requisition Item(s) sub-section within the Sourcing section of the PS e-Form.
Checks for mandatory fields, as required by HKTDC, will be implemented, as outlined in FR-RTR-001 Procurement Strategy (PS) and FR-RTR-003 Preparation of RFQ / Tender Invitations.
These selected line items will remain locked until the procurement process is either finished or awarded. If the linked RFQ / Tender is discarded or terminated, the PR and selected line items can then be unlocked for use in other PS e-Form.
The Platform will enable the preparer (i.e. Procurement Officers) to consolidate multiple PR lines from the FMS into a single quotation item line with a customized quotation item description before issuing the RFQ / Tender invitation. This requirement is detailed in FR-RTR-001 Pricing Schedule with Requisition Item Group(s).
The interface requirements will be documented and reviewed during the subsequent SA&D stage
The following report is available for internal users with access control to track the associated PR in RFQ / Tender exercises:
RFQ / Tender Data View: This report indicates the name/title, details, Publish/Invitation Date, Invitation Closing Date and Time, and Contact Persons of RFQ / Tender exercises. It also lists the associated PR and selected PR line items.

## 依賴項

Interface requirements
Report requirements


