## Machine Learning Extension

A baseline Random Forest model was trained to predict `powerconsumer1_kw` using:
- ship identity
- operational phase
- vessel speed
- propulsion power
- generator output
- time-of-day features
- lagged auxiliary-load features

Results:
- MAE ≈ 2.69 kW
- R² ≈ 0.986

Interpretation:
This performs as a strong short-horizon forecasting benchmark for 5-minute ship telemetry. Because lagged target features are included, it should be interpreted as an operational prediction model rather than a purely causal model.
