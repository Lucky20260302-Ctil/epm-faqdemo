---
tags: [moc, troubleshooting, index]
updated: 2026-05-20
---

# 🔧 解決手冊 — Troubleshooting Knowledge Base

> 本手冊收錄從 Jira 已解決 ticket 中提煉的根因分析與解決方案。
> 目標：避免重複調查相同問題，加速未來故障排除。

---

## 依症狀

### POS 交易流程
| 症狀 | Ticket | 元件 |
|------|--------|------|
| All till 無法完成銷售（購買多件時） | [[FE-1520-coupon-discount-calculation-netnetamt\|FE-1520]] | 折扣計算 |
| Levy Charge + MM Coupon 輸入順序異常 | [[FE-1214-levy-mm-coupon-sequence-barcode-validation\|FE-1214]] | 交易流程 |
| 使用 'X' 關閉零 Levy 數量卻產生 qty=1 | [[FE-1214-levy-mm-coupon-sequence-barcode-validation\|FE-1214/FE-1213]] | 交易流程 |
| Barcode 驗證擋掉短條碼 (< 12 碼) | [[FE-1214-levy-mm-coupon-sequence-barcode-validation\|FE-1214]] | Barcode |
| 換匯交易缺少 VAT/GST 稅金 | [[FE-1688-tax-missing-cn-exchange-transactions\|FE-1688]] | 稅務計算 |
| 錯誤的 Member Discount 套用到同類型 VIP | [[FE-1476-hkjc-rems-member-type-offline-online-mismatch\|FE-1476]] | 會員折扣 |
| MM Coupon 折扣四捨五入方法不一致 | [[FE-1200-mm-coupon-rounding-method\|FE-1200]] | 折扣計算 |
| VAT 金額不正確（Gain No-change 計入 GST） | [[FE-1514-vat-amount-gst-misc-amt-exclude\|FE-1514]] | GST 計算 |
| Promo Code CLE062A 在 POS 未生效 | [[FE-1611-promo-code-zfile-update-failure\|FE-1611]] | Zfile / Promo |
| GetBestCalc pricing 失敗未中斷交易 | [[MP-546-getbestcalc-failure-handling\|MP-546]] | Pricing API |

### MPOS 交易流程
| 症狀 | Ticket | 元件 |
|------|--------|------|
| Queue Busting 完成後訂單仍在佇列中 | [[MP-426-queue-busting-order-close\|MP-426]] | Queue Busting |
| Void 後 e-coupon 未恢復為可用狀態 | [[MP-463-voided-coupon-status-pc-file\|MP-463]] | PC File |
| MPOS member enquiry 查不到會員 | [[MP-511-member-enquiry-region-code\|MP-511]] | Member API |
| MPOS Day End 後不會重啟更新日期 | [[MP-499-mpos-dayend-restart\|MP-499]] | State Sync |
| GetBestCalc 失敗導致 discount variance | [[MP-546-getbestcalc-failure-handling\|MP-546]] | Pricing API |

### Day End / 結算
| 症狀 | Ticket | 元件 |
|------|--------|------|
| Day End PCD 94 漏算 Transfer/Gift Redeem 筆數 | [[FE-1225-dotnet-dayend-missing-transaction-count\|FE-1225]] | Day End |
| PC23XXXX 顯示錯誤的交易筆數 | [[FE-1228-dayend-transaction-count-display\|FE-1228]] | Day End |
| V75 升級後 Day End 無法上傳（cs2kconnect 未觸發） | [[FE-1646-v75-dayend-cs2kconnect-missing\|FE-1646]] | Day End / cs2kconnect |

### 會員 / eName / API
| 症狀 | Ticket | 元件 |
|------|--------|------|
| HK eName 無法預掃 VIP Barcode（CBDT 僅查一次） | [[FE-1318-hk-ename-vip-barcode-cbdt-query\|FE-1318]] | eName / CBDT |
| Thread safety 導致 Member No 錯置 | [[FE-1403-thread-safety-member-no-fix\|FE-1403]] | 會員處理 |
| 交易完成時 Member API 瓶頸導致效能問題 | [[FE-1654-member-api-config-performance\|FE-1654]] | Member API |
| MPOS 在 iOS 15 上閃退 | [[MP-508-mpos-crash-ios15-flutter-upgrade\|MP-508]] | Flutter / iOS |
| MPOS 在 iOS 15 無法安裝 | [[MP-507-mpos-install-fail-ios15-xcode-upgrade\|MP-507]] | Xcode / iOS |

