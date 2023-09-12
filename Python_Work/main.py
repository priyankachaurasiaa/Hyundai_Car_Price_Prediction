import pandas as pd
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained Linear Regression model from the pkl file
with open('LinearRRegressionModell.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user inputs from the form
        car_model = request.form["model"]  # Store the "model" input as a string
        year = int(request.form['year'])
        transmission = request.form['transmission']
        total_driven = float(request.form['total_driven'])
        fuelType = request.form['fuelType']
        tax = float(request.form['tax(£)'])  # Use the correct column name
        mpg = float(request.form['mpg'])
        engineSize = float(request.form['engineSize'])

        # Create a DataFrame with the user input
        input_data = pd.DataFrame({
            'model': [car_model],
            'year': [year],
            'transmission': [transmission],
            'total_driven': [total_driven],
            'fuelType': [fuelType],
            'tax(£)': [tax],        # Use the correct column name 'tax(£)'
            'mpg': [mpg],
            'engineSize': [engineSize]
        })

        # Perform prediction using the model
        prediction = model.predict(input_data)

        return render_template('index.html', prediction=f"Predicted Price: £{prediction[0]:.2f}")

    # If the request method is GET, simply render the HTML template
    return render_template('index.html', prediction="")

if __name__ == "__main__":
    app.run(debug=True)
