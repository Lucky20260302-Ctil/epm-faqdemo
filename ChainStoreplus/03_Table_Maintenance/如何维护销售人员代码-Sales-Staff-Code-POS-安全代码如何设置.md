---
project: ChainStorePlus
title: 如何维护销售人员代码（Sales Staff Code）？POS 安全代码如何设置？
category: 基础表维护
source: v7 Book-1 Section 4.8 Page 49-50
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

此表用于在系统中登记销售人员的详细信息。通过为每个销售人员分配唯一代码，系统将自动跟踪销售人员的访问授权、销售业绩，甚至在 POS 中的登录和签退考勤。

**字段设置说明：**

**POS 安全代码 (POS Security Code)：**
- 需要预先定义 POS 安全代码表
- 此代码已预设了功能访问权限
- 系统会对照相关表验证此代码

**密码设置：**
- 可设置限制此 POS 用户必须使用密码登录 POS
- 密码需要每 N 个月更改一次

**地点访问权限设置：**
- 这是 POS 用户的地点访问权限设置
- 示例中，此 POS 用户被设置为仅允许访问特定的"地点"/店铺
- 授权地点在示例中进一步定义为仅限 A005 地点
- 用户可以为每个用户设置多个访问地点，每个地点可设置不同的功能访问权限
