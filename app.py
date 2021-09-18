import uvicorn
from fastapi import FastAPI
from data_model import BankNote
import numpy as np
import pandas as pd
import pickle

app = FastAPI()

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.get('/')
def index():
    return {'message': 'Model serving API'}


@app.post('/predict')
def predict_banknote(data: BankNote):
    variance = data.variance
    skewness = data.skewness
    curtosis = data.curtosis
    entropy = data.entropy

    prediction = model.predict([[variance,
                                skewness,
                                curtosis,
                                entropy]])

    if prediction[0] > 0.5:
        result = 'The Note is fake.'
    else:
        result = 'The Note is real.'

    return {'prediction': result}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

