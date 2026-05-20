from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal, ROUND_HALF_UP

from hrms_uae.config import PayrollConfig
from hrms_uae.models import OvertimeRecord, SeparationType, SalaryStructure


def _round_aed(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


@dataclass(slots=True)
class PayrollCalculatorService:
    config: PayrollConfig

    def calculate_basic_salary(self, salary: SalaryStructure) -> Decimal:
        return _round_aed(salary.basic_salary)

    def calculate_gross_salary(self, salary: SalaryStructure) -> Decimal:
        return _round_aed(salary.gross_salary)

    def calculate_overtime(self, salary: SalaryStructure, overtime: OvertimeRecord) -> Decimal:
        hourly_rate = salary.basic_salary / Decimal("30") / Decimal(str(self.config.compliance.standard_daily_hours))
        regular = hourly_rate * Decimal(str(overtime.regular_hours)) * Decimal(str(self.config.compliance.overtime_regular_multiplier))
        night = hourly_rate * Decimal(str(overtime.night_hours)) * Decimal(str(self.config.compliance.overtime_night_multiplier))
        return _round_aed(regular + night)

    def calculate_leave_deduction(self, salary: SalaryStructure, unpaid_leave_days: float) -> Decimal:
        per_day = salary.gross_salary / Decimal("30")
        return _round_aed(per_day * Decimal(str(unpaid_leave_days)))

    def calculate_bonus(self, variable_bonus: Decimal, fixed_bonus: Decimal = Decimal("0")) -> Decimal:
        return _round_aed(variable_bonus + fixed_bonus)

    def calculate_gratuity(
        self,
        basic_salary: Decimal,
        start_date: date,
        separation_date: date,
        separation_type: SeparationType,
    ) -> Decimal:
        del separation_type  # reserved for policy extensions
        days_of_service = (separation_date - start_date).days
        if days_of_service <= 0:
            return Decimal("0.00")

        service_years = Decimal(days_of_service) / Decimal("365")
        first_five_years = min(service_years, Decimal("5"))
        years_after_five = max(service_years - Decimal("5"), Decimal("0"))

        per_day_basic = basic_salary / Decimal("30")
        gratuity_days = (
            first_five_years * Decimal(str(self.config.gratuity_first_5_years_days_per_year))
            + years_after_five * Decimal(str(self.config.gratuity_after_5_years_days_per_year))
        )
        gratuity = per_day_basic * gratuity_days
        cap = basic_salary * Decimal(str(self.config.gratuity_cap_years))
        return _round_aed(min(gratuity, cap))

    def calculate_final_settlement(
        self,
        salary: SalaryStructure,
        unpaid_leave_days: float,
        overtime: OvertimeRecord,
        gratuity: Decimal,
        bonus: Decimal = Decimal("0"),
        deductions: Decimal = Decimal("0"),
    ) -> Decimal:
        gross = self.calculate_gross_salary(salary)
        overtime_amt = self.calculate_overtime(salary, overtime)
        leave_deduction = self.calculate_leave_deduction(salary, unpaid_leave_days)
        total = gross + overtime_amt + gratuity + bonus - leave_deduction - deductions
        return _round_aed(total)
