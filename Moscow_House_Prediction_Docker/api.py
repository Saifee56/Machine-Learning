from fastapi import FastAPI
import uvicorn
import pickle
import pandas as pd
import numpy as np
from moscow_class import MoscowHouse

app=FastAPI()
pickle_in=open('moscow_model.pkl','rb')
model=pickle.load(pickle_in)

@app.get('/')
def hello():
    return {"Message":"Hello, Everyone"}

@app.post('/predict')
def predict_price(data:MoscowHouse):
    data=data.dict()
    Apartment_type:data['Apartment_type']
    Metro_station:data['Metro_station']
    Minutes_to_metro:data['Minutes_to_metro']
    Region: data['Region']
    Number_of_rooms: data['Number_of_rooms']
    Area: data['Area']
    Living_area:data['Living_area']
    Kitchen_area:data['Kitchen_area']
    Floor:data['Floor']
    Number_of_floors: data['Number_of_floors']
    RenovationL:data['RenovationL']

    prediction=model.predict([[Apartment_type,Metro_station,Minutes_to_metro,Region,Number_of_rooms,Area,Living_area,Kitchen_area,
                              Floor,Number_of_floors,RenovationL]])
    return {
        'Prediction' : float(prediction)
    }