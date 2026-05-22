---
project: ChainStorePlus
title: 如何设置商品的属性信息（属性I）？
category: 主数据管理
source: v7 Book-2 Section 5.2.3 Pages 25-27
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

商品属性I标签页（Item Attribute I Tab）用于设置商品的各种属性信息，包括品牌、税收、条形码等相关信息。\n\n**操作步骤：**\n1. 进入商品主档维护，选择需要设置的商品\n2. 点击"Item Attribute I（商品属性I）“标签页\n3. 依次填写各项属性字段\n\n**字段说明：**\n\n| 字段名称 | 格式 | 必填/可选 | 说明 |\n|---------|------|----------|------|\n| Tax Code（税码） | - | 可选 | 商品的增值税百分比/增值税金额的税码。此字段关联税率表 |\n| Special Promotion Flag（特别促销标志） | - | 可选 | 控制标志，表示该商品正在进行特别促销。目前无实际流程，仅供参考 |\n| Model Replenishment（按型号补货） | - | 可选 | 控制标志，表示该商品的补货按型号（Model No.）而非按标准商品编号（Item No.）进行 |\n| Owner ID（负责人ID） | X(05) | 必填 | 将针对负责人ID表（Owner ID table）进行验证。这是管理和处理该商品的预先定义的买手/ Merchandiser 代码 |\n| Brand（品牌） | X(06) | 必填 | 将针对品牌表（Brand table）进行验证 |\n| Country（来源国家） | X(02) | 可选 | 将针对国家表（Country table）进行验证。表示商品来源国的国家代码，如有输入需存在于国家代码主档文件中 |\n| Material Code（材料代码） | X(03) | 可选 | 将针对材料代码表（Material Code table）进行验证 |\n| Replenishment（允许补货） | - | 可选 | 勾选表示允许该商品从仓库补货到店铺 |\n| Discontinue Item（停产商品） | - | 可选 | 勾选表示该商品已停产。表示不再采购但仍继续销售。此标记允许系统处理该商品的销售，但停止采购，无需删除该商品记录 |\n| Lock/Release Item（锁定/解锁商品） | - | 可选 | 勾选表示该商品被锁定。此商品将停止所有交易。用户可选择”空白”来解锁此商品 |\n| EAN/UPC Code（EAN/UPC代码） | - | 可选 | 如果商品关联有条码值，在此输入UPC/EAN条形码值 |\n| Bar Code Sequence（条码序列号） | X(07) | 仅显示 | 系统生成的条码序列号。除非另有指定，系统默认使用此条码序列在POS前端系统中表示该商品 |\n| Reference（参考编号） | X(06) | 可选 | 用户自行参考的代码 |\n| Gift（礼品标志） | - | 可选 | 勾选表示该商品可作为礼品赠送，允许零售价和成本为零 |\n| Analysis Code Description（分析代码描述） | X(03) x 10个 | 仅显示 | 描述商品定位的简短代码。根据其在分析代码表维护（Analysis Code Table Maintenance）中定义的位置显示 |\n| Analysis Code（分析代码） | X(03) x 10个 | 可选 | 将针对分析代码表进行验证。用户可为每个字段激活自己的代码，用于将来生成分析报告 |\n| External Season（外部季节码） | X(04) | 可选 | 用于在商品代码结构”外部”需要季节代码的用户，仅供参考 |
