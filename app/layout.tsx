import type { ReactNode } from 'react';

export const metadata = {
  title: 'UAE HRMS',
  description: 'Enterprise-grade UAE HRMS and payroll',
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
