---
project: EPRO
issue_key: ''
issue_type: Functional Requirement
status: Specified
tags:
- epro
- functional-requirement
- spec
title: 'FR-GR-022: Support for Partial Word Search and Search Suggest Drop-down Feature'
quality: complete
category_label: General Requirements
created: '2026-05-22'
---

## 需求描述

    - **3.1.25** The search functions shall support partial word search and provide a search suggest drop-down list based on the searching history and related databases.
## 驗收標準

The Platform does not support search history.
For search based on related databases, it is mainly for supplier search only. Users can input a string with auto wildcard for keyword search and basic search by field. For example, typing "Computer" will filter a list of supplier names starting with "Computer" in the database, or containing "Computer" in between or at the end.
< Screen mock-ups will be provided in the later SA&D stage >
For the suggest drop-down list in basic search, the drop-down will appear after typing the third letter. For example, typing "ABC" will prompt the Platform to display a drop-down showing "ABC Company".
< Screen mock-ups will be provided in the later SA&D stage >
The Use Case will be documented in the RFQ and Tender section of the e-Procurement Requirements and Supplier Management Requirements.


