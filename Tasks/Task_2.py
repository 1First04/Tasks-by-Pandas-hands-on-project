# 1. Identify missing values
print("--- Missing Values Per Column ---")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0]) 
# If it prints an empty series, congrats! Your dataset is clean.
print("\n")

