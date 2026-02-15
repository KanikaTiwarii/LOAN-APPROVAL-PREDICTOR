import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate Synthetic Data
n_rows = 1000
data = {
    'Age': np.random.randint(18, 65, n_rows),
    'Education': np.random.randint(0, 4, n_rows), # 0:School, 1:Grad, 2:PostGrad, 3:PhD
    'Employment': np.random.randint(0, 2, n_rows), # 0:Unemployed, 1:Employed
    'Income_Stability': np.random.uniform(0.1, 1.0, n_rows),
    'Bank_Balance': np.random.randint(500, 10000, n_rows), # Realistic amounts
    'Past_Loan_Records': np.random.randint(0, 2, n_rows), # 0:No, 1:Yes
    'Utility_Payment': np.random.randint(0, 2, n_rows), # 0:Poor, 1:Good
    'Digital_Payment': np.random.randint(0, 2, n_rows),
    'Spending_Percentage': np.random.uniform(0.1, 0.9, n_rows)
}

df = pd.DataFrame(data)

# Logic for Loan Approval (Target)
# We approve if (Income_Stability > 0.5 AND Utility_Payment == 1) OR (Bank_Balance > 5000)
df['Loan_Status'] = ((df['Income_Stability'] > 0.6) & (df['Utility_Payment'] == 1) | (df['Bank_Balance'] > 7000)).astype(int)

df.to_csv('loan_data.csv', index=False)
print("Dataset 'loan_data.csv' created successfully!")