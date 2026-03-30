import pandas as pd
import matplotlib.pyplot as plt
import os


def load_prepare():
    df = pd.read_excel("data/test_dataset.xlsx", sheet_name="test_dataset")

    df["timestamp_dt"] = pd.to_datetime(df["timestamp"], unit="ms")
    df["powerconsumer1_kw"] = df["powerconsumer1_energy_mwh"] * 12 * 1000

    df = df[df["unit"] == "ship1"].copy()

    return df


def scatter_by_phase(df):
    plt.figure(figsize=(8,6))

    for phase, group in df.groupby("phase"):
        plt.scatter(
            group["propulsion_power_mw"],
            group["powerconsumer1_kw"],
            alpha=0.3,
            label=phase
        )

    plt.xlabel("Propulsion Power (MW)")
    plt.ylabel("Powerconsumer1 (kW)")
    plt.title("Ship1: Powerconsumer vs Propulsion (by phase)")
    plt.legend()

    os.makedirs("presentation", exist_ok=True)
    plt.savefig("presentation/task3_phase_relation.png", bbox_inches="tight")

    print("Saved to presentation/task3_phase_relation.png")


if __name__ == "__main__":
    df = load_prepare()
    scatter_by_phase(df)
