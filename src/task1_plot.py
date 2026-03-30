import pandas as pd
import matplotlib.pyplot as plt
import os


def load_prepare():
    df = pd.read_excel("data/test_dataset.xlsx", sheet_name="test_dataset")
    df["timestamp_dt"] = pd.to_datetime(df["timestamp"], unit="ms")
    df["powerconsumer1_kw"] = df["powerconsumer1_energy_mwh"] * 12 * 1000
    df["hour"] = df["timestamp_dt"].dt.hour
    return df


def plot_hourly(df):
    hourly = (
        df.groupby(["unit", "hour"])["powerconsumer1_kw"]
        .mean()
        .reset_index()
    )

    pivot = hourly.pivot(index="hour", columns="unit", values="powerconsumer1_kw")

    plt.figure(figsize=(10,5))
    pivot.plot(marker="o")

    plt.title("Powerconsumer1 vs Time of Day")
    plt.xlabel("Hour of Day")
    plt.ylabel("Powerconsumer1 (kW)")
    plt.grid(True)

    os.makedirs("presentation", exist_ok=True)
    plt.savefig("presentation/task1_time_of_day.png", bbox_inches="tight")
    print("Saved to presentation/task1_time_of_day.png")


if __name__ == "__main__":
    df = load_prepare()
    plot_hourly(df)
