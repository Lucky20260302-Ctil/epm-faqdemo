---
title: "FR-RTR-210: FR-RTR-210: Export of the prescribed Tender Report in Word format"
tags: [epro, EPRO_PostTender]
---

# FR-RTR-210: FR-RTR-210: Export of the prescribed Tender Report in Word format

## 需求描述

Requirement ID:	FR-RTR-210	Requirement Type:	RFQ and Tender	Requirements
Parent Requirement #:
FR-RTR-209	Preparation of Award Recommendation
Description:
- **3.8** Approval of Award Recommendation
    - **3.8.1** Preparation of Award Recommendation
(a) The Contractor shall design and configure the Platform to allow Subject Officers to prepare award recommendations, including but not limited to the following information:
(v) If the total contract price exceeds a certain amount as specified in the PPG, a Tender Report shall be attached for Tender Board approval.
(vi) The Platform can automatically fill in the prescribed Tender Report with the information obtained from the Platform and it shall allow the Subject Officers / PRO Users to make edits on certain fields before sending it out for approval.
Rationale:
None
Acceptance / Fit Criteria:
During , the Platform allows for the export of the required Tender Report in Word format and supports mail merge using reserved placeholders.
Procurement Strategy e-Form related data:
RFQ / Tender exercise related data:
Note: The list of reserved placeholders will be provided in a later SA&D stage.
The Platform used a third-party .NET application API, GemBox.Document, which offers basic text formatting, table structures, and simple styling options for converting HTML to Word format. In comparison, the comprehensive features provided by the Microsoft Word software application include advanced formatting capabilities, intricate layout designs, detailed customization options for fonts, styles, and formatting, and support for complex document structures such as headers, footers, and references. To access the full range of Word format features, HKTDC can provide the Microsoft Word software license for integration with the Platform.
If the total contract price exceeds a specified amount outlined in the PPG, a Tender Report must be attached for Tender Board approval.
Procurement Officers can make edits to the Word document before attaching it for approval.
The prescribed Tender Report template can be managed by System admin users as follows:
Add Template: System admin users can upload a new template, define the template name, and specify the effective date.
Update Template: System admin users can modify the template name, change the effective date, and set the template to inactive status.
Delete Template: System admin users can physically delete a template, but this action is restricted under the condition that the template has not already been used in Tender exercises.
Dependencies:
None
Tailoring Guidelines:
None
Change History:
None