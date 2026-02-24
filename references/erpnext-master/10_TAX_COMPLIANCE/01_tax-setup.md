# Tax Setup

## Quick Reference
Configure taxes in ERPNext using Tax Templates. Apply taxes to items and transactions. Supports GST, VAT, and custom tax structures.

## AI Prompt
```
When setting up taxes:
1. Create tax accounts in COA
2. Define tax categories
3. Create Item Tax Templates
4. Create Sales/Purchase Tax Templates
5. Apply to transactions
```

---

## Tax Accounts

### Create in Chart of Accounts
```
Duties and Taxes
├── GST Input - MC
├── GST Output - MC
├── VAT - MC
└── TDS Payable - MC
```

---

## Item Tax Template

```python
template = frappe.get_doc({
    "doctype": "Item Tax Template",
    "title": "GST 18%",
    "taxes": [
        {
            "tax_type": "GST Output - MC",
            "tax_rate": 18
        }
    ]
})
template.insert()
```

---

## Sales Taxes and Charges Template

```python
template = frappe.get_doc({
    "doctype": "Sales Taxes and Charges Template",
    "title": "GST 18%",
    "taxes": [
        {
            "charge_type": "On Net Total",
            "account_head": "GST Output - MC",
            "rate": 18
        }
    ]
})
template.insert()
```

---

## Applying Tax to Transaction

```python
si = frappe.get_doc({
    "doctype": "Sales Invoice",
    "customer": "ABC Corp",
    "items": [{"item_code": "ITEM-001", "qty": 1, "rate": 1000}],
    "taxes_and_charges": "GST 18% - MC"
})
si.insert()
# Tax auto-calculated: 1000 + 180 = 1180
```

---

## Related Topics
- [GST India](./02_gst-india.md)
