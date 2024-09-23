import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib

# Load the preprocessed data
data = pd.read_csv('backend/data/la_housing_data_preprocessed.csv')

# Step 1: Identify relevant columns related to Los Angeles and Los Angeles County
la_columns = [col for col in data.columns if 'Los Angeles' in col or 'LA' in col or 'LosAngeles' in col or 'Los_Angeles' in col]
la_county_columns = [col for col in data.columns if 'Los Angeles County' in col or 'LA County' in col or 'LosAngelesCounty' in col or 'Los_Angeles_County' in col]

# Print the relevant columns
print("Columns related to 'Los Angeles':")
print(la_columns)

print("Columns related to 'Los Angeles County':")
print(la_county_columns)

# Step 2: Manually clean the features list to include only existing columns
# Remove 'Region_LosAngeles' and other non-existent columns
features = [
    'StateName_LA', 'State_LA', 'City_East Los Angeles', 'City_Los Angeles',
    'Metro_Los Angeles-Long Beach-Anaheim, CA', 'CountyName_Los Angeles County'
]

# Choose the target variable (update this to match your actual target column)
y = data['2024-07-31']  # Replace with the actual target column name

# Step 3: Train the model with the selected features
X = data[features]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae}')

# Save the trained model
joblib.dump(model, 'backend/model/la_house_price_model.pkl')
print("Model trained and saved successfully.")
