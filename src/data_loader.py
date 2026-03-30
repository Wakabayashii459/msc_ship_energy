import pandas as pd


def load_data(path: str):
    """
    Load Excel file with two sheets:
    - test_dataset (data)
    - first sheet (instructions)
    """
    df_data = pd.read_excel(path, sheet_name="test_dataset")
    df_info = pd.read_excel(path, sheet_name=0)

    return df_data, df_info


if __name__ == "__main__":
    data, info = load_data("data/test_dataset.xlsx")

    print("\n=== DATA HEAD ===")
    print(data.head())

    print("\n=== COLUMNS ===")
    print(data.columns)

    print("\n=== INFO SHEET ===")
    print(info.head())
