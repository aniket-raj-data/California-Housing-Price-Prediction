import streamlit as st
import joblib
import pandas as pd
import numpy as np

# 1. वेब ऐप का टाइटल (Heading)
st.title("🏡 California Housing Price Prediction App")
st.write("Enter the details below to predict the median house value.")

# 2. मॉडल को लोड करना (जो सुबह .pkl फाइल बनाई थी)
try:
    model = joblib.load("california_housing_rf_model.pkl")
except Exception as e:
    st.error(f"Error: 'california_housing_rf_model.pkl' file not found! Details: {e}")

# 3. यूजर से इनपुट लेने के लिए बॉक्स बनाना
st.subheader("Property Characteristics")

# MedInc (Median Income) - सबसे मुख्य ड्राइवर
med_inc = st.number_input("Median Income (in $10,000s, e.g., 3.5)", min_value=0.0, max_value=15.0, value=3.5)

# HouseAge (घर की उम्र)
house_age = st.number_input("House Age (Years, e.g., 28)", min_value=1.0, max_value=52.0, value=28.0)

# AveRooms (औसत कमरे)
ave_rooms = st.number_input("Average Rooms per Dwelling (e.g., 5.4)", min_value=1.0, max_value=20.0, value=5.4)

# AveBedrms (औसत बेडरूम)
ave_bedrms = st.number_input("Average Bedrooms per Dwelling (e.g., 1.1)", min_value=1.0, max_value=10.0, value=1.1)

# Population (आबादी)
population = st.number_input("Block Population (e.g., 1400)", min_value=3.0, max_value=35000.0, value=1400.0)

# AveOccup (औसत रहने वाले लोग)
ave_occup = st.number_input("Average House Occupancy (e.g., 3.0)", min_value=1.0, max_value=10.0, value=3.0)

# 4. प्रेडिक्शन बटन और आउटपुट लॉजिक
if st.button("🔮 Predict House Price"):
    # इनपुट्स को एक एरे (Array) में डालना (आखिरी दो 34.0 और -118.0 Latitude/Longitude की डमी वैल्यूज हैं)
    input_data = np.array([[med_inc, house_age, ave_rooms, ave_bedrms, population, ave_occup, 34.0, -118.0]]) 
    
    # प्रेडिक्शन करना
    prediction = model.predict(input_data)
    
    # परिणाम स्क्रीन पर दिखाना ($100,000s में गुना करके)
    final_price = prediction[0] * 100000
    st.success(f"🎉 Estimated Median House Value: ${final_price:,.2f}")
