import pandas as pd


def load_data():
    df = pd.read_excel("data/test_dataset.xlsx", sheet_name="test_dataset")
    df["timestamp_dt"] = pd.to_datetime(df["timestamp"], unit="ms")

    df["powerconsumer1_kw"] = df["powerconsumer1_energy_mwh"] * 12 * 1000
    df["DG1_power_kw"] = df["DG1_energy_produced_mwh"] * 12 * 1000

    return df


def check_missing(df):
    print("\n=== MISSING VALUES ===")
    print(df.isna().sum())


def check_zero_generator(df):
    print("\n=== ZERO GENERATOR COUNT ===")
    print((df["DG1_power_kw"] == 0).sum())


def check_negative_values(df):
    print("\n=== NEGATIVE VALUES ===")
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        count = (df[col] < 0).sum()
        if count > 0:
            print(col, count)


def check_speed_anomalies(df):
    print("\n=== SPEED > 45 knots (unlikely) ===")
    print((df["speed_kn"] > 45).sum())


def check_timestamp_gaps(df):
    df = df.sort_values("timestamp_dt")
    df["gap"] = df["timestamp_dt"].diff().dt.total_seconds() / 60

    print("\n=== GAP DISTRIBUTION (minutes) ===")
    print(df["gap"].value_counts().head())


if __name__ == "__main__":
    df = load_data()

    check_missing(df)
    check_zero_generator(df)
    check_negative_values(df)
    check_speed_anomalies(df)
    check_timestamp_gaps(df)
