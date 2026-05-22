---
project: BE
title: "BE-718: CLONE - Translation issue"
issue_key: BE-718
issue_type: Bug QA
status: Closed
faq_score: 10.0
faq_category: 03_Performance_Timeout
faq_category_label: 效能與逾時
tags: [faq, be, performance_timeout, backend-(web)]
jira_url: "https://ctil.atlassian.net/browse/BE-718"
created: 2023-02-21
resolved: 2023-02-21
resolution: Done
has_images: False
---

# BE-718: CLONE - Translation issue

## 問題描述

Env: [https://172.16.138.101/chainstoreplus/home](https://172.16.138.101/chainstoreplus/home)

The following words are still displaying as English under Chinese Tradition condition

Lang: 繁中

**Location: Home page**

1. Still show as Search, should be 尋找 (1.png)

2. ~~Setting Tab> Still show as Setting, should be 設定 > Still show as Logout, should be 登出 (2.png)~~

3. ~~Logout dialog > Still using Eng, should be 你需要登出嗎? (3.png)~~

4. Setting panel > Layout:

- Record Track Log Panel  紀錄追蹤控制台

- Highlight Search Terms 搜尋關鍵字出現發光效果

- Field Size 欄位長度

- Editable Grid Size 可編輯網格大小

- Rows Per Page 調整每頁可顯示行數

- Show Vertical Grid Line 顯示直方格線

- Highlight Even Rows 紀錄格行著光

- Header Size 標題大小

- Row Height 調整列表高度

- Row Font Size 行文字大小

       5.  Setting panel > Theme  主題

- Primary color 主色

- Highlight color 網頁框架及效果著色

      6. Save Changes? Yse/No/Cancel 儲存更變? 是/否/取消

**Home page >colunm: Table maintenance**

Primary  主表格

      1. ~~Nationality (By Display Sequence)   國籍 (以顯示為排列)~~

副表格 (可選項表格)

      1. ~~Tax Free Products Exclusion Table  非免稅產品~~

      ~~2. Denomination Face Value Table  面值表~~

      ~~3. Secondary Tax Free Eligible Products Table 第二合資格貨品免稅表~~

      ~~4. Sales staff password restricted keyword 員工密碼限制關鍵字~~

      ~~5. Sales staff password Policy Table Maintenance 員工密碼設定規則~~

      ~~6. Sub Color 副顏色~~

      ~~7. Delivery Time Slot 送貨時間表~~

      ~~8. Notification Code 通知碼~~

Specials (Custom):

     ~~1. Associate Store Code Maintenance 相關店舖代碼表格~~

**Home page >colunm: Master Maintenance**

~~Member Master~~

    ~~1. Member Managemant Maintenance 會員管理表格~~

~~Price Promation > Promotion Mix & Match~~

   ~~1. Item  x MM Event(s) Match-Up Process   貨品與促銷活動配搭程序~~

**Home page >colunm: Process**

  ~~1. Order Form Process     訂單表格程序~~

  ~~2. Online Order Reserve Process 線上貨品預訂~~

  ~~3. Online Order Invoice Generation 線上訂單發票生成~~

  ~~4. Print Onlline Order Invoive & Delivery Note 列印線上訂單發票及送貨紀錄~~

  ~~5. Online Order Delivery Note Return 退回線上訂單送貨紀錄~~

 

**Home page >colunm: Inquiry**

1. ~~Master File Amendment Log 主檔修改紀錄~~

2. ~~Notification Sending Status Log 傳送通知狀態紀錄~~

3. -庫存調控 > Delivery Order - Stock In Journal 送貨訂單- 存貨日誌-

**Home page >colunm: Data Interface**

數據輸出

      ~~1. Outbound Interface Log Enquiry  向外界面紀錄查詢~~

      ~~2. Define Account Code for Accounting Interface 為會計界面定義帳戶編碼~~

**Home page >colunm: Administration**

    ~~1. Month End process 月結處理~~

    ~~2. 清除歷史記錄 > Purge Transaction History 清除交易記錄~~

    ~~3. Journal Anendment 日誌修改 > Journal Amendment Log Enquiry 日誌修改記錄查詢~~

    ~~4. Manual User Unlock 手動用戶解鎖~~

    ~~5. User Group Access Listing 用戶群組存取列表~~

    ~~6.  Company File 公司檔案~~

    ~~7. Global B.P. sync process全球B.P.同步程序~~

    ~~8. System Configuration Maintenance 系統設置列表~~

    ~~9. Global System Configuration Maintenance  全球系統設置列表~~

 

Detail page of some tabs still show English in Tradition Chinese mode

**Location:  Detail page of some programs**

1. Category Information (MF0005)  大類資料(MF0005)

2. Payment Type Information (MF0009) 付款種類資料(MF0009)

3. Promotion Discount Information (MF4000)  減價折扣資料(MF4000)

4. Owner ID Information (MF4001)  採購員編號資料 (MF4001)

5. Country Information (MF1009) 地區資料 (MF1009)

6. Price Group Information (MF0008) 售價調控資料 (MF1009)

7. ~~Return Voucher Status Reason Information (MX5001) 店舖退貨憑證狀態原因資料 (MX5001)~~

8. Nationality Code Maintenance (MF4008CO) 國籍代碼表格 (MF4008CO)

9. ~~Reason Code Information (MF5001) 原因資料 (MF5001)~~

10. ~~Inventory Group Information (MX1001) 庫存編號表資料 (MX1001)~~

11. ~~Occupation Information (MX2002) 職業代碼資料 (MX2002)~~

12. Project Code Information (MF4003) 項目代碼資料 (MF4003)

13. ~~Aging Table Information (MF5008) 季度表資料  (MF5008)~~

14. ~~Bank/Petty Cash Information (MF6002) 銀行及零錢資料  (MF6002)~~

15. ~~Credit Card Type Information (MX1003) 信用卡種類資料 (MX1003)~~

16. ~~VAT Tax Rate Information (MX2000) 增值稅率資料 (MX2000)~~

17. ~~Tax Code Information (MX2006) 稅代碼資料 (MX2006)~~

18. ~~Tax Free Products Exclusion Table Information (MX4001)  非免稅產品表資料 (MX4001)~~

19. ~~Denomination Face Value Information (MX4002) 面值表資料 (MX4002)~~

20. ~~Secondary Tax Free Eligible Products Table Information (MX4009) 第二合資格貨品免稅表資料 (MX4009)~~

21. ~~Sales Staff Password Restricted Keyword Information (MX5000) 員工密碼限制關鍵字資料 (MX5000)~~

22. ~~Sales Staff Password Policy Table Information (MX5002)  員工密碼設定規則資料 (MX5002)~~

23. ~~Sub Color (MX0006) 副顏色資料 (MX0006)~~

24. ~~Delivery Time Slot Information (MX5003) 送貨時間表資料 (MX5003)~~

25. ~~Notification Information (MX5004) 通知資料 (MX5004)~~

26. ~~Product Line Information (MF7000) 商品線表資料 (MF7000)~~

27. ~~Region Tree Code Information (MX3001) 區域樹圖代碼資料 (MX3001)~~

28. ~~Survey Form Table Information (MX3004) 問券調查代碼 (MX3004)~~

29. ~~Survey Answer Code Information (MX3006) 問券調查答案資料 (MX3006)~~

30. ~~Gender Information (MF8007) 姓別資料 (MF8007)~~

31. ~~Collection Code Information (MF8009) 系列代碼資料(MF8009)~~

32. ~~Label Code Information (MF9000) 標簽代碼資料 (MF9000)~~

33. Inseam Information (MF4005) 內長資料 (MF4005)

34

## 相關資訊

- **Jira:** [BE-718](https://ctil.atlassian.net/browse/BE-718)
- **解決方式:** Done