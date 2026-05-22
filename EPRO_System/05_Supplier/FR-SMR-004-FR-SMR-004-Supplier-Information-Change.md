---
project: EPRO
issue_key: ''
issue_type: Functional Requirement
status: Specified
tags:
- epro
- functional-requirement
- spec
title: 'FR-SMR-004: Supplier Information Change'
quality: complete
category_label: Supplier
created: '2026-05-22'
---

## 需求描述

3.33	Registered suppliers shall be able to log into the Platform to make changes to company information and contact person details, with necessary supporting documents attached. Internal Users, upon obtaining relevant supporting documents for the information updates, shall be able to perform supplier information changes within the Platform.
3.34	Except for certain identified key items that cannot be updated by the registered supplier, the supplier with the principal account can modify all company information while subaccount holders can only amend their respective contact information. If a supplier needs to change the principal account or other key items, a change request should be submitted to HKTDC.
3.35	The Platform shall integrate with FMS to obtain the most recent information for updates if the supplier’s record already exists in FMS. The Platform shall verify the completion of mandatory fields and the upload of supporting documents before allowing suppliers to submit their changes. All amendments shall be subject to review and approval by F&A and/or other Internal Users. The Contractor shall provide a mechanism to display the change history, highlighting the updated information and indicating the previous information in a user-friendly manner for F&A and/or other Internal Users to approve the changes.
3.36	Both Internal Users and external suppliers should be allowed to modify certain information on the Platform, such as supplier categories, contact information or corresponding address. However, certain information, including the update of suspension period, supplier status, company name and bank information, should only be changed by F&A Users. Such changes require an off-system written request. The Platform shall display an appropriate message to communicate this arrangement.
3.37	All information about the concerned supplier that is applicable for self-service update shall be shown for Internal Users or external suppliers to amend directly. All amendments made should be logged with date and time of entry and approval.
3.38	All records on the Platform and/or FMS shall only be replaced by the amended information upon approval of F&A Users and/or other Internal Users.
3.39	In response to specific actions by Internal Users and external suppliers, F&A Users shall be allowed to change the supplier type and other relevant information during the review process.
3.51	All related supplier information, including new registrations, amendments and deactivations shall be promptly updated on the Platform upon review and approval of F&A Users and/or appropriate approvers.

## 驗收標準

Only the master account of registered suppliers can update contact details for their account and any sub-accounts.
For potential suppliers, the Platform does not allow update to company information. These updates should be managed exclusively by Supplier admin users.
For Registered/Approved suppliers have the privilege to access the Platform, they can update company information and contact person details themselves. Also, they can attach any necessary supporting documents during the updating process. External suppliers should be allowed to update certain information on the Platform, including supplier categories, contact details, and corresponding addresses.
Except for below listed key items, which cannot be changed by the supplier, those with the "Company Admin" user role can update all other company details. If a supplier wants to change the key items, they should submit a request to HKTDC via email or an alternative method.
Note: These details will be documented and reviewed in the latest SA&D stage.
The Platform ensures that mandatory fields are filled out and supporting documents are uploaded before suppliers can submit their changes.
Here is the workflow for submitting Request for Supplier Information Change e-Form:
< Screen mock-ups will be provided in the later SA&D stage >
< Screen mock-ups will be provided in the later SA&D stage >
FMS will not decline the supplier information change..
All records on the Platform and/or FMS will be updated with the amended information upon approval of F&A Users and/or other Internal Users.
Here is the workflow after the Request for Supplier Information Change has been processed from FMS:
< Screen mock-ups will be provided in the later SA&D stage >
The Platform can generate standard notification emails for both internal users and external suppliers based on specific triggers:
Here are the available options and features for the e-Form:
The preparer (External suppliers or Supplier admin users) drafts the e-Form. Drafts can be saved automatically to prevent data loss in case of a session timeout.
The e-Form can be saved in PDF and Excel formats.
PDF version: for attaching to emails for review and audit trails. When submitting the e-Form, the system automatically prints the e-Form as a PDF.
Excel version: Helps the preparer in creating documents for off-system / external processes.
Change history: The Platform automatically logs each field, capturing the date and time, the changer's details, the field modified, and old/new values.
Amendment history: The preparer manually fills in the summary of changes with each save.
Action History captures every e-Form status change, specifying the date, time, initiator, and new status.
A weekly reminder email is sent to the preparer who have pending tasks to complete.

## 依賴項

Interface requirements
Notifications and alerts feature
Reminder features


