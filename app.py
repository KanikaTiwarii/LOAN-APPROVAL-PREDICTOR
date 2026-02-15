from flask import Flask, render_template, request
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load Model
if os.path.exists('model.pkl'):
    model = joblib.load('model.pkl')
else:
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return "Error: model.pkl not found. Run train_model.py first."
    
    try:
        # Capture and Validate Input
        # We 'clamp' the values to the training range to prevent errors
        data = {
            'Age': max(18, min(float(request.form['Age']), 100)),
            'Past_Loan_Records': int(request.form['Past_Loan_Records']),
            'Utility_Rent_Payment_History': int(request.form['Utility_Rent_Payment_History']),
            'Bank_Statements': max(0.0, min(float(request.form['Bank_Statements']), 15.0)),
            'Income_Stability': max(0.0, min(float(request.form['Income_Stability']), 1.0)),
            'Employment': int(request.form['Employment']),
            'Spending_Percentage': max(0.0, min(float(request.form['Spending_Percentage']), 1.0)),
            'Education': int(request.form['Education']),
            'Digital_Payments_Timeliness': int(request.form['Digital_Payments_Timeliness'])
        }

        # Force correct column order
        cols = ['Age', 'Past_Loan_Records', 'Utility_Rent_Payment_History', 'Bank_Statements', 
                'Income_Stability', 'Employment', 'Spending_Percentage', 'Education', 'Digital_Payments_Timeliness']
        
        input_df = pd.DataFrame([data])[cols]
        prediction = model.predict(input_df)[0]
        
        status = "APPROVED ✅" if prediction == 1 else "REJECTED ❌"
        return render_template('result.html', prediction=status)

    except Exception as e:
        return f"Prediction Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)