from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import pickle
import numpy as np
import json
import uvicorn

app = FastAPI()

CROP_RECOMMENDATION_MODEL_PATH = "Models/crop_recommentation_models/crop_recommentation_RF_model.pkl"

CROP_RECOMMENDATION_MODEL = pickle.load(open(
    CROP_RECOMMENDATION_MODEL_PATH,"rb"
    ))


class CropRecommend(BaseModel):
    N : str
    P : str
    K : str
    pH : str
    rainFall : str
    temp : str
    humidity : str

@app.post("/crop_recommend")
async def crop_recommendation(cropRecommend : CropRecommend):
    print("sdsdsdsds")
    N = int(cropRecommend.N)
    P = int(cropRecommend.P)
    K = int(cropRecommend.P)
    pH = float(cropRecommend.pH)
    rainFall = float(cropRecommend.rainFall)
    temp = float(cropRecommend.temp)
    humidity = float(cropRecommend.humidity)

    inputs = np.array([[N,P,K,temp,humidity,pH,rainFall]])
    predictions = CROP_RECOMMENDATION_MODEL.predict_proba(inputs)

    response = []

    for i in zip(CROP_RECOMMENDATION_MODEL.classes_,predictions[0]):
        if i[1] > 0.1:
            result = {}
            result[float(i[1])] = i[0] 
            response.append(result)

    return response

class T(BaseModel):
    msg : str

@app.post("/testing")
def test(t : T):
    return t

@app.get("/")
def home():
    return "{ 'message' : 'welcome home' }"


if __name__ == "__main__":
    uvicorn.run(app,host="192.168.43.135",port=8080)
