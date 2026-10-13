# Insurance Profit and Loss Analytics (insurance_profit_and_loss)

[![Odoo Version](https://img.shields.io/badge/Odoo-17.0%20%7C%2018.0%20%7C%2019.0-714B67?logo=odoo&logoColor=white)](https://www.odoo.com)
[![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-blue.svg)](LICENSE)
[![Category](https://img.shields.io/badge/Category-Accounting%2FFinance-orange.svg)]()
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()

> **Custom Dynamic Profit and Loss Reporting & Underwriting Financial Statements for Insurance Operations.**

---

## 📌 Overview

**Insurance Profit and Loss Analytics** provides specialized, dynamic financial reporting tailored for insurance companies, underwriters, and brokerage firms. It restructures standard Odoo income and expense reporting into insurance-standard formats (Gross Written Premiums, Reinsurance, Net Claims Incurred, Underwriting Expenses, and Net Operating Margins).

---

## ✨ Key Features

### 1. 📑 Dynamic Multi-Level Insurance P&L
- Segregated line structures for insurance-specific accounting:
  - **Premium Revenue & Reinsurance Ceded**
  - **Claims Paid & Incurred But Not Reported (IBNR) Reserves**
  - **Acquisition & Brokerage Commissions**
  - **Operating Underwriting Overhead**

### 2. ⚡ Real-Time Drill-Downs
- Direct interactive drill-downs from high-level statement lines down to individual underlying general ledger journal entries (`account.move.line`).

### 3. 🏢 Multi-Company & Branch Consolidation
- Instant filtering and consolidated comparison across business units, underwriting branches, and financial periods.

---

## 📁 Technical Information

| Attribute | Value |
|---|---|
| **Technical Name** | `insurance_profit_and_loss` |
| **Category** | Accounting |
| **Odoo Compatibility** | Odoo 17.0+ & 18.0+ & 19.0+ |
| **Dependencies** | `base`, `account`, `account_reports` |
| **License** | LGPL-3 |
| **Maintainer** | DraftPOS & Havano Solutions |

---

## 📄 License

This module is licensed under the **GNU Lesser General Public License v3.0 (LGPL-3)**. See the [LICENSE](LICENSE) file for details.
