import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

from feature_engineering import load_data, engineer_features


def fit_model():
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

    model.fit(X, y)

    return model, X, y, numeric_features, categorical_features


def save_prediction_chart():
    pred_df = pd.read_csv("outputs/models/ml_predictions_sample.csv")

    sample = pred_df.head(150).copy()

    plt.figure(figsize=(10, 5))
    plt.plot(sample["actual_powerconsumer1_kw"].values, label="Actual")
    plt.plot(sample["predicted_powerconsumer1_kw"].values, label="Predicted")
    plt.title("ML Baseline: Actual vs Predicted Auxiliary Load")
    plt.xlabel("Sample Index")
    plt.ylabel("Powerconsumer1 (kW)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("presentation/ml_actual_vs_predicted.png", bbox_inches="tight")
    print("Saved: presentation/ml_actual_vs_predicted.png")


def save_feature_importance_chart():
    model, X, y, numeric_features, categorical_features = fit_model()

    preprocessor = model.named_steps["preprocessor"]
    regressor = model.named_steps["regressor"]

    cat_ohe = preprocessor.named_transformers_["cat"].named_steps["onehot"]
    cat_names = cat_ohe.get_feature_names_out(categorical_features)

    feature_names = numeric_features + list(cat_names)
    importances = regressor.feature_importances_

    imp_df = pd.DataFrame({
        "feature": feature_names,
        "importance": importances
    }).sort_values("importance", ascending=False).head(12)

    imp_df.to_csv("outputs/tables/feature_importance.csv", index=False)

    plt.figure(figsize=(10, 6))
    plt.barh(imp_df["feature"][::-1], imp_df["importance"][::-1])
    plt.title("Top Feature Importances - ML Baseline")
    plt.xlabel("Importance")
    plt.tight_layout()
    plt.savefig("presentation/ml_feature_importance.png", bbox_inches="tight")

    print("Saved: presentation/ml_feature_importance.png")
    print("Saved: outputs/tables/feature_importance.csv")


def main():
    save_prediction_chart()
    save_feature_importance_chart()


if __name__ == "__main__":
    main()
