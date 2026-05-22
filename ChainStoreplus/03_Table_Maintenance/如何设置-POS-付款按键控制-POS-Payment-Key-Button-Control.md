---
project: ChainStorePlus
title: 如何设置 POS 付款按键控制（POS Payment Key Button Control）？
category: 基础表维护
source: v7 Book-1 Section 4.10 Page 56
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

此流程允许用户根据个人偏好设置 POS 前台的付款按键顺序。

**操作说明：**

**按键分配规则：**
- 用户可以自由编辑/分配付款流程到每个按钮
- 最后一个 <F10> 按钮保留为 "EXIT"（退出）按钮，不可更改
- 如有必要，用户可以在一个按钮中"分组"多个付款类型
- 示例："Foreign Exchange"（外币）按钮可以将多种可接受的外币归入一个按钮下，如美元、新台币、欧元、日元等

**布局设置：**
- POS 付款按键布局可以分配到店铺级别（Shop Level）
- 如果设置为 "Blank"（空白），则表示适用于所有店铺
- POS 付款按键布局根据每种基础货币（Base Currency）定义：
  - 至少为接收港币（HK$）的香港店铺设置一套布局
  - 为接收人民币（RMB）的中国店铺设置另一套 POS 付款按键布局

**付款代码引用：**
- 按键引用的付款代码需要在 POS 付款方式表（Payment Table）中预先定义
