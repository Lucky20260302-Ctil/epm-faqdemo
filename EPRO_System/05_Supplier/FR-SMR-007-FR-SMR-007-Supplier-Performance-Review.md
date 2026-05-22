---
project: EPRO
issue_key: ''
issue_type: Functional Requirement
status: Specified
tags:
- epro
- functional-requirement
- spec
title: 'FR-SMR-007: Supplier Performance Review'
quality: complete
category_label: Supplier
created: '2026-05-22'
---

## 需求描述

3.46	Brief information on purchase receipt done on FMS (i.e. goods receipts (“GRN”)), including the GRN date and GRN status, shall be transferred to the Platform for supplier performance review. Purchase receipt may be done in stages.
3.47	Currently, supplier performance is evaluated by Subject Officers who input of an average score on FMS for each purchase receipt, regardless of the contract value. With the Platform, it is expected that supplier performance reviews shall be conducted with a customised timeline that varies based on the contract type (e.g. one-off services such as booth construction for a single event may be reviewed upon service completion, while regular services may be reviewed quarterly from the contract commencement date). For contracts with a higher value, ratings for about 8 criteria will be required, whereas contracts with lower values will continue the current practice of inputting an average score.
3.48	The supplier performance review, including ratings for multiple criteria, may be expanded to include other types / values of procurement exercise in the future. The Contractor shall configure the Platform to allow flexibility in adjusting these thresholds.
3.49	The workflow for the supplier performance review, including ratings for multiple criteria, shall be as follows:
3.49.1	The Platform shall send a request for supplier performance review to the Internal User as assigned during the award stage (refer to Section 3.9) according to pre-determined timeline. The Platform should allow the Internal User to forward the request to others where necessary.
3.49.2	Internal User shall access the Platform to complete the supplier performance review form in the prescribed layout. The completed form shall be verified by appropriate approver in the corresponding department upon completion.
3.49.3	After the completion and verification of the supplier performance review form for an individual supplier, the performance scores (general and project specific) shall be calculated and immediately updated on the Platform.
3.49.4	If the overall performance score falls below the passing mark after the performance review, the concerned supplier shall also be excluded from the random selection list for RFQ / tender invitation. However, the Platform shall allow flexibility for Subject Officers to manually select such a supplier for invitation with appropriate approval at a certain grade. The Platform shall automatically send an alert to F&A Users when the overall performance score of a supplier falls below the passing mark for a pre-defined number of consecutive performance reviews.
3.50	The supplier performance score resulted from RFQs, tenders and waivers (excluding low-valued purchases and exemption list items, which will still undergo performance review on FMS) shall be used for the system’s automatic calculation of the average overall performance and average performance score per project based on each PR, PO or Contract. The average overall performance score shall be the primary factor for the random selection of suppliers during the invitation stage.

## 驗收標準

Following the sourcing and selection of suppliers, the subject officer (Buyer) is required to finalize the details for the Contract/Purchase Order (PO) in the Procurement Strategy (PS) form (Part II) at the award stage.
In Part II of the PS form, the subject need to indicate the Quotation/Tender award to the selected supplier(s), The date can be updated by Finance users with supporting documents may be required to be uploaded for offline approval if necessary.
For every contract or PO issued to suppliers, the subject can assign an individual from within the user division/department or from across all divisions/departments to evaluate supplier performance. They can also choose the evaluation template based on different sourcing categories and specify the frequency of reviews. Finance users can update
System admin users can configure the evaluation templates, including ratings for multiple criteria,  according to various sourcing categories. They can configure the template settings and determine whether users should input scores for evaluation, with the Platform automatically calculating the average score, or if users are allowed to input the average score manually.
The assigned individual will receive task request to provide scores using the selected evaluation template.
In case of absence, the assigned individual can use self-operational delegation or delegation by System admin users.
After the and  the supplier performance review form for an individual supplier, the overall score update on the Platform should occur after approval by the designated reviewer. Then, the Platform calculates the overall performance scores from the contracts / purchase orders and updates them immediately.
The supplier performance score resulted from RFQs, tenders and waivers (excluding low-valued purchases and exemption list items, which will still undergo performance review on FMS) will be used for the Platform’s automatic calculation of the average overall performance based on each contract or PO. The average overall performance score will serve as the primary factor for the random selection of suppliers during the invitation stage.
If the overall performance score falls below the passing mark after the performance review, the concerned supplier shall also be excluded from the random selection list for RFQ / tender invitation.
The Platform can generate standard notification emails for designated individual based on specific triggers:
Here are the available options and features for the e-Form:
The preparer (designated individual) drafts the e-Form. Drafts can be saved automatically to prevent data loss in case of a session timeout.
The e-Form can be saved in PDF and Excel formats.
PDF version: for attaching to emails for review and audit trails. When submitting the e-Form, the system automatically prints the e-Form as a PDF.
Excel version: Helps the preparer in creating documents for off-system / external processes.
Change history: The Platform automatically logs each field, capturing the date and time, the changer's details, the field modified, and old/new values.
Amendment history: The preparer manually fills in the summary of changes with each save.
Action History captures every e-Form status change, specifying the date, time, initiator, and new status.
A weekly reminder email is sent to the preparer who have pending tasks to complete.
The Platform supports for the following report:
The report requirements will be documented and reviewed during the subsequent SA&D stage.

## 依賴項

Reminder features
Report requirements


