---
project: EPRO
issue_key: ''
issue_type: Functional Requirement
status: Specified
tags:
- epro
- functional-requirement
- spec
title: 'FR-RTR-303: Purchase of Exemption List Items'
quality: complete
category_label: Others
created: '2026-05-22'
---

## 需求描述

B(iv)	Purchase of Exemption List Items & Low-Valued Purchase
- **3.15** Creation of PR and competitive procurement procedures are not mandatory for items specified on HKTDC’s Exemption List or when the total procurement value is below a certain amount for operation effectiveness.
- **3.16** When Subject Officers choose the related workflow, the Platform shall allow Subject Officers to attach supporting documents at their own discretion and pop up an appropriate message to remind them about the appropriate follow-up action. A separate record reference number shall be assigned for low-valued purchase and purchase of exemption list items. No further action / operation would be required in the Platform.
- **3.17** For the workflow of exemption list item purchase, there shall be an additional step where Subject Officers can choose the type of exemption list item they are going to purchase before the appropriate message of follow-up actions is displayed (which will be the same regardless of the chosen type of exemption list item).
- **3.18** As an optional feature that can be requested and confirmed by HKTDC, Subject Officers shall be allowed to obtain approval for low-valued purchases on the Platform. Please refer to Section E(v) for further details.
## 驗收標準

In the event of purchase items from HKTDC’s Exemption List, the requestor from the Purchasing Division/Department must complete the Procurement Strategy e-form (Part I) at the initial stage, as outlined in FR-RTR-001.
The Procurement Strategy e-form (Part I) for purchase of HKTDC’s Exemption List Items includes the following sections:
The Procurement Strategy e-Form (Part I) allows for only one sourcing (i.e. Purchase of Exemption List Items) with the following sub-sections:
Approval for Procurement Strategy e-Form (Part I) is not required, so the Procurement Officers allowing Procurement Officers to directly prepare and submit the Procurement Strategy e-Form (Part II), as outlined in FR-RTR-209 and FR-RTR-211.
Approval for Procurement Strategy e-Form (Part II) is also not required.
The Procurement Strategy e-Form (Part III) is not required for the "Purchase of Exemption List Items" procurement method. This means that the supplier performance review is not necessary for the "Purchase of Exemption List Items" procurement method.
The Platform can generate standard notification emails for internal users based on specific triggers:
Here are the available options and features for the e-Form:
The preparer drafts the e-Form. Drafts can be saved automatically to prevent data loss in case of a session timeout.
The e-Form can be saved in PDF and Excel formats.
PDF version: for attaching to emails for review and audit trails.
Excel version: Helps the preparer in creating documents for off-system / external processes.
The e-Form can be submitted for approval by the requestor designated by the preparer. If the requestor is designated, the e-Form can be reviewed, edited, and submitted for approval. Following submission, email notifications are sent to individuals based on the approval route, considering parallel or sequential modes.
Approvers (Reviewers, endorsers, and final approvers) can take actions such as approve, reject, return with feedback(s) or withdraw, provided that specific conditions are met.
The requestor is allowed to revoke approval at any time, enabling them to cancel the approval request before the final approver grants approval.
In cases where approval requests involve budget virement issues, the requestor can decide whether to inform the controlling officer of the budget division/department after approval or seek their endorsement within the approval route before final approval.
If an approval request requires the Tender Board Chairman's endorsement before issuing Tender Invitations, Addendums, Extending the closing date/time, or terminating the tender, the requestor can decide whether to inform the Tender Board Chairman after approval or seek their endorsement within the approval route before final approval.
Change history: The Platform automatically logs each field, capturing the date and time, the changer's details, the field modified, and old/new values.
Amendment history: The preparer manually fills in the summary of changes with each save.
Action History captures every e-Form status change, specifying the date, time, initiator, and new status.
Approval history tracks overall approval status changes, including the date, time, and last approver. It also logs individual actions with the date, time, person's name, action taken (e.g., approve, reject, withdraw), reasons or remarks, and attachments if necessary.
A weekly reminder email is sent to the requestor and current approvers who are pending approval based on the approval route.
The Platform should provide Approval Workflow feature, as outlined in FR-GR-012.

## 依賴項

Notifications and alerts feature
Reminder features
Approval Workflow feature


