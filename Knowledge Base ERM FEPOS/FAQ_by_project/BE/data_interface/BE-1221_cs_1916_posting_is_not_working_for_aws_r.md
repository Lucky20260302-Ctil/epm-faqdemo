---
tags: [faq, be, data_interface]
component: "Posting"
symptom: "During testing we found that QA posting not working for all regions. like JP & TW region, we could s"
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-1221
resolved: 2026-02-26
fix-version: ""
---

# BE-1221: [CS-1916] POSTING is not working for AWS regions - QA Env

## 問題

During testing we found that QA posting not working for all regions. like JP & TW region, we could see the data already polling to sqlpcda table, then we try to run the posting via Tidal or run it manually from job server. Data still not posted, it block our testing now. kindly help to check, thanks
Troubleshooting:
Checked 202512-22 posting log found follow error:
2025-12-22 14:44:10.812 [TERMINATE]/  Main ex:The network path was not found.
2025-12-22 14:44:10.874 [TERMINATE]/ Main ex   at [System.IO](http://System.IO).__Error.WinIOError(Int32 errorCode, String maybeFullPath)
   at System.IO.FileStream.Init(String path, FileMode mode, FileAccess access, Int32 rights, Boolean useRights, FileShare share, Int32 bufferSize, FileOptions options, SECURITY_ATTRIBUTES secAttrs, String msgPath, Boolean bFromProxy, Boolean useLongPath, Boolean checkHost)
   at System.IO.FileStream..ctor(String path, FileMode mode, FileAccess access, FileShare share, Int32 bufferSize, FileOptions options, String msgPath, Boolean bFromProxy, Boolean useLongPath, Boolean checkHost)
   at System.IO.StreamWriter.CreateFile(String path, Boolean append, Boolean checkHost)
   at System.IO.StreamWriter..ctor(String path, Boolean append, Encoding encoding, Int32 bufferSize, Boolean checkHost)
   at System.IO.StreamWriter..ctor(String path, Boolean append, Encoding encoding)
   at prj_ic8006.bg_ic8006.prepare_pcdfiles(DateTime& timeout_chkpoint, Int32& rec_count)
   at prj_ic8006.bg_ic8006.posting_loop()
   at prj_ic8006.bg_ic8006.Main(Cls_CSDBObj dbObj, String link_node)
2025-12-22 14:44:10.890 insert_pstlog (node:- MQ_A); msg:- [TERMINATE]Main/The network path was not found.
; filesize:- 0)
2025-12-22 14:44:11.171 update_pstnode_post_flag (node:- MQ_A; post_flag:- D)
2025-12-22 14:44:11.499 stop_taskstat (node:- MQ_A)
2025-12-22 14:44:11.762 insert_pstlog (node:- MQ_A); msg:- Posting Terminated with ERROR; filesize:- 0)
2025-12-22 14:44:11.996
END ic8006_Load() At 2025-12-22 14:44:11

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2026-02-26
### Jira Comments (3 則)
**Cy Lau** (2026-01-19):
Testing VM : 172.16.138.8
**Cy Lau** (2026-01-19):
Situation : 
There’s an enhancement for CSDataInterface and CS2KBNV1 for itmast Lock function which locking items would not be updated by interface.
The CSDataInterface using legacy / different version of Common DLL  which conflicts with CS2KBNV1 Obj , commonly used by polling and posting:
In order to compactable with versions, standalone folder for CSDataInterface would be highly recommended.
Amendment :
1. 
2. 
Installation Path from OBJ to OBJ/CSDataInterface
Calling cmd scripts :
- 
- 
Sample :
Standalone : \\172.16.138.8\csms70\OBJ\CSDataInterface
Command Scripts:
---
After standalone folder for CSDataInterface , it is believed that POSTing and Polling , CSDataInterface Locking would be avaliable .
@@Sherman tse  Please give out a confirmation by QAQC team
cc. @@Joy Li
**Automation for Jira** (2026-02-26):
Issue has been created since
Days since: 64
Week since : 9
Issue due date difference
Days since : 
Weeks since:

## 相關資訊

- Jira: [BE-1221](https://ctil.atlassian.net/browse/BE-1221)
- Fix Version: 未記錄
- 解決日期: 2026-02-26
