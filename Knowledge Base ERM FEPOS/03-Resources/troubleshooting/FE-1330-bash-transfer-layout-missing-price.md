---
tags: [bug, production]
component: Front End
symptom: "Bash Transfer layout printing missing price information in V7.2 POS"
root-cause: "DotNet control for Bash Transfer layout does not include price field in the print template"
solution: "Modified the Bash Transfer print program to include price information in the layout"
jira: FE-1330
resolved: 2024-01-22
---

# FE-1330: Bash Transfer Layout Missing Printing Price Information

## 問題

After checking V7.2 POS using the DotNet control, the Bash Transfer layout printing is missing the price information on the printed receipt/output.

## 根因

The DotNet control print template for Bash Transfer does not include the price field in its layout definition.

## 解法

Modified the Bash Transfer print program to include price information in the printed layout.

**Fix Version**: `v720.02R07ZL`

_See Jira ticket for resolution details._

## 相關問題

- [FE-1219](https://ctil.atlassian.net/browse/FE-1219) — Deposit return display fix (related print/display issue)
