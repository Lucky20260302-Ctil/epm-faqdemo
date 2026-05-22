---
project: ChainStorePlus
title: ChainStore Plus 手册中字段定义的符号（如 X(n)、9(n).9(m)、S）分别代表什么含义？
category: 系统入门
source: v7 Book-1 Section 1.2.1 Page 7
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

手册中使用以下符号和缩写来描述字段的含义：

**1. X(n) - 字母数字字符**
- X 代表字母数字字符 (Alphanumeric character)
- n 表示字符数量
- 例如：X(5) 表示 5 个字母数字字符，可接受 "12Abc"、"ab1d3"、"123" 等

**2. 9(n).9(m) - 数字字符**
- 9 代表数字字符 (Numeric character)
- n 表示整数位数
- m 表示小数点后的位数
- 例如：9(3).99 表示 3 位整数和 2 位小数，可接受 "12.10"、"123.09"，不接受 "as8.99"、"1234.56"、"12.987"

**3. S - 带符号数字字段**
- S 表示该数字字段可带正负号 (Signed)
- 正值 (+) 和负值 (-) 均可接受
