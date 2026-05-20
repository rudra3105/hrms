from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from enum import Enum


class ContractType(str, Enum):
    LIMITED = "limited"
    UNLIMITED = "unlimited"


class SeparationType(str, Enum):
    RESIGNATION = "resignation"
    TERMINATION = "termination"


class SalaryTransferStatus(str, Enum):
    PENDING = "pending"
    TRANSFERRED = "transferred"
    FAILED = "failed"


@dataclass(slots=True)
class EmployeeUAEProfile:
    employee_id: str
    full_name: str
    nationality: str
    emirates_id: str
    passport_number: str
    visa_number: str
    labour_card_number: str
    iban_number: str
    mol_id: str
    insurance_details: str
    work_permit_number: str
    visa_expiry: date
    emirates_id_expiry: date
    passport_expiry: date


@dataclass(slots=True)
class SalaryStructure:
    basic_salary: Decimal
    housing_allowance: Decimal = Decimal("0")
    transport_allowance: Decimal = Decimal("0")
    other_allowances: Decimal = Decimal("0")

    @property
    def gross_salary(self) -> Decimal:
        return (
            self.basic_salary
            + self.housing_allowance
            + self.transport_allowance
            + self.other_allowances
        )


@dataclass(slots=True)
class EmploymentContract:
    contract_type: ContractType
    start_date: date
    end_date: date | None
    probation_end_date: date
    notice_period_days: int


@dataclass(slots=True)
class PayrollEntry:
    employee_id: str
    period_start: date
    period_end: date
    salary_structure: SalaryStructure
    overtime_amount: Decimal = Decimal("0")
    leave_deductions: Decimal = Decimal("0")
    bonus: Decimal = Decimal("0")
    other_deductions: Decimal = Decimal("0")
    transfer_status: SalaryTransferStatus = SalaryTransferStatus.PENDING

    @property
    def net_salary(self) -> Decimal:
        return (
            self.salary_structure.gross_salary
            + self.overtime_amount
            + self.bonus
            - self.leave_deductions
            - self.other_deductions
        )


@dataclass(slots=True)
class OvertimeRecord:
    regular_hours: float = 0.0
    night_hours: float = 0.0


@dataclass(slots=True)
class CompanyTenant:
    company_id: str
    company_name: str
    branch_code: str
    payroll_config_name: str
    employee_ids: list[str] = field(default_factory=list)
