import uvicorn
from fastapi import FastAPI
import pickle
import numpy as np
import pandas as pd
from banknote import BankNote

app=FastAPI()
pickle_in=open("model.pkl","rb")
model=pickle.load(pickle_in)

@app.get("/")
def hello():
    return {"Message": "Hello, everyone"}

@app.post("/predict")
def predict_banknote(data:BankNote):
    data = data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']

    prediction=model.predict([[variance,skewness,curtosis,entropy]])

    if(prediction[0] >0.5):
        prediction="Fake note"
    else:
        prediction="Bank Note"
    return{
        'prediction' : prediction
    }