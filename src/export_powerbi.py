import pandas as pd
from feature_engineering import load_data, engineer_features


def main():
    df = load_data()
    df = engineer_features(df)

    # fact table
    fact_cols = [
        "timestamp_dt", "unit", "phase", "speed_kn", "propulsion_power_mw",
        "fins_status", "powerconsumer1_kw", "DG1_power_kw",
        "consumer_share_dg1", "hour", "day_of_week", "is_weekend", "dg1_on"
    ]
    fact = df[fact_cols].copy()
    fact.to_csv("outputs/powerbi/fact_ship_energy.csv", index=False)

    # hourly comparison table
    hourly = (
        df.groupby(["unit", "hour"], as_index=False)["powerconsumer1_kw"]
        .mean()
        .rename(columns={"powerconsumer1_kw": "avg_powerconsumer1_kw"})
    )
    hourly.to_csv("outputs/powerbi/hourly_profile.csv", index=False)

    # phase summary
    phase_summary = (
        df[df["DG1_power_kw"] > 100]
        .groupby(["unit", "phase"], as_index=False)
        .agg(
            avg_powerconsumer1_kw=("powerconsumer1_kw", "mean"),
            avg_dg1_power_kw=("DG1_power_kw", "mean"),
            avg_propulsion_power_mw=("propulsion_power_mw", "mean"),
            avg_consumer_share_dg1=("consumer_share_dg1", "mean"),
            obs_count=("powerconsumer1_kw", "count"),
        )
    )
    phase_summary.to_csv("outputs/powerbi/phase_summary.csv", index=False)

    # ship summary
    ship_summary = (
        df.groupby("unit", as_index=False)
        .agg(
            avg_powerconsumer1_kw=("powerconsumer1_kw", "mean"),
            avg_dg1_power_kw=("DG1_power_kw", "mean"),
            avg_propulsion_power_mw=("propulsion_power_mw", "mean"),
            max_powerconsumer1_kw=("powerconsumer1_kw", "max"),
            min_powerconsumer1_kw=("powerconsumer1_kw", "min"),
            observations=("powerconsumer1_kw", "count"),
        )
    )
    ship_summary.to_csv("outputs/powerbi/ship_summary.csv", index=False)

    print("Saved Power BI exports:")
    print("- outputs/powerbi/fact_ship_energy.csv")
    print("- outputs/powerbi/hourly_profile.csv")
    print("- outputs/powerbi/phase_summary.csv")
    print("- outputs/powerbi/ship_summary.csv")


if __name__ == "__main__":
    main()
