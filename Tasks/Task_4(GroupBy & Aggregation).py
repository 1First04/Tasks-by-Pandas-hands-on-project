# Task 4: GroupBy & Aggregation

# 1. Calculate total sales by category
sales_by_category = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print("--- Total Sales by Category ---")
print(sales_by_category)
print("\n")

# 2. Calculate total profit by region
profit_by_region = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
print("--- Total Profit by Region ---")
print(profit_by_region)
print("\n")

# 3. Identify top 5 customers based on sales
top_5_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(5)
print("--- Top 5 Customers by Sales ---")
print(top_5_customers)
print("\n")

# 4. Analyze sales trends over time (monthly)
# We group by both Year and Month to see the progression
monthly_trends = df.groupby(['Order Year', 'Order Month'])['Sales'].sum().reset_index()

print("--- Monthly Sales Trends (First 10 Months of Data) ---")
print(monthly_trends.head(10))
