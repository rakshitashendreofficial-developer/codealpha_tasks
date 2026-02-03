# STEP 1: Hardcoded stock prices (dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

# STEP 2: Function to calculate total investment
def calculate_portfolio():
    total_value = 0
    portfolio = {}

    print("📈 Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("Type 'done' when finished.\n")

    while True:
        stock_name = input("Enter stock name: ").upper()

        if stock_name == "DONE":
            break

        if stock_name not in stock_prices:
            print("❌ Stock not found. Try again.")
            continue

        quantity = int(input("Enter quantity: "))

        # Calculate investment value
        investment = stock_prices[stock_name] * quantity
        total_value += investment

        portfolio[stock_name] = quantity

        print(f"Added {quantity} shares of {stock_name}\n")

    return portfolio, total_value


# STEP 3: Save portfolio to a text file (optional)
def save_to_file(portfolio, total_value):
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-----------------------\n")

        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares @ ${price} = ${value}\n")

        file.write(f"\nTotal Investment Value: ${total_value}")


# STEP 4: Main program
def main():
    portfolio, total_value = calculate_portfolio()

    print("\n📊 Portfolio Summary")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares")

    print(f"\n💰 Total Investment Value: ${total_value}")

    save_choice = input("\nSave result to file? (yes/no): ").lower()
    if save_choice == "yes":
        save_to_file(portfolio, total_value)
        print("✅ Portfolio saved to portfolio.txt")


# STEP 5: Run the program
main()
