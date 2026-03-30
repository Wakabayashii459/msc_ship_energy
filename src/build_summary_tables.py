import pandas as pd
import json


def main():
    # task summary table
    task_summary = pd.DataFrame({
        "metric": [
            "Average consumer load (kW)",
            "Average DG1 load (kW)",
            "Average propulsion load (MW)",
            "Ship1 avg consumer share of DG1",
            "Ship2 avg consumer share of DG1",
        ],
        "value": [
            329.69,
            2328.56,
            4.316,
            0.091,
            0.181,
        ]
    })
    task_summary.to_csv("outputs/tables/key_metrics.csv", index=False)

    # ML metrics table if exists
    try:
        with open("outputs/models/ml_baseline_metrics.json", "r") as f:
            metrics = json.load(f)
        ml_table = pd.DataFrame(list(metrics.items()), columns=["metric", "value"])
        ml_table.to_csv("outputs/tables/ml_metrics.csv", index=False)
        print("Saved: outputs/tables/ml_metrics.csv")
    except FileNotFoundError:
        print("ML metrics file not found yet.")

    print("Saved: outputs/tables/key_metrics.csv")


if __name__ == "__main__":
    main()
