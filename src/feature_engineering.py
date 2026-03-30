import pandas as pd
import numpy as np


def load_data(path: str = "data/test_dataset.xlsx") -> pd.DataFrame:
    df = pd.read_excel(path, sheet_name="test_dataset")
    return df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # timestamps
    df["timestamp_dt"] = pd.to_datetime(df["timestamp"], unit="ms")
    df = df.sort_values(["unit", "timestamp_dt"]).reset_index(drop=True)

    # convert 5-minute energy to average power
    df["powerconsumer1_kw"] = df["powerconsumer1_energy_mwh"] * 12 * 1000
    df["DG1_power_kw"] = df["DG1_energy_produced_mwh"] * 12 * 1000

    # time features
    df["date"] = df["timestamp_dt"].dt.date
    df["hour"] = df["timestamp_dt"].dt.hour
    df["minute"] = df["timestamp_dt"].dt.minute
    df["day_of_week"] = df["timestamp_dt"].dt.dayofweek
    df["is_weekend"] = (df["day_of_week"] >= 5).astype(int)

    # cyclical time encoding
    df["hour_sin"] = np.sin(2 * np.pi * df["hour"] / 24)
    df["hour_cos"] = np.cos(2 * np.pi * df["hour"] / 24)

    # lag features by ship
    df["pc1_kw_lag1"] = df.groupby("unit")["powerconsumer1_kw"].shift(1)
    df["pc1_kw_lag2"] = df.groupby("unit")["powerconsumer1_kw"].shift(2)
    df["pc1_kw_roll3"] = (
        df.groupby("unit")["powerconsumer1_kw"]
        .rolling(3, min_periods=1)
        .mean()
        .reset_index(level=0, drop=True)
    )

    # generator availability flag
    df["dg1_on"] = (df["DG1_power_kw"] > 0).astype(int)

    # cleaner fins flag
    df["fins_status"] = df["fins_status"].astype(int)

    # safe consumer share
    df["consumer_share_dg1"] = np.where(
        df["DG1_power_kw"] > 100,
        df["powerconsumer1_kw"] / df["DG1_power_kw"],
        np.nan,
    )

    return df


def main():
    df = load_data()
    df_feat = engineer_features(df)

    df_feat.to_csv("outputs/feature_dataset.csv", index=False)

    print("Saved: outputs/feature_dataset.csv")
    print("\nColumns:")
    print(df_feat.columns.tolist())

    print("\nHead:")
    print(df_feat.head())


if __name__ == "__main__":
    main()
