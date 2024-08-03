import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv('data/Zip_zhvf_growth_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv')

# Handle missing values
data.fillna(data.mean(), inplace=True)

# Encode categorical variables
data = pd.get_dummies(data)

# Normalize numerical features
scaler = StandardScaler()
numerical_features = ['GrLivArea', 'TotalBsmtSF', 'OverallQual', 'YearBuilt', 'LotArea']
data[numerical_features] = scaler.fit_transform(data[numerical_features])

# Save the preprocessed data
data.to_csv('data/la_housing_data_preprocessed.csv', index=False)

print("Preprocessing complete. Preprocessed data saved to 'data/la_housing_data_preprocessed.csv'.")
