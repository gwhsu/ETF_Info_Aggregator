import pandas as pd

# Read the Excel file
df = pd.read_excel("2023_all.xlsx")

# Get user input for stock codes, separated by commas
user_input = input("Enter the stock codes you want to select (separated by spaces): ")

# Split user input by spaces and strip whitespace to create a list of selected stock codes
selected_stocks = [stock.strip() for stock in user_input.split()]

# Select rows with specific stock codes
selected_df = df[df['code'].isin(selected_stocks)]

# Save the selected stocks to a new Excel file
selected_df.to_excel("selected_stocks.xlsx", index=False)
