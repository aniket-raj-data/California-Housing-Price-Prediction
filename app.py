import streamlit as st
import joblib
import gdown
import os

# अपनी फाइल ID यहाँ डाल दी है
file_id = '1N0aLxEfq5kHq3dkJHp6kKickMZ8TpZS-'
url = f'https://drive.google.com/uc?id={file_id}'
output = 'model.pkl'

# अगर फाइल डाउनलोड नहीं है, तभी डाउनलोड करें
if not os.path.exists(output):
    gdown.download(url, output, quiet=False)

# अब मॉडल लोड करें
model = joblib.load(output)

# इसके आगे अपना बाकी का प्रेडिक्शन वाला कोड (UI कोड) यहाँ लिखें
# --- यहाँ से अपना UI कोड पेस्ट करें ---
st.title("California Housing Price Prediction App")
st.write("Enter the details below to predict the median house value.")

# इनपुट बॉक्सेस (ये वही इनपुट हैं जो तुम्हारी ऐप में दिख रहे थे)
med_income = st.number_input('Median Income (in $10,000s, e.g., 3.5)', value=3.5)
house_age = st.number_input('House Age (Years, e.g., 28)', value=28.0)
ave_rooms = st.number_input('Average Rooms per Dwelling (e.g., 5.4)', value=5.4)
ave_bedrms = st.number_input('Average Bedrooms per Dwelling (e.g., 1.1)', value=1.1)
population = st.number_input('Block Population (e.g., 1400)', value=1400.0)
latitude = st.number_input(Latitude,value=37.88)
longitude = st.number_input(Longitude,value=-122.23)
ave_occupation = st.number_input(Average_Occupancy,value=3.0)
# प्रेडिक्शन बटन
if st.button('Predict'):
    # मॉडल को इनपुट देना
    input_data = [[med_income, house_age, ave_rooms, ave_bedrms, population, ave_occup, latitude, longitude]]
    prediction = model.predict(input_data)
    
    # रिजल्ट दिखाना
    st.success(f"The predicted median house value is: ${prediction[0]:.2f}")
