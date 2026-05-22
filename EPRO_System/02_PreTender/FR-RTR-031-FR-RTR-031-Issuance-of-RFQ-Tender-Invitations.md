---
project: EPRO
issue_key: ''
issue_type: Functional Requirement
status: Specified
tags:
- epro
- functional-requirement
- spec
title: 'FR-RTR-031: Issuance of RFQ / Tender Invitations'
quality: complete
category_label: Pre-Tender
created: '2026-05-22'
---

## 需求描述

3.5.	Issuance of RFQ / Tender Invitations
3.5.1	The Contractor shall design and develop the Platform to support HKTDC’s issuance of documents and suppliers’ access to them for different types of RFQ / tender method including:
(a) Selective RFQ / tender (i.e. only suppliers invited by Subject Officers could access the RFQ / Tender Documents and submit proposals); and
(b) Open tendering, which is not covered in the scope of this tender and may be considered as an additional feature, subject to HKTDC’s exploration and consideration. The Contractor shall demonstrate their capability for this potential development in their Technical Proposal.
3.5.2	Prior to issuing the invitation from the Platform, Subject Officers shall input or select the following information:
(a) The issuance date.
(b) The closing date, with the default closing time in Hong Kong time and shall allow Internal Users to make amendments.
(c) Selection of file(s) to be published for suppliers’ access. Only RFQ / Tender Documents approved in previous stage will be sent out for invitation, some documents uploaded for the RFQ / tender will be for internal record and will not be shared with the suppliers.
(d) Selection of contact person(s) of a supplier to receive the invitation notification. Only the selected contact person(s) could access related information and/or submit quotations / tenders. The Contractor shall propose a mechanism to allow Subject Officers to change / update the contact person(s) of an invited supplier at any time before the RFQ / tender is closed.
3.5.3	Once all necessary approvals have been obtained in accordance with HKTDC’s policies, the Platform shall send an email to the selected suppliers to notify them about HKTDC’s invitation. The email template, provided by HKTDC, shall include, at a minimum, RFQ/Tender title and reference number, closing date and time, contact person details and hyperlink to the Platform.
3.5.4	Tenderers participating in this tender shall propose a mechanism or provide comments on the feasibility if the Subject Officer who issues RFQ / tender invitation is not from the same department that raised the PR in FMS in their Technical Proposal.

## 驗收標準

Upon finalizing and obtaining approval, the Platform will automatically generate the RFQ or Tender exercise for Written Quotation and Tender processes. An email notification will be sent to the designated Procurement Officers to specify the required options for the RFQ / Tender exercise and to complete the setup process until it is prepared for sending out invitations.
Open tendering, which is not included in the scope of this phase.
The options for the RFQ / Tender exercise may require different e-Forms for management and control, which can be used before sending out the RFQ / Tender invitations:
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
If an approval request requires the  before issuing Tender Invitations, Addendums, Extending the closing date/time, or terminating the tender, the requestor can seek their endorsement within the approval route before final approval.
Change history: The Platform automatically logs each field, capturing the date and time, the changer's details, the field modified, and old/new values.
Amendment history: The preparer manually fills in the summary of changes with each save.
Action History captures every e-Form status change, specifying the date, time, initiator, and new status.
Approval history tracks overall approval status changes, including the date, time, and last approver. It also logs individual actions with the date, time, person's name, action taken (e.g., approve, reject), reasons or remarks, and attachments if necessary.
A weekly reminder email is sent to the requestor and current approvers who are pending approval based on the approval route.
The Platform should provide Approval Workflow feature, as outlined in FR-GR-012.

## 依賴項

Notifications and alerts feature
Reminder features
Approval Workflow feature
Report requirements
Dependencies:
None


