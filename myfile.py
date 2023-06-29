import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
#color de pagina
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/vector-gratis/diseno-fondo-brote-pandemico-coronavirus-azul-covid-19_1017-24425.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
#####
st.markdown(f'<h1 style="color:#fafdfa;font-size:50px;">{"Casos Positivos Covid"}</h1>', unsafe_allow_html=True)
st.markdown(f'<h1 style="color:#fafdfa;font-size:30px;">{"Total de Casos:"}</h1>', unsafe_allow_html=True)

url = 'https://drive.google.com/file/d/18Rkz4SouRbyf9Xs9GUBJ0y9ce_csghfy/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df = pd.read_csv(path, delimiter=';')

# Convertir la columna 'FECHA_RESULTADO' al formato de fecha y hora
df['FECHA_RESULTADO'] = pd.to_datetime(df['FECHA_RESULTADO'], format='%Y%m%d')

# Asignar min_date y max_date desde el DataFrame
min_date = df['FECHA_RESULTADO'].min().date()
max_date = df['FECHA_RESULTADO'].max().date()

# Crear un deslizador para seleccionar la fecha
selected_date = st.slider("Select a date", min_date, max_date)

# Convertir selected_date al formato de fecha y hora
selected_date = datetime.combine(selected_date, datetime.min.time())

# Filtrar el DataFrame basado en la fecha seleccionada y las fechas anteriores a ella
filtered_df = df[df['FECHA_RESULTADO'] <= selected_date]
total = len(filtered_df)

# Formatear el conteo con comas
formatted_count = "{:,}".format(total)

# Mostrar el conteo formateado
count_display = f"<h1 style='text-align: center;'>{formatted_count}</h1>"
st.markdown(count_display, unsafe_allow_html=True)

#Sistema de filtros

#Construccion del set/list de departamentos (Valores unicos sin NA)
set_departamentos = np.sort(df['DEPARTAMENTO'].dropna().unique())
#Seleccion del departamento
opcion_departamento = st.selectbox('Selecciona un departamento', set_departamentos)
df_departamentos = df[df['DEPARTAMENTO'] == opcion_departamento]
num_filas = len(df_departamentos.axes[0]) 

#Construccion del set/list de provincias (Valores unicos sin NA)
set_provincias = np.sort(df_departamentos['PROVINCIA'].dropna().unique())
#Seleccion de la provincia
opcion_provincia = st.selectbox('Selecciona una provincia', set_provincias)
df_provincias = df_departamentos[df_departamentos['PROVINCIA'] == opcion_provincia]
num_filas = len(df_provincias.axes[0]) 

#Construccion del set/list de distritos (Valores unicos sin NA)
set_distritos = np.sort(df_departamentos['DISTRITO'].dropna().unique())
#Seleccion de la distrito
opcion_distrito = st.selectbox('Selecciona un distrito', set_distritos)
df_distritos = df_departamentos[df_departamentos['DISTRITO'] == opcion_distrito]
num_filas = len(df_distritos.axes[0]) 

st.write('Numero de registros:', num_filas)

#Gráficas

#Gráfica de pie de METODODX
df_metododx = df_distritos.METODODX.value_counts()
df_metododx = pd.DataFrame(df_metododx)
df_metododx = df_metododx.reset_index()  
df_metododx.columns = ['METODODX', 'Total']

fig1, ax1 = plt.subplots()
ax1.pie(df_metododx['Total'], labels=df_metododx['METODODX'], autopct='%1.1f%%')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.write('Distribución por METODODX:')
st.pyplot(fig1)

#Gráfica de barras de SEXO
df_SEXO = df_distritos.SEXO.value_counts()
st.write('Distribución por SEXO:')
st.bar_chart(df_SEXO)

#Gráfica de barras de EDAD
df_edad = df_distritos.EDAD.value_counts()
st.write('Distribución por EDAD:')
st.bar_chart(df_edad)


