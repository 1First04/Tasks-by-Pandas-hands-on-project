import matplotlib.pyplot as plt

# 1. Line chart for sales trend over time
# We group by month to see the trajectory of the business
plt.figure(figsize=(10, 6))
df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum().plot(kind='line', marker='o', color='#2c3e50')
plt.title('Monthly Sales Trend', fontsize=14)
plt.xlabel('Order Month', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('sales_trend.png')

# 2. Bar chart for sales by category
# Sorting the values ensures the highest performing category is prominent
plt.figure(figsize=(8, 6))
df.groupby('Category')['Sales'].sum().sort_values(ascending=False).plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Total Sales by Category', fontsize=14)
plt.ylabel('Sales ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('sales_by_category.png')

# 3. Bar chart for profit by region
plt.figure(figsize=(8, 6))
df.groupby('Region')['Profit'].sum().sort_values(ascending=False).plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Total Profit by Region', fontsize=14)
plt.ylabel('Profit ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('profit_by_region.png')

# 4. Pie chart for segment distribution
# Useful for seeing the proportion of Consumer vs. Corporate sales
plt.figure(figsize=(7, 7))
df['Segment'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99'])
plt.title('Customer Segment Distribution', fontsize=14)
plt.ylabel('') # Remove y-label for aesthetics
plt.tight_layout()
plt.savefig('segment_distribution.png')
