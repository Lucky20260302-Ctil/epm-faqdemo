---
tags: [faq, be, beapicrm]
component: "API"
symptom: "1.2025-01-01 memo OC65-20002034 total amount should be 4555.00."
root-cause: "待提取"
solution: "### Jira Comments (19 則)"
jira: BE-985
resolved: 
fix-version: ""
---

# BE-985: Total amount duplicate when syncing memo OC65 - 20002034 to CN CRM side

## 問題

1.2025-01-01 memo OC65-20002034 total amount should be 4555.00.
Memo OC65-20002034 was voided by OC65-20002036
2.But CRM side received the total amount is '9110'
3.I checked the CRM log,Can also find 2 same SKU.Please help to check the RCA why we send the same SKU twice to CRM?

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (19 則)
**Tovi Wang** (2025-01-15):
@@Cy LauCould you help to check the RCA why we send the same SKU twice to CRM?How to avoid the issue happend again?
**Cy Lau** (2025-01-15):
@@Anson Cheung  believe as Axicom CRM , please check
**Cy Lau** (2025-01-15):
@@Tovi Wang  Please help @@Anson Cheung  for the exe build date and time
**Anson Cheung** (2025-01-15):
@@Tovi Wang Please provide the create date of CRMSanyoPhaseInterface.exe, thanks
**Tovi Wang** (2025-01-15):
@@Anson Cheung The CRMSanyoPhaseInterface.exe created in 2024-12-21 11:37 PM.PLease help to check.Thanks!
**Anson Cheung** (2025-01-15):
I found the duplicate item have different serail_coupon_number
@@Tovi Wang can you help to get the result of below sql?
```
drop table if exists #temp_coustatus
select  ltrim(rtrim(coustatus_no)) as coustatus_no,coustatus_redeem_loc,coustatus_redeem_no   
into #temp_coustatus
from coustatus coustatus  
where
len(coustatus_no)>0  
group by coustatus_no,coustatus_redeem_loc,coustatus_redeem_no   
drop table if exists #temp_coustatus_line;      
select       
    coustatus_redeem_loc
    ,coustatus_redeem_no      
    ,replace(substring(coustatus_no,1,len(coustatus_no)-1),',','&') as coustatus_no      
    into #temp_coustatus_line      
    from      
    (      
    select       
    coustatus_redeem_loc
    ,coustatus_redeem_no      
    ,coustatus_no=(        
    select coustatus_no +N',' from #temp_coustatus as b where b.coustatus_redeem_loc = a.coustatus_redeem_loc and a.coustatus_redeem_no=b.coustatus_redeem_no for xml path('')      
    )       
    from #temp_coustatus as a       
    group by  coustatus_redeem_loc,coustatus_redeem_no      
    ) as t      
where len(t.coustatus_no)>0    
and coustatus_redeem_loc = 'OC65' and coustatus_redeem_no = '20002034'
order by coustatus_redeem_loc 
select *from #temp_coustatus_line
```
**Tovi Wang** (2025-01-15):
@@Anson Cheung direct run bellow sql in DB?right?
`drop table if exists #temp_coustatus select ltrim(rtrim(coustatus_no)) as coustatus_no,coustatus_redeem_loc,coustatus_redeem_no into #temp_coustatus from coustatus coustatus where len(coustatus_no)>0 group by coustatus_no,coustatus_redeem_loc,coustatus_redeem_no drop table if exists #temp_coustatus_line; select coustatus_redeem_loc ,coustatus_redeem_no ,replace(substring(coustatus_no,1,len(coustatus_no)-1),',','&') as coustatus_no into #temp_coustatus_line from ( select coustatus_redeem_loc ,coustatus_redeem_no ,coustatus_no=( select coustatus_no +N',' from #temp_coustatus as b where b.coustatus_redeem_loc = a.coustatus_redeem_loc and a.coustatus_redeem_no=b.coustatus_redeem_no for xml path('') ) from #temp_coustatus as a group by coustatus_redeem_loc,coustatus_redeem_no ) as t where len(t.coustatus_no)>0 and coustatus_redeem_loc = 'OC65' and coustatus_redeem_no = '20002034' order by coustatus_redeem_loc select *from #temp_coustatus_line`
**Anson Cheung** (2025-01-15):
@@Tovi Wang yes
**Tovi Wang** (2025-01-16):
@@Anson Cheung the result for your reference.
**Tovi Wang** (2025-01-20):
@@Anson Cheung May I know anything new update please?Thanks!
**Anson Cheung** (2025-01-20):
cannot reproduce in my env,
@@Tovi Wang can you help to get the result of below sql?
```
drop table if exists #temp_coustatus
                        select  ltrim(rtrim(coustatus_no)) as coustatus_no,coustatus_redeem_loc,coustatus_redeem_no   
                        into #temp_coustatus
                        from coustatus coustatus  
                        where
                        len(coustatus_no)>0  
                        group by coustatus_no,coustatus_redeem_loc,coustatus_redeem_no   
                        drop table if exists #temp_coustatus_line;      
                        select       
                            coustatus_redeem_loc
                            ,coustatus_redeem_no      
                            ,replace(substring(coustatus_no,1,len(coustatus_no)-1),',','&') as coustatus_no      
                            into #temp_coustatus_line      
                            from      
                            (      
                            select       
                            coustatus_redeem_loc
                            ,coustatus_redeem_no      
                            ,coustatus_no=(        
                            select coustatus_no +N',' from #temp_coustatus as b where b.coustatus_redeem_loc = a.coustatus_redeem_loc and a.coustatus_redeem_no=b.coustatus_redeem_no for xml path('')      
                            )       
                            from #temp_coustatus as a       
                            group by  coustatus_redeem_loc,coustatus_redeem_no      
                            ) as t      
                        where len(t.coustatus_no)>0    
                        order by coustatus_redeem_loc  
                        drop table if exists #jouinv
						SELECT *
						INTO #jouinv
						FROM jouinv WHERE jouinv_loc = 'OC65' and jouinv_no = '20002034' 
                                        SELECT jouinv_loc AS store_code
		                        ,jouinv_vip_no AS vip
		                        ,'' AS ouid
		                        ,'' AS order_id
		                        ,CONVERT(varchar, jouinv_date, 23) + ' ' + RIGHT('00' + CONVERT(VARCHAR, jouinv_hour), 2) + ':' + RIGHT('00' + CONVERT(VARCHAR, jouinv_mn), 2) + ':59' AS dateTime
		                        ,jouinv_cust_age AS age_group
		                        ,jouinv_cust_sex AS sex
		                        ,jouinv_cust_nation AS nationality
		                        ,jouinv_no AS sales_memo
		                        ,'POS' AS source
		                        ,jouinv_item_no AS item
		                        ,jouinv_item_col AS color
		                        ,jouinv_item_size AS size
		                        ,itmast_desc AS description
		                        ,itmast_cat AS category
		                        ,itmast_subcat AS sub_cat
		                        ,jouinv_salady_code AS salesman
		                        ,jouinv_item_qty AS qty
                                ,jouinv_item_cost AS cost
                                ,itmast_retail_price_bx AS current_retail
		                        ,jouinv_item_list_price AS original_price
		                        ,jouinv_disc
                                ,CASE WHEN jouinv_item_qty = 0 THEN 0 ELSE jouinv.jouinv_item_sell_price END AS unit_net_sale
                                ,jouinv.jouinv_item_sell_price*jouinv.jouinv_item_qty - jouinv.jouinv_item_disc_adj AS total_net_sales
                                ,REPLACE(LTRIM(RTRIM(jouinv.jouinv_remarks)), ',', ';') as remark
		                        ,jouinv_void_flag AS void
			                    ,RTRIM(jouinv_void_no) AS void_ref
								,REPLACE(LTRIM(RTRIM(jouinv.jouinv_dep_no)), ',', ';') AS settle
								,jouinv_ret_inv_loc AS return_original_loc
								,jouinv_ret_inv_no AS return_original_no
                                ,jouinv_cust_nation AS nationality
								,LTRIM(RTRIM(joudis_1.joudis_disc_code)) AS event_id
								,REPLACE(LTRIM(RTRIM(joudis_2.joudis_disc_code)), ',', ';') AS memo_level
								,'' AS memo_coupon
 								,LTRIM(RTRIM(joudis.joudis_disc_code)) AS disc_code
								,REPLACE(LTRIM(RTRIM(jouinv_pur_type)), ',', ';') AS sales_channel
 								,REPLACE(LTRIM(RTRIM(nation.nation_desc)), ',', ';') AS nation_desc
						 		,REPLACE(LTRIM(RTRIM(coustatus.coustatus_no)), ',', ';') AS serail_coupon_number
                                ,REPLACE(LTRIM(RTRIM(itmcol.itmcol_desc)), ',', ';') AS color_desc
								,REPLACE(LTRIM(RTRIM(itmast.itmast_year)), ',', ';') AS delivery
								,REPLACE(LTRIM(RTRIM(maincat.maincat_desc)), ',', ';') AS category_desc
								,REPLACE(LTRIM(RTRIM(subcat.subcat_desc)), ',', ';') AS sub_cat_desc
                                ,REPLACE(LTRIM(RTRIM(season.season_desc)), ',', ';') AS season
                            FROM #jouinv jouinv
                            LEFT JOIN itmast ON itmast_item_no = jouinv_item_no
                            LEFT JOIN joudis joudis    
								    ON (jouinv.jouinv_loc = joudis.joudis_loc AND     
									    jouinv.jouinv_no = joudis.joudis_no AND     
									    jouinv.jouinv_item_no = joudis.joudis_item_no AND    
									    jouinv.jouinv_item_col = joudis.joudis_col AND     
									    jouinv.jouinv_item_size = ISNULL(joudis.joudis_size,'') AND    
									    joudis.joudis_method='03' and jouinv.jouinv_line = joudis.joudis_line)   
						    LEFT JOIN joudis joudis_1    
								    ON (jouinv.jouinv_loc = joudis_1.joudis_loc AND     
									    jouinv.jouinv_no = joudis_1.joudis_no AND     
									    jouinv.jouinv_item_no = joudis_1.joudis_item_no AND     
									    jouinv.jouinv_item_col = joudis_1.joudis_col AND     
									    jouinv.jouinv_item_size = ISNULL(joudis_1.joudis_size,'') AND     
									    joudis_1.joudis_method='02' and jouinv.jouinv_line = joudis_1.joudis_line)    
						    LEFT JOIN joudis joudis_2    
									    ON (jouinv.jouinv_loc = joudis_2.joudis_loc AND     
										    jouinv.jouinv_no = joudis_2.joudis_no AND     
										    jouinv.jouinv_item_no = joudis_2.joudis_item_no AND     
										    jouinv.jouinv_item_col = joudis_2.joudis_col AND     
										    jouinv.jouinv_item_size = ISNULL(joudis_2.joudis_size,'') AND     
										    joudis_2.joudis_method='09' and jouinv.jouinv_line = joudis_2.joudis_line)    
						    LEFT JOIN nation nation ON nation_code = jouinv_cust_nation  
						    LEFT JOIN #temp_coustatus_line as coustatus  
							    on coustatus_redeem_no = jouinv_no  
							    and coustatus_redeem_loc = jouinv_loc
                            LEFT JOIN itmcol itmcol    
							    ON  jouinv.jouinv_item_col = itmcol.itmcol_code  
						    INNER JOIN subcat subcat    
							    ON  itmast.itmast_cat = subcat.subcat_code    
								    AND itmast.itmast_subcat = subcat.subcat_subcat
						    INNER JOIN maincat maincat    
							    ON itmast.itmast_cat = maincat.maincat_code
                            LEFT JOIN season season    
                                ON itmast.itmast_season = season.season_code
```
**Tovi Wang** (2025-01-20):
@@Anson Cheung Bellow result for your reference.Thanks!
**Anson Cheung** (2025-01-20):
@@Tovi Wang Can you scroll to the right and show the '`serail_coupon_number`' column? Thanks.
**Tovi Wang** (2025-01-20):
@@Anson Cheung FYI.
**Anson Cheung** (2025-01-21):
@@Tovi Wang Do you know if posting was executed around 15:39 - 15:44 on 2025-01-01?
**Andrew_Au** (2025-02-25):
@@Tovi Wang Can I close the ticket ?
**Andrew_Au** (2025-04-08):
@@Tovi Wang @@pierre.shi  Please reply the current ticket status
**Andrew_Au** (2025-04-08):
@@Tovi Wang @@pierre.shi  Please update the ticket status
**Tovi Wang** (2025-04-08):
@@Andrew_Au 最近没有再收到同样的issue callout.先closed ticket我们会继续monitoring.

## 相關資訊

- Jira: [BE-985](https://ctil.atlassian.net/browse/BE-985)
- Fix Version: 未記錄
- 解決日期: 未記錄
