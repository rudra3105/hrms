from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta

from hrms_uae.models import EmployeeUAEProfile, EmploymentContract


@dataclass(slots=True)
class ExpiryAlerts:
    visa_expiring: bool
    emirates_id_expiring: bool
    passport_expiring: bool


@dataclass(slots=True)
class UAEComplianceService:
    alert_window_days: int = 60

    def probation_active(self, contract: EmploymentContract, as_of: date) -> bool:
        return as_of <= contract.probation_end_date

    def notice_period_end(self, contract: EmploymentContract, notice_start: date) -> date:
        return notice_start + timedelta(days=contract.notice_period_days)

    def document_alerts(self, employee: EmployeeUAEProfile, as_of: date) -> ExpiryAlerts:
        boundary = as_of + timedelta(days=self.alert_window_days)
        return ExpiryAlerts(
            visa_expiring=employee.visa_expiry <= boundary,
            emirates_id_expiring=employee.emirates_id_expiry <= boundary,
            passport_expiring=employee.passport_expiry <= boundary,
        )
