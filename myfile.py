import streamlit as st
import pandas as pd
from datetime import datetime

st.title('Casos Positivos Covid')
st.header('Total de Casos:')

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


