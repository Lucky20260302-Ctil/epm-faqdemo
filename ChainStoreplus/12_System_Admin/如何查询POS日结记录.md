---
project: ChainStorePlus
title: 如何查询POS日结记录？
category: 系统管理
source: v7 Book-5 Section 9.1.3 Page 28-32
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

POS日结查询（POS Day End Inquiry）用于记录各店铺的日结活动。POS日结是每日营业结束时由店铺POS人员执行的日常操作，用于结束当前营业日并准备下一个营业日。对于后台管理员来说，确保所有店铺按时正确完成此操作非常重要。

店铺完成日结后会自动向后台发送日结消息。如果没有收到某店铺的日结消息，可能意味着该店铺未完成日结流程，建议进一步调查。

查询画面显示字段：
- Date（日期）：日结日期。
- Time（时间）：日结时间。
- Location（位置）：日结店铺位置。
- Till（收银机编号）：POS的机器ID。
- Cashier（收银员）：收银员员工代码。
- Shift#（班次）：当班收银员员工代码。
- Sales（销售）：销售交易数量。
- Tfx（调拨）：库存调拨交易数量。
- Dep（订金）：订金交易数量。
- Serv（服务）：服务交易数量。
- Gift（礼品券）：礼品券交易数量。
- Gaway（赠品）：赠品交易数量。
- Redm（礼品兑换）：礼品兑换数量。
- Misc. Amount（杂项金额）：杂项收入金额。
- Total Amount（总金额）：总收入金额。
- Check（日结检查标志）：Y = 日结已验证，空白 = 日结未验证。

双击高亮行可查看日结交易明细：
- 点击"Payment"（付款）按钮查看付款详情，显示当日收到的付款方式。
- 点击"Count"（计数）标签查看当日交易数量。
- 点击"Amount"（金额）标签查看当日交易金额。
- 点击"Other"（其他）标签查看哪些交易有错误。
