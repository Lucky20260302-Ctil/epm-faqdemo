---
project: ChainStorePlus
title: POS 付款方式（POS Tender）如何设置？各字段的含义是什么？
category: 基础表维护
source: v7 Book-1 Section 4.9 Page 51-52
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

此表用于定义 POS 前台的销售中接受的付款类型。常见的付款方式包括现金、信用卡（AE、Visa 等）、外币（美元、日元、英镑等），甚至公司发行的现金券都可以在此表定义。

**字段说明：**

| 提示 | 说明 |
|------|------|
| Currency Code（货币代码） | X(03) - 必填字段 - 此付款类型的货币 |
| Payment Code（付款代码） | X(03) - 必填字段 - 表示此特定付款类型的唯一代码。注意："FMM"（会员退款）、"MEM"（会员）、"EPM"（电子支付）为系统保留词，用户不得使用 |
| Location Code（地点代码） | X(04) - 可选字段 - 此付款类型将适用的地点 |
| Payment Name（付款名称） | X(40) - 必填字段 - 此付款类型的描述 |
| Rate（汇率） | 9(05).9(05) - 必填字段 - POS 中此付款类型使用的汇率 |
| Payment Type（付款类型） | 必填字段 - 通过组合框选择 - 对于 POS 前台的退货凭证功能，必须定义 'Return Voucher' 和 'Return Voucher redeem' 类型。对于 POS 前台的 'Deposit Return' 功能，至少必须定义 'Credit Voucher' 类型 |
| S9000 Payment Type（S9000付款类型） | X(10) - 如果 "Payment Type"="A-Electronic Payment" 则为必填，否则为空 - 从 S9000 设备返回的付款类型 |
| Report Type（报表类型） | 必填字段 - 选择 "Card" 属于 Card 组，"Others" 属于 Others 组，"Traveller Cheque" 属于 Traveller Cheque 组，"Cash" 属于 Cash 组 |
| Commission（佣金） | 付款类型的佣金率 |
| Last Modified Date（最后修改日期） | 99/99/9999 (dd/mm/yyyy) - 仅显示 - 上次修改此付款类型记录的日期 |
| Skip Daily Ex. Rate（跳过每日汇率） | 必填字段 - 指示此付款类型是否显示在每日汇率输入屏幕的标志（选择 "Yes" 或 "No"） |