### 資料 / 上傳 / Pay Code
| 症狀 | Ticket | 元件 |
|------|--------|------|
| 無效 '95' pay code 上傳至 BE | [[FE-1487-invalid-95-pay-code-cashflow\|FE-1487]] | Cash Flow |
| 銷售員代碼大小寫 ('aa' vs 'AA') 導致 discount variance | [[FE-1402-sales-associate-code-case-sensitivity\|FE-1402]] | 銷售員代碼 |
| CAR 錯誤 — 備註含 `\|` 導致 Unknown item type | [[FE-1600-car-error-pipe-character-remarks\|FE-1600]] | CAR Interface |
| AO PCD posting error — Bonus Points coupon 未清 | [[FE-1619-ao-pcd-posting-error-bonus-points-coupon\|FE-1619]] | PCD Posting |

### 列印 / 顯示
| 症狀 | Ticket | 元件 |
|------|--------|------|
| Bash Transfer 列印缺少價格資訊 | [[FE-1330-bash-transfer-layout-missing-price\|FE-1330]] | 列印 |
| J429 升級後印表機設定遺失（ADK→OPOS.net） | [[FE-1669-j429-printing-adk-opos-net-device-config\|FE-1669]] | OPOS.net |
| Citizen printer 只印一張收據 | [[MP-521-citizen-printer-one-receipt\|MP-521]] | MPOS Printing |

### 系統服務
| 症狀 | Ticket | 元件 |
|------|--------|------|
| SQL Express service timeout 導致 Standalone mode 異常 | [[FE-1696-sqlexpress-standalone-mode-heartbeat\|FE-1696]] | SQL Express |
| V75 升級後 cs2kconnect 未在 Day End 後執行 | [[FE-1646-v75-dayend-cs2kconnect-missing\|FE-1646]] | cs2kconnect |

### Backend — 資料 / 介面
| 症狀 | Ticket | 元件 |
|------|--------|------|
| CAR 介面時區錯誤 — 使用 HKT 而非 JP/KR 交易時間 | [[BE-1055-car-interface-posting-timezone\|BE-1055/BE-1051]] | CAR Interface |
| Colsiz_seq 滿載導致 ITMEAN 介面 hang | [[BE-841-colsiz-seq-full-itmean-hang\|BE-841]] | ITMEAN |
| 超大 update log 無法自動分割 (>15,000) | [[BE-768-oversized-update-log-auto-split\|BE-768]] | Log |
| HKJC 商品 size category 繼承錯誤 | [[BE-1012-invalid-upc-fasc-size-category\|BE-1012]] | Item Master |
| HK POS reconsolidation CRM phone 不符 | [[BE-1002-hk-pos-reconsolidation-crm-phone-mismatch\|BE-1002]] | CRM Sync |

### Backend — API / CRM
| 症狀 | Ticket | 元件 |
|------|--------|------|
| CRM upsert 吃掉 60% 交易時間 | [[BE-1039-async-upsert-member-performance\|BE-1039]] | BEAPI |
| CRM vip_name 被 BEAPI 覆寫為 'BEAPI' | [[BE-944-crm-vip-name-sync-beapi-overwrite\|BE-944]] | BEAPI |
| CRM vip_no_edm/dm/phone/sms 無法更新 | [[BE-987-crm-vip-expiry-date-update-flag\|BE-987]] | BEAPI |
| CJ DSA OnSalePrice ZeroLength period 無效 | [[BE-1229-dsa-onsalesprice-zerolength-period\|BE-1229]] | PriceChecker |
| JP Posting MQ terminated (transaction context) | [[BE-976-jp-posting-mq-terminated-transaction\|BE-976]] | Posting |

---

## 依元件

