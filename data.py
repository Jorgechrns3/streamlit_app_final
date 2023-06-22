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
