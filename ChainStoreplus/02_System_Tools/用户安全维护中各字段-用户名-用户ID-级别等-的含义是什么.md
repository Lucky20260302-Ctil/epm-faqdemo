---
project: ChainStorePlus
title: 用户安全维护中各字段（用户名、用户ID、级别等）的含义是什么？
category: 系统工具
source: v7 Book-1 Section 3.4 Page 23-24
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

用户安全维护（User Security Maintenance）屏幕用于维护用户的登录信息和系统访问权限。以下是各字段的详细说明：

**字段说明：**

| 提示 | 说明 |
|------|------|
| User Name（用户名） | X(40) - 必填字段 - 用户登录 ID |
| Full Name（全名） | X(40) - 必填字段 - 用户全名 |
| User ID（用户编号） | X(03) - 必填字段 - 系统用户 ID |
| Class（级别） | X(01) - 必填字段 - 用户在公司的级别：0=管理员，1=正式员工（可查看产品成本），2=初级员工（不可查看产品成本） |
| User Group（用户组） | X(40) - 可选字段 - ChainStorePlus 用户组 |
| Dept（部门） | X(01) - 可选字段 - 部门代码 |
| Expiry Period（有效期限） | 月数 - 用户密码的有效期（月数） |
| Expiry Date（到期日期） | dd/mm/yyyy - 用户密码到期日期 |
| Change button（更改按钮） | 用户密码设置按钮 - 使用方法请参见下一段落（用户密码更改） |
