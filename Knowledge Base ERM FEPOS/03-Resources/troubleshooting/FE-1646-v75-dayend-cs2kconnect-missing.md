---
tags: [bug, production, hotfix]
component: Front End
symptom: "V75 upgrade causes 10+ PRC stores daily dayend issue — missing dayend info upload due to cs2kconnect not being triggered"
root-cause: "V75 removed the forced cs2kconnect execution after Till Day End and Consolidated Day End that existed in V72"
solution: "Add call to upload PCD Exe (tblconfig.UPLOADPROG) after Day End writes True PCD; wait for existing upload to complete before starting new instance"
jira: FE-1646
resolved: 2025-10-10
---

# FE-1646: V75 Day End Missing cs2kconnect Schedule

## 問題

PRC region stores upgraded to V75 experienced 10+ stores daily with dayend issues — the dayend info was not uploaded, causing missing records. Investigation found the cs2kconnect schedule was not running after day end.

Affected stores include PRC region (批量出現) and later TW region (OF82, 10 stores callout, 3 verified).

**TW version at fault**: v75.004.1100.0008 (R10, which did NOT include the fix)

**Key finding**: In V72, POS would **force-run cs2kconnect once** after day end. After upgrade to V75, this forced execution was lost. Store staff, unaware of the change, did not wait 10+ minutes, causing mass dayend failures. The issue auto-resolved the next day when cs2kconnect ran on startup and uploaded the pending dayend info.

## 根因

V75 codebase **removed the forced cs2kconnect execution trigger** that existed in V72 after:
- Till Day End
- Consolidated Day End

Without this trigger, stores had to manually wait for the cs2kconnect schedule, and many closed POS before the upload completed.

**Additional config issue**: V72 had `tblconfig.UploadProg = 'C:\CS2000POS\CS2KCONNECT.EXE'`, while V75 defaulted to `'C:\Program Files\CSPlus\CS2KCONNECT.EXE'`. Stores with incorrect paths would silently fail.

## 解法

**Fix in v750.04R09C1, v750.04R11, v750.05:**
- After Till Day End and Consolidated Day End write True PCD, add call to upload PCD Exe (`tblconfig.UPLOADPROG`)
- If another upload PCD Exe is already running, wait for configurable seconds (`tblconfig.UPLOADPROGWAITSEC`, max 300 sec) before starting

**Config requirements:**
- Verify `tblconfig.UploadProg` points to the correct cs2kconnect path:
  - V72: `C:\CS2000POS\CS2KCONNECT.EXE`
  - V75: `C:\Program Files\CSPlus\CS2KCONNECT.EXE`

**Patch reference**: `KTS 250312 Jira FE-1646 v750.04R09C1, v750.04R11, v750.05`

## 相關問題

- [[CS-1377]] — Coach Jira reference
- [[FE-1696]] — Related V75 infrastructure fix
