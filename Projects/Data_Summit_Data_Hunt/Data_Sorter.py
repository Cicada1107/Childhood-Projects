import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the Excel file into a pandas DataFrame
excel_file = 'dataset.xlsx'
df = pd.read_excel(excel_file)

# Step 2: Basic data exploration
# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Display basic statistics about the numerical columns
print("\nSummary statistics:")
print(df.describe())

# Step 3: Data Cleaning (if necessary)
# Check for missing values and handle them if needed
print("\nMissing values:")
print(df.isnull().sum())

# Step 4: Data Analysis
# Perform various analyses on your data here
# Example: Calculate and plot the mean of a numerical column
column_to_analyze = 'YourColumn'
mean_value = df[column_to_analyze].mean()
print(f"\nMean of '{column_to_analyze}': {mean_value}")

# Step 5: Data Visualization (optional)
# Create plots or visualizations to better understand the data
# Example: Create a histogram of a numerical column
plt.hist(df[column_to_analyze], bins=20)
plt.title(f'Histogram of {column_to_analyze}')
plt.xlabel(column_to_analyze)
plt.ylabel('Frequency')
plt.show()

# Step 6: Save the analyzed data or visualization (if needed)
# df.to_excel('analyzed_data.xlsx', index=False)  # To save the DataFrame back to an Excel file

# Step 7: Additional analyses and visualizations as needed
