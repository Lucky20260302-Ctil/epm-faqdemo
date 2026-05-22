---
project: BE
issue_key: BE-736
issue_type: Task
status: Closed
faq_score: 5.5
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-736"
created: 2023-05-22
resolved: 2023-07-26
resolution: Done
has_images: False
---

# BE-736: Item Master Maintenance MF0001 Define Publication changes

> **類型:** Task | **狀態:** Closed
> **分類:** 效能與逾時 | **FAQ 分數:** 5.5
> **解決日期:** 2023-07-26
> **負責人:** Sherman tse
> **組件:** Backend (Web)

## 問題描述

According to the sample screen, add the display values (display only), plus one editable value (itmpubl_gov_order_limit)

below db fields are display only

[itmpubl_sheet_no] [varchar](100) NULL,
[itmpubl_display_name] [nvarchar](500) NULL,
[itmpubl_title] [nvarchar](1000) NULL,
[itmpubl_extension] [nvarchar](100) NULL,
[itmpubl_photo_no] [varchar](50) NULL,
[itmpubl_edition_plan_date] [varchar](20) NULL,
[itmpubl_gazette_sortie_no] [varchar](50) NULL,
[itmpubl_gn_ln_date] [date] NULL,
[itmpubl_loc] [varchar](100) NULL,
[itmpubl_scale] [varchar](20) NULL,
[itmpubl_size_x] [integer] NULL,
[itmpubl_size_y] [integer] NULL,
[itmpubl_colour] [varchar](20) NULL,
[itmpubl_remark] [nvarchar](1000) NULL,
[itmpubl_price_code] [nvarchar](50) NULL,
[itmpubl_production_type] [varchar](10) NULL,
[itmpubl_production_code] [varchar](20) NULL,
[itmpubl_weight] [integer] NULL,
[itmpubl_preview_file] [varchar](500) NULL,
[itmpubl_thumbnail_medium] [varchar](500) NULL,
[itmpubl_thumbnail_low] [varchar](500) NULL,
[itmpubl_is_current_product] [char](1) NULL,
[itmpubl_folio_no] [varchar](80) NULL,
[itmpubl_sales_counter] [varchar](30) NULL,
[itmpubl_status] [varchar](20) NULL,
[itmpubl_effective_at] [date] NULL,
[itmpubl_item_nature] [varchar](50) NULL,
[itmpubl_keyword] [varchar](500) NULL,
[itmpubl_reporting_group] [varchar](70) NULL,
[itmpubl_item_type] [varchar](150) NULL,
~~[itmpubl_available_for_sale] [char](1) NULL,~~
~~[itmpubl_last_date] [datetime] NULL,~~

database info:
ip: 172.16.138.128
database: csdata99
login: csuser
login: csuser



## 相關資訊

- **Jira:** [BE-736](https://ctil.atlassian.net/browse/BE-736)
- **解決方式:** Done