import { PayrollEntry, SalaryStructure, SeparationType } from '@/types/hrms';

const DAYS_IN_MONTH = 30;
const UAE = {
  standardDailyHours: 8,
  regularOT: 1.25,
  nightOT: 1.5,
  gratuityFirstFiveYearsDays: 21,
  gratuityAfterFiveYearsDays: 30,
  gratuityCapYears: 2,
  currency: 'AED',
};

export const round2 = (value: number) => Math.round((value + Number.EPSILON) * 100) / 100;

export const calculateGrossSalary = (salary: SalaryStructure) =>
  round2(salary.basicSalary + salary.housingAllowance + salary.transportAllowance + salary.otherAllowances);

export const calculateNetSalary = (entry: PayrollEntry) =>
  round2(
    calculateGrossSalary(entry.salary) +
      entry.overtimeAmount +
      entry.bonus -
      entry.leaveDeductions -
      entry.otherDeductions,
  );

export const calculateOvertime = (basicSalary: number, regularHours: number, nightHours: number) => {
  const hourlyRate = basicSalary / DAYS_IN_MONTH / UAE.standardDailyHours;
  const regular = hourlyRate * regularHours * UAE.regularOT;
  const night = hourlyRate * nightHours * UAE.nightOT;
  return round2(regular + night);
};

export const calculateLeaveDeduction = (grossSalary: number, unpaidDays: number) =>
  round2((grossSalary / DAYS_IN_MONTH) * unpaidDays);

export const calculateGratuity = (
  basicSalary: number,
  startDate: string,
  separationDate: string,
  separationType: SeparationType,
) => {
  void separationType;
  const start = new Date(startDate);
  const end = new Date(separationDate);
  const days = Math.max(0, Math.floor((end.getTime() - start.getTime()) / (1000 * 60 * 60 * 24)));
  const years = days / 365;
  const firstFive = Math.min(years, 5);
  const afterFive = Math.max(years - 5, 0);
  const gratuityDays = firstFive * UAE.gratuityFirstFiveYearsDays + afterFive * UAE.gratuityAfterFiveYearsDays;
  const gratuity = (basicSalary / DAYS_IN_MONTH) * gratuityDays;
  return round2(Math.min(gratuity, basicSalary * UAE.gratuityCapYears));
};

export const calculateFinalSettlement = (payload: {
  salary: SalaryStructure;
  unpaidLeaveDays: number;
  regularHours: number;
  nightHours: number;
  gratuity: number;
  bonus: number;
  deductions: number;
}) => {
  const gross = calculateGrossSalary(payload.salary);
  const overtime = calculateOvertime(payload.salary.basicSalary, payload.regularHours, payload.nightHours);
  const leaveDeduction = calculateLeaveDeduction(gross, payload.unpaidLeaveDays);
  return round2(gross + overtime + payload.gratuity + payload.bonus - leaveDeduction - payload.deductions);
};

export const payrollConfig = UAE;
