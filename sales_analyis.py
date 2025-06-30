import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv('sales_data.csv')

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Total sales by product
product_sales = df.groupby('Product')['Sales'].sum()
print("\n📊 Total Sales by Product:\n", product_sales)

# Total sales by region
region_sales = df.groupby('Region')['Sales'].sum()
print("\n🌍 Total Sales by Region:\n", region_sales)

# Daily sales trend
daily_sales = df.groupby('Date')['Sales'].sum()
print("\n📅 Daily Sales Trend:\n", daily_sales)

# Plot: Sales by Product
product_sales.plot(kind='bar', title='Total Sales by Product', color='skyblue')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig('product_sales.png')  # Save image
plt.show()

# Plot: Sales by Region
region_sales.plot(kind='pie', title='Sales by Region', autopct='%1.1f%%')
plt.ylabel('')
plt.tight_layout()
plt.savefig('region_sales.png')  # Save image
plt.show()

# Plot: Daily Sales
daily_sales.plot(kind='line', marker='o', title='Daily Sales Trend', color='green')
plt.ylabel('Total Sales')
plt.xlabel('Date')
plt.grid(True)
plt.tight_layout()
plt.savefig('daily_sales.png')  # Save image
plt.show()
