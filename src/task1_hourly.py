import pandas as pd


def load_and_prepare():
    df = pd.read_excel("data/test_dataset.xlsx", sheet_name="test_dataset")

    df["timestamp_dt"] = pd.to_datetime(df["timestamp"], unit="ms")

    df["powerconsumer1_kw"] = df["powerconsumer1_energy_mwh"] * 12 * 1000

    df["hour"] = df["timestamp_dt"].dt.hour

    return df


def hourly_average(df):
    result = (
        df.groupby(["unit", "hour"])["powerconsumer1_kw"]
        .mean()
        .reset_index()
        .sort_values(["unit", "hour"])
    )

    print("\n=== HOURLY AVERAGE ===")
    print(result)

    print("\n=== PIVOT TABLE ===")
    pivot = result.pivot(index="hour", columns="unit", values="powerconsumer1_kw")
    print(pivot)


if __name__ == "__main__":
    df = load_and_prepare()
    hourly_average(df)
