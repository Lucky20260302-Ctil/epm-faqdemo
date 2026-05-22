---
tags: [faq, fe, 交易流程]
component: "Day End"
symptom: "MY 最近频繁有dayend issue,检查发现是会员名字有特殊字符导致posting的时候有报错"
root-cause: "待提取"
solution: "### Jira Comments (5 則)"
jira: FE-1820
resolved: 
fix-version: ""
---

# FE-1820: [INC3317824] MY OC600 dayend issue

## 問題

MY 最近频繁有dayend issue,检查发现是会员名字有特殊字符导致posting的时候有报错
1.
2.
34		OC600WM00556051	??? ‘	M	--	1982	OC600	20251125	18909718203	18209718203	???	‘			20251125	C	20261125		19820402		--
3.FE capture:

## 根因

（需從 Jira 提取）

## 解法

### Jira Comments (5 則)
**Tovi Wang** (2025-11-27):
SOG和店铺确认此会员是从Ename create,
查询DB发现此会员在DB已经存在，且 first name是特殊字符。
@@pierre.shi 后面请monitoring MY这个dayend issue,如还有继续发生，请把Ticket no贴到这里来。
CC @@Joy Li
**Tovi Wang** (2025-11-28):
Add more find info:
MY region,PCD file有中文的话无法posted到DB并且会有error.把中文去掉可以posted到DB.
现在有2个问题：
1.Ename创建的会员名在PCD file里为什么会有特殊字符？MYregion无法解析中文名嘛？
2.PCD 01 code里面如果有中文，posting时会有error.
@@Sang @@Joy Li  Please help to take a look this case.If need other info please ping me.Thanks!
**Tovi Wang** (2025-11-28):
@@pierre.shi 请copy OC600 till1 2025-11-25 PCD file to @@Sang  further checking.
**Sang** (2025-11-28):
Released CSPLUS have not fully support Unicode yet. MY Backend database and Upload PCD/Download Z-file Encoding is support EN only.
**Tovi Wang** (2025-11-28):
@@Sang Thanks for your confirm.
@@Joy Li @@pierre.shi May I know your any conments for this case?Let us keep monitoring this issue in later?

## 相關資訊

- Jira: [FE-1820](https://ctil.atlassian.net/browse/FE-1820)
- Fix Version: 未記錄
- 解決日期: 未記錄
