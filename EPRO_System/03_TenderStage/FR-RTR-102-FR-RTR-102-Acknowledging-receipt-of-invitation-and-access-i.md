---
project: EPRO
issue_key: ''
issue_type: Functional Requirement
status: Specified
tags:
- epro
- functional-requirement
- spec
title: 'FR-RTR-102: Acknowledging receipt of invitation and access invitation documents'
quality: complete
category_label: Tender Stage
created: '2026-05-22'
---

## 需求描述

- **3.6** Submission of Quotations / Tenders
    - **3.6.2** External suppliers shall possess with a supplier account on the Platform to perform the following actions during the quotation / tendering period: (c) Acknowledging receipt of invitation and access invitation documents
## 驗收標準

Upon approved, the Platform will send an email notification to bidders/tenderers using a standard email template that includes the name/title, Publish/Issue Date, Invitation Closing Date and Time, Contact Persons, and additional requirements such as:
The need for signing NDA/Confidentiality Undertaking before they can access, view details, download RFQ / Tender documents
The need for a registration form for Briefing / Site visits before they can submit queries, or responses to the RFQ / Tender with or without an offer.
In the event that Procurement Officers configure the RFQ/Tender exercise to require bidders/tenderers to acknowledge the invitation before they can access, view details, and download RFQ / Tender documents, bidders/tenderers must provide acknowledgement before they can access the RFQ / Tender on the Platform.
The e-Form for acknowledging the RFQ/Tender invitation can be used before invitation closing date and time of the RFQ / Tender:
Outlined below are specific scenarios with their corresponding exception handling:
The following report is available for internal users with access control to track the status of bidders/tenderers regarding the RFQ / Tender Invitations:
RFQ / Tender Performance: This report indicates whether bidders/tenderers have responded to the RFQ / Tender Invitations. If they have, it lists them along with the date and time they acknowledged the notification.
The Platform can generate weekly reminder email for internal users and external suppliers on every Monday at 8:00 AM:
Here are the available options and features for the e-Form:
The preparer (External suppliers, including master account and sub-accounts with the Tender Admin role) drafts the e-Form. Drafts can be saved automatically to prevent data loss in case of a session timeout.
The e-Form can be saved in PDF and Excel formats.
PDF version: for attaching to emails for review and audit trails.
Excel version: Helps the preparer in creating documents for off-system / external processes.
Change history: The Platform automatically logs each field, capturing the date and time, the changer's details, the field modified, and old/new values.
Amendment history: The preparer manually fills in the summary of changes with each save.
Action History captures every e-Form status change, specifying the date, time, initiator, and new status.
A weekly reminder email is sent to the the preparer who have pending tasks to complete.

## 依賴項

Notifications and alerts feature
Reminder features
Report requirements


