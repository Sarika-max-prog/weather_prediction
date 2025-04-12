
# **☁️ Weather Forecasting with Machine Learning & Streamlit**  
**Predicting weather conditions and visualizing them in real-time using Python, Machine Learning, and Streamlit**

![image](https://github.com/user-attachments/assets/c2481bc2-74ee-42b0-ba66-5df77b53af0a)
![image](https://github.com/user-attachments/assets/ac6ad3ab-dc71-43ab-81ec-7378d1f9f1ba)

---

## **📖 Table of Contents**  
### **1️⃣ Executive Summary**  
- This project uses machine learning to predict weather conditions based on historical weather data.
- The final predictions and insights are visualized using an interactive Streamlit dashboard.
- The dashboard displays weather patterns across different Indian states, including temperature, weather conditions, and precipitation trends.

---

### **2️⃣ Project Scope & Objectives**  
- **Problem Statement**:  
  Can we predict upcoming weather conditions using historical data, and visualize those predictions in an interactive way?

- **Objectives**:  
  - Predict weather conditions using machine learning models.
  - Create a real-time, user-interactive dashboard to visualize weather trends.
  - Provide insights into temperature variations, weather conditions, and precipitation levels.

- **Target Audience**:  
  - Weather researchers, meteorologists, data analysts, and general users interested in weather predictions.

---

### **3️⃣ Methodology & Approach**  
- **📥 Data Collection**:  
  Dataset: `seattle-weather.csv` (open-source)  
  Fields: `precipitation`, `temp_max`, `temp_min`, `wind`, `weather`, `date`

- **🧹 Preprocessing & Feature Engineering**:  
  - Converted the categorical `weather` column into a binary feature `weather_binary` (Rain = 1, Others = 0).
  - Handled missing data and extracted new features, such as the sum of temperatures and precipitation by state.

- **⚙️ Machine Learning Model**:  
  - Model: `RandomForestClassifier`
  - Features: `precipitation`, `temp_max`, `temp_min`, `wind`
  - Accuracy Achieved: **94%**

- **💾 Model Deployment**:  
  - Saved the trained model using `pickle`.
  - The model makes predictions on updated CSV files in real-time, with the results saved to `weather_with_predictions.csv`.

- **📊 Visualization**:  
  - Streamlit dashboard used for:
    - Displaying predicted weather conditions
    - Visualizing temperature distributions and precipitation trends
    - Interactive filters to explore different states, weather conditions, and date ranges

---

### **4️⃣ Key Insights from Dashboard**  
📌 Notable observations from the dashboard:  
- **Telangana** saw the highest temperature (35°C) with frequent rain conditions.  
- **Kerala** and **Gujarat** mainly experienced sunny or cloudy weather.  
- **Precipitation** had notable spikes during early and late 2015.  
- The most common temperature range observed was between **24°C and 36°C**.  
- Filters allow users to interact with data by **state**, **weather condition**, and **quarter-wise trends**.

---

### **5️⃣ Tools & Technologies Used**  
- **Python** – For data manipulation, machine learning, and model deployment  
- **Pandas, Scikit-learn** – For data preprocessing and model building  
- **Streamlit** – For building the interactive dashboard  
- **Pickle** – For saving and loading the trained machine learning model  

---

### **6️⃣ How to Use the Project**  
1. Clone the repository to your local machine  
2. Install necessary libraries using `pip install -r requirements.txt`  
3. Train the model or load the saved model (`weather_model.pkl`)  
4. Update the weather data in `seattle-weather.csv`  
5. Generate weather predictions and save the results in `weather_with_predictions.csv`  
6. Run the Streamlit dashboard with `streamlit run weather_dashboard.py`  
7. Interact with the dashboard to explore weather trends and predictions  

---
7️⃣ Conclusion
This project successfully demonstrates how machine learning can be used to forecast weather conditions with high accuracy and deliver meaningful insights through an interactive Streamlit dashboard.

By combining historical data analysis, predictive modeling, and user-friendly visualization, this solution enables users to monitor regional weather trends in real time and make informed decisions.

Whether for researchers, weather departments, or the general public, this tool offers a practical and accessible way to understand and explore weather patterns using data-driven techniques.




