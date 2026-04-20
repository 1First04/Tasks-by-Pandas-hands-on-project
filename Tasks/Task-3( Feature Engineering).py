# Task 3: Feature Engineering

# 1. Extract Month and Year from the Order Date
# We use the .dt accessor which is available for datetime columns
df['Order Month'] = df['Order Date'].dt.month
df['Order Year'] = df['Order Date'].dt.year

# 2. Create a new column: Profit Margin
# This is a classic business metric: How much profit are we making per dollar of sales?
# Formula: Profit / Sales
df['Profit Margin'] = df['Profit'] / df['Sales']

# 3. Create another useful column: Discount Amount
# Sometimes it's useful to see the actual dollar value of the discount applied
df['Discount Value'] = df['Sales'] * df['Discount']

# --- Task 3: Verification ---

print("--- Feature Engineering Verification ---")
# Let's look at the specific columns we just created to ensure they look right
check_cols = ['Order Date', 'Order Month', 'Order Year', 'Sales', 'Profit', 'Profit Margin']
print(df[check_cols].head())

# Logical Check: Ensure Profit Margin doesn't have weird infinity values
# (This could happen if Sales was 0)
print("\nChecking for logical consistency in Profit Margin:")
if df['Profit Margin'].isnull().any() or (df['Profit Margin'] == float('inf')).any():
    print("Warning: Detected nulls or infinite values in Profit Margin.")
else:
    print("Logic Check Passed: Profit Margin looks clean.")

# Statistical check: Does the Month range from 1 to 12?
print(f"\nMonth Range: {df['Order Month'].min()} to {df['Order Month'].max()}")