### Front End — 交易流程
- [[FE-1520-coupon-discount-calculation-netnetamt\|Coupon Discount 計算基準]] — `v750.04R07+`
- [[FE-1214-levy-mm-coupon-sequence-barcode-validation\|Levy/MM Coupon 輸入順序 & Barcode 驗證]] — `v710.02R14ZL`
- [[FE-1688-tax-missing-cn-exchange-transactions\|換匯交易稅金處理]] — `FE-V75.04R13A`
- [[FE-1200-mm-coupon-rounding-method\|MM Coupon 四捨五入方法]] — `v720.02R20A`
- [[FE-1514-vat-amount-gst-misc-amt-exclude\|VAT/GST Misc Amt 排除]] — `v750.04R10`
- [[FE-1611-promo-code-zfile-update-failure\|Promo Code Zfile 更新失敗]] — `v750.04R10`
- [[FE-1619-ao-pcd-posting-error-bonus-points-coupon\|Bonus Points PCD Posting]] — `v720.02R07ZS`

### Front End — 會員 / API
- [[FE-1318-hk-ename-vip-barcode-cbdt-query\|HK eName VIP Barcode / CBDT Query]] — `v720.02R26A`, `v750.04`
- [[FE-1476-hkjc-rems-member-type-offline-online-mismatch\|HKJC Offline/Online Member Type Mismatch]] — `v750.01R02N`
- [[FE-1403-thread-safety-member-no-fix\|Thread Safety Member No]] — `v750.04R04I`
- [[FE-1654-member-api-config-performance\|Member API 效能 Config]] — `v750.04R11A`

### Front End — Day End
- [[FE-1225-dotnet-dayend-missing-transaction-count\|DotNet Day End 漏算 TR Out]] — `v750.02R01G`
- [[FE-1228-dayend-transaction-count-display\|PC23XXXX 交易筆數顯示]] — `7.5.0.02`
- [[FE-1646-v75-dayend-cs2kconnect-missing\|V75 Day End cs2kconnect 排程]] — `v750.04R11`

### Front End — 資料/上傳
- [[FE-1487-invalid-95-pay-code-cashflow\|無效 Pay Code 上傳]] — `v750.04R04I`
- [[FE-1402-sales-associate-code-case-sensitivity\|銷售員代碼大小寫]] — `v750.04R02B`
- [[FE-1600-car-error-pipe-character-remarks\|CAR Error Pipe 字元]] — `2024-01-02 CAR Release`

### Front End — 列印
- [[FE-1330-bash-transfer-layout-missing-price\|Bash Transfer 列印價格]] — `v720.02R07ZL`
- [[FE-1669-j429-printing-adk-opos-net-device-config\|J429 ADK→OPOS.net 設定遺失]] — `v75.004.1100.0008+`

### SQL Express Service
- [[FE-1696-sqlexpress-standalone-mode-heartbeat\|SQL Express 心跳監控]] — `FE-V75.04R13A`

### Backend — 資料/介面/API
- [[BE-1229-dsa-onsalesprice-zerolength-period\|CJ DSA OnSalePrice ZeroLength]] — `BE-V70R3.145`
- [[BE-1055-car-interface-posting-timezone\|CAR Interface 時區修正]] — `BE-V70R3.102`
- [[BE-1039-async-upsert-member-performance\|Async Member Upsert]] — `v1.7.14`
- [[BE-1012-invalid-upc-fasc-size-category\|HKJC UPC Size Category]] — 待確認
- [[BE-1002-hk-pos-reconsolidation-crm-phone-mismatch\|HK POS Reconsolidation CRM]] — 待確認
- [[BE-987-crm-vip-expiry-date-update-flag\|CRM Expiry Date Flag]] — `v1.6.20`
- [[BE-976-jp-posting-mq-terminated-transaction\|JP Posting MQ Rollback]] — 待確認
- [[BE-944-crm-vip-name-sync-beapi-overwrite\|CRM VIP Name Sync]] — 待確認
- [[BE-841-colsiz-seq-full-itmean-hang\|Colsiz_seq 滿載]] — `BE-V70R3.59`
- [[BE-768-oversized-update-log-auto-split\|Oversized Log Split]] — `BE-V70R3.14a`

