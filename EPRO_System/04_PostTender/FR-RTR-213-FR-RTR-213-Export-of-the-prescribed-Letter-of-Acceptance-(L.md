---
project: EPRO
issue_key: ''
issue_type: Functional Requirement
status: Specified
tags:
- epro
- functional-requirement
- spec
title: 'FR-RTR-213: Export of the prescribed Letter of Acceptance (LOA) for the Awarded Suppliers before the'
quality: complete
category_label: Post-Tender
created: '2026-05-22'
---

## 需求描述

3.9.	RFQ / Tender Award and Contract Management
3.9.2	For Tender
(a) Following approval by the Tender Board, Subject Officers shall be required to prepare a Letter of Acceptance (“LOA”) for the awarded suppliers before the PO. The Contract Document shall be prepared and finalised with the awarded suppliers within an agreed-upon timeframe.
(b) Standard templates for LOA and/or Contract Document shall be maintained on the Platform for Subject Officers’ use. Template references shall be provided by the HKTDC. The Platform shall allow Subject Officers to modify the templates and select which clause(s) to exclude (except for mandatory clauses) in the final LOA or Contract Documents in a user-friendly manner.
(c) Upon approval of the PO on FMS, the PO information, including PO number, status and amount, shall be available on the Platform. Internal Users shall upload the duly signed LOA and/or Contract Document to the Platform with input of necessary information for supplier performance review and, if appropriate, a reminder for contract renewal.

## 驗收標準

For Tender exercises,  the approval of the award recommendation, i.e. Procurement Strategy e-Form (Part II), Procurement Officers are required to prepare a Letter of Acceptance (LOA) for the awarded suppliers.
The Platform allows for the export of the required LOA in Word format and supports mail merge using reserved placeholders.
Procurement Strategy e-Form related data:
RFQ / Tender exercise related data:
Note: The list of reserved placeholders will be provided in a later SA&D stage.
The Platform used a third-party .NET application API, GemBox.Document, which offers basic text formatting, table structures, and simple styling options for converting HTML to Word format. In comparison, the comprehensive features provided by the Microsoft Word software application include advanced formatting capabilities, intricate layout designs, detailed customization options for fonts, styles, and formatting, and support for complex document structures such as headers, footers, and references. To access the full range of Word format features, HKTDC can provide the Microsoft Word software license for integration with the Platform.
Procurement Officers can make edits to the Word document before attaching it for approval.
The prescribed Letter of Acceptance (LOA) template can be managed by System admin users as follows:
Add Template: System admin users can upload a new template, define the template name, and specify the effective date.
Update Template: System admin users can modify the template name, change the effective date, and set the template to inactive status.
Delete Template: System admin users can physically delete a template, but this action is restricted under the condition that the template has not already been used in Tender exercises.


