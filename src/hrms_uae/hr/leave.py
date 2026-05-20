from dataclasses import dataclass


@dataclass(slots=True)
class UAELeavePolicy:
    annual_leave_days: int = 30
    sick_leave_days: int = 90
    maternity_leave_days: int = 60
    paternity_leave_days: int = 5
    bereavement_leave_days: int = 5
    hajj_umrah_leave_days: int = 30


@dataclass(slots=True)
class LeaveBalance:
    annual_used: float = 0
    sick_used: float = 0
    maternity_used: float = 0
    paternity_used: float = 0
    bereavement_used: float = 0
    hajj_umrah_used: float = 0


class LeaveAccrualService:
    def accrue_annual_leave(self, months_of_service: int, policy: UAELeavePolicy) -> float:
        return round((policy.annual_leave_days / 12.0) * months_of_service, 2)
