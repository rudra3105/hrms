from dataclasses import dataclass


@dataclass(slots=True)
class DashboardMetrics:
    payroll_pending_alerts: int
    visa_expiry_alerts: int
    passport_expiry_alerts: int
    attendance_analytics: dict
    leave_analytics: dict
    salary_analytics: dict
