import pandas as pd

# Task 1: Load the dataset into a Pandas DataFrame
# Note: This specific dataset often requires 'windows-1252' or 'latin1' encoding 
# because of special characters in the text.
try:
    file_path = 'Sample - Superstore.csv'
    df = pd.read_csv(r"C:\Users\hp\Desktop\Data Science\CSEASTU Bootcamp\Sample - Superstore.csv", encoding='windows-1252')
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: The file was not found. Please check the file path.")

# 1. Display the first few rows
print("--- First 5 Rows ---")
print(df.head())
print("\n")

# 2. Check data types and dataset structure
print("--- Dataset Structure and Information ---")
# .info() provides the count of non-null values, column names, and data types
print(df.info())
print("\n")

# 3. Generate summary statistics
print("--- Summary Statistics (Numerical Columns) ---")
# .describe() provides mean, standard deviation, min, max, and quartiles
print(df.describe())

# Optional: Generate summary statistics for categorical columns
print("\n--- Summary Statistics (Categorical Columns) ---")
print(df.describe(include='object'))
