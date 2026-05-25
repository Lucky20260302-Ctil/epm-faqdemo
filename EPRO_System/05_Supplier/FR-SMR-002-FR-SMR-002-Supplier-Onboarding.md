---
project: EPRO
issue_key: ''
issue_type: Functional Requirement
status: Specified
tags:
- epro
- functional-requirement
- spec
title: 'FR-SMR-002: Supplier Onboarding'
quality: complete
category_label: Supplier
created: '2026-05-22'
---

## 需求描述

- **3.21** Registration of new suppliers for RFQ / tender invitation shall primarily be initiated by Subject Officers on the Platform with entry of basic information and declaration of conflict of interest. The Platform shall then perform a checking on the supplier name against the existing supplier list and display appropriate messages if the same / similar supplier already exists on the Platform or FMS. The Contractor shall provide a mechanism to validate the supplier’s name against the existing supplier list. For suppliers existed in current supplier list (including supplier records newly initiated in the Platform or migrated/synced from FMS to the Platform), Subject Officers can select them for RFQ / tender invitation. The Contractor shall provide a mechanism to handle account opening/activation of these existing suppliers on the new Platform.
- **3.23** The supplier type of all new suppliers on the Platform shall be defaulted as a specific type defined by HKTDC.
- **3.24** Upon initiation by Internal Users and subsequent verification and approval by the appropriate approvers, the Platform shall generate and assign a supplier number to newly created suppliers (not exist in the supplier list of FMS) in accordance with HKTDC’s prescribed format. F&A Users or Subject Officers shall then initiate to send registration invitation emails to the newly created supplier(s) using the prescribed registration form. The Platform shall be able to update the supplier’s record upon receipt and approval of information from the supplier(s).
- **3.25** The single registration form with different document submission requirements and mandatory input fields shall be developed for different supplier categories (i.e. product or services categories). The Platform shall be able to validate the registration form against the mandatory items for each corresponding supplier category before suppliers can submit the form.
- **3.26** Information recorded in the Platform (entered by Subject Officers as new suppliers as per Section 3.21 or migrated/synced from FMS to the Platform) shall be brought forward and displayed on the registration form for external suppliers to update and/or complete.
- **3.27** The Contractor shall propose a registration mechanism incorporates the concept of a principal account and sub-accounts with multiple access rights for individual Tender No. 2774 Annex B - Tender Specifications Part 1 - Functional Requirements Page 28 departments / contact persons within the same organisation. The Contractor should note that input of different information shall be allowed for the principal account and subaccounts respectively (e.g. principal account and its sub-account(s) may have different contact details and correspondence address).
- **3.28** Before proceeding to registration, the Platform shall require suppliers to accept the Terms of Use.
- **3.29** Setting of passwords shall be in line with HKTDC’s security policies. Suppliers shall log in the Platform with the provided activation details to complete registration form and, if necessary, enable sub-account(s).
- **3.30** Upon duly completion of registration form on the Platform, the arrangement of information transferral shall be different as follows: For suppliers that already exist in the supplier list of FMS, all information and uploaded documents, whether mandatory or optional, shall be updated in FMS following review and approval by F&A Users and/or other appropriate approvers; For new suppliers that do not exist in the supplier list of FMS, all information and uploaded documents, whether mandatory or optional, shall be stored within the Platform following review and approval by F&A Users and/or other appropriate approvers, as described in Section 3.23. The information from an approved registration form will only be transferred to the FMS Supplier Platform when the respective new supplier is awarded and F&A Users acquired additional necessary information (e.g. bank information) from the new supplier.
- **3.31** The supplier types, supplier categories and information transferred from registration form may be changed during or after the review. The Contractor shall advise a mechanism to allow flexibility for external suppliers and Internal Users to supplement information / attach additional documents during the review process.
- **3.32** Notification emails regarding the appropriate progress update shall be sent to the relevant Internal Users and subject suppliers.
- **3.51** All related supplier information, including new registrations, amendments and deactivations shall be promptly updated on the Platform upon review and approval of F&A Users and/or appropriate approvers.
## 驗收標準

