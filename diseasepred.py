# diseasepred.py

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# Load the trained model
dia_model = pickle.load(open("diabetes.sav", "rb"))

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        menu_title='🩺 E-Doctor - Diabetes Predictor',
        options=['Diabetes Prediction'],
        icons=['activity'],
        default_index=0
    )

# Main page logic
if selected == 'Diabetes Prediction':
    st.markdown("<h1 style='color: #2C3E50;'>Diabetes Prediction using ML 🧠</h1>", unsafe_allow_html=True)

    # Input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0)
    with col2:
        Glucose = st.number_input('Glucose Level', min_value=0)
    with col3:
        BloodPressure = st.number_input('Blood Pressure value', min_value=0)
    with col1:
        SkinThickness = st.number_input('Skin Thickness value', min_value=0)
    with col2:
        Insulin = st.number_input('Insulin Level', min_value=0)
    with col3:
        BMI = st.number_input('BMI value', format="%.1f", min_value=0.0)
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', format="%.3f", min_value=0.0)
    with col2:
        Age = st.number_input("Age of the Person", min_value=1)

    diab_diagnosis = ''

    # Prediction button
    if st.button('Get Diabetes Test Result'):
        input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                                Insulin, BMI, DiabetesPedigreeFunction, Age]])
        prediction = dia_model.predict(input_data)

        if prediction[0] == 1:
            diab_diagnosis = '🔴 The person is **diabetic**.'
        else:
            diab_diagnosis = '🟢 The person is **not diabetic**.'

        st.success(diab_diagnosis)

    # Footer note
    st.markdown("<hr><p style='text-align:center;'>Created by Akshada Mane | Machine Learning Web App</p>", unsafe_allow_html=True)
