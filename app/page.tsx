import { payrollConfig } from '@/lib/payroll/engine';

const cards = [
  'WPS payroll status',
  'Gratuity automation',
  'Visa expiry alerts',
  'Passport expiry alerts',
  'Attendance analytics',
  'Leave analytics',
  'Salary analytics',
  'Multi-company branches',
];

export default function HomePage() {
  return (
    <main style={{ fontFamily: 'Inter, sans-serif', margin: '0 auto', maxWidth: 980, padding: 32 }}>
      <h1>UAE HRMS & Payroll (Next.js)</h1>
      <p>
        Enterprise UAE payroll foundation with no-income-tax payroll assumptions, WPS-friendly structure, AED
        calculations, and labour-law aligned gratuity/overtime formulas.
      </p>
      <p>
        <b>Currency:</b> {payrollConfig.currency} | <b>Timezone:</b> Asia/Dubai | <b>Cycle:</b> Monthly
      </p>
      <section style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(200px,1fr))', gap: 12 }}>
        {cards.map((card) => (
          <article key={card} style={{ border: '1px solid #ddd', borderRadius: 8, padding: 14 }}>
            {card}
          </article>
        ))}
      </section>
    </main>
  );
}
