# 1. Identify missing values
 # Check missing values
missing = df.isnull().sum()
missing_prct = (missing / len(df) * 100).round(2) # missing values in percentage
missing_df = pd.DataFrame({'Missing Count': missing, 'Percentage(%)': missing_prct})
missing_df = missing_df[missing_df['Missing Count'] > 0].sort_values('Percentage(%)', ascending=False) 
print("Columns with Missing Values:")
print(missing_df)

# 2. Handle missing data appropriately
# Note: The standard Superstore dataset is usually complete. 
# However, if you had missing values, you might use:
# df['Column'] = df['Column'].fillna(df['Column'].mean()) # For numerical
# df.dropna(subset=['Critical Column'], inplace=True)     # To remove rows

# 3. Convert relevant columns to correct data types
# Dates are often loaded as 'object' (strings). We need them as datetime objects.

date_columns = ['Order Date', 'Ship Date']

for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce')

# Pro-tip: 'Postal Code' is often treated as a number, but it's actually a category. 
# Let's convert it to a string to avoid weird math issues.

df['Postal Code'] = df['Postal Code'].astype(str)

print("--- Updated Data Types ---")
print(df[['Order Date', 'Ship Date', 'Postal Code']].dtypes)

# 4. Verify the changes
print("\nFirst 5 rows of cleaned date columns:")
print(df[['Order Date', 'Ship Date']].head())
