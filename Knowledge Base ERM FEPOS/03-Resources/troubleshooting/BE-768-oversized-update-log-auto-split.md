---
tags: [bug, production, hotfix]
component: Backend
symptom: "PRC stores failed to auto-split oversized update log file (>15,000 records) causing zlog file creation failure"
root-cause: "The send log file routine fails to create multiple zlog files when the update log exceeds the maximum record threshold"
solution: "Fix the send log file splitting logic to properly create multiple zlog files when the update log exceeds the size limit"
jira: BE-768
resolved: 2023-06-16
---

# BE-768: Failed to Auto-Split on Oversized Update Log File

## 問題

PRC region stores reported that the system failed to auto-split oversized update log files. When the update log exceeds **15,000 records**, the system should split the log into multiple files, but instead it fails to create any zlog files.

This prevents the update log from being properly uploaded and processed.

## 根因

The send log file routine has a threshold check for oversized logs (>15,000 records), but the splitting mechanism fails when triggered. Instead of creating multiple zlog files (each under the threshold), the process fails entirely and produces no output.

The exact failure point is in the logic that handles the transition between splitting the file and creating the next segment.

## 解法

Fix applied to correct the send log file splitting logic, ensuring oversized update logs are properly split into multiple zlog files when the record count exceeds 15,000.

**Fix Version**: `BE-V70R3.14a`

## 相關問題

- [[CS-552]] — Original issue reference
