import pandas as pd

# Read the original dataset
df = pd.read_csv('https://raw.githubusercontent.com/ZoeyW99/bres/main/bres1.csv')

# Reshape the dataset to the desired format
df = df.melt(id_vars=['Code'], var_name='City_Year', value_name='Value')

# Split the 'City_Year' column into separate 'City' and 'Year' columns
df[['City', 'Year']] = df['City_Year'].str.extract(r'(.+)_(\d{4})')



# Remove the 'City_Year' column
df.drop(columns=['City_Year'], inplace=True)

# Reorder the columns
df = df[['Code', 'City', 'Year', 'Value']]

# Sort the dataset by 'Code', 'City', and 'Year'
df.sort_values(['Code', 'City', 'Year'], inplace=True)

# Reset the index
df.reset_index(drop=True, inplace=True)

# Display the resulting dataset
print(df)

print(df.info)

df['Year'] = df['Year'].astype(int)

print(df.dtypes)


# df.to_csv("/Users/zoeyw/Desktop/bres2.csv", index=False)

