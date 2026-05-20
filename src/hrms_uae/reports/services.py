from dataclasses import dataclass


@dataclass(slots=True)
class ReportCatalog:
    payslip_pdf: str = "payslip_pdf"
    wps_payroll_report: str = "wps_payroll_report"
    salary_summary: str = "salary_summary"
    overtime_report: str = "overtime_report"
    leave_balance_report: str = "leave_balance_report"
    gratuity_report: str = "gratuity_report"
