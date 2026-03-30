import pandas as pd
import matplotlib.pyplot as plt
import os


def load_prepare():
    df = pd.read_excel("data/test_dataset.xlsx", sheet_name="test_dataset")

    df["timestamp_dt"] = pd.to_datetime(df["timestamp"], unit="ms")

    df["powerconsumer1_kw"] = df["powerconsumer1_energy_mwh"] * 12 * 1000

    # only ship1
    df = df[df["unit"] == "ship1"].copy()

    return df


def correlation_analysis(df):
    corr = df["powerconsumer1_kw"].corr(df["propulsion_power_mw"])

    print("\n=== CORRELATION ===")
    print(f"Correlation powerconsumer vs propulsion: {corr:.4f}")


def scatter_plot(df):
    plt.figure(figsize=(8,6))

    plt.scatter(
        df["propulsion_power_mw"],
        df["powerconsumer1_kw"],
        alpha=0.3
    )

    plt.xlabel("Propulsion Power (MW)")
    plt.ylabel("Powerconsumer1 (kW)")
    plt.title("Ship1: Powerconsumer1 vs Propulsion")

    os.makedirs("presentation", exist_ok=True)
    plt.savefig("presentation/task3_propulsion_relation.png", bbox_inches="tight")

    print("Saved to presentation/task3_propulsion_relation.png")


if __name__ == "__main__":
    df = load_prepare()
    correlation_analysis(df)
    scatter_plot(df)
