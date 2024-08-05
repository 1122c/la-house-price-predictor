import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the dataset
print("loading dataset...")
data = pd.read_csv('data/Zip_zhvf_growth_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv')
print("dataset loaded correctly")

#seperate numeric and non-numeric columns
numeric_columns = data.select_dtypes(include=['number']).columns
non_numeric_columns = data.select_dtypes(exclude=['number']).columns

# Handle missing values
print("handling missing values...")
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())

# data.fillna(data.mean(), inplace=True)

# Encode categorical variables
print("encoding categorical variables...")
data = pd.get_dummies(data, columns=non_numeric_columns)
print("categorical variables encoded")

# Normalize numerical features
print("normalizing numerical features...")
scaler = StandardScaler()
# numerical_features = ['GrLivArea', 'TotalBsmtSF', 'OverallQual', 'YearBuilt', 'LotArea']
data[numeric_columns] = scaler.fit_transform(data[numeric_columns])
print("numerical features normalized")

# Save the preprocessed data
output_path = os.path.join(os.getcwd(), 'data', 'la_housing_data_preprocessed.csv')
print("saving preprocessed data to {output_path}...")

data.to_csv(output_path, index=False)

print("Preprocessing complete. Preprocessed data saved to 'data/la_housing_data_preprocessed.csv'.")
