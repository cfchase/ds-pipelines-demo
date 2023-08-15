import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv("all.stocks.csv")

# Convert 'Date' column to datetime type
df["Date"] = pd.to_datetime(df["Date"])

# Group the DataFrame by Stock Symbol
grouped = df.groupby("Stock Symbol")

# Plot the Close value over Date for each Stock Symbol
for symbol, data in grouped:
    plt.plot(data["Date"], data["Close"], label=symbol)

# Customize the plot
plt.title("Stock Prices")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.grid(True)
plt.legend()

# Rotate the x-axis tick labels for better readability
plt.xticks(rotation=45)

# Save the plot as a PNG file
plt.savefig("stock_prices.png")

# Display the plot
plt.show()
