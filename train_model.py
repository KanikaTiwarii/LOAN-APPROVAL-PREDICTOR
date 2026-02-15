import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1. Create Synthetic Data with Logical Patterns
np.random.seed(42)
n = 1000
data = {
    'Age': np.random.randint(18, 65, n),
    'Past_Loan_Records': np.random.randint(0, 2, n),
    'Utility_Rent_Payment_History': np.random.randint(0, 2, n),
    'Bank_Statements': np.random.uniform(5.0, 15.0, n), # Scale used in your notebook
    'Income_Stability': np.random.uniform(0.1, 1.0, n),
    'Employment': np.random.randint(0, 2, n),
    'Spending_Percentage': np.random.uniform(0.1, 0.9, n),
    'Education': np.random.randint(0, 4, n),
    'Digital_Payments_Timeliness': np.random.randint(0, 2, n)
}
df = pd.DataFrame(data)

# Logic: Approve if (History is Good AND Stability is High) OR (Balance is very high)
df['Loan_Status'] = ((df['Utility_Rent_Payment_History'] == 1) & (df['Income_Stability'] > 0.4) | (df['Bank_Statements'] > 13)).astype(int)

# 2. Train the Model
X = df.drop('Loan_Status', axis=1)
y = df['Loan_Status']
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# 3. Save the Model
joblib.dump(model, 'model.pkl')
print("✅ model.pkl created successfully!")