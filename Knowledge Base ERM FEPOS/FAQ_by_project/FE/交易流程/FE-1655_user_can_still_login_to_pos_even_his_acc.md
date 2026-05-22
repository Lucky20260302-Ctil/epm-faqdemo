---
tags: [faq, fe, 交易流程]
component: "Front End v720.02"
symptom: "After Tico's clarification, the case should be that the user can still log in to the POS even if his"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: FE-1655
resolved: 2025-08-28
fix-version: ""
---

# FE-1655: User can still login to POS even his account is not in any RTM Domain Group

## 問題

After Tico's clarification, the case should be that the user can still log in to the POS even if his account is not in any RTM domain group. This is because we updated the ENABLEDASECROLE to 'N', which disables domain group validation. Instead, the POS system will use the user role from the POS database, allowing the user to log in.
The current process of 'Check Sales Staff user group' involves checking the user role in the POS database to see if it exists in the AD membership. To address this issue, we should set ‘ENABLEDASECROE to ‘Y’,  and then we need to modify the 'Check Sales Staff user group' process to verify whether the user is in any RTM domain group (RTMHK_FE*). If the user belongs to any RTM domain group, he will be allowed to log in with the user role from the POS database. Otherwise, the login will be rejected.
If you agree with this approach, we will proceed with modifying the program to resolve this issue.
<u>**The current logic:**</u>
<u>**To be changed logic:**</u>

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-08-28
### Jira Comments (9 則)
**Andrew_Au** (2025-03-20):
@@Gavin Zhou  FYI
**Sang** (2025-03-20):
@@Andrew_Au Any WM can use to test JC WIAM (Jira FE-1655) ?
**Sang** (2025-03-20):
@@Bobby @@Gavin Zhou @@Andrew_Au @@Cy Lau
Amended program uploaded to \\ds411\share\POS_FE_Release\20250320 JC RTM v720.01R07G Patch
'720.01R07G
1.
**Andrew_Au** (2025-03-20):
@@Anson Cheung  Please compile the setup package.
**Anson Cheung** (2025-03-20):
@@Gavin Zhou 
Release package:
\\172.16.183.201\supportftp\20250320\setup_72.0107.5001.exe
**Anson Cheung** (2025-03-21):
@@Gavin Zhou 
Release package:
\\172.16.183.201\supportftp\20250321\setup_72.0107.5002.exe
**Andrew_Au** (2025-03-21):
\\172.16.183.201\localuser\support\20250321\setup_72.0107.5006.exe
**Andrew_Au** (2025-03-21):
@bobby 
Andrew_Au March 21, 2025 at 2:00 PM
\\172.16.183.201\localuser\support\20250321\setup_72.0107.5006.exe\setup_72.0107.5006.exe
**Andrew_Au** (2025-08-28):
The POS package released. Close the ticket.

## 相關資訊

- Jira: [FE-1655](https://ctil.atlassian.net/browse/FE-1655)
- Fix Version: 未記錄
- 解決日期: 2025-08-28
