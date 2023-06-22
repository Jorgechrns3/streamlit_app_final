import streamlit as st
import pandas as pd
import numpy as np

st.title('Casos Positivos Covid')
st.write('Aquí revisaremos los casos positivos de covid en Perú a lo largo del tiempo. Trabajo Final Prueba')

#df = pd.read_csv('positivos_covid.csv')
#st.line_chart(df)
date=st.date_input('Seleccionar fecha')

import streamlit as st
import pandas as pd
import gdown

#id = 1op-iq0XhBXBQOPlagCPE9TzFsFkkNVjQ
@st.experimental_memo
def download_data():
  #https://drive.google.com/uc?id=
  url = "https://drive.google.com/uc?id=1op-iq0XhBXBQOPlagCPE9TzFsFkkNVjQ"
  output= "data.csv"
  gdown.download(url,output,quiet = False)
  
download_data()
data = pd.read_csv("data.csv", sep = ";", parse_dates = ["FECHA_CORTE","FECHA_RESULTADO"])
Simplificado = data.drop(columns = ["DISTRITO","FECHA_CORTE","FECHA_RESULTADO","UBIGEO","id_persona"])
