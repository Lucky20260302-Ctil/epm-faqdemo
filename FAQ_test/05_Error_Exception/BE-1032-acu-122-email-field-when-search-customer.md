---
project: BE
issue_key: BE-1032
issue_type: Improvement
status: Closed
faq_score: 6.0
faq_category: 05_Error_Exception
faq_category_label: 錯誤與異常
tags: [faq, be, error_exception, api]
jira_url: "https://ctil.atlassian.net/browse/BE-1032"
created: 2025-03-19
resolved: 2025-05-02
resolution: Done
has_images: False
---

# BE-1032: [ACU-122] Email field (When search customer) should have validation in backend

> **類型:** Improvement | **狀態:** Closed
> **分類:** 錯誤與異常 | **FAQ 分數:** 6.0
> **解決日期:** 2025-05-02
> **負責人:** Anson Cheung
> **組件:** API

## 問題描述

Add verification with the format of "Email", 

if input value is not a valid email format, 

show error message to the POS terminal, without calling API to search member.

# Consider about searchExact only

Sample :

```
public class EmailValidator
{
    public static bool IsValidEmail(string email)
    {
        if (string.IsNullOrWhiteSpace(email))
        {
            return false;
        }

        string pattern = @"^[^@\s]+@[^@\s]+\.[^@\s]+$";
        return Regex.IsMatch(email, pattern);
    }
}

```



## 相關資訊

- **Jira:** [BE-1032](https://ctil.atlassian.net/browse/BE-1032)
- **解決方式:** Done