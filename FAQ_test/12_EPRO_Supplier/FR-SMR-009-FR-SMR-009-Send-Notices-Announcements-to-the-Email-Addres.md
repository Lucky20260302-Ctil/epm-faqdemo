---
title: "FR-SMR-009: FR-SMR-009: Send Notices / Announcements to the Email Addresses of all / selected Registered Supplie"
tags: [epro, EPRO_Supplier]
---

# FR-SMR-009: FR-SMR-009: Send Notices / Announcements to the Email Addresses of all / selected Registered Suppliers when necessary

## 需求描述

Requirement ID:	FR-SMR-009	Requirement Type:	Supplier Management
Requirements
Parent Requirement #:
None
Description:
3.53	The Platform shall allow F&A Users to send notices / announcements to the email addresses of all / selected registered suppliers when necessary.
Rationale:
None
Acceptance / Fit Criteria:
The Platform supports e-Form for Supplier admin users to send email to all or selected registered suppliers as needed.
The e-Form includes fields for the effective date, email subject, email message (e.g., notice or announcement), CC list, and the selection of all registered suppliers or specific registered supplier(s) based on search criteria:
Supplier Name
Classification Indicator: Potential Supplier and Approved Supplier
< Screen mock-ups will be provided in the later SA&D stage >
Upon submission of the e-Form, the Platform sends the email on the specified effective date using a standard email address (e.g. no-reply@e-tendering.com) as the sender and sends the email to all registered suppliers or selected registered supplier(s) using BCC.
The Platform can generate standard notification emails for internal users based on specific triggers:
Here are the available options and features for the e-Form:
The preparer (Supplier admin users) drafts the e-Form. Drafts can be saved automatically to prevent data loss in case of a session timeout.
The e-Form can be saved in PDF and Excel formats.
PDF version: for attaching to emails for review and audit trails. When submitting the e-Form, the system automatically prints the e-Form as a PDF.
Excel version: Helps the preparer in creating documents for off-system / external processes.
Change history: The Platform automatically logs each field, capturing the date and time, the changer's details, the field modified, and old/new values.
Amendment history: The preparer manually fills in the summary of changes with each save.
Action History captures every e-Form status change, specifying the date, time, initiator, and new status.
A weekly reminder email is sent to the preparer who have pending tasks to complete.
Dependencies:
Notifications and alerts feature
Reminder features
Tailoring Guidelines:
None
Change History:
None