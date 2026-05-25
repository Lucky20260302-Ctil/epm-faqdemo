---
project: EPRO
issue_key: ''
issue_type: Functional Requirement
status: Specified
tags:
- epro
- functional-requirement
- spec
title: 'FR-RPT-410: Tender Opening Record (for tenders)'
quality: complete
category_label: Reports
created: '2026-05-22'
---

## 需求描述

D.	Generation of Reports / Documents
- **3.55** Summaries and documents to be generated for the features and functions related to different procurement procedures shall include but not limited to the following: (j) Tender Opening Record (for tenders)
## 驗收標準

The Platform allows the following user role to use this feature:
The Platform supports the feature to export the prescribed Tender Opening Record in Word format for any RFQ/Tender exercise and use mail merge with reserved placeholders:
Procurement Strategy e-Form related data:
RFQ / Tender exercise related data:
RFQ / Tender Opening data:
Note: The list of reserved placeholders will be provided in a later SA&D stage.
The Platform used a third-party .NET application API, GemBox.Document, which offers basic text formatting, table structures, and simple styling options for converting HTML to Word format. In comparison, the comprehensive features provided by the Microsoft Word software application include advanced formatting capabilities, intricate layout designs, detailed customization options for fonts, styles, and formatting, and support for complex document structures such as headers, footers, and references. To access the full range of Word format features, HKTDC can provide the Microsoft Word software license for integration with the Platform.
The prescribed Tender Opening Record template can be managed by System admin users as follows:
Add Template: System admin users can upload a new template, define the template name, and specify the effective date.
Update Template: System admin users can modify the template name, change the effective date, and set the template to inactive status.
Delete Template: System admin users can physically delete a template, but this action is restricted under the condition that the template has not already been used in Tender exercises.

## 依賴項

Report requirements


