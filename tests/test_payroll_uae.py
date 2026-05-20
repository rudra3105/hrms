from datetime import date
from decimal import Decimal

from hrms_uae.config import PayrollConfig
from hrms_uae.models import OvertimeRecord, SalaryStructure, SeparationType
from hrms_uae.payroll.calculators import PayrollCalculatorService


def test_gratuity_uses_basic_salary_with_cap():
    calc = PayrollCalculatorService(PayrollConfig())
    gratuity = calc.calculate_gratuity(
        basic_salary=Decimal("10000"),
        start_date=date(2010, 1, 1),
        separation_date=date(2026, 1, 1),
        separation_type=SeparationType.RESIGNATION,
    )
    assert gratuity == Decimal("20000.00")


def test_overtime_calculation():
    calc = PayrollCalculatorService(PayrollConfig())
    salary = SalaryStructure(
        basic_salary=Decimal("6000"),
        housing_allowance=Decimal("2000"),
        transport_allowance=Decimal("1000"),
    )
    overtime = OvertimeRecord(regular_hours=10, night_hours=2)
    amount = calc.calculate_overtime(salary, overtime)
    assert amount == Decimal("387.50")
