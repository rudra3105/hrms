export type SalaryTransferStatus = 'pending' | 'transferred' | 'failed';
export type ContractType = 'limited' | 'unlimited';
export type SeparationType = 'resignation' | 'termination';

export interface SalaryStructure {
  basicSalary: number;
  housingAllowance: number;
  transportAllowance: number;
  otherAllowances: number;
}

export interface PayrollEntry {
  employeeId: string;
  periodStart: string;
  periodEnd: string;
  salary: SalaryStructure;
  overtimeAmount: number;
  leaveDeductions: number;
  bonus: number;
  otherDeductions: number;
  transferStatus: SalaryTransferStatus;
}

export interface EmployeeUAEProfile {
  employeeId: string;
  fullName: string;
  nationality: string;
  emiratesId: string;
  passportNumber: string;
  visaNumber: string;
  labourCardNumber: string;
  ibanNumber: string;
  molId: string;
  insuranceDetails: string;
  workPermitNumber: string;
  visaExpiry: string;
  emiratesIdExpiry: string;
  passportExpiry: string;
}
