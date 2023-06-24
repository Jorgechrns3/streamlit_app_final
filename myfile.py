import streamlit as st
import pandas as pd
import numpy as np

st.title('Casos Positivos Covid')
st.header('Total de Casos:')

data = pd.read_csv('positivos_covid.csv')
total=len(data)
st.dataframe(total)
#date=st.date_input('Seleccionar fecha')
