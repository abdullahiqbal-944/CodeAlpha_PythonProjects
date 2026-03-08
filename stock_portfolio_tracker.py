stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "AMZN": 3300
}

total_value = 0

print("Stock Portfolio Tracker")

for stock in stocks:
    quantity = int(input(f"Enter quantity for {stock}: "))
    value = quantity * stocks[stock]
    total_value += value

print("\nTotal Investment Value:", total_value)

# Optional: save to file
with open("portfolio.txt", "w") as file:
    file.write("Total Investment Value: " + str(total_value))

print("Result saved to portfolio.txt")
