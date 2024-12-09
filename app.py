from flask import Flask, render_template, request, redirect, url_for, flash
import joblib
import pandas as pd

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# Load the model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    data = request.form.to_dict()
    
    # Validate input and handle empty fields
    try:
        input_features = {
            'Age': float(data['Age']),
            'Past_Loan_Records': int(data['Past_Loan_Records']) if data['Past_Loan_Records'] else 0,
            'Utility_Rent_Payment_History': int(data['Utility_Rent_Payment_History']) if data['Utility_Rent_Payment_History'] else 0,
            'Bank_Statements': float(data['Bank_Statements']) if data['Bank_Statements'] else 0.0,
            'Income_Stability': float(data['Income_Stability']) if data['Income_Stability'] else 0.0,
            'Employment': int(data['Employment']) if data['Employment'] else 0,
            'Spending_Percentage': float(data['Spending_Percentage']) if data['Spending_Percentage'] else 0.0,
            'Education': int(data['Education']) if data['Education'] else 0,
            'Digital_Payments_Timeliness': int(data['Digital_Payments_Timeliness']) if data['Digital_Payments_Timeliness'] else 0,
        }
    except ValueError as e:
        flash(f"Invalid input: {e}")
        return redirect(url_for('home'))

    # Create a DataFrame for prediction
    input_df = pd.DataFrame([input_features])
    
    # Make prediction
    prediction = model.predict(input_df)
    return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
