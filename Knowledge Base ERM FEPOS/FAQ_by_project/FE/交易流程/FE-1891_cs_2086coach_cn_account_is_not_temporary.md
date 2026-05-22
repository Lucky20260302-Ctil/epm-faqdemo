---
tags: [faq, fe, 交易流程]
component: "Front End"
symptom: "# **Defect Description: Your User Account is Not temporary Prohibited for Login**"
root-cause: "待提取"
solution: "### Jira Comments (7 則)"
jira: FE-1891
resolved: 
fix-version: ""
---

# FE-1891: CS-2086:Coach_CN| Account is Not temporary Prohibited while Login With Locked Account As Cashier & In Admin

## 問題

# **Defect Description: Your User Account is Not temporary Prohibited for Login**
# **🔁 ****Steps to Replicate:**
1. 
2. 
3. 
4. 
5. 
# **❌ ****Actual Result:**** No error throwing**
# **✅ Expected Result: Error should reflect as Your User Account is Now temporary Prohibited for Login**
---
Comment from Joy:
**Issue:**
When a user enters an invalid password more than four times in the CSPLUS application (POS 10.34.103.4), the account becomes locked as expected. However, when attempting to log in again—whether as a Cashier or Admin—the system does **not** display the required error message.
**Actual Result:**
- 
**Expected Result:**
- 
Login
login cashier:
Admin - Change cash flow:

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (7 則)
**Sang** (2026-02-24):
@@Joy Li  Please check configuration ‘LOGIN_CONTROL’ is enable
**Joy Li** (2026-02-24):
@@Sang checked in testing PC
|  |  |
| --- | --- |
Login
login cashier:
Admin - Change cash flow:
**Sang** (2026-02-24):
@@Joy Li please check is tblconfig.LockAllAccount='Y'
**Joy Li** (2026-02-24):
@@Sang confirmed in testing PC
Please be informed that the behavior observed—where no error message is displayed when a locked user attempts to log in—can be resolved through system configuration.
To enable the correct error handling, kindly update the following configuration:
```
tblconfig.LockAllAccount = Y
```
Once this parameter is set to **“Y”**, the system will properly enforce the lockout mechanism and display the expected error message:
**“Your User Account is Now Temporarily Prohibited for Login.”**
**Automation for Jira** (2026-02-24):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Automation for Jira** (2026-02-24):
Issue has been created since
Days since: 0
Week since : 0
Issue due date difference
Days since : 
Weeks since:
**Joy Li** (2026-02-24):
@@Joy Li @@Tovi Wang Please noted

## 相關資訊

- Jira: [FE-1891](https://ctil.atlassian.net/browse/FE-1891)
- Fix Version: 未記錄
- 解決日期: 未記錄
