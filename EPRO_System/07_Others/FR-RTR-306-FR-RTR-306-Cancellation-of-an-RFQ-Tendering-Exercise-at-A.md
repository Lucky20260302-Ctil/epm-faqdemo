---
project: EPRO
issue_key: ''
issue_type: Functional Requirement
status: Specified
tags:
- epro
- functional-requirement
- spec
title: 'FR-RTR-306: Cancellation of an RFQ / Tendering Exercise at Any Stage'
quality: complete
category_label: Others
created: '2026-05-22'
---

## 需求描述

B(v)	Other Requirements
- **3.19** The Platform shall have the following features: (e) The Platform shall include a “Terminate” function which allows for the suspension of an RFQ / tendering exercise at any stage with mandatory input of reasons and approval from appropriate reviewers and approvers in accordance with PPG.
## 驗收標準

The e-Form for submitting an approval request for the suspension of an RFQ/Tender exercise can be used after the RFQ/Tender invitations have been sent and before the RFQ/Tender exercise has been awarded:
The following report is available for internal users with access control to track the status of requests for the Cancellation of an RFQ/Tender exercise:
RFQ / Tender Data View: This report indicates whether any requests for the Cancellation of an RFQ/Tender exercise have been made. If they have, it lists them along with submission dates and times, as well as approval dates and times.
The Platform can generate standard notification emails for internal users and external suppliers based on specific triggers:
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

## 依賴項

Notifications and alerts feature
Reminder features
Approval Workflow feature
Report requirements


