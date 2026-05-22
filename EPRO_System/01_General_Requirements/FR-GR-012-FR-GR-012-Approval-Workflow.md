---
project: EPRO
issue_key: ''
issue_type: Functional Requirement
status: Specified
tags:
- epro
- functional-requirement
- spec
title: 'FR-GR-012: Approval Workflow'
quality: complete
category_label: General Requirements
created: '2026-05-22'
---

## 需求描述

3.1.11	The Platform shall support multiple layers of review and approval for each procurement process, aligning with the respective guidelines. This involves establishing the approval flow for user departments and / or the F&A. Additionally, the Administrator shall have the authority to modify or customise the approval flow as necessary.
Samples of simple and complicated approval flows are illustrated below for reference. The actual approval flow settings shall be subject to HKTDC’s pre-determined reporting line and approval threshold.
Example for simple approval flow
Example for complicated approval flow
3.1.12	Any approval process in the Platform shall be associated with the following features:
“Disapproval” and “Revoke Approval” options with a field to input remarks and comments and, if applicable, an option to select a person of any previous level to reject the item;
Addition of attachments by approver of each stage, ensuring all Internal Users involved in the approval can access and review them; and
Internal Users could check status of each approval process, view the complete path of the approval flow according to the appropriate hierarchy and access the approval history, including associated remarks and comments, subject to the pre-defined access rights.
3.1.13	Any “Submit” option in the Platform shall be associated with “Withdraw” or “Recall” option.
3.1.14	The actions of “Disapproval”, “Revoke Approval” and “Withdraw”/“Recall” shall be prohibited if the item had been approved by the next / upper level.

## 驗收標準

The Platform should have the flexibility to allow the organization to configure and customize approval flows based on their specific procurement policies and procedures.
Here are the available options and features for each Request e-Form:
The preparer drafts the Request e-Form. Drafts can be saved automatically to prevent data loss in case of a session timeout.
The Request e-Form can be saved in PDF and Excel formats.
PDF version: for attaching to emails for review and audit trails.
Excel version: Helps the preparer in creating documents for off-system / external processes.
The request e-Form can be submitted for approval by the requestor designated by the preparer. If the requestor is designated, the e-Form can be reviewed, edited, and submitted for approval. Following submission, email notifications are sent to individuals based on the approval route, considering parallel or sequential modes.
Approvers (Reviewers, endorsers, and final approvers) can take actions such as approve, reject, or, provided that specific conditions are met.
The requestor is allowed to revoke approval at any time, enabling them to cancel the approval request before the final approver grants approval.
In cases where approval requests involve budget virement issues, the requestor can decide whether to inform the controlling officer of the budget division/department after approval or seek their endorsement within the approval route before final approval.
If an approval request requires the Tender Board Chairman's endorsement before issuing Tender Invitations, Addendums, Extending the closing date/time, or terminating the tender, the requestor can seek their endorsement within the approval route before final approval.
Change history: The Platform automatically logs each field, capturing the date and time, the changer's details, the field modified, and old/new values.
Amendment history: The preparer manually fills in the summary of changes with each save.
Action History captures every e-Form status change, specifying the date, time, initiator, and new status.
Approval history tracks overall approval status changes, including the date, time, and last approver. It also logs individual actions with the date, time, person's name, action taken (e.g., approve, reject), reasons or remarks, and attachments if necessary.
A weekly reminder email is sent to the requestor and current approvers who are pending approval based on the approval route.
The configuration of complex approval flows with multiple levels of authorization and parallel approval processes should be supported by the Platform.
Multi-level or parallel approval processes are as follows:
The ability to view and manage their approvals that are ready and waiting for a user to perform them should be available to the Requestor, previous, and current Approvers.
The status of the Request e-Form approval is as follow:
The status flow of the Request e-Form approval is shown below:
The Platform executes the following flowchart and logic to regulate the approval workflow:
Approval is given with remark(s) if necessary, rejected with reason(s), and returned with feedback(s) by the approver:
Clarification tools during Approval:
The Platform provides clarification tools similar to a discussion group, such as a WhatsApp group. This discussion group is dedicated to the approval request and can only be accessed by the requestor, .
< Screen mock-ups will be provided in the later SA&D stage >
The current approver, and previous approvers who have already approved, can raise questions or request clarifications to the requestor and/or previous approvers before final approval.
In response to questions or clarification requests, a flexible deadline can be specified with only a target end date, without a strict deadline. Email notifications are sent only to the initiator who raised the question or request for clarification and selected recipients who will provide answers or replies.
When providing answers or replies to questions or clarifications, resubmissions are allowed. Email notifications are sent only to the initiator, the approver who raised the question or request for clarification, and copied to the respondent who answers the question or provides clarification.
respondent must reply to the approver's question or clarification request for the approver to proceed with approval. Failure to will result in the approver only being able to take action to reject the request.
Any approver can access, view, and download any attachments if available.
The discussion group automatically closed or .
The approval can be revoked by the requestor at any time without being finally approved:
Approval is withdrawn by the approver after it has been approved:
The Platform should provide a change history feature.
The Platform should provide an approval history feature.
All actions performed on individual user accounts must be recorded and logged.
Outlined below are specific scenarios with their corresponding exception handling:
The Platform shall successfully perform all the actions outlined in the Use Case 12.

## 依賴項

FR-GR-017 Audit Trails Feature
FR-GR-013 Notification and Alert Feature


