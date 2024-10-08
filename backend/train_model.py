import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib
import os

# Load the preprocessed data
data = pd.read_csv('data/la_housing_data_preprocessed.csv')

# Load the saved scaler
scaler_path = os.path.join('model', 'scaler.pkl')
scaler = joblib.load(scaler_path)

# Load the saved feature names used during scaling
features_path = os.path.join('model', 'features.pkl')
scaled_features = joblib.load(features_path)

# Ensure that the features exist in the preprocessed data
missing_features = [f for f in scaled_features if f not in data.columns]
if missing_features:
    raise KeyError(f"The following features are missing from the dataset: {missing_features}")

# Define the target variable (e.g., '2024-07-31')
y = data['2024-07-31']  # Adjust to your actual target column

# Use only the features that were used during scaling
X = data[scaled_features]

# Scale the features using the same scaler
X_scaled = scaler.transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train the model
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae}')

# Save the trained model
model_path = os.path.join('model', 'la_house_price_model.pkl')
joblib.dump(model, model_path)
print(f"Model trained and saved to {model_path}")
