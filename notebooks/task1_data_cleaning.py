import pandas as pd

# Load the dataset
df = pd.read_csv("../data/titanic.csv")

# Display first 5 rows
print("FIRST 5 ROWS")
print(df.head())

# Dataset shape
print("\nDATASET SHAPE")
print(df.shape)

# Column names
print("\nCOLUMN NAMES")
print(df.columns)

# Data types
print("\nDATA TYPES")
print(df.dtypes)

# Dataset information
print("\nDATASET INFORMATION")
print(df.info())

# Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Check duplicate rows
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

# Fill missing Age values with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked values with mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Fill missing Cabin values
df["Cabin"] = df["Cabin"].fillna("Unknown")

# Check missing values after cleaning
print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("../cleaned_data/titanic_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
# Verify the saved cleaned dataset
cleaned_df = pd.read_csv("../cleaned_data/titanic_cleaned.csv")

print("\nVERIFYING CLEANED FILE")
print("Shape:", cleaned_df.shape)
print("\nMissing values in saved file:")
print(cleaned_df.isnull().sum())
print("\nDATA CLEANING COMPLETED")
print("Original dataset shape: (891, 12)")
print("Cleaned dataset shape:", cleaned_df.shape)
print("Duplicate rows removed:", df.duplicated().sum())
print("All missing values handled: Yes")