When inviting suppliers for pre-registration or full-registration, the Platform mandates that the subject officer (Buyer) or Supplier admin user fills out the e-Form request. Within the e-Form, the Platform verifies that the supplier name, telephone number, and email address provided do not already exist. The supplier name validation uses the real-time API from HKTDC to check for existing supplier names in FMS. The telephone number and email address , including master and sub-accounts on the Platform. Additionally, the subject or Supplier admin user must indicate the relationship between this new supplier and any existing suppliers, such as Parent Company and Subsidiary, or Parent Company and Branch.
< Screen mock-ups will be provided in the later SA&D stage >
After approval, the Platform will proceed with opening the supplier account by assigning a login username and generating a 32-character access code for account activation. Subsequently, the Platform will send an invitation for pre-registration or full-registration via email using a standard email template. The email will include supplier account details, such as the login username, access code for account activation, and a URL link for the account activation process.
Here is the workflow for inviting suppliers for pre-registration or full-registration:
< Screen mock-ups will be provided in the later SA&D stage >
Outlined below are specific scenarios with their corresponding exception handling:
Upon receiving the invitation email, the supplier needs to click the URL link and enter the access code provided in the email to activate their account. To complete the verification process, a 2FA is required, where the Platform generates a one-time password (OTP) and sends it to the specified email address. Once verified, the supplier can set up their password for the master account. Setting of passwords must be in line with HKTDC’s security policies outlined in FR-GR-019 and configured by System admin users. Suppliers are required to log in to the Platform using the provided activation details to complete the registration form and, if necessary, enable sub-account(s).
Here is the workflow for activating a supplier account and creating a password:
< Screen mock-ups will be provided in the later SA&D stage >
Outlined below are specific scenarios with their corresponding exception handling:
The suppliers on the Platform are categorized as follows:
Upon initiation by Internal Users and subsequent verification and approval by the appropriate approvers, the Platform will assign a unique supplier number to newly created suppliers.
The format for the supplier numbers on the Platform for pre-registration and full-registration is outlined as follows:
The supplier type of the supplier is categorized as follows:
Note: For new suppliers, there is a duplicate name checking feature in place. This check will verify against any existing suppliers with supplier type of "Registering", "Normal", or "Suspended" to ensure that no duplicate names are registered within the Platform.
Before proceeding with registration, the Platform will prompt suppliers to agree to the Terms of Use.
Upon completion and submission of the supplier registration form, the handling procedures are as follows:
The supplier registration form for pre-registration and full-registration with different document submission requirements and mandatory input fields as outlined below:
The supplier categories, including product and service categories, will be structured into three levels:
Every supplier can choose a maximum of three product/service categories.
The maintenance of supplier categories can be performed by System admin users.
.
< Screen mock-ups will be provided in the later SA&D stage >
Here is the workflow for registration upon account activation and password creation:
< Screen mock-ups will be provided in the later SA&D stage >
Here is the workflow after the registration has been submitted:
< Screen mock-ups will be provided in the later SA&D stage >
Here is the workflow after the full-registration has been processed from FMS:
< Screen mock-ups will be provided in the later SA&D stage >
The Platform can generate standard notification emails for both internal users and external suppliers based on specific triggers:
A weekly reminder email is sent to both internal users and external suppliers who are currently in a pending or awaiting approval status after submission.
For pre-registration suppliers, it is recommended that Supplier admin users list all suppliers annually. After conducting an analysis, the supplier type should be changed to "Terminated", based on the following possible reasons:
The supplier type is "Registering" with an unexpectedly prolonged pending date.
The supplier type is "Normal" but has not RFQ/Tender for over 3 years.
The Platform supports for the following report:
The report requirements will be documented and reviewed in the later SA&D stage.

## 依賴項

Notifications and alerts feature
Reminder features
Interface requirements
Report requirements


