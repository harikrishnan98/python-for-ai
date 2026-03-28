import pandas as pd
import json
import os
from helpers import calculate_total as calTot, format_currency as curr_f

# Read the csv file
df = pd.read_csv('data/sales.csv')
print("CSV Data")
print(df)
print(f"\nShape: {df.shape[0]} Rows and {df.shape[1]} Columns")

# Calculate total for each row

df["total"] = df['price'] * df['quantity']
print("\n With total")
print(df)

# Using iterrow fn:
totals =[]
for index,row in df.iterrows():
    total = calTot(row['quantity'] , row['price'])
    totals.append(total)

# Add total_2 in df
df["total_2"] = totals
curr_f(row['price'])

# Display with formatted data 
print('Sales Data:')
for index,row in df.iterrows():
    formated_tot = curr_f(row['total'])
    print(f"{row['product']}: {curr_f(row['price'])}")

# Show Grand total
grand_total = df['total'].sum()
formatted_grand_total = curr_f(grand_total)
print(f"\n Grand Total: {formatted_grand_total}")

# Create output directory
os.makedirs('output', exist_ok=True)

#Output the file in different formats

#1. JSON format (good for web API's)
df.to_json('output/sales_analyzer.json', orient='records')

#2. Excel format (good for sharing)
df.to_excel('output/sales_analyzer.xlsx', index=False)

#3. Updated CSV Format with our total price value

df.to_csv('output/sales_analyzer.csv', index=False)

# Reading files
read_csv_ff = pd.read_csv('output/sales_analyzer.csv')
