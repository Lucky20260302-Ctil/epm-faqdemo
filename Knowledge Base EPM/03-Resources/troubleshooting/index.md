---
tags: [moc, troubleshooting, index]
updated: 2026-05-21
---

# EPM 解決手冊

> 本手冊收錄從 Jira `EPMTDCPROT` 專案已解決工單中提煉的根因分析與解決方案。
> 目標：避免重複調查相同問題，加速未來故障排除。

---

## 依症狀

### Tender & RFQ（13）
| 症狀 | Ticket | 元件 |
|------|--------|------|
| Pre-register / Pre-Tender Stage blocked — unable to validate & submit | [[EPMTDCPROT-1039-troubleshooting\|EPMTDCPROT-1039]] | Tender & RFQ |
| Tender submission blocked after evaluation complete | [[EPMTDCPROT-2293-troubleshooting\|EPMTDCPROT-2293]] | Tender & RFQ |
| Supplier cannot view/download tender documents | [[EPMTDCPROT-2513-troubleshooting\|EPMTDCPROT-2513]] | Tender & RFQ |
| Evaluation score not saving or reverting after page refresh | [[EPMTDCPROT-2839-troubleshooting\|EPMTDCPROT-2839]] | Tender & RFQ |
| RFQ submission error — duplicate supplier response handling | [[EPMTDCPROT-2985-troubleshooting\|EPMTDCPROT-2985]] | Tender & RFQ |
| Award recommendation workflow stuck at approval stage | [[EPMTDCPROT-3023-troubleshooting\|EPMTDCPROT-3023]] | Tender & RFQ |
| Tender Part I creation validation error | [[EPMTDCPROT-3041-troubleshooting\|EPMTDCPROT-3041]] | Tender & RFQ |
| Tender box opening date/time mismatch across timezones | [[EPMTDCPROT-3067-troubleshooting\|EPMTDCPROT-3067]] | Tender & RFQ |
| E-Form approval flow for tender extension fails | [[EPMTDCPROT-3087-troubleshooting\|EPMTDCPROT-3087]] | Tender & RFQ |
| Issue Date / Submission Date calculation incorrect | [[EPMTDCPROT-3127-troubleshooting\|EPMTDCPROT-3127]] | Tender & RFQ |
| Tender addendum not visible to all invited suppliers | [[EPMTDCPROT-3265-troubleshooting\|EPMTDCPROT-3265]] | Tender & RFQ |
| RFQ evaluation score reset after page refresh | [[EPMTDCPROT-3267-troubleshooting\|EPMTDCPROT-3267]] | Tender & RFQ |
| Tender checklist item cannot be checked/completed | [[EPMTDCPROT-3268-troubleshooting\|EPMTDCPROT-3268]] | Tender & RFQ |

### E-Form & Workflow（10）
| 症狀 | Ticket | 元件 |
|------|--------|------|
| E-Form validation fails on mandatory field | [[EPMTDCPROT-1308-troubleshooting\|EPMTDCPROT-1308]] | E-Form & Workflow |
| Workflow approval stuck at specific stage | [[EPMTDCPROT-1685-troubleshooting\|EPMTDCPROT-1685]] | E-Form & Workflow |
| E-Form draft not auto-saving during editing | [[EPMTDCPROT-2200-troubleshooting\|EPMTDCPROT-2200]] | E-Form & Workflow |
| E-Form submit button greyed out after validation | [[EPMTDCPROT-2255-troubleshooting\|EPMTDCPROT-2255]] | E-Form & Workflow |
| Field display issue after workflow transition | [[EPMTDCPROT-3005-troubleshooting\|EPMTDCPROT-3005]] | E-Form & Workflow |
| Conditional field logic not triggering correctly | [[EPMTDCPROT-3006-troubleshooting\|EPMTDCPROT-3006]] | E-Form & Workflow |
| Attachment upload timeout on large files | [[EPMTDCPROT-3046-troubleshooting\|EPMTDCPROT-3046]] | E-Form & Workflow |
| Approval delegation not working after role change | [[EPMTDCPROT-3140-troubleshooting\|EPMTDCPROT-3140]] | E-Form & Workflow |
| E-Form linked to wrong template version | [[EPMTDCPROT-3389-troubleshooting\|EPMTDCPROT-3389]] | E-Form & Workflow |
| Signature panel not rendering in browser | [[EPMTDCPROT-3525-troubleshooting\|EPMTDCPROT-3525]] | E-Form & Workflow |

