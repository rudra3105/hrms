import { EmployeeUAEProfile } from '@/types/hrms';

export const isProbationActive = (probationEndDate: string, asOf: string) =>
  new Date(asOf).getTime() <= new Date(probationEndDate).getTime();

export const getNoticePeriodEndDate = (noticeStartDate: string, noticePeriodDays: number) => {
  const dt = new Date(noticeStartDate);
  dt.setDate(dt.getDate() + noticePeriodDays);
  return dt.toISOString().slice(0, 10);
};

export const getDocumentExpiryAlerts = (
  employee: EmployeeUAEProfile,
  asOf: string,
  alertWindowDays = 60,
) => {
  const asOfDate = new Date(asOf);
  const boundary = new Date(asOfDate);
  boundary.setDate(boundary.getDate() + alertWindowDays);

  const isExpiring = (date: string) => new Date(date).getTime() <= boundary.getTime();

  return {
    visaExpiring: isExpiring(employee.visaExpiry),
    emiratesIdExpiring: isExpiring(employee.emiratesIdExpiry),
    passportExpiring: isExpiring(employee.passportExpiry),
  };
};
