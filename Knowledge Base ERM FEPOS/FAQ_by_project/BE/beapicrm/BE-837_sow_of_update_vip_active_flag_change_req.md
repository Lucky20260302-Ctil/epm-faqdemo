---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "Modify COACH_CRM.exe to handle a new vip_active_flag field in vipmaster file."
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-837
resolved: 2024-04-26
fix-version: ""
---

# BE-837: SOW of Update vip_active_flag change request

## 問題

Modify COACH_CRM.exe to handle a new vip_active_flag field in vipmaster file.

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2024-04-26
### Jira Comments (2 則)
**Bobby** (2024-03-18):
I double checked the vip_insert trigger, and we need to modify it to make it work with the new customer registration. When a row is inserted into the 'vip' table, it should also insert a row into the 'vip_flag' table with the vip_active_flag set to 'Y'. Could you please perform a test on COACH_CRM.exe to see what happens when we add a new VIP record from the VIP Master Data Interface file? Since COACH_CRM.exe also inserts rows into the 'vip_flag' table, I have modified the vip_insert trigger to check if the row already exists before inserting. Please check if COACH_CRM.exe needs to handle the case when a row already exists as well.
Attached is the updated SOW and the SQL to alter sp_active_vip_flag stored procedure for your reference.
2	Remove the Triggers from vip table in SQL Server database
Since eName new customer registration, the new created record should be active by default. Therefore, we need to modify the vip_insert trigger always update the vip_active_flag = ‘Y’ when insert a row into vip table. The update and delete triggers will be removed. The vip_active_flag will be updated by VIP Master Data Interface from AGREX instead.
•	Remove vip_delete and vip_update triggers
•	Modify vip_insert trigger
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER trigger [dbo].[vip_insert] ON  [dbo].[vip] 
After insert
AS
BEGIN
declare @ID_NO nvarchar(15)
declare @VIP_NO nvarchar(25)
declare @VIP_type nvarchar(15)
set @ID_NO = (SELECT vip_id_no FROM inserted);
set @vip_no = (SELECT vip_no FROM inserted);
set @vip_type = (SELECT vip_type FROM inserted);
IF NOT EXISTS (SELECT 1 FROM vip_flag WHERE [vip_no] = @vip_no)
BEGIN
INSERT INTO vip_flag ([vip_no], [vip_active_flag], [vip_id_no])
VALUES (@vip_no, 'Y', @ID_NO);
END;
END
**Joy Li** (2024-04-25):
Release of COACH_L4.0.0_V70R3.53 - SOW of Update vip_active_flag change request
Release on 2024-03-27 
Tester: Andy
@@Bobby Release email for reference

## 相關資訊

- Jira: [BE-837](https://ctil.atlassian.net/browse/BE-837)
- Fix Version: 未記錄
- 解決日期: 2024-04-26
