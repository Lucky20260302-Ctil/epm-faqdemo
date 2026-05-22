---
project: ChainStorePlus
title: POS 付款类型（Payment Type）ID 及其功能有哪些？
category: 基础表维护
source: v7 Book-1 Section 4.9 Page 53-55
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

POS 付款类型的功能设置及其使用说明如下：

| ID | 付款类型 | 说明 |
|----|----------|------|
| A | Electronic Payment（电子支付） | 仅在启用"信用卡接口"选项时需要。客户通过已认证的 S9000 卡终端支付时，终端会自动返回代码识别具体信用卡类型（如 Visa、Master Card）。需要与表中的 "S9000 Payment Type" 字段配合使用 |
| B | EPS（易办事） | 允许 S9000 连接的 EPS 支付 |
| C | Credit Card（信用卡） | 在没有 S9000 卡终端连接的情况下接受信用卡支付。常见信用卡类型（Visa、AE、Master 等）在表中的 Payment Code 字段定义 |
| D | Credit Voucher（信用凭证） | 用于 POS 退货的不可兑换退款凭证 |
| E | Credit Card Refund（信用卡退款） | 用于销售退货或商品退货操作中的信用卡退款控制 |
| F | Return Voucher Redeem（退货凭证兑换） | 此特定付款方式归类为客户兑换退货凭证 |
| G | Cash Voucher（现金券） | 用于非序列号基的现金券 |
| H | Uniform Coupon（制服券） | 此付款代码用于"员工制服"兑换目的 |
| I | NOT use（不使用） | 不使用 |
| J | Cash Coupon（现金券，序列号） | 用于基于序列号的现金券。使用时将验证现金券的序列号 |
| K | Credit Sales（赊销） | 此付款代码归类为赊销 |
| L | Cheque（支票） | 个人银行支票付款 |
| P | Gift Certificate（礼品券） | 礼品券付款。必须使用礼品券序列号并进行验证 |
| R | Return Voucher（退货凭证） | 用于 POS 退货的可兑换现金券。必须使用退货凭证序列号并进行验证 |
| O | Online Coupon Redeem（在线券兑换） | 此付款方式由客户在线可用积分兑换的奖励积分支付 |

**S9000 相关类型：**
| ID | 付款类型 | 说明 |
|----|----------|------|
| 0 | S9000(EPM) | 仅在启用"信用卡接口"选项时需要。客户通过 S9000 卡终端使用信用卡（除 CUP 卡外）支付时使用 |
| 1 | S9000(CUP) | 仅在启用"信用卡接口"选项时需要。客户通过 S9000 卡终端使用 CUP 卡支付时使用 |
| 2 | Octopus（八达通） | 仅在启用"八达通"接口选项时需要。通过八达通智能卡支付的付款方式。需要额外的八达通读取设备和程序 |
| 3 | EPAY(Installment)（分期付款） | 不再使用 |
| 4 | S9000 (EIN) | 仅在启用"信用卡接口"选项时需要。S9000 的分期付款功能 |
