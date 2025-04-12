#Main Streamlit app
import streamlit as st
import pandas as pd
from datetime import datetime
from config import REGIONS
from data_handler import load_historical_data, load_past_predictions, save_prediction
from model import predict_weather
from utils import highlight_prediction, show_weather_summary

st.set_page_config(page_title="Smart Weather Predictor", layout="wide")
st.title("☁️ Smart Weather Predictor")
st.markdown("Know your weather based on input or location")

page = st.sidebar.radio("📂 Navigation", ["🌦️ Predict Weather", "📊 Past Predictions"])
df = load_historical_data()
past_df = load_past_predictions()

if page == "🌦️ Predict Weather":
    st.subheader("📍 Choose Region and Date")
    region = st.selectbox("Region", REGIONS)
    selected_date = st.date_input("Select Date", value=datetime(2012, 1, 1))

    row = df[df['date'] == pd.to_datetime(selected_date)]
    if not row.empty:
        precipitation = row['precipitation'].values[0]
        temp_max = row['temp_max'].values[0]
        temp_min = row['temp_min'].values[0]
        wind = row['wind'].values[0]
        st.success("Weather data auto-filled from historical dataset.")
    else:
        st.warning("Date not in dataset. Please input manually.")
        precipitation = st.slider("Precipitation (mm)", 0.0, 50.0, 10.0)
        temp_max = st.number_input("Max Temperature (°C)", value=30.0)
        temp_min = st.number_input("Min Temperature (°C)", value=20.0)
        wind = st.slider("Wind Speed (km/h)", 0.0, 100.0, 10.0)

    if st.button("🔮 Predict Weather"):
        label, emoji = predict_weather([precipitation, temp_max, temp_min, wind])
        st.subheader(f"Predicted weather: {emoji} {label}")

        new_row = {
            "date": selected_date,
            "region": region,
            "precipitation": precipitation,
            "temp_max": temp_max,
            "temp_min": temp_min,
            "wind": wind,
            "prediction": label
        }
        past_df = save_prediction(new_row, past_df)

elif page == "📊 Past Predictions":
    st.subheader("📅 View Past Predictions")
    if not past_df.empty:
        region_filter = st.selectbox("Filter by Region", ["All"] + sorted(past_df['region'].unique().tolist()))
        date_filter = st.date_input("Filter by Date", value=None, key="filter")

        filtered_df = past_df.copy()
        if region_filter != "All":
            filtered_df = filtered_df[filtered_df['region'] == region_filter]
        if date_filter:
            filtered_df = filtered_df[filtered_df['date'] == pd.to_datetime(date_filter)]

        st.dataframe(filtered_df.style.apply(highlight_prediction, axis=1))
        show_weather_summary(filtered_df)
    else:
        st.info("No past predictions found.")