### Authentication & Login（6）
| 症狀 | Ticket | 元件 |
|------|--------|------|
| User unable to login after password reset | [[EPMTDCPROT-2860-troubleshooting\|EPMTDCPROT-2860]] | Authentication & Login |
| SSO login enters redirect loop | [[EPMTDCPROT-3033-troubleshooting\|EPMTDCPROT-3033]] | Authentication & Login |
| Account locked after single failed password attempt | [[EPMTDCPROT-3188-troubleshooting\|EPMTDCPROT-3188]] | Authentication & Login |
| Supplier account activation link expired prematurely | [[EPMTDCPROT-3450-troubleshooting\|EPMTDCPROT-3450]] | Authentication & Login |
| MFA verification code not received by email | [[EPMTDCPROT-3540-troubleshooting\|EPMTDCPROT-3540]] | Authentication & Login |
| Password expiry notification not sent to suppliers | [[EPMTDCPROT-3553-troubleshooting\|EPMTDCPROT-3553]] | Authentication & Login |

### Email & Notification（3）
| 症狀 | Ticket | 元件 |
|------|--------|------|
| System notification not sent after workflow approval | [[EPMTDCPROT-2394-troubleshooting\|EPMTDCPROT-2394]] | Email & Notification |
| Email template missing dynamic field values | [[EPMTDCPROT-3118-troubleshooting\|EPMTDCPROT-3118]] | Email & Notification |
| Reminder email sent to wrong recipient group | [[EPMTDCPROT-3155-troubleshooting\|EPMTDCPROT-3155]] | Email & Notification |

### Payment & Fee（3）
| 症狀 | Ticket | 元件 |
|------|--------|------|
| Payment gateway timeout during tender fee payment | [[EPMTDCPROT-2843-troubleshooting\|EPMTDCPROT-2843]] | Payment & Fee |
| Incorrect fee calculation for multi-lot tender | [[EPMTDCPROT-2869-troubleshooting\|EPMTDCPROT-2869]] | Payment & Fee |
| Refund processing stuck in pending state | [[EPMTDCPROT-3114-troubleshooting\|EPMTDCPROT-3114]] | Payment & Fee |

### Reporting & Export（3）
| 症狀 | Ticket | 元件 |
|------|--------|------|
| Report generation timeout for large dataset | [[EPMTDCPROT-3121-troubleshooting\|EPMTDCPROT-3121]] | Reporting & Export |
| Export to Excel missing columns from template | [[EPMTDCPROT-3129-troubleshooting\|EPMTDCPROT-3129]] | Reporting & Export |
| PDF report layout broken after system version update | [[EPMTDCPROT-3145-troubleshooting\|EPMTDCPROT-3145]] | Reporting & Export |

### Supplier Management（3）
| 症狀 | Ticket | 元件 |
|------|--------|------|
| Supplier profile update not reflected in active tenders | [[EPMTDCPROT-3040-troubleshooting\|EPMTDCPROT-3040]] | Supplier Management |
| Supplier registration duplicate detection failure | [[EPMTDCPROT-3119-troubleshooting\|EPMTDCPROT-3119]] | Supplier Management |
| Supplier performance score calculation error | [[EPMTDCPROT-3414-troubleshooting\|EPMTDCPROT-3414]] | Supplier Management |

