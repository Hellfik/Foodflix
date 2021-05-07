import pandas as pd
import streamlit as st

df = pd.read_csv('../Data/final_data/foodflix.csv')


st.beta_container()
col1, col2 = st.beta_columns(2)
col1.subheader('Col1')
col2.subheader('Col2')


st.beta_container()
img = st.beta_columns(1)
st.image('./assets/foodflix.png')
st.title('FoodFlix recommendation System')

with st.beta_expander('Purée'):
    st.write('Juicy deets')

st.text_input('Enter some text')
st.beta_columns(1)
''' _This_ is some __Markdown__ '''