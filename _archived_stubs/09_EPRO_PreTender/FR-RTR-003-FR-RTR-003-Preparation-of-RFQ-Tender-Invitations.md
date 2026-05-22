---
project: ''
issue_key: ''
issue_type: ''
status: ''
tags:
- epro
- epro_pretender
- faq
symptom: ''
root_cause: ''
solution: ''
jira_url: ''
created: ''
resolved: ''
fix_version: ''
components: []
has_images: false
category: ''
category_label: ''
quality: stub
title: 'FR-RTR-003: FR-RTR-003: Preparation of RFQ / Tender Invitations'
---
# FR-RTR-003: FR-RTR-003: Preparation of RFQ / Tender Invitations

## 需求描述

Requirement ID:	FR-RTR-003	Requirement Type:	RFQ and Tender	Requirements
Parent Requirement #:
None
Description:
3.4.	Preparation of RFQ / Tender Invitations
3.4.1.	Selective information brought from FMS shall be editable by Internal Users before issuing invitations (the edit record shall remain on the Platform and edited information may not need to synchronise back to corresponding PR in FMS). The attachments of the PR included in FMS shall be transferred to the Platform, of which Internal Users shall be allowed to choose which attachment(s) to send out for RFQ / tender invitations.
3.4.2.	Information brought forward from FMS shall be mapped and auto-filled at corresponding fields on the Platform for issuance preparation. Checking on mandatory fields as required by HKTDC shall be applied. The Platform shall allow Internal Users to group multiple PR lines from FMS into a single quotation item line with customized quotation item description before issuing RFQ / tender invitation since a procurement item might be split into different PR lines in FMS according to financial years or budget codes, etc.
3.4.3.	Internal Users who initiate the purchase should assign a procurement coordinator (“Subject Officers”), who will be responsible for inputting and performing other necessary actions on the Platform to facilitate the issuance of invitations. This encompasses various tasks, including but not limited to, providing the following information:
(a) Selection of RFQ / Tender Method and Potential Suppliers to be Invited
(i) Subject Officers shall select the appropriate RFQ / tender method. At the initial project stage, the Platform will default to “Selective RFQ / tender”.
(ii) If the information was inputted, the item (i) specified in Section 3.3.2 shall be included as one of the selective suppliers to be invited.
(iii) Subject Officers shall select additional suppliers to be invited from the corresponding supplier type in our Supplier Master list. It is preferable for the Platform to generate a summary that shows the engagement history for the same procured item number, which can be referenced by Internal Users.
(iv) The Platform shall perform a random selection of supplier(s) based on a pre-set rule. This rule shall primarily consider the previous performance of suppliers under corresponding category, meaning that suppliers with higher performance scores have a higher chance of being selected.
(v) The Platform shall be able to check and ensure that the minimum number of external suppliers to be invited, as determined by HKTDC’s policy, is met. If the number of external suppliers does not achieve the minimum requirement, a reminder shall pop up indicating the mandatory application of random selection of supplier(s). If the minimum number of suppliers is achieved, Subject Officers can apply random selection, as mentioned in (iii) above, at their own discretion.
(vi) The Platform shall perform a check on all invited suppliers and alert Subject Officers if any of the pre-defined details (e.g. contact details) of the invited suppliers are the same. The Platform should not allow the process to proceed if suppliers with the same pre-defined details are selected for invitation.
(b) Selection of RFQ / Tender Approach
(i) Depending on the purchase amount, there are two (2) approaches for both RFQ and tender: Single Envelope Approach, which is used for price assessment only, and the Two Envelope Approach, which is used for both technical and price assessment.
(ii) For the Two Envelope Approach, the Platform shall allow for the completion of the technical assessment prior to the opening of fee proposals.
(iii) The selection of approach in this stage shall affect the assessment in later stage.
(iv) When Two Envelope Approach is chosen for an RFQ / a tender, the Platform shall require Subject Officers to input the following information:
Technical / Fee weightings (input of reasons shall be mandatory when the weighting exceeds a certain ratio);
Assessment criteria and/or sub-criteria, allowing for two layers of criteria setting;
Maximum mark for each criterion / sub-criterion;
Overall passing mark and, if applicable, passing mark for selective criteria / sub-criteria;
Assignment of technical assessment panel members with a check of staff grading according to pre-determined levels. The Platform shall mandate Subject Officers to input justifications and/or attach supporting documents for F&A Users to approve in case non-qualified grading is detected; and
Assignment of RFQ / tender opening team members. The Platform shall allow different settings for the minimum numbers and requirements of opening team members for RFQ and tenders; and modify them with appropriate approval obtained.
(c) Development of Pricing Schedule
(i) The Platform shall allow Subject Officers to upload / import a pricing schedule with customised contents and layout that are suitable for individual RFQ / tender requirements.
(ii) If standard template(s) of pricing schedule are available for the proposed packaged solution, they shall be maintained on the Platform for Subject Officers to choose and modify as needed for individual RFQ / tender submissions with the following requirements:
Information stated in Section 3.3.2 shall be appropriately mapped to the corresponding field for further modification.
The finalised pricing schedule shall be issued in Excel format (or any other format suggested by the Contractor, which allows flexibility and further validation of submissions) for invited suppliers to fill in. Invited Suppliers shall be prevented from making changes from fields and contents other than the pricing field.
(iii) Whether using a customised or standard template of the Pricing Schedule, the Platform shall be designed to facilitate price assessment. It should provide two separate sections for the entry of mandatory items and optional items, streamlining the evaluation process.
(d) Declaration of Conflict of Interest
(i) Subject Officers and all reviewers, assessors or approvers involved in the subject purchase on the Platform shall declare any conflict of interest they may have with the invited suppliers.
(e) Selection of Mandatory or Optional Items
(i) Subject Officers shall indicate whether the requirement of respective item is mandatory or optional, which shall be brought forward to the pricing schedule for suppliers’ information.
(ii) The selection of mandatory and optional nature of items at this stage shall affect the assessment in later stage.
(f) Indication of Involvement of Pre-Qualification Process
(i) The pre-qualification process of supplier selection shall be conducted off-system at the initial project stage. Upon request and confirmation from the HKTDC, it may be added as an additional feature in the Platform. Tenderers shall quote this feature as an optional item in Annex D - Pricing Schedule.
(ii) Subject Officer is required to attach a pre-qualification evaluation report and all related documents to the Platform when the pre-qualification process has been performed. A reminder to attach the pre-qualification evaluation report shall be popped up when the relevant option is selected.
(g) Need for Signing Non-Disclosure Undertaking
(i) The Platform shall include a process where suppliers can access the RFQ / tender documents only after signing a Non-Disclosure Undertaking. The undertaking will be submitted by the suppliers and checked by Subject Officers.
(ii) Standard template(s) of Non-Disclosure Undertaking shall be developed and maintained on the Platform for Subject Officers to choose and modify according to the requirements of each RFQ / tender that requires such prior undertaking.
(h) Need for Briefing / Site Visit
(i) Briefing / Site visit for an RFQ / tender may be mandatory or optional. Suppliers shall be prohibited from submitting quotations / tenders if they did not attend mandatory briefing / site visit.
(ii) Subject Officers shall indicate whether briefing / site visit is required for respective RFQ / tender and specify its nature, which shall affect the qualification of suppliers to submit quotations / tenders.
(iii) When Subject Officers indicate the necessity of a briefing / site visit, it is mandatory to enter information including the response end time and briefing / site visit details.
(iv) Please refer to Section 3.6.5 for operation requirements for the briefing / site visit.
(i) Upload of Finalised RFQ / Tender Documents
(i) The Platform shall allow Internal Users to upload the finalised invitation documents, with a maximum file size of 30MB in total per RFQ/tender (comprising of several documents). Tenderers participating in this tender shall state any size limitations for uploading documents in their Technical Proposal. Tenderers shall also propose an effective mechanism to prevent Subject Officers from accidentally selecting internal records for invitation issuance.
Subject Officers are responsible for preparing a Tender Proposal, along with the finalised Tender Documents, which shall be duly approved by appropriate approvers before issuing tender invitations. The information entered into the Platform, including items (a), (b) and (f) above, shall be mapped to a predefined standard form of Tender Proposal. Subject Officers will be allowed to make further modifications to the Tender Proposal before submitting it for approval. The Platform shall allow it to be exported in Word format and/or directly modify within the Platform.
3.4.4.	Appropriate internal approvals shall be obtained for the finalisation of RFQ / Tender Documents. When the estimated purchase value exceeds a certain amount, among other approvers, additional approval from PRO / F&A is required. The Platform shall send notifications with a link to the designated Internal User(s) for approval requests and ensure the completion of all necessary approvals.
Rationale:
None
Acceptance / Fit Criteria:
Before initiating the sourcing process, the requestor from either the User Division/Department or the Purchasing Division/Department must complete the Procurement Strategy (PS) e-form and obtain approval at the project's initial stage.
The requestor is required to adhere to the following requirements and procedures, before and after approval:
The requestor of the PS e-Form should designate a Procurement Officer in each Sourcing section of the PS e-Form, as outlined in FR-RTR-001 Procurement Strategy (PS). This Procurement Officer will be responsible for inputting information and performing other necessary actions on the Platform to facilitate the issuance of invitations.
The selective information from the PR imported from FMS shall be editable by the requestor before issuing invitations, as outlined in FR-RTR-002 Purchase Requisition (PR).
Choose the appropriate method in Procurement Method section of PS e-Form, as outlined in FR-RTR-004 Selection of RFQ / Tender Method.
To invite potential suppliers, the requestor is required to complete the Shortlisting Methods sub-section within Sourcing section of the PS e-Form, as outlined in FR-RTR-001 Procurement Strategy (PS).
To assign members to the technical assessment panel, the requestor is required to complete the Set up an Assessment Panel (AP) sub-section within Sourcing section of the PS e-Form, following the procedures outlined in FR-RTR-010 Assignment of Technical Assessment Panel Members.
To assign members to the RFQ / Tender opening team, the Procurement Officers or Finance users are required to follow the procedures outlined in FR-RTR-011 Assignment of RFQ / Tender Opening Team Members.
To complete and finalize Pricing Schedule, the Procurement Officers are required to follow the procedures outlined in FR-RTR-012 Development of Pricing Schedule.
Depending on the requirements specified in the Conflicts of Interest section of the PS e-Form, internal users participating in the RFQ / Tender may be required to complete the DOI e-Form online, as outlined in FR-RTR-013 Declaration of Conflict of Interest.
To specify mandatory or optional item groups, the Procurement Officers are required to follow the procedures outlined in FR-RTR-012 Development of Pricing Schedule.
Indication of Involvement of Pre-Qualification Process, which is not included in the scope of this phase.
To specify the requirement for bidders/tenderers to sign a non-disclosure undertaking before accessing the RFQ / Tender documents, the Procurement Officers are required to follow the procedures outlined in FR-RTR-014 Need for Signing Non-Disclosure Undertaking.
To specify the requirement for bidders/tenderers to register for a briefing/site visit for the RFQ / Tender before qualifying to submit quotations/tenders, the Procurement Officers are required to follow the procedures outlined in FR-RTR-015 Need for Briefing / Site Visit.
To upload the finalized RFQ / Tender documents and complete the approval process, the Procurement Officers are required to follow the procedures outlined in FR-RTR-020  Upload of Finalised RFQ / Tender Documents.
Dependencies:
None
Tailoring Guidelines:
None
Change History:
None