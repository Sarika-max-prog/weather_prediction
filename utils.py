#Helper functions
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def highlight_prediction(row):
    if "Rainy" in row['prediction']:
        return ["background-color: #d0e2ff; color: black; font-weight: bold;"] * len(row)
    elif "Sunny" in row['prediction']:
        return ["background-color: #fff7d0; color: black; font-weight: bold;"] * len(row)
    return ["color: black; font-weight: bold;"] * len(row)

def show_weather_summary(df):
    counts = df['prediction'].value_counts()
    emojis = {"Rainy / Cloudy": "🌧️", "Clear / Sunny": "☀️"}
    st.write("### Weather Stats Summary")
    for label, count in counts.items():
        st.markdown(f"<span style='font-size:18px'><strong>{emojis.get(label, '')} {label}</strong>: {count} times</span>", unsafe_allow_html=True)

    # Smaller pie chart
    fig, ax = plt.subplots(figsize=(2.5, 2.5))
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 9})
    ax.axis('equal')
    st.pyplot(fig)

    # Line chart for predictions over time
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
        daily_counts = df.groupby(['date', 'prediction']).size().unstack(fill_value=0)
        st.line_chart(daily_counts)

