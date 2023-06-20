import streamlit as st
import pandas as pd
import numpy as np

st.title('Casos Positivos Covid')
st.write('Aquí revisaremos los casos positivos de covid en Perú a lo largo del tiempo. Trabajo Final Prueba')

#df = pd.read_csv('positivos_covid.csv')
#st.line_chart(df)
date=st.date_input('Seleccionar fecha')

