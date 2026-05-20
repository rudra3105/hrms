# UAE HRMS & Payroll Core

Enterprise-grade UAE-first HRMS and payroll domain core designed for SaaS scale (similar product direction: Zoho People, Bayzat, Darwinbox).

## Implemented UAE Compliance Modules

- **Payroll engine (modular + configurable):**
  - Basic, housing, transport, and other allowances.
  - Gross salary and net salary computation.
  - Monthly payroll compatibility fields.
  - Reusable formulas for overtime, leave deduction, bonus, gratuity, and final settlement.
- **WPS compatibility:**
  - WPS export record object with AED currency and transfer status support.
- **UAE gratuity automation:**
  - 21 days/year for first 5 years.
  - 30 days/year after 5 years.
  - Based **only on basic salary**.
  - Cap at **2 years basic salary**.
  - Supports resignation/termination scenario parameterization.
- **UAE overtime rules:**
  - Standard 8h/day and 48h/week config.
  - +25% regular overtime and +50% night overtime.
  - Ramadan hours setting included in compliance config.
- **UAE leave support:**
  - Annual, sick, maternity, paternity, bereavement, and Hajj/Umrah leave policy model.
  - Leave accrual service.
- **UAE employment compliance:**
  - Probation and notice period tracking.
  - Limited/unlimited contracts.
  - Visa, Emirates ID, and passport expiry alerts.
- **UAE employee master data fields:**
  - Emirates ID, passport, visa, labour card, nationality, IBAN, MOL ID, insurance, work permit.
- **Reports registry:**
  - Payslip PDF, WPS payroll report, salary summary, overtime, leave balance, gratuity.
- **Dashboard metrics model:**
  - Visa/passport expiry, payroll pending, attendance, leave, and salary analytics.
- **Multi-company architecture baseline:**
  - Tenant registry with per-company/branch payroll config identity.

## Structure

- `src/hrms_uae/config.py` – UAE payroll and compliance config.
- `src/hrms_uae/models.py` – domain entities.
- `src/hrms_uae/payroll/calculators.py` – reusable payroll formulas.
- `src/hrms_uae/payroll/wps.py` – WPS export model/service.
- `src/hrms_uae/hr/compliance.py` – probation, notice, and document expiry logic.
- `src/hrms_uae/hr/leave.py` – UAE leave policy and accrual.
- `src/hrms_uae/reports/services.py` – UAE payroll report catalog.
- `src/hrms_uae/dashboard/alerts.py` – dashboard metrics objects.
- `src/hrms_uae/tenant.py` – multi-company tenant registry.

## Next Enterprise Steps

1. Add persistence layer (PostgreSQL) with row-level tenant isolation.
2. Add REST/GraphQL APIs and auth.
3. Generate actual payslip PDFs and WPS SIF files.
4. Add Arabic-ready i18n and RTL UI support.
5. Add rule-admin UI for configurable formula parameters.
