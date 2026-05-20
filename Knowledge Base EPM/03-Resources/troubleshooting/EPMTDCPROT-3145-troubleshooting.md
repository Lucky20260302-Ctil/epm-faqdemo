---
tags: bug, jira, tdc-hotfix, uat-phase1-hotfixbatch2, hotfix
component: Reporting & Export
symptom: ""
root-cause: ""
solution: "2 Test Result ： The report data exported by Summary of Query Response is the same as the data submitted by Query Respons"
jira: EPMTDCPROT-3145
resolved: 2026-01-14
---

# EPMTDCPROT-3145: EPRO-791 [Phase 1 Hot Fix Batch 2] Report Generation Error and Misalignment

## 問題

[Link:https://hktdc.atlassian.net/browse/EPRO-791]

## 根因

HotFix2 Test Result ：The Closing date and Time (Original) and Closing date and Time (Final) Data in the Tender/RFO Data View report have been modified correctly and the test has passed
item 3： Summary of Queries
HotFix2 Test Result： 5 suppliers submitted the Raise RFQ/Tender Query. The buyer passed 2 of the Query checking. The data displayed in the report was correct and the test was passed
@712020:c211d22b-b468-4c45-9400-0bfac9893906  Please review
HotFix2 Test Result ： buyer selects Not Attended in Briefing/Site Visit Attendance Confirmation, report shows correct, test passed
@640691130a4a47fb8d2394b0  Please check again.
HotFix 2 Test Result ： The report data exported by Summary of Query Response is the same as the data submitted by Query Response lssuance. The test is passed
item 5：Briefing/Site Visit Sign-up Summary
UAT Test Result ： buyer selects Not Attended in Briefing/Site Visit Attendance Confirmation, report shows correct, test passed
item 4：RFQ/Tender Data View
UAT Test Result ：The Closing date and Time (Original) and Closing date and Time (Final) Data in the Tender/RFO Data View report have been modified correctly and the test has passed
UAT Test Result ： The report data exported by Summary of Query Response is the same as the data submitted by Query Response lssuance. The test is passed
item 3： Summary of Queries
UAT Test Result： 4 suppliers submitted the Raise RFQ/Tender Query. The buyer passed 3 of the Query checking. The data displayed in the report was correct and the test was passed
@712020:c211d22b-b468-4c45-9400-0bfac9893906

## 解法

2 Test Result ： The report data exported by Summary of Query Response is the same as the data submitted by Query Response lssuance. The test is passed

## 相關問題

- [[EPRO-791]]

