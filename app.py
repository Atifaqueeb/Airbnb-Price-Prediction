from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the pre-trained Random Forest model and the dataset with forecast prices
rf_model = joblib.load('random_forest_model.pkl')
forecast_data = pd.read_csv('sarima_predictions_with_average_actuals.csv')
forecast_data['date'] = pd.to_datetime(forecast_data['date'])

# Prepare dropdown data for the template
categories = {
    'room_type': {
        'Entire home/apt': 0,
        'Hotel room': 1,
        'Private room': 2,
        'Shared room': 3
    },
    'property_type': {
        'Boat': 0,
        'Entire condo': 1,
        'Entire guest suite': 2,
        'Entire guesthouse': 3,
        'Entire home': 4,
        'Entire loft': 5,
        'Entire place': 6,
        'Entire rental unit': 7,
        'Entire serviced apartment': 8,
        'Entire townhouse': 9,
        'Entire vacation home': 10,
        'Private room': 11,
        'Private room in bed and breakfast': 12,
        'Private room in condo': 13,
        'Private room in guest suite': 14,
        'Private room in home': 15,
        'Private room in rental unit': 16,
        'Private room in serviced apartment': 17,
        'Private room in townhouse': 18,
        'Room in hotel': 19,
        'Shared room in condo': 20,
        'Shared room in rental unit': 21,
        'Tiny home': 22
    },
    'has_availability': {'No': 0, 'Yes': 1},

}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return predict()
    return render_template('index.html', categories=categories)

@app.route('/predict', methods=['POST'])
def predict():
    input_date = pd.to_datetime(request.form['date'])
    forecast_price_data = forecast_data[forecast_data['date'] == input_date]
    if forecast_price_data.empty:
        return render_template('index.html', prediction_text='No forecast available for selected date.', categories=categories)

    forecast_price = forecast_price_data['predicted_price'].values[0]

    # Collecting and converting input from form using encoded values
    features = {
        'forecast_price': forecast_price,
        'accommodates': float(request.form['accommodates']),
        'bedrooms': float(request.form['bedrooms']),
        'beds': float(request.form['beds']),
        'room_type': int(request.form['room_type']),
        'property_type': int(request.form['property_type']),
        'bathrooms': float(request.form['bathrooms']),
        'latitude': float(request.form['latitude']),
        'longitude': float(request.form['longitude']),
        'host_is_superhost': int(request.form.get('host_is_superhost', '0')),  # Check for 'host_is_superhost' and default to '0'
        'instant_bookable': int(request.form.get('instant_bookable', '0')),  # Check for 'instant_bookable' and default to '0'
        'host_verifications': int(request.form['host_verifications']),
        'number_of_reviews': float(request.form['number_of_reviews'])
    }
    
    df = pd.DataFrame([features])
    prediction = rf_model.predict(df)[0]
    
    return render_template('index.html', prediction_text=f'Estimated Price: ${prediction:.2f}', categories=categories)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
