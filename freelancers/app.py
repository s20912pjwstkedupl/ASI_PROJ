# app.py

import streamlit as st
import pandas as pd
from autogluon.tabular import TabularPredictor

# Ścieżka do modelu
MODEL_PATH = 'models/autogluon_model/'

# Ścieżka do danych (żeby wyciągnąć unikalne wartości dla dropdownów)
DATA_PATH = 'datasets/freelancer_earnings_bd.csv'

# Wczytaj model
predictor = TabularPredictor.load(MODEL_PATH)

# Wczytaj dane
raw_data = pd.read_csv(DATA_PATH)

# Tytuł aplikacji
st.title("🎯 Predykcja Job Success Rate")

st.write("Wprowadź dane projektu freelancera:")

# Przygotowanie list wyboru na podstawie danych
def get_unique_options(column_name):
    return sorted(raw_data[column_name].dropna().unique())

# Generujemy listy opcji
job_category_options = get_unique_options('Job_Category')
platform_options = get_unique_options('Platform')
experience_level_options = get_unique_options('Experience_Level')
client_region_options = get_unique_options('Client_Region')
payment_method_options = get_unique_options('Payment_Method')
project_type_options = get_unique_options('Project_Type')

# Formularz
input_data = {}

input_data['Job_Category'] = st.selectbox('Job Category', job_category_options)
input_data['Platform'] = st.selectbox('Platform', platform_options)
input_data['Experience_Level'] = st.selectbox('Experience Level', experience_level_options)
input_data['Client_Region'] = st.selectbox('Client Region', client_region_options)
input_data['Payment_Method'] = st.selectbox('Payment Method', payment_method_options)
input_data['Job_Completed'] = st.number_input('Job Completed', min_value=0)
input_data['Earnings_USD'] = st.number_input('Earnings (USD)', min_value=0.0)
input_data['Hourly_Rate'] = st.number_input('Hourly Rate', min_value=0.0)
input_data['Estimated_Earnings'] = st.number_input('Estimated Earnings', min_value=0.0)
input_data['Success_Weighted_Impact'] = st.number_input('Success Weighted impact', min_value=0.0)
input_data['Rehire_Impact'] = st.number_input('Rehire impact', min_value=0.0)
input_data['Client_Rating'] = st.number_input('Client Rating', min_value=0.0, max_value=5.0, step=0.1)
input_data['Job_Duration_Days'] = st.number_input('Job Duration (Days)', min_value=0)
input_data['Project_Type'] = st.selectbox('Project Type', project_type_options)
input_data['Rehire_Rate'] = st.number_input('Rehire Rate (%)', min_value=0.0, max_value=100.0, step=0.1)
input_data['Marketing_Spend'] = st.number_input('Marketing Spend', min_value=0.0)

# Po kliknięciu przycisku
if st.button('📈 Przewiduj'):
    # Tworzymy DataFrame
    input_df = pd.DataFrame([input_data])

    # Predykcja
    prediction = predictor.predict(input_df)

    # Wyświetlamy wynik
    st.success(f"🎉 Przewidywany Job Success Rate: **{prediction.iloc[0]}**")