### UI/UX（3）
| 症狀 | Ticket | 元件 |
|------|--------|------|
| Page layout broken on tablet viewport | [[EPMTDCPROT-3075-troubleshooting\|EPMTDCPROT-3075]] | UI/UX |
| Button click not responding in Safari browser | [[EPMTDCPROT-3082-troubleshooting\|EPMTDCPROT-3082]] | UI/UX |
| Date picker component not localizing to zh-TW | [[EPMTDCPROT-3187-troubleshooting\|EPMTDCPROT-3187]] | UI/UX |

### User Management（3）
| 症狀 | Ticket | 元件 |
|------|--------|------|
| User role update not taking effect immediately | [[EPMTDCPROT-3116-troubleshooting\|EPMTDCPROT-3116]] | User Management |
| Bulk user import skipping records without error | [[EPMTDCPROT-3226-troubleshooting\|EPMTDCPROT-3226]] | User Management |
| Department hierarchy not updating in user profile | [[EPMTDCPROT-3373-troubleshooting\|EPMTDCPROT-3373]] | User Management |

### Integration（1）
| 症狀 | Ticket | 元件 |
|------|--------|------|
| API integration with ERP system returning 500 error | [[EPMTDCPROT-3117-troubleshooting\|EPMTDCPROT-3117]] | Integration |

### General（2）
| 症狀 | Ticket | 元件 |
|------|--------|------|
| System performance degradation during peak hours | [[EPMTDCPROT-1915-troubleshooting\|EPMTDCPROT-1915]] | General |
| Database connection pool exhaustion under load | [[EPMTDCPROT-844-troubleshooting\|EPMTDCPROT-844]] | General |

---

## 依元件

### Tender & RFQ
- [[EPMTDCPROT-1039-troubleshooting\|Pre-register / Pre-Tender blocked]] — `2025-03-13`
- [[EPMTDCPROT-2293-troubleshooting\|Tender submission after evaluation]] — `2025-07-23`
- [[EPMTDCPROT-2513-troubleshooting\|Supplier document access]] — `2025-07-14`
- [[EPMTDCPROT-2839-troubleshooting\|Evaluation score saving]] — `2025-11-04`
- [[EPMTDCPROT-2985-troubleshooting\|RFQ duplicate response]] — `2025-11-04`
- [[EPMTDCPROT-3023-troubleshooting\|Award recommendation workflow]] — `2025-10-03`
- [[EPMTDCPROT-3041-troubleshooting\|Part I creation validation]] — `2025-10-15`
- [[EPMTDCPROT-3067-troubleshooting\|Box opening time mismatch]] — `2025-10-11`
- [[EPMTDCPROT-3087-troubleshooting\|Tender extension approval]] — `2025-11-04`
- [[EPMTDCPROT-3127-troubleshooting\|Issue/Submission date calculation]] — `2025-11-28`
- [[EPMTDCPROT-3265-troubleshooting\|Addendum visibility]] — `2026-01-26`
- [[EPMTDCPROT-3267-troubleshooting\|Evaluation score reset]] — `2026-01-14`
- [[EPMTDCPROT-3268-troubleshooting\|Checklist item check]] — `2025-12-30`

### E-Form & Workflow
- [[EPMTDCPROT-1308-troubleshooting\|Validation on mandatory field]] — `2025-05-08`
- [[EPMTDCPROT-1685-troubleshooting\|Approval stuck at stage]] — `2025-05-20`
- [[EPMTDCPROT-2200-troubleshooting\|Draft auto-save]] — `2025-07-07`
- [[EPMTDCPROT-2255-troubleshooting\|Submit button greyed out]] — `2025-07-07`
- [[EPMTDCPROT-3005-troubleshooting\|Field display after transition]] — `2025-09-29`
- [[EPMTDCPROT-3006-troubleshooting\|Conditional logic]] — `2025-09-29`
- [[EPMTDCPROT-3046-troubleshooting\|Attachment upload timeout]] — `2025-11-04`
- [[EPMTDCPROT-3140-troubleshooting\|Approval delegation]] — `2025-12-22`
- [[EPMTDCPROT-3389-troubleshooting\|Wrong template linkage]] — `2026-04-13`
- [[EPMTDCPROT-3525-troubleshooting\|Signature panel]] — `2026-04-28`

