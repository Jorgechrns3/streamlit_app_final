import streamlit as st
import pandas as pd
import numpy as np

st.title('Casos Positivos Covid')

#df = pd.read_csv('positivos_covid.csv')
#st.line_chart(df)
date=st.date_input('Seleccionar fecha')

