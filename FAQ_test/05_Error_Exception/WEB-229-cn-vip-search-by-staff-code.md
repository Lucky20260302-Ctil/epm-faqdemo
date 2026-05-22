---
project: WEB
title: "WEB-229: CN VIP search by staff code"
issue_key: WEB-229
issue_type: Bug PRD
status: Closed
faq_score: 6.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, web, error_exception, beapi]
jira_url: "https://ctil.atlassian.net/browse/WEB-229"
created: 2022-06-13
resolved: 2022-06-23
resolution: Done
has_images: False
---

# WEB-229: CN VIP search by staff code

## 問題描述

exec sp_executesql N'SELECT top (100) * FROM vip  where [vip.vip_staff_no=@vip_staff_no](mailto:vip.vip_staff_no=@vip_staff_no) order by vip.vip_no',N'@excludeVipEmail nvarchar(4000),@excludeVipName nvarchar(4000),@prev_no nvarchar(4000),@vip_email nvarchar(4000),@vip_tel_1 nvarchar(4000),@vip_tel_2 nvarchar(4000),@vip_id_no nvarchar(4000),@vip_no nvarchar(4000),@vip_name1 nvarchar(4000),@vip_first_name nvarchar(4000),@vip_last_name nvarchar(4000),@vip_staff_no nvarchar(6),@vip_kana_first_name nvarchar(4000),@vip_kana_last_name nvarchar(4000)',@excludeVipEmail=N'',@excludeVipName=N'',@prev_no=N'',@vip_email=N'',@vip_tel_1=N'',@vip_tel_2=N'',@vip_id_no=N'',@vip_no=N'',@vip_name1=N'',@vip_first_name=N'',@vip_last_name=N'',@vip_staff_no=N'657477',@vip_kana_first_name=NULL,@vip_kana_last_name=NULL

– 300 s

exec sp_executesql N'SELECT top (100) * FROM vip  where (vip.vip_tel_1 = @vip_tel_1 OR vip.vip_tel_2 = @vip_tel_1) order by vip.vip_no',N'@excludeVipEmail nvarchar(4000),@excludeVipName nvarchar(4000),@prev_no nvarchar(4000),@vip_email nvarchar(4000),@vip_tel_1 nvarchar(11),@vip_tel_2 nvarchar(4000),@vip_id_no nvarchar(4000),@vip_no nvarchar(4000),@vip_name1 nvarchar(4000),@vip_first_name nvarchar(4000),@vip_last_name nvarchar(4000),@vip_staff_no nvarchar(4000),@vip_kana_first_name nvarchar(4000),@vip_kana_last_name nvarchar(4000)',@excludeVipEmail=N'',@excludeVipName=N'',@prev_no=N'',@vip_email=N'',@vip_tel_1=N'15001838033',@vip_tel_2=N'',@vip_id_no=N'',@vip_no=N'',@vip_name1=N'',@vip_first_name=N'',@vip_last_name=N'',@vip_staff_no=N'',@vip_kana_first_name=NULL,@vip_kana_last_name=NULL

– 14 ms

 

 

Bo Li updated sql:

=====

exec sp_executesql N'SELECT top (100) * FROM vip  where [vip.vip_staff_no=@vip_staff_no](mailto:vip.vip_staff_no=@vip_staff_no) order by vip.vip_no',N'@excludeVipEmail nvarchar(4000),@excludeVipName nvarchar(4000),@prev_no nvarchar(4000),@vip_email nvarchar(4000),@vip_tel_1 nvarchar(4000),@vip_tel_2 nvarchar(4000),@vip_id_no nvarchar(4000),@vip_no nvarchar(4000),@vip_name1 nvarchar(4000),@vip_first_name nvarchar(4000),@vip_last_name nvarchar(4000),@vip_staff_no varchar(6),@vip_kana_first_name nvarchar(4000),@vip_kana_last_name nvarchar(4000)',@excludeVipEmail=N'',@excludeVipName=N'',@prev_no=N'',@vip_email=N'',@vip_tel_1=N'',@vip_tel_2=N'',@vip_id_no=N'',@vip_no=N'',@vip_name1=N'',@vip_first_name=N'',@vip_last_name=N'',@vip_staff_no='657477',@vip_kana_first_name=NULL,@vip_kana_last_name=NULL

 



## 相關資訊

- **Jira:** [WEB-229](https://ctil.atlassian.net/browse/WEB-229)
- **解決方式:** Done