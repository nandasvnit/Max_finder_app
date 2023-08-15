import streamlit as st
import pandas as pd
import pickle

st.write("""
# Largest Number Finder App

This app finds the largest of 3 numbers
""")
#Get Input

st.header('User Input Numbers')

def user_input_features():
    Num1 = st.number_input("Num1",step=1)
    Num2 = st.number_input("Num2",step=1)
    Num3 = st.number_input("Num3",step=1)

    data = {'Num1': Num1,
            'Num2': Num2,
            'Num3': Num3
            }
    features = pd.Series(data)
    return features

df = user_input_features()


st.subheader('The Largest Number is:')
st.write(df.max())
