from fastapi import FastAPI
import uvicorn
import pickle
import pandas as pd
import numpy as np
from loan_class import Loan

app=FastAPI()
pickle_in=open("model.pkl","rb")
model=pickle.load(pickle_in)

@app.get("/")
def hello():
    return {"Message": "Hello, Everyone"}

@app.post("/predict")
def predict_loan(data :Loan):
    data=data.dict()
    CurrentLoanAmount=data['CurrentLoanAmount']
    Term=data['Term']
    CreditScore=data['CreditScore']
    AnnualIncome=data['AnnualIncome']
    HomeOwnership=data['HomeOwnership']
    Purpose=data['Purpose']
    MonthlyDebt=data['MonthlyDebt']
    YearsofCreditHistory=data['YearsofCreditHistory']
    NumberofOpenAccounts=data['NumberofOpenAccounts']
    NumberofCreditProblems=data['NumberofCreditProblems']
    CurrentCreditBalance=data['CurrentCreditBalance']
    MaximumOpenCredit=data['MaximumOpenCredit']
    Bankruptcies=data['Bankruptcies']
    TaxLiens=data['TaxLiens']

    prediction=model.predict([[CurrentLoanAmount,Term,CreditScore,AnnualIncome,HomeOwnership,Purpose,MonthlyDebt,YearsofCreditHistory,NumberofOpenAccounts
                               ,NumberofCreditProblems,CurrentCreditBalance,MaximumOpenCredit,Bankruptcies,TaxLiens]])
    
    if(prediction[0] >0.5):
        prediction="Charged off"
    else:
        prediction="Fully paid"
    return{
        'prediction' : prediction
    }



