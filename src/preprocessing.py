import pandas as pd


def load_dataset(path: str) -> pd.DataFrame:
    df = pd.read_excel(path, sheet_name="test_dataset")
    return df


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Convert epoch milliseconds to datetime
    df["timestamp_dt"] = pd.to_datetime(df["timestamp"], unit="ms")

    # Convert 5-minute energy to average power
    df["powerconsumer1_power_mw"] = df["powerconsumer1_energy_mwh"] * 12
    df["powerconsumer1_power_kw"] = df["powerconsumer1_power_mw"] * 1000

    df["DG1_power_mw"] = df["DG1_energy_produced_mwh"] * 12
    df["DG1_power_kw"] = df["DG1_power_mw"] * 1000

    # Time features
    df["date"] = df["timestamp_dt"].dt.date
    df["hour"] = df["timestamp_dt"].dt.hour
    df["minute"] = df["timestamp_dt"].dt.minute

    return df


def print_overview(df: pd.DataFrame) -> None:
    print("\n=== DTYPES ===")
    print(df.dtypes)

    print("\n=== TIME RANGE ===")
    print("start:", df["timestamp_dt"].min())
    print("end:  ", df["timestamp_dt"].max())

    print("\n=== UNITS ===")
    print(df["unit"].value_counts(dropna=False))

    print("\n=== PHASES ===")
    print(df["phase"].value_counts(dropna=False))

    print("\n=== FINS STATUS ===")
    print(df["fins_status"].value_counts(dropna=False))

    print("\n=== ELAPSED TIME ===")
    print(df["elapsed_time_min"].value_counts(dropna=False).sort_index())

    print("\n=== NUMERIC SUMMARY ===")
    cols = [
        "speed_kn",
        "powerconsumer1_energy_mwh",
        "powerconsumer1_power_kw",
        "DG1_energy_produced_mwh",
        "DG1_power_kw",
        "propulsion_power_mw",
    ]
    print(df[cols].describe())

    print("\n=== SAMPLE ROWS ===")
    print(
        df[
            [
                "timestamp",
                "timestamp_dt",
                "unit",
                "phase",
                "speed_kn",
                "powerconsumer1_power_kw",
                "DG1_power_kw",
                "propulsion_power_mw",
                "fins_status",
            ]
        ].head(10)
    )


if __name__ == "__main__":
    df = load_dataset("data/test_dataset.xlsx")
    df = preprocess(df)
    print_overview(df)
