# MSC Ship Energy Analysis ⚓

This project analyzes auxiliary energy consumption from cruise ship telemetry data and derives operational insights relevant to fuel efficiency, generator optimization, and vessel energy management.

---

# Project Objective
The goal of this project is to:

- Analyze auxiliary power consumer behaviour
- Compare vessels operationally
- Evaluate relation with propulsion demand
- Assess generator contribution
- Identify data quality considerations
- Provide engineering insights for cruise ship energy optimization

---

# Dataset Description
The dataset resembles a ship telemetry extract with:

- 5-minute aggregated measurements
- Two vessels (`ship1`, `ship2`)
- Auxiliary consumer energy
- Generator energy production (DG1)
- Propulsion power
- Vessel speed
- Operational phase
- Stabilizer fins status

---

# Project Structure
---

# Analysis Tasks

## Task 1 — Time-of-day behaviour
- Converted 5-minute energy to kW
- Analyzed hourly average consumption
- Compared ships

Insight:
Auxiliary load varies by hour and differs between vessels.

---

## Task 2 — Ship comparison
- Ship2 shows higher baseline auxiliary demand
- Suggests different vessel configuration

---

## Task 3 — Propulsion relationship
Correlation between propulsion and auxiliary load:

Weak negative correlation (~ -0.20)

Insight:
Auxiliary load is largely independent from propulsion.

---

## Task 4 — Generator share
Consumer relative to generator output:

- SEA ≈ 9%
- MAN ≈ 16%
- ANCHOR ≈ 22%
- PORT ≈ 54%

Insight:
Auxiliary loads dominate in low propulsion conditions.

---

## Task 5 — Data quality
Findings:

- No missing values
- Consistent 5-minute sampling
- DG1 inactive in many rows (multiple generators likely)
- One telemetry gap (~8 hours)

---

# Engineering Interpretation

The auxiliary consumer likely represents:

- HVAC subsystem
- Stabilizer fins
- Hotel electrical loads

These loads are:

- relatively constant
- independent from propulsion
- dominant in port operations

---

# Business Value

This analysis can support:

- Fuel consumption optimization
- Generator dispatch improvement
- Auxiliary load monitoring
- Port energy efficiency improvements
- Decarbonization initiatives

---

# Future Work

- Full generator modelling
- Fuel consumption estimation
- Machine learning forecasting
- Power BI dashboard
- Fleet-wide comparison
- GCC operational scenario modelling

---

# Technologies Used

- Python
- Pandas
- Matplotlib
- WSL (Ubuntu)
- Git / GitHub

---

# Author

Energy Analytics Case Study  
Prepared for Cruise Ship Energy Optimization Interviews