### Authentication & Login
- [[EPMTDCPROT-2860-troubleshooting\|Password reset login]] — `2025-09-02`
- [[EPMTDCPROT-3033-troubleshooting\|SSO redirect loop]] — `2025-11-04`
- [[EPMTDCPROT-3188-troubleshooting\|Account lockout]] — `2026-01-22`
- [[EPMTDCPROT-3450-troubleshooting\|Activation link expired]] — `2026-04-16`
- [[EPMTDCPROT-3540-troubleshooting\|MFA code not received]] — `2026-04-28`
- [[EPMTDCPROT-3553-troubleshooting\|Password expiry notification]] — `2026-05-13`

### Email & Notification
- [[EPMTDCPROT-2394-troubleshooting\|Notification after approval]] — `2025-07-21`
- [[EPMTDCPROT-3118-troubleshooting\|Email template fields]] — `2025-12-22`
- [[EPMTDCPROT-3155-troubleshooting\|Reminder to wrong group]] — `2025-11-28`

### Payment & Fee
- [[EPMTDCPROT-2843-troubleshooting\|Gateway timeout]] — `2025-09-18`
- [[EPMTDCPROT-2869-troubleshooting\|Multi-lot fee calculation]] — `2025-09-18`
- [[EPMTDCPROT-3114-troubleshooting\|Refund processing stuck]] — `2025-11-03`

### Reporting & Export
- [[EPMTDCPROT-3121-troubleshooting\|Report generation timeout]] — `2025-12-22`
- [[EPMTDCPROT-3129-troubleshooting\|Excel missing columns]] — `2025-12-22`
- [[EPMTDCPROT-3145-troubleshooting\|PDF layout broken]] — `2026-01-14`

### Supplier Management
- [[EPMTDCPROT-3040-troubleshooting\|Profile update not reflected]] — `2025-10-15`
- [[EPMTDCPROT-3119-troubleshooting\|Duplicate detection failure]] — `2025-12-22`
- [[EPMTDCPROT-3414-troubleshooting\|Performance score error]] — `2026-03-10`

### UI/UX
- [[EPMTDCPROT-3075-troubleshooting\|Tablet layout broken]] — `2025-10-15`
- [[EPMTDCPROT-3082-troubleshooting\|Safari button click]] — `2025-10-15`
- [[EPMTDCPROT-3187-troubleshooting\|Date picker localization]] — `2026-04-13`

### User Management
- [[EPMTDCPROT-3116-troubleshooting\|Role update delay]] — `2025-11-28`
- [[EPMTDCPROT-3226-troubleshooting\|Bulk import skip]] — `2026-04-16`
- [[EPMTDCPROT-3373-troubleshooting\|Department hierarchy]] — `2026-01-28`

### Integration
- [[EPMTDCPROT-3117-troubleshooting\|ERP API integration]] — `2025-12-22`

### General
- [[EPMTDCPROT-1915-troubleshooting\|Peak hour performance]] — `2025-05-27`
- [[EPMTDCPROT-844-troubleshooting\|DB connection pool]] — `2025-08-04`

---

## 索引總表

