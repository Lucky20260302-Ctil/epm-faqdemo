---
project: EPRO
issue_key: ''
issue_type: Functional Requirement
status: Specified
tags:
- epro
- functional-requirement
- spec
title: 'FR-GR-014: File Upload Feature'
quality: complete
category_label: General Requirements
created: '2026-05-22'
---

## 需求描述

3.1.16	The Platform shall support the uploading of documents in commonly used formats, such as PDF, Microsoft Excel, Microsoft Word, Microsoft PowerPoint, Microsoft Project, JPEG, MP4, Adobe Illustrator, email files, zipped files, etc. File size control shall be available and configurable, allowing users to manage the maximum file size for uploads. Please refer to Sections 3.1.6, 3.4.3 and 3.6.3 for required capacity of document uploading and retention.

## 驗收標準

Internal Users should be able to upload files for final Tender and addendum documents and etc. according to the specified formats and size limits:
External Suppliers should be able to upload files for RFQ and Tender supplier submissions, and etc. in the specified formats and sizes:
The configuration of supported file formats and sizes globally can be done by System admin users.
The file upload function should allow batch uploads, enabling users to select multiple files or drag and drop them from Windows File Explorer.
Files are uploaded using 10MB file chunks in the file upload function.
The Use Case will be documented in the RFQ and Tender section of the e-Procurement Requirements and Supplier Management Requirements.


