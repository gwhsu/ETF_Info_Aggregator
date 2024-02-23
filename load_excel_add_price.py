import pandas as pd
import yfinance as yf
from datetime import datetime
# Read the Excel file
origin_file = input("Input load file name :")
load_file = str(origin_file) + ".xlsx"
df = pd.read_excel(load_file)

df = df.rename(columns={'Unnamed: 0': 'code', 'Unnamed: 1': 'name'})
print(df.columns)
# Define a function to add '00' prefix to two-digit or three-digit numbers
def add_zeros(num):
    if isinstance(num, int):
        num_str = str(num)
        if len(num_str) == 2 or 3:
            return '00' + num_str

    return num

# Apply the function to the first column
df.iloc[:, 0] = df.iloc[:, 0].apply(add_zeros)
# print(df)


# Function to fetch today's closing price for a given symbol
def get_today_closing_price(symbol):
    tmp = symbol
    try:
        symbol = tmp + ".TW"
        stock = yf.Ticker(symbol)
        today_data = stock.history(period='1d')
        if today_data.empty:
            print("No data available for symbol,Fetch TWO", symbol)
            symbol = tmp + ".TWO"
            stock = yf.Ticker(symbol)
            today_data = stock.history(period='1d')

        return today_data['Close'].values[0]
    except Exception as e:
        print("Error fetching data for symbol:", symbol)
        print(e)  # Print the exception message for debugging
        return None

# Add today's closing price as a new column
df.insert(2, 'Price', df['code'].apply(get_today_closing_price))

print(df)
# 将 DataFrame 存储到新的 Excel 文件中
output_file_name = str(origin_file) + "_all.xlsx"
df.to_excel(output_file_name, index=False)