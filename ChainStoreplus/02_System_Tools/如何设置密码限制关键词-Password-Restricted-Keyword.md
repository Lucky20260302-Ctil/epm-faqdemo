---
project: ChainStorePlus
title: 如何设置密码限制关键词（Password Restricted Keyword）？
category: 系统工具
source: v7 Book-1 Section 3.6 Page 26-27
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

密码限制关键词功能允许用户在创建账户或更改密码时禁止某些字符或字符串。此表用于查看和输入不能作为密码的全部或部分内容的文字或字符串。

**操作步骤：**
1. 进入 Administration 菜单下的 User Password Restricted Keyword
2. 输入需要限制的关键词
3. 保存设置

**字段说明：**

| 提示 | 说明 |
|------|------|
| Restricted Keyword（限制关键词） | X(40) - 必填字段 - 不能作为用户密码全部或部分内容的文字或字符串 |

**作用：**
- 设置后，任何用户在创建或更改密码时，如果密码包含这些关键词（全部或部分），系统将拒绝该密码
- 这有助于防止使用公司名称、品牌名等易被猜测的密码
