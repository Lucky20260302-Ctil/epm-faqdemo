---
tags: bug, jira, tdc-hotfix
component: Tender & RFQ
symptom: "Tender Closing Date and Time is 1 November 2025 12:00 noon."
root-cause: ""
solution: ""
jira: EPMTDCPROT-3127
resolved: 2025-11-28
---

# EPMTDCPROT-3127: EPRO-804 [Health Check] Price Score was calculated before Closing Date and Time

## 問題

[Link:https://hktdc.atlassian.net/browse/EPRO-804] 
[Image]
Tender Closing Date and Time is 1 November 2025 12:00 noon.
When Buyer generated RFQ / Tender Data View Report, the price score was calculated in the column of Overall Assessment Score.
This will let buyer induce the price offered by tenderers before closing date and technical assessment. As an compliance issue, this must be fixed before launch for IT pilot projects.
cc [accountid:5df204e72702bc0ec7e7af0b] [accountid:5f2a0d1b170ffc0023ffab32] [accountid:712020:9d3711ef-d393-4f93-9a23-9f1aa6e398fa]

## 解法

_See Jira ticket for resolution details._

## 相關問題

- [[EPRO-804]]

