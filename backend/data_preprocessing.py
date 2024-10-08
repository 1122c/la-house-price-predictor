import os
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Load the dataset
print("loading dataset...")
data = pd.read_csv('data/Zip_zhvf_growth_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv')
print("dataset loaded correctly")

# Separate numeric and non-numeric columns
numeric_columns = data.select_dtypes(include=['number']).columns
non_numeric_columns = data.select_dtypes(exclude=['number']).columns

# Handle missing values
print("handling missing values...")
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())

# Encode categorical variables
print("encoding categorical variables...")
data = pd.get_dummies(data, columns=non_numeric_columns)
print("categorical variables encoded")

# Normalize numerical features
print("normalizing numerical features...")
scaler = StandardScaler()
data[numeric_columns] = scaler.fit_transform(data[numeric_columns])

# Save the scaler and the feature names used during scaling
scaler_path = os.path.join('model', 'scaler.pkl')
joblib.dump(scaler, scaler_path)
print(f"Scaler saved to {scaler_path}")

# Save the feature names
features_path = os.path.join('model', 'features.pkl')
joblib.dump(numeric_columns, features_path)  # Save the columns used during scaling
print(f"Features used during scaling saved to {features_path}")

# Save the preprocessed data
output_path = os.path.join('data', 'la_housing_data_preprocessed.csv')
data.to_csv(output_path, index=False)
print("Preprocessing complete. Preprocessed data saved.")

