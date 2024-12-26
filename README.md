# Airbnb Price Prediction Flask App

link : https://6715383d-8484-4b5d-9513-92d2c242b3ec-00-3voi76t0dkywd.riker.repl.co:5000

## Project Overview

### Introduction
This project develops a comprehensive solution for predicting Airbnb rental prices using historical data and advanced forecasting techniques. The goal is to provide Airbnb hosts and real estate analysts with accurate price predictions that reflect market conditions and property characteristics. This tool can help hosts optimize their pricing strategies and maximize their rental income.

### Motivation
The dynamic nature of the rental market, with fluctuating prices due to seasonality, demand, and other factors, makes it essential for hosts to adapt their pricing to remain competitive while maximizing revenue. Traditional pricing methods may not account for all variables affecting rental prices. This project addresses this gap by incorporating both historical data analysis and forecasted market trends into the pricing model.

### Functionality
- **Data Integration**: Merges detailed listing information from Airbnb with calendar-based pricing data to form a comprehensive dataset.
- **Advanced Forecasting**: Utilizes a Seasonal ARIMA (SARIMA) model to analyze and forecast future price trends based on historical data.
- **Machine Learning Prediction**: Employs a RandomForestRegressor trained on merged data to predict rental prices, considering both static features of properties and dynamic market conditions.
- **User Interface**: Provides a Flask-based web interface where users can input property details and obtain instant price predictions.
- **Data Visualization**: Offers visual insights into pricing trends and model predictions, aiding in transparent and informed decision-making.

### Benefits
- **Accuracy**: Combines machine learning and time-series forecasting to enhance prediction accuracy.
- **Usability**: Easy-to-use web interface allows non-technical users to benefit from sophisticated data analysis tools.
- **Adaptability**: The model can update predictions based on new data, ensuring relevance despite market changes.
- **Insightful**: Helps users understand factors influencing rental prices, supporting strategic decision-making.

### Technologies Used
- **Flask**: Serves the backend and frontend of the application, facilitating user interactions and data presentation.
- **Pandas and NumPy**: Handle data manipulation and numerical calculations, respectively.
- **Scikit-Learn**: Provides machine learning tools to train and evaluate the RandomForest model.
- **Statsmodels**: Used for building and fitting the SARIMA model for time-series analysis.
- **Joblib**: Utilized for model serialization and deserialization, allowing for efficient storage and retrieval of the predictive models.

![AE905977-3B2A-4D9A-A079-BCC6F380EE21](https://github.com/user-attachments/assets/fa5c0ee9-1762-49f9-8cf6-31a7ebd44896)

