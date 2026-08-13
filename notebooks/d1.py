import pandas as pd
df=pd.read_csv("../data/titanic.csv")
print("FIRST 5 ROWS")
print(df.head())
print("\nDATASET SHAPE")
print(df.shape)
print("\nCOLUMN  NAMES")
print(df.columns)
print("\nDATA TYPES")
print(df.dtypes)
print("\nDATASET INFORMATION")
df.info()
print("\nMISSING VALUES")
print(df.isnull().sum())
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())
# Create a copy of the original dataset
cleaned_df = df.copy()

# Fill missing Age values with the median age
cleaned_df["Age"] = cleaned_df["Age"].fillna(cleaned_df["Age"].median())

# Fill missing Cabin values with "Unknown"
cleaned_df["Cabin"] = cleaned_df["Cabin"].fillna("Unknown")

# Fill missing Embarked values with the most common value
cleaned_df["Embarked"] = cleaned_df["Embarked"].fillna(
    cleaned_df["Embarked"].mode()[0]
)

print("\nMISSING VALUES AFTER CLEANING")
print(cleaned_df.isnull().sum())
df.to_csv("../cleaned_data/titanic_cleaned.csv", index=False)

print("Cleaned dataset saved successfully!")