### MPOS — 行動 POS
- [[MP-508-mpos-crash-ios15-flutter-upgrade\|iOS 15 閃退 (Flutter)]] — `3.13.2`
- [[MP-507-mpos-install-fail-ios15-xcode-upgrade\|iOS 15 安裝失敗 (Xcode)]] — `3.13.2`
- [[MP-499-mpos-dayend-restart\|Day End 後未重啟]] — `3.13.0`
- [[MP-546-getbestcalc-failure-handling\|GetBestCalc 失敗處理]] — 批次待確認
- [[MP-426-queue-busting-order-close\|Queue Busting 關單]] — `3.9.2a`
- [[MP-463-voided-coupon-status-pc-file\|Void e-coupon 狀態恢復]] — `3.10.2`
- [[MP-511-member-enquiry-region-code\|Member Enquiry Region Code]] — `3.14.0`
- [[MP-521-citizen-printer-one-receipt\|Citizen Printer 單張列印]] — `3.14.1`

---

## 索引總表

| Ticket | 摘要 | 根因明確 | 解法明確 | Fix Version | 標籤 |
|--------|------|---------|---------|-------------|------|
| [[FE-1696-sqlexpress-standalone-mode-heartbeat\|FE-1696]] | SQL Express 心跳監控 | ✅ | ✅ | `FE-V75.04R13A` | #jira/FE-1696 |
| [[FE-1688-tax-missing-cn-exchange-transactions\|FE-1688]] | 換匯交易缺稅金 | ✅ | ✅ | `FE-V75.04R13A` | #jira/FE-1688 |
| [[FE-1646-v75-dayend-cs2kconnect-missing\|FE-1646]] | Day End cs2kconnect 遺失 | ✅ | ✅ | `v750.04R11` | #jira/FE-1646 |
| [[FE-1611-promo-code-zfile-update-failure\|FE-1611]] | Promo Code Zfile 失敗 | ✅ | ✅ | `v750.04R10` | #jira/FE-1611 |
| [[FE-1600-car-error-pipe-character-remarks\|FE-1600]] | CAR Error Pipe 字元 | ✅ | ✅ | `2024-01-02` | #jira/FE-1600 |
| [[FE-1514-vat-amount-gst-misc-amt-exclude\|FE-1514]] | VAT GST Misc Amt | ✅ | ✅ | `v750.04R10` | #jira/FE-1514 |
| [[FE-1619-ao-pcd-posting-error-bonus-points-coupon\|FE-1619]] | Bonus Points PCD | ✅ | ✅ | `v720.02R07ZS` | #jira/FE-1619 |
| [[FE-1669-j429-printing-adk-opos-net-device-config\|FE-1669]] | J429 ADK→OPOS.net | ✅ | ✅ | `v75.004.x` | #jira/FE-1669 |
| [[FE-1654-member-api-config-performance\|FE-1654]] | Member API Config | ✅ | ✅ | `v750.04R11A` | #jira/FE-1654 |
| [[FE-1520-coupon-discount-calculation-netnetamt\|FE-1520]] | 折扣計算基準錯誤 | ✅ | ✅ | `V750.04R07A` | #jira/FE-1520 |
| [[FE-1487-invalid-95-pay-code-cashflow\|FE-1487]] | 無效 Pay Code 上傳 | ✅ | ✅ | `v750.04R04I` | #jira/FE-1487 |
| [[FE-1476-hkjc-rems-member-type-offline-online-mismatch\|FE-1476]] | HKJC 會員類型不一致 | ✅ | ✅ | `v750.01R02N` | #jira/FE-1476 |
| [[FE-1318-hk-ename-vip-barcode-cbdt-query\|FE-1318]] | HK eName VIP 查詢 | ✅ | ✅ | `v720.02R26A` | #jira/FE-1318 |
| [[FE-1200-mm-coupon-rounding-method\|FE-1200]] | MM Coupon 四捨五入 | ✅ | ✅ | `v720.02R20A` | #jira/FE-1200 |
| [[FE-1403-thread-safety-member-no-fix\|FE-1403]] | Thread Safety | ✅ | ✅ | `v750.04R04I` | #jira/FE-1403 |
| [[FE-1402-sales-associate-code-case-sensitivity\|FE-1402]] | 銷售員代碼大小寫 | ✅ | ✅ | `v750.04R02B` | #jira/FE-1402 |
| [[FE-1330-bash-transfer-layout-missing-price\|FE-1330]] | Bash Transfer 列印 | ✅ | ✅ | `v720.02R07ZL` | #jira/FE-1330 |
| [[FE-1225-dotnet-dayend-missing-transaction-count\|FE-1225]] | Day End 漏算 | ✅ | ✅ | `v750.02R01G` | #jira/FE-1225 |
| [[FE-1214-levy-mm-coupon-sequence-barcode-validation\|FE-1214]] | Levy/MM + Barcode | ✅ | ✅ | `v710.02R14ZL` | #jira/FE-1214 |
| [[FE-1228-dayend-transaction-count-display\|FE-1228]] | Day End 交易筆數 | ⚠️ | ✅ | `7.5.0.02` | #jira/FE-1228 |
| [[MP-508-mpos-crash-ios15-flutter-upgrade\|MP-508]] | iOS 15 Crash (Flutter) | ✅ | ✅ | `3.13.2` | #jira/MP-508 |
| [[MP-507-mpos-install-fail-ios15-xcode-upgrade\|MP-507]] | iOS 15 Install (Xcode) | ✅ | ✅ | `3.13.2` | #jira/MP-507 |
| [[MP-499-mpos-dayend-restart\|MP-499]] | MPOS Day End Restart | ✅ | ✅ | `3.13.0` | #jira/MP-499 |
| [[MP-546-getbestcalc-failure-handling\|MP-546]] | GetBestCalc Failure | ✅ | ✅ | — | #jira/MP-546 |
| [[MP-426-queue-busting-order-close\|MP-426]] | Queue Busting Close | ✅ | ✅ | `3.9.2a` | #jira/MP-426 |
| [[MP-463-voided-coupon-status-pc-file\|MP-463]] | Void Coupon Status | ✅ | ✅ | `3.10.2` | #jira/MP-463 |
| [[MP-511-member-enquiry-region-code\|MP-511]] | Member Enquiry Region | ✅ | ✅ | `3.14.0` | #jira/MP-511 |
| [[MP-521-citizen-printer-one-receipt\|MP-521]] | Citizen Printer | ✅ | ✅ | `3.14.1` | #jira/MP-521 |
| [[BE-1229-dsa-onsalesprice-zerolength-period\|BE-1229]] | DSA OnSalePrice ZeroLength | ✅ | ✅ | `BE-V70R3.145` | #jira/BE-1229 |
| [[BE-1055-car-interface-posting-timezone\|BE-1055]] | CAR Interface 時區 | ✅ | ✅ | `BE-V70R3.102` | #jira/BE-1055 |
| [[BE-1039-async-upsert-member-performance\|BE-1039]] | Async Upsert 效能 | ✅ | ✅ | `v1.7.14` | #jira/BE-1039 |
| [[BE-1012-invalid-upc-fasc-size-category\|BE-1012]] | UPC Size Category | ✅ | ✅ | — | #jira/BE-1012 |
| [[BE-1002-hk-pos-reconsolidation-crm-phone-mismatch\|BE-1002]] | HK CRM Phone Mismatch | ⚠️ | ⚠️ | — | #jira/BE-1002 |
| [[BE-987-crm-vip-expiry-date-update-flag\|BE-987]] | CRM Expiry Date Flag | ✅ | ✅ | `v1.6.20` | #jira/BE-987 |
| [[BE-976-jp-posting-mq-terminated-transaction\|BE-976]] | JP Posting MQ Rollback | ✅ | ✅ | — | #jira/BE-976 |
| [[BE-944-crm-vip-name-sync-beapi-overwrite\|BE-944]] | CRM VIP Name Sync | ✅ | ✅ | — | #jira/BE-944 |
| [[BE-841-colsiz-seq-full-itmean-hang\|BE-841]] | Colsiz_seq 滿載 | ✅ | ✅ | `BE-V70R3.59` | #jira/BE-841 |
| [[BE-768-oversized-update-log-auto-split\|BE-768]] | Oversized Log Split | ✅ | ✅ | `BE-V70R3.14a` | #jira/BE-768 |

> **圖例**: ✅ = 完整資訊  ⚠️ = 部分資訊  ❌ = 無資訊
