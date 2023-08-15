# I just need one more package and I'm too lazy to create a custom runtime image
import importlib


def import_or_install(package_name):
    try:
        importlib.import_module(package_name)
    except ImportError:
        import pip

        pip.main(["install", package_name])
        importlib.invalidate_caches()


import_or_install("yfinance==0.2.22")


# now this is the function
import yfinance as yf
import pandas as pd


def download_stock_data(stock_symbol):
    # Download stock data
    stock_data = yf.download(stock_symbol, period="5y")

    if stock_data.empty:
        print(f"No data available for {stock_symbol}.")
        return

    # Create a DataFrame from the downloaded data
    stock_df = pd.DataFrame(stock_data)

    # Add a new column for stock name
    stock_df["Stock Symbol"] = stock_symbol

    # Save the DataFrame as a CSV file
    file_name = f"{stock_symbol}_stock_data.csv"
    stock_df.to_csv(file_name)

    # Display the number of records
    num_records = len(stock_df)
    print(f"Stock data saved as {file_name}.")
    print(f"Number of records: {num_records}")


# Example usage
# download_stock_data("TSLA")
