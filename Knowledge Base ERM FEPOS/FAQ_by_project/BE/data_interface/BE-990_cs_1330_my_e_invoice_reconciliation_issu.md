---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "we got callout from BDO side, for below Coach MY transaction at Jan-19, total amount send to BDO is "
root-cause: "待提取"
solution: "- **Resolution:** Done"
jira: BE-990
resolved: 2025-05-06
fix-version: ""
---

# BE-990: [CS-1330] - MY E-invoice Reconciliation Issue

## 問題

we got callout from BDO side, for below Coach MY transaction at Jan-19, total amount send to BDO is incorrect, I've check the log on that day, CS2K do miss line item send to BDO. Log attached, could you please help to further check? Thanks
1.OCF75-20192764
DB total amount: 1806
2.OCF75-20192764
MY_Einvoice log total amount(BDO): 1521
Variance is 285,Missing the item CT743  285 amount.
3.sqlp
cd table

## 根因

（需從 Jira 提取）

## 解法

- **Resolution:** Done
- **日期:** 2025-05-06
### Jira Comments (21 則)
**Tovi Wang** (2025-01-22):
@@Anson Cheung log here.If need anything other logs,Please ping me here.Thanks!
**Anson Cheung** (2025-01-22):
@@Tovi Wang can you provide the records of: ‘jouinv’, ‘joudis’, ‘itmast’ of these two documents?
**Tovi Wang** (2025-01-22):
@@Anson Cheung After checked the DB & Einvoice log,Found Variance is 285,Missing the item CT743 285 amount.Description detials for your refrence.Please check why the 285 amount for item CT743 missing in the log?Please double check the send logic.Thanks!
**Anson Cheung** (2025-01-22):
@@Tovi Wang can you provide the result of these two sql?
```
select top 1 rtrim(dbconfig_long_value) COLLATE Latin1_General_CI_AS from dbconfig where dbconfig_key='BDO_GWP_cat_filters'
SELECT * FROM itmast WHERE itmast_item_no = 'CT743'
```
**Tovi Wang** (2025-01-22):
@@Anson Cheung FYI.
**Anson Cheung** (2025-01-22):
@@Tovi Wang can you help to get the result? Thanks.
```
DECLARE @frdate nvarchar(20) = '20250101'
DECLARE @todate nvarchar(20) = '20250120'
DECLARE @divisionCode nvarchar(20) = '0200'
DECLARE @BDO_GWP_cat_filters NVARCHAR(MAX) = ''
                                select top 1 @BDO_GWP_cat_filters = rtrim(dbconfig_long_value) COLLATE Latin1_General_CI_AS from dbconfig where dbconfig_key='BDO_GWP_cat_filters'
                                SELECT loctab_code 
                                INTO #ec_loctab
                                FROM loctab WITH (NOLOCK)
                                WHERE loctab_code like 'OCE%' OR loctab_type = 'E' OR loctab_depart_store = 'Y'
								SELECT * INTO #jougic
								FROM jougic WITH (NOLOCK)
								WHERE jougic_date BETWEEN @frdate
										AND @todate
									AND jougic_qty <> 0
                                SELECT * 
                                INTO #jouinv
                                FROM jouinv WITH (NOLOCK)
                                WHERE jouinv_date BETWEEN @frdate AND @todate
                                SELECT * FROM (
	                                SELECT
			                                  'BRN' AS supplierRegistrationFlag
			                                  ,'B2C' AS transactionType
			                                  ,CASE WHEN pos > 0 AND ne = 0 THEN '01'
					                                WHEN pos = 0 AND ne > 0 THEN '04'
					                                WHEN pos > 0 AND ne > 0 THEN 
						                                CASE WHEN jouinv_item_qty > 0 THEN '01'
							                                 WHEN jouinv_item_qty < 0 THEN '02'
						                                END
				                                END AS eInvoiceType
			                                  , @divisionCode AS divisionCode
			                                  , RTRIM(j.jouinv_loc) AS branchCode
			                                  , j.[jouinv_no] AS jouinv_no
			                                  ,'EI00000000010' AS buyerTIN
			                                  --,CASE WHEN pos > 0 AND ne > 0 AND jouinv_item_qty > 0 THEN document_no + '-2'
					                                --WHEN pos > 0 AND ne > 0 AND jouinv_item_qty < 0 THEN document_no + '-1' 
					                                --ELSE document_no END 
					                                --AS documentNumber
											  , document_no AS documentNumber
			                                  , CONVERT(varchar(10), j.jouinv_date, 103) AS documentDate
			                                  , documentTime AS documentTime
			                                  , ISNULL(CASE WHEN ne > 0 AND jouinv_item_qty < 0 THEN RTRIM(orig_loc) + '-' + RTRIM(orig_no) ELSE '' END, 'NA') AS originalERPReferenceDocumentNumber
			                                  , '022' AS classificationCode
			                                  , itmast_desc AS descriptionOfProductOrService
			                                  , '06' AS taxType
			                                  , ABS(j.jouinv_item_qty) AS quantity
			                                  , jouinv_item_list_price AS unitPrice
			                                  , ABS(jouinv_item_qty) * jouinv_item_list_price subTotal
			                                  , CAST(ROUND(ABS((jouinv_item_list_price -jouinv_item_sell_price) * jouinv_item_qty), 2) AS decimal(10, 2)) AS discountAmount
			                                  , 0 AS feeOrChargeAmount
			                                  , CAST(ABS((jouinv_item_list_price * jouinv_item_qty) - ROUND((jouinv_item_list_price -jouinv_item_sell_price) * jouinv_item_qty, 2)) AS decimal(10, 2)) AS lineItemTotalExcludingTax
			                                  , CAST(ABS((jouinv_item_list_price * jouinv_item_qty) - ROUND((jouinv_item_list_price -jouinv_item_sell_price) * jouinv_item_qty, 2)) AS decimal(10, 2)) AS itemTaxableAmount
			                                  , 0 AS taxRate
			                                  , 0 AS taxAmount
			                                  , CAST(ABS((jouinv_item_list_price * jouinv_item_qty) - ROUND((jouinv_item_list_price -jouinv_item_sell_price) * jouinv_item_qty, 2)) AS decimal(10, 2)) AS lineItemIncludingTax
			                                  , CAST(ROUND(CASE WHEN pos > 0 AND ne > 0 THEN 
						                                CASE WHEN jouinv_item_qty > 0 THEN
								                                pos_sum_jouinv_item_disc_adj
							                                 WHEN jouinv_item_qty < 0 THEN
								                                ne_sum_jouinv_item_disc_adj
						                                END
					                                ELSE sum_jouinv_item_disc_adj END
				                                , 2) AS decimal(10, 2)) AS invoiceAdditionalDiscountAmount
			                                  , 0 AS invoiceAdditionalFeeAmount
			                                  , CAST(ROUND(CASE WHEN pos > 0 AND ne > 0 THEN 
						                                CASE WHEN jouinv_item_qty > 0 THEN
								                                pos_sum_jouinv_item_disc_adj
							                                 WHEN jouinv_item_qty < 0 THEN
								                                ne_sum_jouinv_item_disc_adj
						                                END
					                                ELSE sum_jouinv_item_disc_adj END
				                                , 2) AS decimal(10, 2))AS totalDiscountValue
			                                  , 0 AS totalFeeOrChargeAmount
			                                  , CAST(ROUND(CASE WHEN pos > 0 AND ne > 0 THEN
					                                CASE WHEN jouinv_item_qty > 0 THEN pos_sum_lineItemTotalExcludingTax
						                                 WHEN jouinv_item_qty < 0 THEN ne_sum_lineItemTotalExcludingTax
					                                END
				                                ELSE pos_sum_lineItemTotalExcludingTax + ne_sum_lineItemTotalExcludingTax 
				                                END
			                                   , 2) AS decimal(10, 2)) AS totalNetAmount
			                                  , CAST(ROUND(CASE WHEN pos > 0 AND ne > 0 THEN
					                                CASE WHEN jouinv_item_qty > 0 THEN pos_sum_lineItemTotalExcludingTax
						                                 WHEN jouinv_item_qty < 0 THEN ne_sum_lineItemTotalExcludingTax
					                                END
				                                ELSE pos_sum_lineItemTotalExcludingTax + ne_sum_lineItemTotalExcludingTax 
				                                END
				                                 - 
				                                CASE WHEN pos > 0 AND ne > 0 THEN 
					                                CASE WHEN jouinv_item_qty > 0 THEN
							                                pos_sum_jouinv_item_disc_adj
							                                WHEN jouinv_item_qty < 0 THEN
							                                ne_sum_jouinv_item_disc_adj
					                                END
				                                ELSE sum_jouinv_item_disc_adj END
				                                , 2) AS decimal(10, 2)) AS totalExcludingTax
			                                  , 0 AS totalTaxAmount
			                                  , CAST(ROUND(CASE WHEN pos > 0 AND ne > 0 THEN
					                                CASE WHEN jouinv_item_qty > 0 THEN pos_sum_lineItemTotalExcludingTax
						                                 WHEN jouinv_item_qty < 0 THEN ne_sum_lineItemTotalExcludingTax
					                                END
				                                ELSE pos_sum_lineItemTotalExcludingTax + ne_sum_lineItemTotalExcludingTax 
				                                END
				                                 - 
				                                CASE WHEN pos > 0 AND ne > 0 THEN 
					                                CASE WHEN jouinv_item_qty > 0 THEN
							                                pos_sum_jouinv_item_disc_adj
							                                WHEN jouinv_item_qty < 0 THEN
							                                ne_sum_jouinv_item_disc_adj
					                                END
				                                ELSE sum_jouinv_item_disc_adj END
				                                , 2) AS decimal(10, 2)) AS totalIncludingTax
			                                ,CAST(ROUND(sum_P_joupay_pay_amt_fx, 2) AS decimal(10, 2)) AS prePaymentAmount
			                                , CAST(ROUND(CASE WHEN pos > 0 AND ne > 0 THEN
					                                CASE WHEN jouinv_item_qty > 0 THEN pos_sum_lineItemTotalExcludingTax
						                                 WHEN jouinv_item_qty < 0 THEN ne_sum_lineItemTotalExcludingTax
					                                END
				                                ELSE pos_sum_lineItemTotalExcludingTax + ne_sum_lineItemTotalExcludingTax 
				                                END
				                                 - 
				                                CASE WHEN pos > 0 AND ne > 0 THEN 
					                                CASE WHEN jouinv_item_qty > 0 THEN
							                                pos_sum_jouinv_item_disc_adj
							                                WHEN jouinv_item_qty < 0 THEN
							                                ne_sum_jouinv_item_disc_adj
					                                END
				                                ELSE sum_jouinv_item_disc_adj END
				                                - sum_P_joupay_pay_amt_fx
				                                , 2) AS decimal(10, 2))AS totalPayableAmount
			                                  , RTRIM(jouinv_curr) AS invoiceCurrencyCode
			                                  , '47199' AS supplierMSICCode
			                                  , 'RETAILING OF FOOTWEAR, READY TO WEAR (APPAREL), LEATHER GOODS AND ACCESSORIES FOR LUXURY MARKETS BEARING THE TRADEMARK OF COACH AND KATE SPADE IN MALAYSIA' AS supplierBusinessActivityDescription
			                                  , '' supplierAddress0
			                                  , '' supplierCity
			                                  , '14' supplierStateCode
			                                  , 'MYS' supplierCountryCode
			                                  , '60321138888' supplierContactNumber
			                                  , LEFT(ISNULL(concat_joupay_vhr_no, ''), 150) prePaymentReferenceNumber
	                                FROM #jouinv j WITH (NOLOCK)
	                                INNER JOIN 
	                                (	
		                                SELECT jouinv_date
				                                ,RTRIM([jouinv_loc]) + '-' + RTRIM([jouinv_no]) document_no
				                                   ,RIGHT('00' + CONVERT(VARCHAR, jouinv_hour), 2) + ':' + RIGHT('00' + CONVERT(VARCHAR, jouinv_mn), 2) + ':00' AS documentTime
				                                  ,[jouinv_loc]
				                                  ,[jouinv_no]
				                                  ,CASE WHEN jouinv_ret_inv_loc IS NULL AND jouinv_ret_inv_no IS NULL THEN jouinv_loc 
						                                ELSE jouinv_ret_inv_loc END AS orig_loc
				                                  ,CASE WHEN jouinv_ret_inv_loc IS NULL AND jouinv_ret_inv_no IS NULL THEN jouinv_void_no 
						                                ELSE jouinv_ret_inv_no END AS orig_no
				                                  ,SUM(CASE WHEN jouinv_item_qty > 0 THEN 1 ELSE 0 END) pos
				                                  ,SUM(CASE WHEN jouinv_item_qty < 0 THEN 1 ELSE 0 END) ne
				                                  ,ABS(SUM(jouinv_item_disc_adj)) sum_jouinv_item_disc_adj
				                                  ,ABS(SUM(CASE WHEN jouinv_item_qty > 0 THEN jouinv_item_disc_adj ELSE 0 END )) pos_sum_jouinv_item_disc_adj
				                                  ,ABS(SUM(CASE WHEN jouinv_item_qty < 0 THEN jouinv_item_disc_adj ELSE 0 END )) ne_sum_jouinv_item_disc_adj
				                                  ,ABS(SUM(CASE WHEN jouinv_item_qty > 0 THEN (jouinv_item_list_price * jouinv_item_qty) - ROUND((jouinv_item_list_price -jouinv_item_sell_price) * jouinv_item_qty, 2) ELSE 0 END)) pos_sum_lineItemTotalExcludingTax
				                                  ,ABS(SUM(CASE WHEN jouinv_item_qty < 0 THEN (jouinv_item_list_price * jouinv_item_qty) - ROUND((jouinv_item_list_price -jouinv_item_sell_price) * jouinv_item_qty, 2) ELSE 0 END)) ne_sum_lineItemTotalExcludingTax
	                                  FROM #jouinv WITH (NOLOCK)
	                                  where jouinv_date BETWEEN @frdate AND @todate AND jouinv_item_qty <> 0 --AND jouinv_no = '20004888' and jouinv_loc = 'OC11'
	                                  GROUP BY [jouinv_loc]
		                                  ,[jouinv_no], jouinv_date,jouinv_hour, jouinv_mn, jouinv_ret_inv_loc, jouinv_ret_inv_no, jouinv_void_no--, joudis_loc, joudis_no
	                                )a 
	                                ON j.jouinv_loc = a.jouinv_loc AND j.jouinv_no = a.jouinv_no
	                                LEFT JOIN itmast ON itmast_item_no = jouinv_item_no
	                                LEFT JOIN joudis ON j.jouinv_loc = joudis_loc
													AND j.jouinv_no = joudis_no
													AND jouinv_line = joudis_line
	                                INNER JOIN (
		                                SELECT joupay_loc, joupay_no, joupay_memo_type, SUM(joupay_pay_amt_fx) sum_joupay_pay_amt_fx
			                                , SUM(CASE WHEN paytab_chg_flag = 'P' THEN joupay_vhr_amt ELSE 0 END) sum_P_joupay_pay_amt_fx
			                                , STUFF((
					                                SELECT ', ' + RTRIM(joupay_vhr_no)
					                                FROM joupay AS j2
					                                WHERE j2.joupay_loc = joupay.joupay_loc
						                                AND j2.joupay_no = joupay.joupay_no
						                                AND j2.joupay_memo_type = joupay.joupay_memo_type
						                                AND j2.joupay_vhr_no <> ''
					                                FOR XML PATH('')
				                                ), 1, 2, '') AS concat_joupay_vhr_no
		                                FROM joupay WITH (NOLOCK)
		                                LEFT JOIN paytab ON joupay_pay_code = paytab_code 
		                                GROUP BY joupay_loc, joupay_no, joupay_memo_type
	                                )p ON j.jouinv_loc = joupay_loc AND j.jouinv_no = joupay_no AND joupay_memo_type = 'S'
	                                WHERE jouinv_item_qty <> 0
										AND (
												(jouinv_item_amt <> 0 AND jouinv_item_list_price <> 0 AND jouinv_item_sell_price <> 0)
												OR itmast_cat NOT IN (SELECT Value FROM dbo.SplitString(',', @BDO_GWP_cat_filters))
											)
		                                AND NOT EXISTS (SELECT 1 FROM #ec_loctab WHERE j.jouinv_loc = loctab_code)
		                                AND j.jouinv_date BETWEEN @frdate AND @todate
										AND (j.jouinv_loc = 'OCF75' AND j.jouinv_no = '20192764') OR (j.jouinv_loc = 'OCF79' AND j.jouinv_no = '10112802')
	                                GROUP BY document_no, pos, ne, j.jouinv_loc, j.jouinv_date, documentTime, orig_loc, orig_no, itmast_desc
	                                , jouinv_item_qty, jouinv_item_curr_price, jouinv_item_list_price, jouinv_item_amt, jouinv_tot_amt, jouinv_misc_amt, jouinv_curr, jouinv_key, jouinv_item_sell_price
	                                , sum_jouinv_item_disc_adj, sum_P_joupay_pay_amt_fx, concat_joupay_vhr_no, pos_sum_jouinv_item_disc_adj, ne_sum_jouinv_item_disc_adj, pos_sum_lineItemTotalExcludingTax, ne_sum_lineItemTotalExcludingTax
									, j.jouinv_no
	                                UNION ALL
		                                SELECT
			                                  'BRN' AS supplierRegistrationFlag
			                                  ,'B2C' AS transactionType
			                                  ,CASE WHEN jougic_qty > 0 THEN '01'
					                                WHEN jougic_qty < 0 THEN '04'
				                                END AS eInvoiceType
			                                  , @divisionCode AS divisionCode
			                                  , RTRIM(j.jougic_loc) AS branchCode
											  , j.jougic_no AS jouinv_no
			                                  ,'EI00000000010' AS buyerTIN
			                                  ,RTRIM(j.jougic_loc) + '-' + RTRIM(j.jougic_no) 
				                                  documentNumber
			                                  , CONVERT(varchar(10), jougic_date, 103) AS documentDate
			                                  , RIGHT('00' + CONVERT(VARCHAR, jougic_hour), 2) + ':' + RIGHT('00' + CONVERT(VARCHAR, jougic_min), 2) + ':00' AS documentTime
			                                  , CASE WHEN jougic_qty < 0 THEN ISNULL(RTRIM(j.jougic_loc) + '-' + RTRIM(jougic_void_no), 'NA') ELSE '' END AS originalERPReferenceDocumentNumber
			                                  , '022' AS classificationCode
			                                  , 'Gift Certificate' AS descriptionOfProductOrService
			                                  , '06' AS taxType
			                                  , ABS(jougic_qty) AS quantity
			                                  , jougic_unit_price AS unitPrice
			                                  , CAST(ROUND(ABS(jougic_qty) * jougic_unit_price, 2) AS decimal(10, 2)) subTotal
			                                  , 0 AS discountAmount
			                                  , 0 AS feeOrChargeAmount
			                                  , CAST(ROUND(ABS(jougic_unit_price * jougic_qty), 2) AS decimal(10, 2)) AS lineItemTotalExcludingTax
			                                  , CAST(ROUND(ABS(jougic_unit_price * jougic_qty), 2) AS decimal(10, 2)) AS itemTaxableAmount
			                                  , 0 AS taxRate
			                                  , 0 AS taxAmount
			                                  , CAST(ROUND(ABS(jougic_unit_price * jougic_qty), 2) AS decimal(10, 2)) AS lineItemIncludingTax
			                                  , 0 AS invoiceAdditionalDiscountAmount
			                                  , 0 AS invoiceAdditionalFeeAmount
			                                  , 0 AS totalDiscountValue
			                                  , 0 AS totalFeeOrChargeAmount
			                                  , total_amt AS totalNetAmount
			                                  , total_amt AS totalExcludingTax
			                                  , 0 AS totalTaxAmount
			                                  , total_amt AS totalIncludingTax
			                                  , 0 AS prePaymentAmount
			                                  , total_amt AS totalPayableAmount
			                                  , RTRIM(jougic_curr) AS invoiceCurrencyCode
			                                  , '47199' AS supplierMSICCode
			                                  , 'RETAILING OF FOOTWEAR, READY TO WEAR (APPAREL), LEATHER GOODS AND ACCESSORIES FOR LUXURY MARKETS BEARING THE TRADEMARK OF COACH AND KATE SPADE IN MALAYSIA' AS supplierBusinessActivityDescription
			                                  , '' supplierAddress0
			                                  , '' supplierCity
			                                  , '14' supplierStateCode
			                                  , 'MYS' supplierCountryCode
			                                  , '60321138888' supplierContactNumber
			                                  , '' prePaymentReferenceNumber
										FROM #jougic j WITH (NOLOCK)
										INNER JOIN (
											SELECT jougic_loc, jougic_no, SUM(CAST(ROUND(ABS(jougic_unit_price * jougic_qty), 2) AS DECIMAL(10, 2))) total_amt
											FROM #jougic WITH (NOLOCK)
											GROUP BY jougic_loc, jougic_no
										)a ON j.jougic_loc = a.jougic_loc
											AND j.jougic_no = a.jougic_no
		                                WHERE NOT EXISTS (SELECT 1 FROM #ec_loctab WHERE j.jougic_loc = loctab_code)
											  AND (jougic_unit_price <> 0 AND jougic_qty <> 0)
                                )eInvoice
                                ORDER BY documentNumber
                                DROP TABLE #ec_loctab
                                DROP TABLE #jouinv                                
								DROP TABLE #jougic
```
**Tovi Wang** (2025-01-22):
@@Anson Cheung FYI.Thanks!
**Anson Cheung** (2025-01-22):
@@Tovi Wang the sql result is normal, documents can return the correct amount.
Could you check if multiple pdc were posted? I suspect the data was incomplete during the first scan.
**Tovi Wang** (2025-01-22):
@@Anson Cheung Posting log here.Please check.
**Anson Cheung** (2025-01-23):
The issue can be confirmed as caused by the interface retrieving invoice while the data is still posting, resulting in incomplete data. An enhancement is needed.
**Tovi Wang** (2025-01-23):
@@Anson Cheung  Many Thanks for your keep updating.May I know the about time of ETA for the enhancement?Thanks!
**Tovi Wang** (2025-01-23):
sqlpcd table
**Tovi Wang** (2025-01-23):
Another same issue memo OCF79-10112802 for your reference.Just only first line send to BDO.
**Tovi Wang** (2025-01-23):
Resend MY E-invoice to BDO for bellow 2 memo
1.OCF75 - 20192764
2.OCF79 - 10112802
**Anson Cheung** (2025-01-23):
Release:
[\\ds411\public\anson\MY_eInvoice](file://ds411/public/anson/MY_eInvoice)\MY_eInvoice_v1.0.0_20250123.zip
Release notes:
- 
-
**Tovi Wang** (2025-02-05):
@@Sherman tse Please help to testing this issue.Thanks!
**Sherman tse** (2025-02-06):
Verified on QA
Attached test case
**Tovi Wang** (2025-04-07):
@@Anson Cheung Coach team callout BDO receive incomplete sales amt data for bellow 2 sales memo.
After checked the log,I just only find the first item sales data in log,But missing the second item sales data.Please help to double check and confirm the RCA?Thanks!
1.
OCF77-20229270 2025-03-18
OCF79-10119181 2025-03-20
2.OCF77-20229270 2025-03-18
3.OCF79-10119181 2025-03-20
**Anson Cheung** (2025-04-09):
@@Tovi Wang This case has same cause with last callout. By config, program scans the memo not within 10 mins, but the posting is done after 18 mins. I suggest setting the **scanDelayMin **config to 20.
**Andrew_Au** (2025-05-02):
@@Tovi Wang @@pierre.shi Please update the ticket status
**Tovi Wang** (2025-05-06):
data patch done and will keep monitoring.Closed firstly.

## 相關資訊

- Jira: [BE-990](https://ctil.atlassian.net/browse/BE-990)
- Fix Version: 未記錄
- 解決日期: 2025-05-06
