import numpy as np
import pickle
import pandas as pd

import streamlit as st 
pickle_in = open(r"C:\Users\SVI\Desktop\ML_learn\multiple_linear_reg\project\students\reg.pkl","rb")
reg=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_note_authentication(hs,ps,ea,sh,sqp):   
    prediction=reg.predict([[hs,ps,ea,sh,sqp]])
    print(np.round(prediction,2))
    return np.round(prediction,2)



def main():
    st.title("Performance Index")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Performance App</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    hs = st.number_input("Hours Studied")
    ps = st.number_input("Previous Scores")
    ea = st.number_input("Extracurricular Activities")
    sh = st.number_input("Sleep Hours")
    sqp = st.number_input("Sample Question Papers Practiced")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(hs,ps,ea,sh,sqp)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()