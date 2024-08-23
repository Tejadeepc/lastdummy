import pandas as pd

# Create a sample DataFrame with categorical data
data = {
    'Temperature': ['Hot', 'Cold', 'Warm', 'Cold'],
    'Weather': ['Sunny', 'Rainy', 'Sunny', 'Cloudy']
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Create dummy variables using pd.get_dummies
dummy_df = pd.get_dummies(df, drop_first=True)

# Display the DataFrame with dummy variables
print("\nDataFrame with Dummy Variables:")
print(dummy_df)