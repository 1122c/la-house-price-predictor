import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Load the preprocessed data
data = pd.read_csv('backend/data/la_housing_data_preprocessed.csv')

# Load the trained model
model = joblib.load('backend/model/la_house_price_model.pkl')

# Define the features and target variable
features = ['StateName_LA', 'State_LA', 'City_East Los Angeles', 'City_Los Angeles',
            'Metro_Los Angeles-Long Beach-Anaheim, CA', 'CountyName_Los Angeles County']
X = data[features]
y = data['2024-07-31']  # Replace with the actual target column name

# Make predictions
y_pred = model.predict(X)

# Calculate residuals
residuals = y - y_pred

# Identify outliers based on a residual threshold
threshold = 3  # Adjust threshold as needed
outliers = data[np.abs(residuals) > threshold]

# Display the outliers
print("Outliers based on residuals:")
print(outliers)

# Optional: Plot the residuals (already done in previous step)
plt.scatter(y_pred, residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs Predicted Values')
plt.show()

