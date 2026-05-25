---
project: EPRO
issue_key: ''
issue_type: Functional Requirement
status: Specified
tags:
- epro
- functional-requirement
- spec
title: 'FR-RTR-108: Submission of Quotations / Tenders with Offer Response'
quality: complete
category_label: Tender Stage
created: '2026-05-22'
---

## 需求描述

- **3.6** Submission of Quotations / Tenders
    - **3.6.1** The design and development of Platform shall support the following submission type: (a) Quotation / Fee Proposal only (For Single Envelope Approach); (b) Technical and Fee Proposals (For Two Envelope Approach)
    - **3.6.2** External suppliers shall possess with a supplier account on the Platform to perform the following actions during the quotation / tendering period: (e) Submission of quotation, technical and fee proposals with validation
    - **3.6.3** The Platform shall be developed with the following features: (a) For Two Envelope Approach, Technical Proposals and Fee Proposals shall be submitted in separate sections with clear instructions provided. (b) The Platform shall allow a minimum capacity of 20MB per document and 1GB in total for uploading proposals. Tenderers participating in this tender shall indicate any limitations on uploading and retention capacity in their Technical Proposals. (c) Notices shall be displayed to indicate uploading process and successful upload of any document. Timeout mechanism (logging out the user after certain inactivity period) shall not be applied when the supplier is uploading a document. (d) The finalised pricing schedule, as stated in Section 3.4.3(c), shall be made available for suppliers’ download and/or input, ensuring standardisation for future analysis. Suppliers shall not be allowed to change the contents and layout of the pricing schedule, except for inputting unit rates and specific quotation remarks. (e) In addition to filling in pricing schedule, suppliers shall be required to undertake some terms and conditions and allowed to upload supplementary information. (f) The currency shall initially be defaulted as per information transferred from the PR. (g) The Platform shall perform validation and necessary checking before accepting quotations / proposals. (h) Suppliers shall be allowed to withdraw and/or resubmit quotations / proposals before the closing time. However, such changes shall be restricted to the same account (i.e. If Sub-account A submitted a quotation / proposal, he will be the primary account to manage and amend the submissions which other sub-accounts cannot be able to supersede / amend them). (i) The Platform should reject any amendments or submissions of proposals after the closing time (documents in uploading process / documents uploaded successfully but suppliers did not click “Submit” button to confirm their submission at closing time will not be considered). (j) The Platform should send an email notification to the supplier upon successful submission of quotation / proposal. (k) The corresponding Subject Officer and/or F&A User shall have real time access to the number of submissions received on the Platform.
## 驗收標準

Procurement Officers configure the RFQ/Tender exercise to allow bidders/tenderers to submit their quotations / tenders to the E-Tender Box online through the Platform.
The Platform restricts the submission of quotations / tenders to occur only before the invitation closing date and time set by Procurement Officers. For example, if the invitation closing date and time is 24-Sep at 15:00 HKT (GMT+8), submissions will only be accepted until 24-Sep at 3:00 PM Hong Kong time. The E-Tender Box will close and lock promptly at 3:00 PM on 24-Sep Hong Kong time.
Bidders/tenderers responding to the RFQ / Tender, submissions must begin before the closing time, and all submissions must be completed before the closing time. Any submissions that do not meet this requirement will be classified as "Invalid submission" and recorded in the Submission History.
The handling of sample and oversized tender submissions will remain  current process.
Bidders/tenderers can submit their quotations / tenders if none of the following conditions are not mandatory. However, if any of these conditions are mandatory, bidders/tenderers must either complete the necessary actions or pass the compliance verification before they can submit their quotations / tenders:
Acknowledging the invitation
Submission of the signed NDA/Confidentiality Undertaking
for the briefing/site visit
The e-Form for submitting quotations / tenders with offer response related to the RFQ / Tender can be used before invitation closing date and time of the RFQ / Tender:
The Platform use One-Time Password (OTP) authentication to verify the identity of bidders/tenderers before each submission.
After submission, the Submission History will show the date and time of each submission, along with the status of submission results (e.g. Valid submission or Invalid submission).
The Platform allows bidders/tenderers have the option to supersede their submission by submitting again or to submit a withdrawal request to take back their previous submission after submitting their quotations/tenders with an offer response.
Procurement Officers and Finance users have real-time access to the number of submissions received on the Platform, including:
The number of bidders/tenderers whose submissions of quotations/tenders with offers have been received on the Platform
The number of bidders/tenderers who submissions of quotations/tenders without offers have been received on the Platform
The number of bidders/tenderers with no submissions received on the Platform
The number of bidders/tenderers with no response to the RFQ/Tender exercise on the Platform
Outlined below are specific scenarios with their corresponding exception handling:
The following report is available for internal users with access control to track the status of bidders/tenderers regarding the respond to RFQ / Tender, after invitation closing date and time:
RFQ / Tender Performance: This report indicates whether bidders/tenderers have responded to the RFQ / Tender. If they have, it lists them along with the date and time of each submission, the submission type (such as Offer, No Offer, Withdraw), and the status of submission results (such as Valid submission and Invalid submission).
The Platform can generate standard notification emails for external suppliers based on specific triggers:
The Platform  the Email Log to allow internal users with access control to view standard notification emails regarding the submission of quotations/tenders. These emails will only be listed after the invitation closing date and time.
Here are the available options and features for the e-Form:
The preparer (External suppliers, including master account and sub-accounts with the Tender Admin role) drafts the e-Form. Drafts can be saved automatically to prevent data loss in case of a session timeout.
The e-Form can be saved in PDF and Excel formats.
PDF version: for attaching to emails for review and audit trails.
Excel version: Helps the preparer in creating documents for off-system / external processes.
Change history: The Platform automatically logs each field, capturing the date and time, the changer's details, the field modified, and old/new values.
Amendment history: The preparer manually fills in the summary of changes with each save.
Action History captures every e-Form status change, specifying the date, time, initiator, and new status.
A weekly reminder email is sent to the preparer who have pending tasks to complete.

## 依賴項

Notifications and alerts feature
Reminder features
Report requirements


