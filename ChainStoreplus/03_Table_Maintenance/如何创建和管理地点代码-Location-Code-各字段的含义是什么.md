---
project: ChainStorePlus
title: 如何创建和管理地点代码（Location Code）？各字段的含义是什么？
category: 基础表维护
source: v7 Book-1 Section 4.2 Page 37-41
tags:
- chainstoreplus
- user-manual
- faq
quality: complete
created: '2026-05-22'
---

地点代码用于识别特定地点的用途。系统在许多关键流程中使用地点信息。

**功能：**
1. 创建记录 (Create Record)
2. 修改记录 (Modify Record)
3. 删除记录 (Delete Record)
4. 查看记录 (View Record)
5. 复制记录为新记录 (Copy Record as new)
6. 查找记录 (Find Record)
7. 按列标题排序 (Sort by header)
8. 调整列宽指示 (Adjust column indication)

**(I) 汇总显示 (Summary Display)**

**(II) 常规信息屏幕 (General Info) 字段：**

| 提示 | 说明 |
|------|------|
| Location Code（地点代码） | X(08) - 必填字段 - 首字符应引用部门代码 - 用于定义地点的唯一代码 |
| Location Type（地点类型） | X(01) - 必填字段 - 用户必须从选择框中选择地点类型 |
| Franchisee Operation（特许经营） | 可选复选框 - 如果是特许经营店铺则勾选，其处理流程可能与常规自有店铺不同 |
| Location Name（地点名称） | X(40) - 必填字段 - 地点的描述或名称 |

**(III) 其他属性 (Other Properties) 字段：**

| 提示 | 说明 |
|------|------|
| Open/Close（开店/关店日期） | 输入店铺开业或关闭日期 - dd/mm/yyyy |
| Interface Loc（接口地点） | 可选。仅用于与第三方系统接口对接，其地点代码与 ChainStorePlus 不同 |
| Repl. W/H（补货仓库） | 可选。仅当地点有特殊补货仓库时使用 |
| Project Location（项目地点） | X(01) - 可选字段 - 勾选则启用为此地点为项目地点，需要项目编号才能在项目地点安装 POS |
| Department Store（百货商店） | X(01) - 可选字段 - 勾选则启用为此地点为百货商店 |
| Not Download to POS（不下载到POS） | X(01) - 可选字段 - 勾选则此地点不下载到前端 POS |
| Tax Exemption Allowed（允许免税） | X(01) - 可选字段 - 勾选则此地点允许免税 |
| Not allowed in Stock Transfer（不允许库存调拨） | X(01) - 可选字段 - 勾选则此地点不包含在 POS 库存调拨选择中 |
| Exclude O/H（排除在库存外） | X(01) - 可选字段 - 勾选则此地点排除在现有库存计算之外 |
| Country（国家） | X(02) - 必填字段 - 地点所在的国家代码 |
| Channel（渠道） | 必填字段 - 手动维护的渠道属性，如 1-Retail（零售）、2-Outlet（折扣店）、3-Others（其他） |

**(IV) 组分配 (Group Assignment) - 内部地区结构：**
- 用于定义地点的"内部地区结构"（即该店铺属于哪个地区）
- 示例中地点被定义为"广州市"的"城市级"
- 树状结构显示在列表框中供用户参考
- 注意：各层级之间的树状关系需要先在"Location Tree"（地点树）表中定义
- 控制地点从"店铺到仓库"和"店铺到店铺"的调拨权限
- 在示例中，该店铺设置允许向"省"级别的仓库调拨，店铺间调拨仅限"城市"内
