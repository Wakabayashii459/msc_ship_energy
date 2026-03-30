import pandas as pd
import numpy as np
import json
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor, IsolationForest
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

from feature_engineering import load_data, engineer_features


def main():
    df = engineer_features(load_data())

    model_df = df.dropna(subset=["powerconsumer1_kw"]).copy()

    features = [
        "unit",
        "phase",
        "speed_kn",
        "propulsion_power_mw",
        "fins_status",
        "hour",
        "day_of_week",
        "is_weekend",
        "hour_sin",
        "hour_cos",
        "DG1_power_kw",
        "dg1_on",
        "pc1_kw_lag1",
        "pc1_kw_lag2",
        "pc1_kw_roll3",
    ]

    target = "powerconsumer1_kw"

    X = model_df[features]
    y = model_df[target]

    numeric_features = [
        "speed_kn",
        "propulsion_power_mw",
        "fins_status",
        "hour",
        "day_of_week",
        "is_weekend",
        "hour_sin",
        "hour_cos",
        "DG1_power_kw",
        "dg1_on",
        "pc1_kw_lag1",
        "pc1_kw_lag2",
        "pc1_kw_roll3",
    ]

    categorical_features = ["unit", "phase"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", Pipeline([
                ("imputer", SimpleImputer(strategy="median"))
            ]), numeric_features),
            ("cat", Pipeline([
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehot", OneHotEncoder(handle_unknown="ignore"))
            ]), categorical_features),
        ]
    )

    model = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(
            n_estimators=200,
            max_depth=8,
            random_state=42,
            n_jobs=-1
        ))
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    metrics = {
        "mae_kw": float(mae),
        "r2": float(r2),
        "n_train": int(len(X_train)),
        "n_test": int(len(X_test)),
    }

    with open("outputs/models/ml_baseline_metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    pred_df = X_test.copy()
    pred_df["actual_powerconsumer1_kw"] = y_test.values
    pred_df["predicted_powerconsumer1_kw"] = preds
    pred_df["abs_error_kw"] = np.abs(
        pred_df["actual_powerconsumer1_kw"] - pred_df["predicted_powerconsumer1_kw"]
    )
    pred_df.to_csv("outputs/models/ml_predictions_sample.csv", index=False)

    # anomaly model
    anomaly_input = model_df[[
        "powerconsumer1_kw", "DG1_power_kw", "propulsion_power_mw", "speed_kn", "hour"
    ]].copy()

    iso = IsolationForest(
        n_estimators=200,
        contamination=0.02,
        random_state=42
    )
    anomaly_labels = iso.fit_predict(anomaly_input)

    anomaly_df = model_df[[
        "timestamp_dt", "unit", "phase", "speed_kn",
        "propulsion_power_mw", "powerconsumer1_kw", "DG1_power_kw"
    ]].copy()
    anomaly_df["anomaly_flag"] = (anomaly_labels == -1).astype(int)
    anomaly_df.to_csv("outputs/models/anomaly_flags.csv", index=False)

    print("ML baseline completed.")
    print(f"MAE (kW): {mae:.2f}")
    print(f"R^2: {r2:.4f}")
    print("Saved:")
    print("- outputs/models/ml_baseline_metrics.json")
    print("- outputs/models/ml_predictions_sample.csv")
    print("- outputs/models/anomaly_flags.csv")


if __name__ == "__main__":
    main()
