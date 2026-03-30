import pandas as pd


def load_prepare():
    df = pd.read_excel("data/test_dataset.xlsx", sheet_name="test_dataset")

    df["timestamp_dt"] = pd.to_datetime(df["timestamp"], unit="ms")

    df["powerconsumer1_kw"] = df["powerconsumer1_energy_mwh"] * 12 * 1000
    df["DG1_power_kw"] = df["DG1_energy_produced_mwh"] * 12 * 1000

    # filter very small generator values
    df = df[df["DG1_power_kw"] > 100].copy()

    df["consumer_share"] = df["powerconsumer1_kw"] / df["DG1_power_kw"]

    return df


def summary(df):
    print("\n=== CLEANED SHARE ===")
    print(df["consumer_share"].describe())

    print("\n=== BY PHASE ===")
    print(df.groupby("phase")["consumer_share"].mean())

    print("\n=== BY SHIP ===")
    print(df.groupby("unit")["consumer_share"].mean())


if __name__ == "__main__":
    df = load_prepare()
    summary(df)