| Ticket | 摘要 | 元件 | 根因 | 解法 | 日期 |
|--------|------|------|------|------|------|
| [[EPMTDCPROT-3553-troubleshooting\|3553]] | Password expiry notification | Auth & Login | ❌ | ❌ | 2026-05-13 |
| [[EPMTDCPROT-3540-troubleshooting\|3540]] | MFA code not received | Auth & Login | ❌ | ❌ | 2026-04-28 |
| [[EPMTDCPROT-3525-troubleshooting\|3525]] | E-Form signature panel | E-Form | ❌ | ❌ | 2026-04-28 |
| [[EPMTDCPROT-3450-troubleshooting\|3450]] | Account activation link | Auth & Login | ❌ | ❌ | 2026-04-16 |
| [[EPMTDCPROT-3414-troubleshooting\|3414]] | Supplier performance score | Supplier Mgmt | ❌ | ❌ | 2026-03-10 |
| [[EPMTDCPROT-3389-troubleshooting\|3389]] | Wrong template linkage | E-Form | ❌ | ❌ | 2026-04-13 |
| [[EPMTDCPROT-3373-troubleshooting\|3373]] | Department hierarchy | User Mgmt | ❌ | ❌ | 2026-01-28 |
| [[EPMTDCPROT-3268-troubleshooting\|3268]] | Checklist item check | Tender & RFQ | ❌ | ❌ | 2025-12-30 |
| [[EPMTDCPROT-3267-troubleshooting\|3267]] | Evaluation score reset | Tender & RFQ | ❌ | ❌ | 2026-01-14 |
| [[EPMTDCPROT-3265-troubleshooting\|3265]] | Addendum visibility | Tender & RFQ | ❌ | ❌ | 2026-01-26 |
| [[EPMTDCPROT-3226-troubleshooting\|3226]] | Bulk import skip | User Mgmt | ❌ | ❌ | 2026-04-16 |
| [[EPMTDCPROT-3188-troubleshooting\|3188]] | Account lockout | Auth & Login | ❌ | ❌ | 2026-01-22 |
| [[EPMTDCPROT-3187-troubleshooting\|3187]] | Date picker localization | UI/UX | ✅ | ✅ | 2026-04-13 |
| [[EPMTDCPROT-3155-troubleshooting\|3155]] | Reminder to wrong group | Email | ❌ | ❌ | 2025-11-28 |
| [[EPMTDCPROT-3145-troubleshooting\|3145]] | PDF layout broken | Reporting | ✅ | ✅ | 2026-01-14 |
| [[EPMTDCPROT-3140-troubleshooting\|3140]] | Approval delegation | E-Form | ❌ | ❌ | 2025-12-22 |
| [[EPMTDCPROT-3129-troubleshooting\|3129]] | Excel missing columns | Reporting | ❌ | ❌ | 2025-12-22 |
| [[EPMTDCPROT-3127-troubleshooting\|3127]] | Issue/Submission date | Tender & RFQ | ❌ | ❌ | 2025-11-28 |
| [[EPMTDCPROT-3121-troubleshooting\|3121]] | Report generation timeout | Reporting | ❌ | ❌ | 2025-12-22 |
| [[EPMTDCPROT-3119-troubleshooting\|3119]] | Duplicate detection fail | Supplier Mgmt | ❌ | ❌ | 2025-12-22 |
| [[EPMTDCPROT-3118-troubleshooting\|3118]] | Email template fields | Email | ❌ | ❌ | 2025-12-22 |
| [[EPMTDCPROT-3117-troubleshooting\|3117]] | ERP API integration | Integration | ❌ | ❌ | 2025-12-22 |
| [[EPMTDCPROT-3116-troubleshooting\|3116]] | Role update delay | User Mgmt | ❌ | ❌ | 2025-11-28 |
| [[EPMTDCPROT-3114-troubleshooting\|3114]] | Refund processing stuck | Payment | ❌ | ❌ | 2025-11-03 |
| [[EPMTDCPROT-3087-troubleshooting\|3087]] | Tender extension approval | Tender & RFQ | ✅ | ✅ | 2025-11-04 |
| [[EPMTDCPROT-3082-troubleshooting\|3082]] | Safari button click | UI/UX | ✅ | ✅ | 2025-10-15 |
| [[EPMTDCPROT-3075-troubleshooting\|3075]] | Tablet layout broken | UI/UX | ✅ | ✅ | 2025-10-15 |
| [[EPMTDCPROT-3067-troubleshooting\|3067]] | Box opening time mismatch | Tender & RFQ | ❌ | ❌ | 2025-10-11 |
| [[EPMTDCPROT-3046-troubleshooting\|3046]] | Attachment upload timeout | E-Form | ✅ | ✅ | 2025-11-04 |
| [[EPMTDCPROT-3041-troubleshooting\|3041]] | Part I creation validation | Tender & RFQ | ❌ | ❌ | 2025-10-15 |
| [[EPMTDCPROT-3040-troubleshooting\|3040]] | Profile update not reflected | Supplier Mgmt | ❌ | ❌ | 2025-10-15 |
| [[EPMTDCPROT-3033-troubleshooting\|3033]] | SSO redirect loop | Auth & Login | ❌ | ❌ | 2025-11-04 |
| [[EPMTDCPROT-3023-troubleshooting\|3023]] | Award recommendation | Tender & RFQ | ✅ | ✅ | 2025-10-03 |
| [[EPMTDCPROT-3006-troubleshooting\|3006]] | Conditional logic | E-Form | ❌ | ❌ | 2025-09-29 |
| [[EPMTDCPROT-3005-troubleshooting\|3005]] | Field display after transition | E-Form | ❌ | ❌ | 2025-09-29 |
| [[EPMTDCPROT-2985-troubleshooting\|2985]] | RFQ duplicate response | Tender & RFQ | ✅ | ✅ | 2025-11-04 |
| [[EPMTDCPROT-2869-troubleshooting\|2869]] | Multi-lot fee calculation | Payment | ❌ | ❌ | 2025-09-18 |
| [[EPMTDCPROT-2860-troubleshooting\|2860]] | Password reset login | Auth & Login | ✅ | ✅ | 2025-09-02 |
| [[EPMTDCPROT-2843-troubleshooting\|2843]] | Gateway timeout | Payment | ❌ | ❌ | 2025-09-18 |
| [[EPMTDCPROT-2839-troubleshooting\|2839]] | Evaluation score saving | Tender & RFQ | ❌ | ❌ | 2025-11-04 |
| [[EPMTDCPROT-2513-troubleshooting\|2513]] | Supplier document access | Tender & RFQ | ✅ | ✅ | 2025-07-14 |
| [[EPMTDCPROT-2394-troubleshooting\|2394]] | Notification after approval | Email | ❌ | ❌ | 2025-07-21 |
| [[EPMTDCPROT-2293-troubleshooting\|2293]] | Tender after evaluation | Tender & RFQ | ❌ | ❌ | 2025-07-23 |
| [[EPMTDCPROT-2255-troubleshooting\|2255]] | Submit button greyed out | E-Form | ❌ | ❌ | 2025-07-07 |
| [[EPMTDCPROT-2200-troubleshooting\|2200]] | Draft auto-save | E-Form | ❌ | ❌ | 2025-07-07 |
| [[EPMTDCPROT-1915-troubleshooting\|1915]] | Peak hour performance | General | ❌ | ❌ | 2025-05-27 |
| [[EPMTDCPROT-1685-troubleshooting\|1685]] | Approval stuck at stage | E-Form | ❌ | ❌ | 2025-05-20 |
| [[EPMTDCPROT-1308-troubleshooting\|1308]] | Validation on mandatory field | E-Form | ❌ | ❌ | 2025-05-08 |
| [[EPMTDCPROT-1039-troubleshooting\|1039]] | Pre-register blocked | Tender & RFQ | ❌ | ❌ | 2025-03-13 |
| [[EPMTDCPROT-844-troubleshooting\|844]] | DB connection pool | General | ❌ | ❌ | 2025-08-04 |

> **圖例**: ✅ = 完整資訊（有根因與解法）  ❌ = 待補充（佔位筆記，需查閱 Jira 工單）
>
> 50 篇中 **10 篇（20%）** 已完整回填，**40 篇（80%）** 為自動同步的佔位筆記。參閱 [[Welcome|新手入門指南]] 了解如何使用。
