---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "Tried to generate 04-17 sales file to landlord."
root-cause: "待提取"
solution: "### Jira Comments (12 則)"
jira: BE-1066
resolved: 
fix-version: ""
---

# BE-1066: [INC2961835] SG store OC554 Retrieve 04-17 sales records to Landlord have error

## 問題

Tried to generate 04-17 sales file to landlord.
showing error: Object reference not set to an instance of an object.
Please help to check and advise
Thanks!
1.
查看interface log发现retrieve 04-17的 sales records有error.
Log details:
Sales Data Export / MBSS v1.2 By Sanyo Exteneded -=2025-04-18 01:30:05
Parameter Used
-- config : sample.ini
-- business date : 2025-04-17
-- output path : D:\DCS_OC554\
-- loc code : OC554
Retrieve sales records on 04/17/2025
Escape on following error
Object reference not set to an instance of an object.
Done!
2.retrieve 04-16的 sales records正常，没有error

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (12 則)
**Tovi Wang** (2025-05-09):
@@Anson Cheung As talked.Please help to double check why have error when generating 04-17 sales file to landlord?Thanks!
Follow are Details logs and exe,config:
**Tovi Wang** (2025-05-09):
log path:
\\apawipwposjsw22\SystemInterfaces\MBSS
**Anson Cheung** (2025-05-09):
@@Tovi Wang Please help to run this sql:
```
select a.shop_no, a.jouinv_date, a.jouinv_hour, a.sales_value sales_amount,
a.jouinv_gst_amt sales_tax, ISNULL(b.sales_count, 0) sales_count from
( select '18000043' shop_no, jouinv_date, jouinv_hour, sum(case jouinv_line when '1' then jouinv_gst_amt else 0 end) jouinv_gst_amt,
sum(case jouinv_line when '1' then jouinv_misc_amt else 0 end) jouinv_misc_amt,
sum(dbo.sales_amt(jouinv_loc, jouinv_no, jouinv_line,
jouinv_item_no, jouinv_item_col,
jouinv_item_size, jouinv_item_qty,
jouinv_item_amt, jouinv_item_disc_adj)  -
case jouinv_line when '1' then jouinv_misc_amt else 0 end
) sales_value
from jouinv
where jouinv_date='2025-04-17' and jouinv_loc='OC554'
group by jouinv_date, jouinv_hour
) a left outer join (
select '18000043' shop_no, jouinv_date, jouinv_hour,
count(distinct(jouinv_no)) sales_count
from jouinv
where jouinv_date='2025-04-17' and jouinv_loc='OC554'
and jouinv_item_qty>0
and isnull(jouinv_void_flag, ' ') not in ('1','2')
group by jouinv_date, jouinv_hour
) b on a.shop_no = b.shop_no and a.jouinv_date = b.jouinv_date
and a.jouinv_hour = b.jouinv_hour
order by a.jouinv_date, a.jouinv_hour
```
**Tovi Wang** (2025-05-09):
@@Anson Cheung Bellow is 04-17 sql excute result:
**Tovi Wang** (2025-05-09):
@@Anson Cheung 下面截图是04-18号的 sql excute result for your compare:
**Anson Cheung** (2025-05-12):
@@Tovi Wang can you try to run the program manually in command prompt by using the command: 
HrSALExport.exe simple.ini 20250417
also, you need to change the directory to the .exe file location before running the command.
**Tovi Wang** (2025-05-12):
@@Anson Cheung
“you need to change the directory to the .exe file location before running the command.”
-->How can I change this one?Could you guid me the details please?
**Anson Cheung** (2025-05-12):
@@Tovi Wang use command: cd <folder full path>
sample:
**Tovi Wang** (2025-05-13):
尝试用命令可以正常生成04-17 interface data.
**Andrew_Au** (2025-06-05):
@@Tovi Wang @@pierre.shi Please update the ticket status
**Andrew_Au** (2025-10-08):
@@Tovi Wang @@pierre.shi @@Joy Li Please update the status
**Tovi Wang** (2025-10-09):
Fixed.Please closed.

## 相關資訊

- Jira: [BE-1066](https://ctil.atlassian.net/browse/BE-1066)
- Fix Version: 未記錄
- 解決日期: 未記錄
