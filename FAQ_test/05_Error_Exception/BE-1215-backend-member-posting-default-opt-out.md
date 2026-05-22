---
project: BE
title: "BE-1215: Backend member posting - default Opt-Out"
issue_key: BE-1215
issue_type: Task
status: Closed
faq_score: 7.5
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, posting]
jira_url: "https://ctil.atlassian.net/browse/BE-1215"
created: 2025-11-28
resolved: 2026-02-11
resolution: Done
has_images: True
---

# BE-1215: Backend member posting - default Opt-Out 

## 問題描述

The ANZ region requests that new members created via BE Posting should have a configurable default opt-out setting for communication channels.

---

### **Current Behavior:**

- FE has already added a configuration:
`tblconfig.NVIPInputCommOpt` to control default opt-out behavior on the FE side.

- When a new member is created via BE Posting using **PC file record type 34**, the following columns are currently set to **NULL** by default:

- `vip_no_edm`

- `vip_no_dm`

- `vip_no_phone`

- `vip_no_sms`

---

### **Change Request:**

Add a new BE configuration:
`posting_member_Opt_default`

**Behavior:**

- If `posting_member_Opt_default = Y`
→ Set `vip_no_edm`, `vip_no_dm`, `vip_no_phone`, `vip_no_sms` to **Y** when creating a new member.

- If `posting_member_Opt_default = N`
→ Set `vip_no_edm`, `vip_no_dm`, `vip_no_phone`, `vip_no_sms` to **NULL** when creating a new member.

---

### **Acceptance Criteria:**

1. BE Posting program reads `posting_member_Opt_default` configuration.

2. Applies default opt-out values based on the configuration during member creation.

> 📎 **image-20251128-081446.png** — [查看附件](https://ctil.atlassian.net/rest/api/3/attachment/content/f9724fe9-c25f-493b-ab6b-afea80acfc48)（需 Jira 登入）


## 附件截圖

1. 📎 **image-20251128-081446.png** — [在 Jira 查看](https://ctil.atlassian.net/rest/api/3/attachment/content/f9724fe9-c25f-493b-ab6b-afea80acfc48)

## 相關資訊

- **Jira:** [BE-1215](https://ctil.atlassian.net/browse/BE-1215)
- **解決方式:** Done