---
project: ChainStorePlus
title: 如何设置商品的附加属性信息（属性II）？
category: 主数据管理
source: v7 Book-2 Section 5.2.4 Pages 28-31
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

商品属性II标签页（Item Attribute II Tab）用于设置商品更多的附加属性信息，包括品牌名称、年份、型号、季节、图片、出版信息以及特殊日期等。\n\n**操作步骤：**\n1. 进入商品主档维护，选择需要设置的商品\n2. 点击"Item Attribute II（商品属性II）“标签页\n3. 填写各项属性字段\n4. 查看商品图片和重要日期信息\n\n**常规属性字段说明：**\n\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Brand（品牌名称） | X(30) | 可选 | 商品有品牌名称时使用 |\n| Year（年份） | X(04) | 可选 | 产品的年份 |\n| Category（类别） | X(12) | 可选 | 商品的类别代码 |\n| Model Number（型号） | X(20) | 可选 | 商品的型号 |\n| Article（货号） | X(30) | 可选 | 商品的货号 |\n| Variante（变体） | X(?) | 可选 | 商品的变体信息 |\n| Sex（性别） | X(04) | 可选 | 商品的性别信息 |\n| Season（季节） | X(02) | 可选 | 季节信息，需在”季节代码（Season Code）“中预定义 |\n| Collection（系列） | X(30) | 可选 | 商品的系列/集合 |\n| Sub Category（子类别） | X(12) | 可选 | 商品的子类别代码 |\n| Label（标签） | X(20) | 可选 | 商品的标签 |\n| Product（产品） | X(20) | 可选 | 商品的产品信息 |\n\n**图片（Image）按钮：**\n- 此按钮将显示该商品的图片\n- 图片需要存储在先前定义的专用图片文件夹中\n- 图片文件名必须遵循以下格式：<文件名> = 商品编号_999，其中'999'是图片的序列号\n  - 例如：A9008765433_001, A9008765433_002, A9008765433_003 等\n- 系统将自动收集该商品的所有图片，并在标准的Windows图片浏览器中一次性显示\n\n**出版信息字段（Publication Section，适用于书籍/出版物类商品）：**\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Magazine Code（期刊代码） | X(20) | 可选 | 出版物的ID编号 |\n| Edition No.（版次） | X(20) | 可选 | 出版物的版次 |\n| Language Version（语言版本） | X(20) | 可选 | 出版物特定语言版本的版本号 |\n| Publisher（出版社） | X(40) | 可选 | 出版社名称 |\n| Author（作者） | X(40) | 可选 | 作者名称 |\n\n**特殊与日期标签页（Special & Date Tab）字段说明：**\n\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Model Number（型号） | X(30) | 可选 | 商品关联的型号。商品查询功能中有针对此型号的特殊搜索键。非常适合手表和珠宝零售商或有类似产品性质的用户 |\n| Warranty Number（保修编号） | X(30) | 可选 | 商品关联的唯一序列号。商品查询功能中有针对此序列号搜索的特殊搜索键。非常适合手表和珠宝零售商或有类似产品性质的用户 |\n| Body Number（机身号） | X(20) | 可选 | 来自制造商的信息编号 |\n| Style Number（款号） | X(12) | 可选 | 用户自行参考的代码 |\n| Volume / Content / Container（卷/内容/容器） | - | 可选 | 用户自行参考的代码 |\n| Expiration Date（有效期） | dd/mm/yyyy | 可选 | 表示商品的有效期（如有），仅供参考 |\n\n**重要日期（仅显示，不可编辑）：**\n| 字段名称 | 格式 | 说明 |\n|---------|------|------|\n| Creation Date（创建日期） | dd/mm/yyyy | 该商品主档记录创建时的日期 |\n| First Receipt Date（首次收货日期） | dd/mm/yyyy | 该商品主档记录首次收货的日期 |\n| Last Receipt Date（最后收货日期） | dd/mm/yyyy | 该商品主档记录最近一次收货的日期 |\n| First Transfer Date（首次调拨日期） | dd/mm/yyyy | 该商品主档记录首次调拨的日期（通常首次调拨是从仓库到店铺） |\n| Last Sales Date（最后销售日期） | dd/mm/yyyy | 该商品主档记录最后一次销售的日期 |\n| New Season 1st Delivery Date（新季节首次交货日期） | dd/mm/yyyy | 该商品标记为季节首次交货的日期，仅适用于特殊季节产品 |\n| Last Modified Date（最后修改日期） | dd/mm/yyyy | 该商品主档记录最后被修改并记录用户ID的日期 |
