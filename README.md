# MSC Ship Energy Analysis

This project analyses auxiliary electrical consumption from cruise ship telemetry data.  
The goal is to understand how an onboard auxiliary consumer behaves operationally and how it relates to propulsion demand, generator output, and vessel operating mode.

The work focuses on turning raw 5-minute telemetry into operational insights that could support energy optimisation, generator scheduling, and monitoring.

---

## Dataset

The dataset resembles an extract from a ship energy monitoring system and contains:

- 5-minute aggregated measurements
- two vessels (ship1, ship2)
- auxiliary consumer energy
- generator output (DG1)
- propulsion power
- vessel speed
- operational phase (SEA, MAN, PORT, ANCHOR)
- stabilizer fins status

Energy values are converted to average power to enable comparisons across operating conditions.

---

## Project Structure
msc_ship_energy/│
├── data/ raw dataset
├── src/ analysis and modelling scripts
├── outputs/ generated tables and model outputs
├── presentation/ charts used for reporting
├── dashboards/ placeholder for BI dashboards
├── notebooks/ exploratory analysis
---

## Analysis Overview

The analysis follows four main steps:

1. Descriptive analysis of auxiliary load behaviour  
2. Comparison between vessels  
3. Relationship with propulsion demand  
4. Generator contribution and load share  
5. Data quality review  
6. Predictive modelling extension  

---

## Key Observations

### Auxiliary load behaviour
The auxiliary consumer shows relatively stable behaviour across operating conditions, with moderate variation by time of day.

### Ship comparison
Ship2 operates with a slightly higher baseline auxiliary demand, suggesting differences in onboard systems or operational profile.

### Relation with propulsion
The correlation between propulsion power and auxiliary load is weak.  
This indicates the consumer is not propulsion-driven and is more likely part of the hotel or auxiliary electrical domain.

### Generator share
The consumer represents a small portion of generator output during sea operations but becomes relatively more significant in low propulsion conditions such as port and anchoring.

### Data quality
The telemetry is complete with consistent 5-minute intervals.  
DG1 is inactive in part of the dataset, indicating additional generators or shore power may be supplying the vessel.

---

## Feature Engineering

A feature dataset is created including:

- time-of-day indicators
- lagged auxiliary load values
- rolling averages
- generator availability flags
- consumer share relative to generator output
- operational phase indicators

This dataset supports both analysis and modelling.

---

## Machine Learning Extension

A baseline Random Forest regression model is trained to predict auxiliary load using:

- vessel identity
- operational phase
- vessel speed
- propulsion power
- generator output
- time-of-day features
- lagged load values

Model performance:

- Mean Absolute Error ≈ 2.7 kW  
- R² ≈ 0.99  

The model performs well due to the smooth nature of 5-minute telemetry and the inclusion of lag features.  
This should be interpreted as a short-horizon forecasting model rather than a purely causal explanation.

Potential applications include:

- auxiliary load forecasting
- generator scheduling support
- anomaly detection
- operational monitoring

---

## Outputs

The project generates:

- cleaned feature dataset
- Power BI export tables
- model predictions
- anomaly flags
- feature importance metrics
- summary tables for reporting

These outputs are stored under the `outputs/` directory.

---

## Possible Extensions

This analysis can be extended by:

- incorporating full generator modelling
- estimating fuel consumption
- integrating route or climate information
- building interactive dashboards
- expanding to fleet-wide comparison

---

## Tools Used

- Python
- Pandas
- Scikit-learn
- Matplotlib
- WSL (Ubuntu)
- Git / GitHub

---

## Notes

This project is designed as a realistic energy analytics case study based on cruise ship telemetry.  
The emphasis is on operational interpretation rather than purely statistical modelling.

