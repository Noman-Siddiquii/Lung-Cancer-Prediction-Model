import streamlit as st
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pickle
import pandas as pd
import numpy as np

# Load the model
with open('Model.pkl', 'rb') as file:
    model = pickle.load(file)
st.title('Lungs Cancer Prediction APP')
# Load the data
df = pd.read_csv('Cleaned_data.csv')
df.drop(['Unnamed: 0', 'chronic Lung Disease', 'Fatigue', 'Wheezing', 'Alcohol use','YELLOW_FINGERS'], axis=1, inplace=True)

# UI Inputs
Gender = st.selectbox('Gender', df['Gender'].unique())
Age = st.number_input('Age', min_value=0)
Smoking = st.selectbox('Smoking', df['Smoking'].unique())
Anxiety = st.selectbox('Anxiety', df['Anxiety'].unique())
Peer_pressure = st.selectbox('Peer_Pressure', df['Peer_Pressure'].unique())
ALLERGY = st.selectbox('ALLERGY ', df['ALLERGY '].unique())
COUGHING = st.selectbox('COUGHING', df['COUGHING'].unique())
Shortness_of_Breath = st.selectbox('Shortness of Breath', df['Shortness of Breath'].unique())
Swallowing_Difficulty = st.selectbox('Swallowing Difficulty', df['Swallowing Difficulty'].unique())
CHEST_PAIN = st.selectbox('CHEST PAIN', df['CHEST PAIN'].unique())

if st.button('Predict'):
    # Fit LabelEncoder on the entire column to ensure it handles all labels
    lb = LabelEncoder()
    df_encoded = df.copy()
    for col in df_encoded.select_dtypes(include=['object']).columns:
        df_encoded[col] = lb.fit_transform(df_encoded[col])
    
    # Scale the Age input using StandardScaler
    sd = StandardScaler()
    df_encoded[['Age']] = sd.fit_transform(df_encoded[['Age']])
    
    # Transform inputs
    input_data = {
        'Gender': lb.fit_transform([Gender])[0],
        'Age': sd.transform([[Age]])[0][0],
        'Smoking': lb.fit_transform([Smoking])[0],
        'Anxiety': lb.fit_transform([Anxiety])[0],
        'Peer_pressure': lb.fit_transform([Peer_pressure])[0],
        'ALLERGY': lb.fit_transform([ALLERGY])[0],
        'COUGHING': lb.fit_transform([COUGHING])[0],
        'Shortness_of_Breath': lb.fit_transform([Shortness_of_Breath])[0],
        'Swallowing_Difficulty': lb.fit_transform([Swallowing_Difficulty])[0],
        'CHEST_PAIN': lb.fit_transform([CHEST_PAIN])[0]
    }
    
    input_values = np.array(list(input_data.values())).reshape(1, -1)
    
    # Predict
    prediction = model.predict(input_values)
    
    if prediction == 0:
        st.write('The patient has cancer')
    else:
        st.write('The patient does not have cancer')
