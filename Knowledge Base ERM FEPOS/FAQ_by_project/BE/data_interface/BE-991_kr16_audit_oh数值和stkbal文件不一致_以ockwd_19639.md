---
tags: [faq, be, data_interface]
component: "Data Interface"
symptom: "1.Coach Team call out KR Audit_oh数值和Stkbal导出的文件数值不一致。"
root-cause: "待提取"
solution: "### Jira Comments (10 則)"
jira: BE-991
resolved: 
fix-version: ""
---

# BE-991: KR(16)-Audit_oh数值和Stkbal文件不一致  以OCKWD 196395455843 CU068 B4/BK为例

## 問題

1.Coach Team call out KR Audit_oh数值和Stkbal导出的文件数值不一致。
oh_qty 和 trx_qty 都是 ‘11’，为什么导出的接口文件 qty是 ‘-1’？‘-1’从哪里来的？请帮忙检查确认导出文件的逻辑,谢谢！
UPC code: 196395455843
item no: CU068
item color: B4/BK
2.下面这个是正常例子,db里的qty和导出接口文件的qty一致都是‘1’

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (10 則)
**Tovi Wang** (2025-01-22):
@@Cy Lau @@Anson Cheung interface file 16Stkbal_20250112023006.dat and exe for your reference.Could you help to clarify the logic and provide the RCA?Thanks!
**Tovi Wang** (2025-01-23):
\\apawipwposapp21\DATA70\Log log list for your reference.@@Cy Lau
**Cy Lau** (2025-01-23):
The QTY for STKBAL :
So the question for the negative would be , what is the value for itmdtl_qty and intransit_qty at that moment.
@@Tovi Wang
SQL
SELECT itmdtl.*, a.intransit_qty
 FROM itmdtl
 INNER JOIN loctab
 ON itmdtl_loc = loctab_code
    AND loctab_project = 'Y'
 LEFT JOIN
           (SELECT joutfx_to_loc,
                   joutfx_item_no,
                   joutfx_col,
                   joutfx_size,
                   SUM(joutfx_qty) as intransit_qty
            FROM joutfx
            WHERE  ISNULL(joutfx_chk, ' ')  = ' '
                 AND  ISNULL(joutfx_void_flag, ' ')  = ' '
            GROUP BY joutfx_to_loc,
                     joutfx_item_no,
                     joutfx_col,
                     joutfx_size
           ) a
 ON itmdtl_loc = joutfx_to_loc
    AND itmdtl_item_no = joutfx_item_no
    AND itmdtl_col = joutfx_col
    AND itmdtl_size = joutfx_size
**Tovi Wang** (2025-01-23):
@@Cy Lau Log here for your further checking.Thanks!
**Tovi Wang** (2025-01-24):
select top 10 * from audit_oh where oh_loc = 'OCKWD' and oh_item_no = 'CU068' and oh_color = 'B4/BK'
select * from audit_trx where trx_loc = 'OCKWD' and trx_item_no = 'CU068' and trx_color = 'B4/BK'
select itmdtl_qty,* from itmdtl where itmdtl_item_no = 'CU068' and itmdtl_col = 'B4/BK' and itmdtl_loc = 'OCKWD'
SELECT joutfx_to_loc,joutfx_item_no,joutfx_col,joutfx_size,joutfx_qty,joutfx_chk,joutfx_void_flag,* from joutfx where
joutfx_item_no = 'CU068' and joutfx_col = 'B4/BK' and joutfx_to_loc = 'OCKWD'
and ISNULL(joutfx_chk, ' ')  = ' ' and  ISNULL(joutfx_void_flag, ' ')  = ' '
**Tovi Wang** (2025-02-05):
Dear ALL,
I has explain the details logic to Lein.
**Tovi Wang** (2025-02-06):
Dear @@Cy Lau One more question from Lein.
For sample case :trx_loc = 'OCKW1' and trx_item_no = '6303' and trx_color = 'IMBLK',
The itmdtl_qty = '-1',Question is that where is the itmdtl_qty = '-1' come from?Could you help to take a look and give some advice?Thanks!
SQL:
SELECT itmdtl.*, a.intransit_qty FROM itmdtl INNER JOIN loctab ON itmdtl_loc = loctab_code    AND loctab_project = 'Y' LEFT JOIN           (SELECT joutfx_to_loc,                   joutfx_item_no,                   joutfx_col,                   joutfx_size,                   SUM(joutfx_qty) as intransit_qty            FROM joutfx            WHERE  ISNULL(joutfx_chk, ' ')  = ' '                 AND  ISNULL(joutfx_void_flag, ' ')  = ' '            GROUP BY joutfx_to_loc,                     joutfx_item_no,                     joutfx_col,                     joutfx_size           ) a ON itmdtl_loc = joutfx_to_loc    AND itmdtl_item_no = joutfx_item_no    AND itmdtl_col = joutfx_col    AND itmdtl_size = joutfx_sizewhere itmdtl_item_no = '6303' and itmdtl_col = 'IMBLK' and itmdtl_loc = 'OCKW1'
**Tovi Wang** (2025-02-07):
Dear ALL,
Transfer variance data patch done.@@Bobby Thanks for your assist.
**Andrew_Au** (2025-02-24):
@@Tovi Wang Can I close the ticket ?
**Tovi Wang** (2025-02-24):
@@Andrew_Au issue fixed.Please closed the case.

## 相關資訊

- Jira: [BE-991](https://ctil.atlassian.net/browse/BE-991)
- Fix Version: 未記錄
- 解決日期: 未記錄
