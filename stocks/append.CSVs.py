import os
import pandas as pd


def read_csv_files():
    current_dir = os.getcwd()
    print("Current Dir is" + current_dir)

    csv_files = [file for file in os.listdir(current_dir) if file.endswith(".csv")]

    if not csv_files:
        print("No CSV files found in the current directory.")
        return None

    dfs = []
    for file in csv_files:
        file_path = os.path.join(current_dir, file)
        print("Reading file" + file_path)
        df = pd.read_csv(file_path)
        num_records = len(df)
        print(f"Read {num_records} records from {file}")
        dfs.append(df)

    combined_df = pd.concat(dfs, ignore_index=True)
    total_rec = len(combined_df)
    print(f"Total Combined file has {total_rec} records")

    combined_csv_path = os.path.join(current_dir, "all.stocks.csv")
    combined_df.to_csv(combined_csv_path)
    print(f"Combined data saved as {combined_csv_path}")

    return combined_df


# Example usage
combined_df = read_csv_files()
