---
project: EPRO
issue_key: ''
issue_type: Functional Requirement
status: Specified
tags:
- epro
- functional-requirement
- spec
title: 'FR-SMR-010: Prevent Duplicate Update Request on a Supplier Record'
quality: complete
category_label: Supplier
created: '2026-05-22'
---

## 需求描述

3.54	To prevent duplicate update request on a supplier record, the Platform should integrate with FMS Supplier Platform. The Platform should share the non-completed change requests, enabling FMS Supplier Platform to take appropriate measures to block Internal User from submitting duplicate request for the same supplier record.

## 驗收標準

The Platform supports a block mode feature for when supplier information change is submitted on the Platform by the supplier or on FMS by internal users.
< Screen mock-ups will be provided in the later SA&D stage >
The block mode will be released upon the completion of the previous update.
Outlined below are specific scenarios with their corresponding exception handling:
The interface requirements will be documented and reviewed during the subsequent SA&D stage.

## 依賴項

Supplier Information Change
Suspension or Permanent Termination of specific Supplier(s) under special circumstances
Interface requirements


