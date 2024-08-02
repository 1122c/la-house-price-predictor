
# LA House Price Predictor

## Description

The LA House Price Predictor is a machine learning application designed to predict house prices in Los Angeles. This project aims to provide accurate price predictions based on various property features such as square footage, number of bedrooms and bathrooms, overall quality, and more. The application consists of a backend API for making predictions and a frontend interface for users to input data and view results.

## Features

- **Predictive Model**: Utilizes machine learning techniques to predict house prices based on historical data and property features.
- **Data Visualization**: Provides visual insights into the dataset and model performance (planned feature).
- **Scalable Backend**: Built with FastAPI, allowing for easy scalability and integration.
- **Responsive Frontend**: Developed using React, offering a user-friendly interface for data input and result display.

## Technologies Used

### Backend

- **Python**: Core language for data processing and model development.
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **Uvicorn**: An ASGI server for serving the FastAPI application.
- **Pandas**: Used for data manipulation and analysis.
- **Scikit-learn**: A machine learning library used for model training and evaluation.
- **Joblib**: For saving and loading machine learning models.
- **Matplotlib & Seaborn**: Libraries for data visualization (planned).

### Frontend

- **React**: A JavaScript library for building user interfaces.
- **Axios**: For making HTTP requests to the backend API.

### Deployment

- **GitHub**: Source code management and version control.
- **Cloud Platform**: (To be decided) for hosting the backend and frontend applications.

## Installation

### Prerequisites

- Python 3.7+
- Node.js and npm
- Git

### Backend Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/la-house-price-predictor.git
   cd la-house-price-predictor
   ```

2. **Set up a Python virtual environment:**

   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```sh
     .\venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

5. **Run the FastAPI server:**

   ```sh
   uvicorn backend.app:app --reload
   ```

### Frontend Setup

1. **Navigate to the frontend directory:**

   ```sh
   cd frontend
   ```

2. **Install the required packages:**

   ```sh
   npm install
   ```

3. **Start the React development server:**

   ```sh
   npm start
   ```

## Usage

- **Backend API**: The FastAPI server runs on `http://localhost:8000` by default. Use this endpoint to interact with the prediction API.
- **Frontend Interface**: The React frontend runs on `http://localhost:3000` by default. Use this interface to input property data and view price predictions.

## Contribution

Contributions are welcome! Please open an issue or submit a pull request for any improvements, features, or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

Special thanks to the City of Los Angeles, Zillow, and other data providers for making housing data publicly available.

---

