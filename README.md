## Project Overview
This project delivers an end-to-end workforce analytics solution focused on employee attrition and experience drivers. Using Python and Power BI, I built a reproducible data pipeline and self-service BI dashboard to support HR decision-making and workforce insights.

## Business Questions
- What is the overall employee attrition rate?
- Which departments and job roles experience the highest attrition?
- How does attrition vary by tenure, overtime status, and satisfaction indicators?
- Which workforce segments may require targeted retention strategies?

## Data Pipeline & Architecture
- Raw HR data ingested and cleaned using Python
- Employee-level clean table created for self-service exploration
- Curated attrition metrics table built to support consistent KPIs and fast BI performance
- Data exported as processed CSVs and visualized in Power BI

This structure mirrors common BI and analytics engineering practices used in enterprise HR analytics teams.

## Power BI Dashboard
The Power BI dashboard enables self-service workforce analytics through interactive filters and standardized metrics.

A static PDF version of the Power BI dashboard is available here:
[📄 View Attrition Dashboard (PDF)](dashboards/screenshots/attrition_report.pdf)

A static PDF version of the Power BI dashboard w/Research Scientist Slicer in use here:
[📄 View Attrition Dashboard (PDF)](dashboards/screenshots/research_scientist_slicer.png)

Features include:
- Executive KPIs (headcount, attrition, attrition rate, average income)
- Attrition analysis by department, job role, and tenure
- Attrition drivers including overtime, job satisfaction, and work-life balance

## Key Insights
- Attrition is highest among employees with less than two years of tenure, indicating early retention as a key risk area.
- Employees working overtime show significantly higher attrition rates compared to non-overtime employees.
- Certain job roles consistently exhibit above-average attrition, suggesting role-specific workload or compensation pressures. (Sales Representatives, Laboratory Technicians)

## Data Quality & Governance
Basic data quality checks were applied, including standardized categorical values and controlled KPI definitions to ensure metric consistency across reports.


