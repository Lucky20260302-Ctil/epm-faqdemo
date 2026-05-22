---
project: ''
issue_key: ''
issue_type: ''
status: ''
tags:
- epro
- epro_others
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: ''
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: ''
category_label: ''
quality: stub
title: 'FR-RTR-302: FR-RTR-302: Waiver'
---
# FR-RTR-302: FR-RTR-302: Waiver

## 需求描述

Requirement ID:	FR-RTR-302	Requirement Type:	RFQ and Tender	Requirements
Parent Requirement #:
None
Description:
B(iii)	Waiver
3.14.	There shall be another designated workflow on the Platform to handle waiving of competitive procurement procedures (e.g. single source purchase) to support the following procedures:
3.14.1	PR shall be created by Subject Officers and gone through normal approval procedures on FMS. Similar to RFQ / Tender, the Platform shall be able to identify PR approval status in FMS and only proceed to the next stage after verifying the entry of an approved PR number.
3.14.2	The Platform shall allow Subject Officers, relevant reviewers and approvers to declare conflict of interest, input waiver justifications, attach a waiver memo and/or other supporting documents for approval.
3.14.3	The approval flow shall follow the threshold of RFQ / Tender.
3.14.4	The Contractor shall provide a user-friendly way to let Internal Users to select appropriate approvers and/or Tender Board members for individual waiver approval.
3.14.5	Upon approval, related information shall be transferred to FMS. With integration with FMS, Internal Users shall be able to search for the request approved on the Platform with specified reference number for PO creation.
3.14.6	Information and attachments from the Platform shall be mapped and auto-filled in appropriate fields / transferred to appropriate locations on FMS for Internal User’s editing before submission of PO for approval.
Rationale:
None
Acceptance / Fit Criteria:
In the event of waiving of competitive procurement (e.g. single source purchase), the requestor from the Purchasing Division/Department must complete the Procurement Strategy e-form (Part I) and obtain approval at the project's initial stage, as outlined in FR-RTR-001.
The Procurement Strategy e-form (Part I) for waiving of competitive procurement includes the following sections:
The Procurement Strategy e-Form (Part I) allows for only one sourcing (i.e. Waiver) with the following sub-sections:
Upon approved, an email notification will be sent to the Procurement Officers, allowing them to directly prepare and submit the Procurement Strategy e-Form (Part II) for approval, as outlined in FR-RTR-209 and FR-RTR-211.
Also, after the Procurement Strategy e-Form (Part II) is approved, Procurement Officers can directly submit the necessary information for the supplier performance review within the Procurement Strategy e-Form (Part III), as outlined in FR-RTR-216. Necessary information will be brought forward from PS Part I.
The Platform can generate standard notification emails for internal users based on specific triggers:
Here are the available options and features for the e-Form:
The preparer drafts the e-Form. Drafts can be saved automatically to prevent data loss in case of a session timeout.
The e-Form can be saved in PDF and Excel formats.
PDF version: for attaching to emails for review and audit trails.
Excel version: Helps the preparer in creating documents for off-system / external processes.
The e-Form can be submitted for approval by the requestor designated by the preparer. If the requestor is designated, the e-Form can be reviewed, edited, and submitted for approval. Following submission, email notifications are sent to individuals based on the approval route, considering parallel or sequential modes.
Approvers (Reviewers, endorsers, and final approvers) can take actions such as approve, reject, return with feedback(s), provided that specific conditions are met.
The requestor is allowed to revoke approval at any time, enabling them to cancel the approval request before the final approver grants approval.
In cases where approval requests involve budget virement issues, the requestor can decide whether to inform the controlling officer of the budget division/department after approval or seek their endorsement within the approval route before final approval.
If an approval request requires the Tender Board Chairman's endorsement before issuing Tender Invitations, Addendums, Extending the closing date/time, or terminating the tender, the requestor can decide whether to inform the Tender Board Chairman after approval or seek their endorsement within the approval route before final approval.
Change history: The Platform automatically logs each field, capturing the date and time, the changer's details, the field modified, and old/new values.
Amendment history: The preparer manually fills in the summary of changes with each save.
Action History captures every e-Form status change, specifying the date, time, initiator, and new status.
Approval history tracks overall approval status changes, including the date, time, and last approver. It also logs individual actions with the date, time, person's name, action taken (e.g., approve, reject, withdraw), reasons or remarks, and attachments if necessary.
A weekly reminder email is sent to the requestor and current approvers who are pending approval based on the approval route.
The Platform should provide Approval Workflow feature, as outlined in FR-GR-012.
Dependencies:
Notifications and alerts feature
Reminder features
Approval Workflow feature
Tailoring Guidelines:
None
Change History:
None