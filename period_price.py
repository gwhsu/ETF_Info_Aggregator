import yfinance as yf
from datetime import datetime, timedelta

# Function to calculate price change and percentage change for a given stock symbol and time period
def calculate_price_change(symbol, start_date, end_date):
    # Get historical data for the given symbol and time period
    stock_data = yf.download(symbol, start=start_date, end=end_date)

    # Extract the closing prices for start and end dates
    start_price = stock_data['Close'].iloc[0]
    end_price = stock_data['Close'].iloc[-1]

    # Calculate price change
    price_change = end_price - start_price

    # Calculate percentage change
    percentage_change = (price_change / start_price) * 100

    return price_change, percentage_change

# Example usage
symbol = 'AAPL'  # Apple Inc. stock symbol
end_date = datetime.now().date()  # Current date
start_date_1_month_ago = end_date - timedelta(days=30)  # 1 month ago
start_date_1_year_ago = end_date - timedelta(days=365)  # 1 year ago
start_date_5_years_ago = end_date - timedelta(days=5*365)  # 5 years ago

# Calculate price change and percentage change for different time periods
price_change_1_month, percentage_change_1_month = calculate_price_change(symbol, start_date_1_month_ago, end_date)
price_change_1_year, percentage_change_1_year = calculate_price_change(symbol, start_date_1_year_ago, end_date)
price_change_5_years, percentage_change_5_years = calculate_price_change(symbol, start_date_5_years_ago, end_date)

# Print the results
print(f"Price change in the last 1 month: {price_change_1_month:.2f}, Percentage change: {percentage_change_1_month:.2f}%")
print(f"Price change in the last 1 year: {price_change_1_year:.2f}, Percentage change: {percentage_change_1_year:.2f}%")
print(f"Price change in the last 5 years: {price_change_5_years:.2f}, Percentage change: {percentage_change_5_years:.2f}%")