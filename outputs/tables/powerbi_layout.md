# Power BI Dashboard Layout

## Page 1 - Executive Overview
Purpose:
- Give a quick comparison of ship1 vs ship2
- Show overall consumer and generator behaviour

Visuals:
- KPI cards:
  - Average powerconsumer1_kw
  - Average DG1_power_kw
  - Average propulsion_power_mw
  - DG1 availability %
- Line chart:
  - Hourly average powerconsumer1_kw by ship
- Bar chart:
  - Average consumer share of DG1 by ship
- Table:
  - Ship summary

Filters:
- Ship
- Phase
- Date

---

## Page 2 - Operational Behaviour
Purpose:
- Understand how auxiliary load behaves operationally

Visuals:
- Scatter plot:
  - propulsion_power_mw vs powerconsumer1_kw
  - colored by phase
- Boxplot / column chart:
  - powerconsumer1_kw by phase
- Line chart:
  - speed_kn vs powerconsumer1_kw over time
- Matrix:
  - phase x ship summary

Filters:
- Ship
- Phase
- DG1 on/off

---

## Page 3 - Generator & Load Balance
Purpose:
- Assess consumer significance relative to DG1 output

Visuals:
- Bar chart:
  - average consumer_share_dg1 by phase
- Histogram:
  - consumer_share_dg1 distribution
- Donut / stacked bar:
  - DG1 on vs off counts
- Table:
  - phase summary

Filters:
- Ship
- Phase
- DG1 on/off

---

## Page 4 - Machine Learning / Monitoring
Purpose:
- Show predictive extension and anomaly-monitoring capability

Visuals:
- Line chart:
  - actual vs predicted powerconsumer1_kw
- Bar chart:
  - top feature importances
- KPI cards:
  - MAE
  - R^2
  - anomaly count
- Table:
  - anomaly rows

Filters:
- Ship
- Phase
- Time window

