# UAE HRMS (Next.js)

This project is now implemented in **Next.js + TypeScript** (not Python), with UAE-specific HR and payroll domain logic designed for enterprise SaaS products.

## Implemented UAE-first modules

- Modular payroll engine in TypeScript:
  - Basic, housing, transport, other allowances
  - Gross/net salary
  - Overtime (+25% regular, +50% night)
  - Leave deductions
  - Gratuity (21/30 day law logic, basic-only, 2-year cap)
  - Final settlement
- WPS-ready payroll structure and salary transfer status model
- UAE employee profile fields (Emirates ID, visa, passport, MOL, IBAN, labour card, insurance)
- Compliance helpers: probation, notice period, visa/passport/Emirates ID expiry alerts
- Report catalog and dashboard-ready metrics domain
- Multi-company baseline registry for UAE SaaS architecture

## Stack

- Next.js (App Router)
- TypeScript
- React

## Run

```bash
npm install
npm run dev
```

## UAE market fit focus

- WPS support
- Gratuity automation
- Visa/passport expiry tracking
- Allowance-heavy salary model
- Multi-company architecture
- Arabic-friendly UI can be added in next iteration
