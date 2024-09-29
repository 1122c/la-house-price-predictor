import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the preprocessed data
data = pd.read_csv('data/la_housing_data_preprocessed.csv')

# Filter to only include Los Angeles County data
la_data = data[data['CountyName_Los Angeles County'] == True]

# Select the target column, which contains the housing prices
housing_prices = la_data['2024-07-31']  # Replace with the actual target column name if changing

# Print statistical summary
print("Statistical Summary of Housing Prices in Los Angeles County:")
print(housing_prices.describe())

# Plot the distribution of housing prices for Los Angeles County
plt.figure(figsize=(10, 6))
sns.histplot(housing_prices, kde=True, bins=30)
plt.xlabel('Housing Prices')
plt.ylabel('Frequency')
plt.title('Distribution of Housing Prices in Los Angeles County')
plt.show()

