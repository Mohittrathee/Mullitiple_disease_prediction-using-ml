# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 13:11:38 2025

@author: mohit rathee
"""
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

with open("D:/workspace/MachIne Learning/multiple_disease_prediction webapp/Diabetes_prediction_raw (1).sav", 'rb') as file:
    diabetes_model = pickle.load(file)

with open("D:/workspace/MachIne Learning/multiple_disease_prediction webapp/heart_disease_raw.sav", 'rb') as file:
    heart_disease_model = pickle.load(file)


with open("D:/workspace/MachIne Learning/multiple_disease_prediction webapp/parkinsons_data_raw.sav", 'rb') as file:
    parkinson_model = pickle.load(file)


with st.sidebar:
    selected=option_menu('Multiple disease prediction System',
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinson Disease Prediction'],
                         
                         icons = ['bag-heart-fill','heart','person'],
                         
                         default_index=0)
    
    
if (selected=='Diabetes Prediction'):
    st.title='Diabetes Prediction Model'
    
    col_1, col_2, col_3=st.columns(3)
    
    with col_1:
        Pregnancy= st.text_input("Number of pregnacies")
    
    with col_2:
        Glucose=st.text_input("Level of Glucose")
    
    with col_3:
        Blood_pressure=st.text_input("Level of Bp")
    
    with col_1:
        Skin_thickness=st.text_input("What is your skin thickness")
    
    with col_2:
        Insulin=st.text_input("Level of Insulin")
    
    with col_3:
        BMI=st.text_input("What is your BMI")
    
    with col_1:
        Diabetes_pedigree_function=st.text_input("Your diabetes pedigree function")
    
    with col_2:
        Age=st.text_input("What is your age")
    
    Diabetes_diagnosis=''
    
    if st.button('Test Results'):
        diabete_prediction=diabetes_model.predict([[Pregnancy,Glucose,Blood_pressure,Skin_thickness,Insulin,BMI,Diabetes_pedigree_function,Age]])
        
        if (diabete_prediction[0]==1):
            Diabetes_diagnosis="The person is not Diabetic"
        else:
            Diabetes_diagnosis="The person is a Diabetic"
    st.success(Diabetes_diagnosis)
    

    
    

if (selected=='Heart Disease Prediction'):
    st.title='Heart Disease Prediction Model'
    
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        age=st.text_input('Age')
        
    with col2:
        sex=st.text_input('Your Sex')
        
    with col3:
        cp=st.text_input('Chest Pain Type')
        
    with col1:
        trestbps=st.text_input('Resting BP')
        
    with col2:
        chol=st.text_input('Serum Cholestrol in mg/dL')
        
    with col3:
        fbs=st.text_input('Fasting Blood Sugar >120 mg/dL')
        
    with col1:
        restecg=st.text_input('Resting Electrocardiographic Results')
        
    with col2:
        thalach=st.text_input('Maximum heart rate achieved')
    
    with col3:
        exang=st.text_input('Exercise induced angina')
        
    with col1:
        oldpeak=st.text_input(' ST depression induced by exercise relative to rest')
        
    with col2:
        slope=st.text_input('The slope of the peak exercise ST segment')
        
    with col3:
        ca=st.text_input('Number of major vessels (0-3) colored by flourosopy')
        
    with col1:
        thal=st.text_input(' 0 = normal; 1 = fixed defect; 2 = reversable defect')
        

    Heart_disease_diagnosis=''
     
    if st.button('Test Results'):
         Heart_disease_prediction=heart_disease_model.predict([[age,sex.cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
         if (Heart_disease_prediction[0]==1):
             Heart_disease_diagnosis="The person has heart disease"
         else:
             Heart_disease_diagnosis="The person has no heart disease"
             
         st.success(Heart_disease_diagnosis)
            
             
             
if (selected=='Parkinson Disease Prediction'):
    st.title='Parkinson Disease Prediction Model'
   
    
    col1,col2,col3=st.columns(3)
    with col1:
        name=st.text_input('ASCII SUBJECT NAME AND RECORDING NUMBER')
        
    with col2:
        fo=st.text_input('MDVP:Fo(Hz)')
        
    with col3:
        fhi=st.text_input('MDVP:Fhi(Hz)')
        
    with col1:
        flo=st.text_input('MDVP:Flo(Hz)')
        
    with col2:
        Jitter_percent=st.text_input('MDVP:Jitter(%')
        
    with col3:
        Jitter_abs=st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP=st.text_input('MDVP:RAP')
        
    with col2:
        PPQ=st.text_input('MDVP:PPQ')
        
    with col3:
        DDP=st.text_input('Jitter:DDP')
        
    with col1:
        Shimmer=st.text_input('MDVP:Shimmer')
        
    with col2:
        Shimmer_dB=st.text_input('MDVP:Shimmer(dB)')
        
    with col3:
        Shimmer_APQ3=st.text_input('Shimmer:APQ3')
        
    with col1:
        Shimmer_APQ5=st.text_input('Shimmer:APQ5')
        
    with col2:
        MDV_APQ=st.text_input('MDV:APQ')
        
    with col3:
        Shimmer_DDA=st.text_input('Shimmer_DDA')
        
    with col1:
        NHR=st.text_input('NHR')
        
    with col2:
        HNR=st.text_input('HNR')
    
    with col3:
        RPDE=st.text_input('RPDE')
        
    with col1:
        DFA=st.text_input('DFA')
        
    with col2:
        spread1=st.text_input('Spread 1 ')
        
    with col3:
        spread2=st.text_input('Spread 2 ')
        
    with col1:
        D2=st.text_input('D2')
        
    with col2:
        PPE=st.text_input('PPE ')
        
        
    Parkinson_disease_diagnosis=''
      
    if st.button('Parkinson Test Result'):
        # ✅ Define the variable before using it
        Parkinson = parkinson_model.predict([[fo, fhi, flo, Jitter_percent,Jitter_abs,
                                              RAP, PPQ, DDP, Shimmer, Shimmer_dB,
                                              Shimmer_APQ3, Shimmer_APQ5, MDV_APQ, Shimmer_DDA, NHR, HNR,
                                              RPDE, DFA, spread1, spread2, D2, PPE]])

        if (Parkinson[0] == 1):
            Parkinson_disease_diagnosis = "The person has Parkinson's Disease"
        else:
            Parkinson_disease_diagnosis = "The person does not have Parkinson's Disease"

        st.success(Parkinson_disease_diagnosis)
    