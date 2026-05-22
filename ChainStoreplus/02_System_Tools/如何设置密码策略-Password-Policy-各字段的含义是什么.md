---
project: ChainStorePlus
title: 如何设置密码策略（Password Policy）？各字段的含义是什么？
category: 系统工具
source: v7 Book-1 Section 3.7 Page 28-29
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

密码策略定义了密码强度规则，用于判断新密码是否有效。此功能设定密码必须遵守的规则。

**字段说明：**

| 提示 | 说明 |
|------|------|
| Effective Date（生效日期） | X(dd/mm/yyyy) - 必填字段 - 此组密码策略的生效日期 |
| Restrict the reuse recently used passwords times（限制近期密码重复使用次数） | X(5) - 必填字段 - 决定在旧密码可重新使用之前，用户账户必须关联多少个唯一新密码 |
| min char（最小字符数） | X(02) - 可选字段 - 密码的最小字符数 |

**作用：**
- 确保用户设置的新密码满足组织安全要求
- 防止密码短期内重复使用
- 设置最小密码长度，增强密码强度
