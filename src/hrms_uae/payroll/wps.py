from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from hrms_uae.models import PayrollEntry


@dataclass(slots=True)
class WPSRecord:
    employee_id: str
    iban: str
    period_end: date
    net_salary: Decimal
    currency: str = "AED"


class WPSExportService:
    def build_wps_record(self, entry: PayrollEntry, employee_iban: str) -> WPSRecord:
        return WPSRecord(
            employee_id=entry.employee_id,
            iban=employee_iban,
            period_end=entry.period_end,
            net_salary=entry.net_salary,
        )
