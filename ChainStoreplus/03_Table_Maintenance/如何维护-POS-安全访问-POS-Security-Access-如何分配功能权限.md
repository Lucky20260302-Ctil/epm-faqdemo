---
project: ChainStorePlus
title: 如何维护 POS 安全访问（POS Security Access）？如何分配功能权限？
category: 基础表维护
source: v7 Book-1 Section 4.14 Page 63-64
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

POS 安全访问维护用于定义不同的安全代码及其功能访问权限。

**摘要页面：**
- 列出系统中已定义的所有"安全代码"(Security Code)
- 这些代码根据定义的"角色描述"赋予不同的功能访问权限
- 例如："Shop Manager"（店铺经理）角色的访问权限应与 "Shop Supervisor"（店铺主管）或 "Shop Trainee"（店铺实习生）不同

**权限分配：**
- 首先需要为您需要的角色创建访问权限，如"Shop Manager"或"Sales Supervisor"的不同 POS 安全代码
- 然后将此安全代码（如店铺经理）分配给在店铺中担任销售经理角色的销售人员（或一组店铺）

**功能权限设置：**
- 勾选符号（Tick）表示已授权访问该流程的功能
- 锁符号（Lock）表示禁止访问该流程功能

**示例：**
- 管理员 (Administrator) 角色拥有所有功能的访问权限（全部勾选）
- 普通销售人员可能只有销售相关功能的访问权限
