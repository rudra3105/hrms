export interface CompanyTenant {
  companyId: string;
  companyName: string;
  branchCode: string;
  payrollConfigName: string;
  employeeIds: string[];
}

export class MultiCompanyRegistry {
  private tenants = new Map<string, CompanyTenant>();

  register(tenant: CompanyTenant) {
    this.tenants.set(tenant.companyId, tenant);
  }

  get(companyId: string) {
    return this.tenants.get(companyId);
  }
}
