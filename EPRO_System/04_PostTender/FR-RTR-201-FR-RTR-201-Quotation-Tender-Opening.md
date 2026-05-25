---
project: EPRO
issue_key: ''
issue_type: Functional Requirement
status: Specified
tags:
- epro
- functional-requirement
- spec
title: 'FR-RTR-201: Quotation / Tender Opening'
quality: complete
category_label: Post-Tender
created: '2026-05-22'
---

## 需求描述

- **3.6** Submission of Quotations / Tenders
    - **3.6.7** Quotation / Tender Opening (a) Quotations / Tenders received through the Platform shall be inaccessible by Internal Users before the pre-set closing time. (b) Dual / Multiple password mechanism shall be applied for RFQ / tender opening (either Single or Two Envelope Approach). Password of at least two Internal Users shall be entered after the pre-set closing time in order to obtain the received quotations / proposals. The Contractor shall suggest a way to authenticate the identity of users for RFQ / tender opening, e.g. entry of respective Window log-in password. (c) Only the final version of submissions entered / uploaded to the Platform shall be opened and remained in the Platform. The previous version shall be discarded upon successful upload of the replaced document, but the details of all uploads, replacements and discards should be recorded and remain in the trail log. It should be noted that replacement of a particular document from a batch of submissions from an invited supplier shall be allowed. (d) The Platform shall generate an RFQ / tender opening summary that includes information such as all invited suppliers (whether they are submitted or not), receipt of Technical and/or Fee Proposals, list of documents uploaded by each supplier, opening date and time, Internal Users involved in RFQ / tender opening and a column for remarks. The summary contents may differ for RFQs and tenders. (e) The Platform shall allow flexibility to handle offline submissions that Subject Officers and/or F&A Users shall be allowed to indicate receipt of such offline submission in the RFQ / tender opening summary and upload quotations / proposals and/or input price information on the Platform subsequently. (f) The Platform shall incorporate the following processes for RFQs / tenders adopting Two Envelope Approach: (i) allowing the responsible Subject Officer or F&A User to verify the compliance of technical proposals before releasing to other Internal Users; and
## 驗收標準

The process for assigning RFQ / Tender Opening team members is detailed in FR-RTR-011.
The procedure required for RFQ / Tender opening includes:
Step 1 – Unlock the E-Tender Box and/or Physical Tender Box
Step 2 – Record of Hard-copy Submissions
Step 3 – Record of Sample / Oversized Submissions
Step 4 – Compliance Verification for Technical Proposals Submissions
Step 5 – Endorsement of RFQ / Tender Opening
The e-Forms for RFQ / Tender Opening can be used after the invitation closing date and time:
The following reports are available for internal users with access control:
RFQ / Tender Performance: This report indicates whether bidders / tenderers have responded to the RFQ / Tender. If they have, it lists them along with the date and time of each submission, the submission type (such as Offer, No Offer, Withdraw), and the status of submission results (such as Valid submission and Invalid submission).
The Platform can generate standard notification emails for internal users based on specific triggers:
Here are the available options and features for the e-Form:
The preparer drafts the e-Form. Drafts can be saved automatically to prevent data loss in case of a session timeout.
The e-Form can be saved in PDF and Excel formats.
PDF version: for attaching to emails for review and audit trails.
Excel version: Helps the preparer in creating documents for off-system / external processes.
The e-Form can be submitted for approval by the requestor designated by the preparer. If the requestor is designated, the e-Form can be reviewed, edited, and submitted for approval. Following submission, email notifications are sent to individuals based on the approval route, considering parallel or sequential modes.
Approvers (Reviewers, endorsers, and final approvers) can take actions such as approve, reject, return with feedback(s) , provided that specific conditions are met.
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
Report requirements


