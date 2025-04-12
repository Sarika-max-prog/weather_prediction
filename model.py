#Model prediction logic
import pickle
import numpy as np
from config import MODEL_PATH, WEATHER_LABELS

model = pickle.load(open(MODEL_PATH, "rb"))

def predict_weather(features):
    prediction = model.predict(np.array([features]))[0]
    return WEATHER_LABELS[prediction]