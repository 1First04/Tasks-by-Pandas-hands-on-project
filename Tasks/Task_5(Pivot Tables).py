# Task 5: Pivot Tables

# 1. Sales by Category and Region
# This creates a cross-tabulation showing how categories perform across different areas.
pivot_cat_region = df.pivot_table(index='Category', 
                                  columns='Region', 
                                  values='Sales', 
                                  aggfunc='sum')

print("--- Sales by Category and Region ---")
print(pivot_cat_region)
print("\n")

# 2. Sales trends by Segment over time
# We use the 'Order Year' we created in Task 3 to see how different customer groups evolve.
pivot_segment_trends = df.pivot_table(index='Order Year', 
                                      columns='Segment', 
                                      values='Sales', 
                                      aggfunc='sum')

print("--- Annual Sales Trends by Segment ---")
print(pivot_segment_trends)
print("\n")

# 3. Profit by Sub-Category
# Even for single-index summaries, pivot_table is useful for its clean syntax.
pivot_profit_subcat = df.pivot_table(index='Sub-Category', 
                                     values='Profit', 
                                     aggfunc='sum').sort_values(by='Profit', ascending=False)

print("--- Total Profit by Sub-Category ---")
print(pivot_profit_subcat)
