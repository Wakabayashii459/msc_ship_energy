import pandas as pd


def load_and_prepare():
    df = pd.read_excel("data/test_dataset.xlsx", sheet_name="test_dataset")

    # timestamp conversion
    df["timestamp_dt"] = pd.to_datetime(df["timestamp"], unit="ms")

    # power conversion
    df["powerconsumer1_kw"] = df["powerconsumer1_energy_mwh"] * 12 * 1000
    df["DG1_power_kw"] = df["DG1_energy_produced_mwh"] * 12 * 1000

    # time features
    df["hour"] = df["timestamp_dt"].dt.hour
    df["minute"] = df["timestamp_dt"].dt.minute
    df["time_of_day"] = df["hour"] + df["minute"]/60

    return df


def task1_overview(df):
    print("\n=== SHIPS ===")
    print(df["unit"].unique())

    print("\n=== HOUR DISTRIBUTION ===")
    print(df["hour"].value_counts().sort_index())

    print("\n=== SAMPLE ===")
    print(df[[
        "timestamp_dt",
        "unit",
        "hour",
        "powerconsumer1_kw"
    ]].head(10))


if __name__ == "__main__":
    df = load_and_prepare()
    task1_overview(df)
