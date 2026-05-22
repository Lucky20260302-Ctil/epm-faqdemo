---
tags: [faq, be, beapicrm]
component: "Backend (ChainStorePlus 7.0)"
symptom: "ssue Detail,"
root-cause: "待提取"
solution: "### Jira Comments (11 則)"
jira: BE-1053
resolved: 
fix-version: ""
---

# BE-1053: [CS-1388]Issue_PRC_Price Group is not working

## 問題

ssue Detail,
Coupon already set us FOC, but not able to apply to FOC stores.

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (11 則)
**Cy Lau** (2025-04-22):
@@Bobby  maybe need your help on this
**Tovi Wang** (2025-05-12):
[1.QA](http://1.QA) normal zlog file provided by Bobby.Contain 40 & 43 line.
2.[Pro](http://2.Pro) abnormal Zlog file provided by Lein. Missing 40 line.
Pro 生成的 MM promo Zlog file 好像不完整。 从QA 和 Pro Zlog file对比结果来看。Zlog file有差异。
QA 有 40，43这2行。
Pro只看到 43这一行，没有40这一行。
I think RCA should be this one.
@@Jerry Wong @@Cy Lau Could you help to double confirm?Thanks!
CC @@Joy Li @@Bobby
**Tovi Wang** (2025-05-12):
select * from tmnhist where tmnhist_date = '2025-04-29'
**Tovi Wang** (2025-05-12):
**Tovi Wang** (2025-05-12):
@@Jerry Wong ，我和 @@Bobby 在QA测试正常，Zlog file和生产环境 43，09 line，无法reproduce这个issue.
生产环境此MM coupon已经过期。我怀疑是不是Pro 此 MM coupon setting哪里有问题？
1.Event:
Coupon:
2[.QA](http://1.QA) Normal Zlog file,have 43,D9 line,Same with pro zlog file.
QA Zlog file
3.FE POS can normal select this MM coupon.
**Tovi Wang** (2025-05-12):
Just noted QA is normal:
1.
40 line是mixtab table
select * from mixtab where mixtab_event like '0429%'
2.
D9 是 mixtabg table
select * from mixtabg
3.SELECT TOP (1000) * FROM dbtmnlog where dbtmnlog_zlog = 'z250512.02' and dbtmnlog_table_name = 'mixtabg'
**Tovi Wang** (2025-05-12):
Coach callout有问题的生产环境的MM coupon setting(Just noted):
1.Event:
2.Purchase:
3.Coupon:
4.Conditions:
**Tovi Wang** (2025-05-12):
@@Jerry Wong PRO mixtabg table missing the MM coupon data.This should be the RCA.Could you help to further investigating why PRO mixtabg table missing the MM coupon data?Thanks!
**Andrew_Au** (2025-10-06):
@@Tovi Wang Please update the status
**Andrew_Au** (2025-11-03):
@@Tovi Wang @@Joy Li Please update the ticket status
**Tovi Wang** (2025-11-03):
Please closed this one.After checked with Coach team, it seems like the issue occurred on the specific coupon however as coupons are expired currently.They will raise another one once the same issue occrs.

## 相關資訊

- Jira: [BE-1053](https://ctil.atlassian.net/browse/BE-1053)
- Fix Version: 未記錄
- 解決日期: 未記錄
