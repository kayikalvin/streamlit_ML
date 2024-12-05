import streamlit as st
import pandas as pd

st.title('🎈 Streamlit_ml')
st.info('This app creates a machine learning model')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
