# 1. Split the dataset into two meaningful DataFrames
# We'll split by columns: one for "Order Metadata" and one for "Financial Metrics"
# We keep 'Row ID' in both as the "Primary Key" to link them later.

order_metadata = df[['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Customer Name', 'Segment', 'Region']].copy()
financial_metrics = df[['Row ID', 'Sales', 'Quantity', 'Discount', 'Profit']].copy()

print(f"Metadata Shape: {order_metadata.shape}")
print(f"Financials Shape: {financial_metrics.shape}")
print("\n--- Metadata Sample ---")
print(order_metadata.head(2))
print("\n--- Financials Sample ---")
print(financial_metrics.head(2))
print("\n")

# 2. Merge them back into a single dataset
# We use an 'inner' join on 'Row ID'
merged_df = pd.merge(order_metadata, financial_metrics, on='Row ID', how='inner')

# 3. Ensure the merged result is correct
print("--- Verification ---")

# Check 1: Do the shapes match the original?
if merged_df.shape[0] == df.shape[0]:
    print(f"Success: Row count matches original ({merged_df.shape[0]})")
else:
    print("Warning: Row count mismatch!")

# Check 2: Are there any nulls created by the merge (common if keys don't match)?
if merged_df.isnull().sum().sum() == 0:
    print("Success: No missing values introduced by the merge.")
else:
    print("Warning: Null values detected after merge.")

# Check 3: Check a specific value to ensure data integrity
original_val = df.loc[0, 'Sales']
merged_val = merged_df.loc[0, 'Sales']
if original_val == merged_val:
    print(f"Success: Data integrity verified for 'Sales' (Value: {merged_val})")
