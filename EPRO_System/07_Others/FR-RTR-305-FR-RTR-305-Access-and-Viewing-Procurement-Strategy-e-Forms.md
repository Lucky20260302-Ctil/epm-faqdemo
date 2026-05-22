---
project: EPRO
issue_key: ''
issue_type: Functional Requirement
status: Specified
tags:
- epro
- functional-requirement
- spec
title: 'FR-RTR-305: Access and Viewing Procurement Strategy e-Forms'
quality: complete
category_label: Others
created: '2026-05-22'
---

## 需求描述

B(v)	Other Requirements
3.19.	The Platform shall have the following features:
(a) There shall be search, sorting and filter functions of RFQ / tender based on user privilege and specified selection criteria (e.g. by department, closing date, assessment approach, invitation types, relevant document reference number of upstream or downstream stages, etc.). The selection criteria shall be different for Internal Users and external suppliers.
(b) The search results shall be shown in a systematic way designed by the Contractor with related information, e.g. PR / Tender number and title, issuance and closing dates, etc.
(c) By selecting a search result item, all related details, including the following, shall be shown:
(i) All published documents, including Tender Documents, Tender Query and Tender Addendum
(ii) Immediate information on which suppliers have acknowledged receipt of the invitation documents and, if applicable, replied attendance of briefing / site visit or signing of Non-Disclosure Undertaking (for Internal Users only)
(iii) The number of declined offer and quotations / tender received (for Internal Users only)
(d) Subject to the HKTDC’s security setting, Internal Users shall only have access to RFQ / tender information for themselves, their responsible department(s) or all departments.

## 驗收標準

The Platform supports the following user roles to search, list, and view Procurement Strategy e-Forms, including Part I, Part II, and Part III, as well as their associated RFQ/Tender exercises:
The Platform supports to access to view change history, amendment history, and approval history.
The Platform supports wildcard functionality for keyword search, allowing internal users to search for matches between the entered value and fields:
Concatenated first name and last name of Procurement Officer (Buyer)
The Platform supports basic search functionality that allows internal users to narrow down their search by using one or more of the following search fields:
RFQ / Tender / Waiver / Low-Value Purchase:
Other than specific user role (to be defined), it is supposed the search results will be restricted to his/her own department(s).
System Reference Number
PS Title, partial word search, suggest drop-down list.Nature of Purchase, drop down list to choose (RFQ / Tender / Waiver / Low-Value Purchase / Exemption List)
FMS PR Number
FMS PO Number
Procurement Method, drop down list to choose
Budget Division/Department, drop down list to choose
Purchasing Division/Department, drop down list to choose
User Division/Department, drop down list to choose
Bulk Procurement: All, Yes, or No
Buyer / Co-Buyer, if the staff for a specific role was entered in ProSmart through integration with the workflow, the staff name will be "Fanny WY Kam". This means that the first name and last name concatenated will be input as "Fanny Kam", but the Platform will search the results "Fanny WY Kam".
Procurement Officer, (i.e. the responsible F&A User)
Reviewer / Endorser / Approver
FMS Supplier number: starting with input string or exact match
ProSmart Supplier number: starting with input string or exact match
Supplier name: starting with input string, containing input string, or exact match. And, for the suggestion drop-down list in basic search, the drop-down will appear after typing the third letter. For example, typing "ABC" will prompt the Platform to display a drop-down showing "ABC Company".
Procurement/Soucring categories: All, or selection up to 2 levels
Financial Year (e.g. 24-25), financial year is from 1 April to 31 March of following year
Range of Budgeted Amount
Not Exceeding $10,000
$10,001 to $50,000
$50,001 to $250,000
$250,001 to $500,000
$500,001 to $1,000,000
$1,000,001 to $2,000,000
Exceeding $2,000,000Range of Awarded Amount
Not Exceeding $10,000
$10,001 to $50,000
$50,001 to $250,000
$250,001 to $500,000
$500,001 to $1,000,000
$1,000,001 to $2,000,000
Exceeding $2,000,000
Date range of First Submission for Approval (FMS PR / PS / Invitation Issuance / Award / FMS PO)
Date range of Approval (FMS PR / PS / Invitation Issuance / Award / FMS PO)
Supplier:
Supplier Name, auto-complete against FMS and ProSmart Database partial word search, suggest drop-down list
FMS Supplier Number
ProSmart Supplier Number
Supplier Type, (Pre-register / Potential (completed pre-registration) / Registered (completed full registration / existing vendors in FMS) / Approved (awarded with tenders)
Supplier Category, All, or selection up to 2 levels
Location, dropdown list to choose registered country
Range of Overall Performance Score
Below 6
6
7-8
9-10
Date range of First Submission for Approval (Pre-registration / Full registration)
Date range of Approval (Pre-registration / Full registration)
The Platform supports internal users to customize their listings by sorting options, including:
System Reference Number
Submission date followed by System Reference Number
Approval date followed by System Reference Number
The Platform supports internal users to export the results in Excel format.
The Platform supports internal users to access and download the corresponding e-Forms, in PDF format.

## 依賴項

Report requirements


