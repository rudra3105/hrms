from dataclasses import dataclass, field

from hrms_uae.models import CompanyTenant


@dataclass(slots=True)
class MultiCompanyRegistry:
    tenants: dict[str, CompanyTenant] = field(default_factory=dict)

    def register(self, tenant: CompanyTenant) -> None:
        self.tenants[tenant.company_id] = tenant

    def get(self, company_id: str) -> CompanyTenant:
        return self.tenants[company_id]
