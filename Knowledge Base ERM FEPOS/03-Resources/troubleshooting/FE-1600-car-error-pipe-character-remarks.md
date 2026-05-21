---
tags: [bug, production, hotfix]
component: Interface
symptom: "CAR error 'Unknown Sales item type code 9999' for transaction MY-OC602-40060402 due to pipe character in user remarks"
root-cause: "CAR interface file uses '|' as field separator; user input in remarks containing '|' breaks the file parsing and causes unknown type code"
solution: "Enhance CAR processing to automatically replace '|' with space in remarks fields before file generation"
jira: FE-1600
resolved: 2025-02-12
---

# FE-1600: CAR Error — Pipe Character in Remarks Breaks File Parsing

## 問題

CAR (Coach Automated Reporting) system returned error "Unknown Sales item type code 9999" for transaction `MY-OC602-40060402` on 12/20. Investigation found the CAR interface file was being parsed incorrectly.

## 根因

The CAR interface file uses the pipe character `|` as its field separator. When a user enters remarks that contain the `|` character, the CAR file parser misinterprets the pipe as a field boundary, causing the file structure to break.

This results in fields being read with wrong values, ultimately causing the "Unknown Sales item type code 9999" error since the parser reads garbage data as the item type code.

**Root cause confirmed**: "The issue caused by user input remarks which contain '|'."

## 解法

**Enhancement applied to CAR processing:**
- Source target: `svn://sanyosvn.ctil.com/svn/cs2000/Trunk/BackEnd.Net(VS2017 FW 4.5.2 NEW)/Coach_CAR`
- Logic: `replace("|", " ")` — automatically remove pipe characters from remarks fields before CAR file generation
- Applies regardless of which channel enters data into the CAR remarks field

**Deployment**: Release at `\\ds411\csms60\delivery\coach\update_coachCAR-2024-01-02`

**Note**: Only the `.exe` needs to be deployed (not full DLL set).

## 相關問題

- [CS-1309](https://hktdc.atlassian.net/browse/CS-1309) — Coach Jira reference
- [FE-1659](https://ctil.atlassian.net/browse/FE-1659) — Related CAR file issue (invalid field)
