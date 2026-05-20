from dataclasses import dataclass, field
from zoneinfo import ZoneInfo


@dataclass(slots=True)
class UAEComplianceConfig:
    currency_code: str = "AED"
    timezone: ZoneInfo = ZoneInfo("Asia/Dubai")
    date_format: str = "%d/%m/%Y"
    standard_daily_hours: float = 8.0
    standard_weekly_hours: float = 48.0
    overtime_regular_multiplier: float = 1.25
    overtime_night_multiplier: float = 1.50
    ramadan_daily_hours: float = 6.0


@dataclass(slots=True)
class PayrollConfig:
    compliance: UAEComplianceConfig = field(default_factory=UAEComplianceConfig)
    monthly_cycle_day: int = 1
    gratuity_first_5_years_days_per_year: int = 21
    gratuity_after_5_years_days_per_year: int = 30
    gratuity_cap_years: int = 2
