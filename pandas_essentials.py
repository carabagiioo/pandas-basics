"""
pandas_essentials.py

This script provides a comprehensive overview of the essential features
of the pandas library, a cornerstone for data manipulation and analysis in Python.

It covers:
1.  Installation (as a comment)
2.  Creating Series and DataFrames
3.  Reading and Writing Data (commented out to prevent file creation)
4.  Viewing and Inspecting Data
5.  Selection and Indexing
6.  Handling Missing Data
7.  Grouping and Aggregation (groupby)

To run this script:
1. Make sure you have pandas installed: pip install pandas numpy
2. Execute the file: python pandas_essentials.py
"""

import pandas as pd
import numpy as np


def main():
    """Main function to run all pandas examples."""

    # 1. Installation
    # You need to install pandas first. Open your terminal or command prompt and run:
    # pip install pandas

    print("### 2. Creating DataFrames and Series ###\n")

 
    # --- Creating a DataFrame (2D) ---
    # The most common way is from a dictionary of lists.
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank'],
        'Age': [24, 27, 22, 32, 29, 23],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Chicago'],
        'Score': [85.5, 90.2, 88.0, 76.8, 92.1, 81.3]
    }
    df = pd.DataFrame(data) 

    print("--- A pandas DataFrame ---")
    print(df)
    print("-" * 25 + "\n")

    print("### 3. Reading and Writing Data ###\n")
    # A very common task is to load data from a file (like a CSV).
    # The following lines are commented out to prevent creating files automatically.
    # You can uncomment them to test reading and writing.

    # --- Writing to a CSV file ---
    # The `index=False` argument prevents pandas from writing the DataFrame index as a column.
    # df.to_csv('output.csv', index=False)
    # print("DataFrame saved to output.csv")

    # --- Reading from a CSV file ---
    # df_from_csv = pd.read_csv('output.csv')
    # print("\n--- DataFrame read from output.csv ---")
    # print(df_from_csv)

    # Pandas can also read/write many other formats like Excel, JSON, SQL, etc.
    # df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)
    # df_from_excel = pd.read_excel('output.xlsx')
    print("Reading/Writing examples are in the code but commented out.\n")

    print("### 4. Viewing and Inspecting Data ###\n")

    # --- View the first 5 rows ---
    print("--- df.head() ---")
    print(df.head())
    print("-" * 25 + "\n")

    # --- View the last 3 rows ---
    print("--- df.tail(3) ---")
    print(df.tail(3))
    print("-" * 25 + "\n")

    # --- Get a concise summary of the DataFrame ---
    # This is extremely useful for checking data types and missing values.
    print("--- df.info() ---")
    df.info()
    print("-" * 25 + "\n")

    # --- Get descriptive statistics for numerical columns ---
    print("--- df.describe() ---")
    print(df.describe())
    print("-" * 25 + "\n")

    # --- Get the dimensions (rows, columns) ---
    print(f"Shape of the DataFrame: {df.shape}\n")

    print("### 5. Selection and Indexing ###\n")

    # --- Selecting a single column (returns a Series) ---
    print("--- Selecting a single column: df['Age'] ---")
    print(df['Age'])
    print("-" * 25 + "\n")

    # --- Selecting multiple columns (returns a DataFrame) ---
    print("--- Selecting multiple columns: df[['Name', 'City']] ---")
    print(df[['Name', 'City']])
    print("-" * 25 + "\n")

    # --- Selecting rows by label/index: .loc ---
    print("--- Row with index 2 (using .loc[2]) ---")
    print(df.loc[2])
    print("-" * 25 + "\n")

    # --- Selecting rows by integer position: .iloc ---
    print("--- Row at position 3 (using .iloc[3]) ---")
    print(df.iloc[3])
    print("-" * 25 + "\n")

    # --- Slicing rows and selecting columns with .loc ---
    print("--- Slicing with .loc[1:3, ['Name', 'Score']] ---")
    print(df.loc[1:3, ['Name', 'Score']])
    print("-" * 25 + "\n")

    # --- Conditional Selection (Boolean Indexing) ---
    print("--- People older than 25: df[df['Age'] > 25] ---")
    print(df[df['Age'] > 25])
    print("-" * 25 + "\n")

    # --- Combine conditions: People from Chicago AND younger than 25 ---
    print("--- People from Chicago AND younger than 25 ---")
    print(df[(df['City'] == 'Chicago') & (df['Age'] < 25)])
    print("-" * 25 + "\n")

    print("### 6. Handling Missing Data ###\n")

    # Let's create a DataFrame with missing data
    data_missing = {
        'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, np.nan, 8],
        'C': [10, 20, 30, 40]
    }
    df_miss = pd.DataFrame(data_missing)
    print("--- DataFrame with Missing Values ---")
    print(df_miss)
    print("-" * 25 + "\n")

    # --- Count missing values in each column ---
    print("--- Count of missing values: .isnull().sum() ---")
    print(df_miss.isnull().sum())
    print("-" * 25 + "\n")

    # --- Drop rows with any missing values ---
    print("--- Dropping rows with NaNs: .dropna() ---")
    print(df_miss.dropna())
    print("-" * 25 + "\n")

    # --- Fill missing values with a specific value ---
    print("--- Filling NaNs with 0: .fillna(0) ---")
    print(df_miss.fillna(value=0))
    print("-" * 25 + "\n")

    print("### 7. Grouping and Aggregation (groupby) ###\n")

    # --- Group by 'City' and calculate the mean score for each city ---
    print("--- Mean score by city: .groupby('City')['Score'].mean() ---")
    city_scores = df.groupby('City')['Score'].mean()
    print(city_scores)
    print("-" * 25 + "\n")

    # --- Group by 'City' and get multiple aggregations ---
    print("--- Multiple aggregations by city using .agg() ---")
    city_stats = df.groupby('City').agg(
        Mean_Age=('Age', 'mean'),
        Max_Score=('Score', 'max'),
        Count=('Name', 'count')
    )
    print(city_stats)
    print("-" * 25 + "\n")


if __name__ == "__main__":
    main()
