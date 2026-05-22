---
project: ChainStorePlus
title: 如何在POS系统中进行在线信用检查以及设置会员升级规则？
category: 主数据管理
source: v7 Book-2 Section 5.4.2 Pages 36-37
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

在线信用检查（Online Credit Check）功能和会员升级规则（Upgrade Rules）用于控制员工/会员的总购买限额以及会员类型的自动升级。

**一、在线信用检查（Online Credit Check on Staff / Member's Total Purchase）**

如果特定客户类型（如员工购买）启用了购买限额，POS系统将通过互联网连接在后台执行在线信用检查，以避免超限购买。如果发现会员（通常是员工购买）在控制周期内超出购买限额，POS前端系统将拒绝该笔销售交易。

**二、会员升级规则（Upgrade Rules for Member Customer）**

这是适用于所有客户从一种客户类型升级到另一种客户类型的通用升级规则，当满足以下定义的条件时触发。此会员升级流程将由后台按用户设定的计划以批处理作业方式执行。

**POS提示提醒控制设置（POS Prompt Alert Controls）：**
| 功能 | 说明 |
|------|------|
| Alert Prompt（提醒提示） | 勾选此选项并填写有效期限（天数）后，POS前端系统将在有效期内自动显示右侧的文本消息，作为POS用户的提醒 |
| Effected Period（有效期限） | 以天数表示的有效期 |

示例说明：
当属于客户类型"F"的会员客户在自该客户首次购买日期起计算的180天内在店铺进行购买时，将导致POS系统在销售操作期间自动弹出右侧的文本消息，作为对POS用户的提醒。

**会员类型升级控制设置（Member Type Upgrade Controls）：**
| 功能 | 说明 |
|------|------|
| 升级目标类型 | 如果自首次购买日期以来赚取的奖励积分总额超过输入的数值，该客户类型内的所有会员将升级到指定的新会员类型 |

示例说明：
如果自首次购买日期以来赚取的奖励积分总额超过"5,000"分，客户类型"F"内的所有会员将升级到会员类型"E"。

**重要说明：**
截至版本6.4.3，尚无会员降级机制。
