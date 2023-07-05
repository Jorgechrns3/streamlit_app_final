import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)  # Desactivar advertencia de deprecated
# Título y encabezado
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://api.time.com/wp-content/uploads/2021/02/GettyImages-1212490540.jpg");
        background-attachment: fixed;
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(f'<h1 style="color:#fafdfa;font-size:50px;">{"Casos Positivos Covid"}</h1>', unsafe_allow_html=True)
# Información sobre la fuente de datos y última actualización
# Cargar datos desde el archivo
df = pd.read_csv("positivos_covid-cortado.csv", delimiter=';', encoding='latin-1')
fecha_corte = pd.to_datetime(df['FECHA_CORTE'].max(), format='%Y%m%d')
st.markdown('''
            <div style="background-color: rgba(8, 8, 8, 0.8); padding: 10px;border-radius: 10px;">
                <strong>Casos positivos por COVID-19 - [Ministerio de Salud - MINSA]</strong>
                <ul>
                    <li>Fuente: Instituto Nacional de Salud y Centro Nacional de Epidemiologia, prevención y Control de Enfermedades – MINSA.</li>
                    <li>Última Actualización: {}</li>
                </ul>
            </div>
            '''.format(fecha_corte.strftime("%d/%m/%Y").replace(" 00:00:00", "")), unsafe_allow_html=True)

st.header("Total de Casos:")
# Convertir la columna 'FECHA_RESULTADO' al formato de fecha y hora
df['FECHA_RESULTADO'] = pd.to_datetime(df['FECHA_RESULTADO'], format='%Y%m%d')
# Obtener lista de departamentos
departamentos = df['DEPARTAMENTO'].unique()
# Barra lateral para la selección de parámetros
st.sidebar.title("Parámetros")
date_range = st.sidebar.selectbox("Rango de fechas", ("Última semana", "Último mes", "Último año", "Todo el tiempo"))
show_all_locations = st.sidebar.checkbox("Mostrar todos los lugares")
selected_departamento = st.sidebar.selectbox("Departamento", departamentos)
# Filtrar el DataFrame en base a los parámetros seleccionados
filtered_df = df.copy()
# Filtrar por rango de fechas
if date_range == "Última semana":
    filtered_df = filtered_df[filtered_df['FECHA_RESULTADO'] >= pd.to_datetime('today') - pd.DateOffset(weeks=1)]
elif date_range == "Último mes":
    filtered_df = filtered_df[filtered_df['FECHA_RESULTADO'] >= pd.to_datetime('today') - pd.DateOffset(months=1)]
elif date_range == "Último año":
    filtered_df = filtered_df[filtered_df['FECHA_RESULTADO'] >= pd.to_datetime('today') - pd.DateOffset(years=1)]
# Filtrar por ubicación
if not show_all_locations:
    if selected_departamento != "":
        filtered_df = filtered_df[filtered_df['DEPARTAMENTO'] == selected_departamento]
        provincias = filtered_df['PROVINCIA'].unique()
        selected_provincia = st.sidebar.selectbox("Provincia", provincias)

        if selected_provincia != "":
            filtered_df = filtered_df[filtered_df['PROVINCIA'] == selected_provincia]
            distritos = filtered_df['DISTRITO'].unique()
            selected_distrito = st.sidebar.selectbox("Distrito", distritos)

            if selected_distrito != "":
                filtered_df = filtered_df[filtered_df['DISTRITO'] == selected_distrito]
# Obtener el total de casos
total_cases = len(filtered_df)
contador = "{:,}".format(total_cases)
# Mostrar el total de casos
st.markdown(f"<h1 style='text-align: center;'>{contador}</h1>", unsafe_allow_html=True)
#
st.markdown("# ")
# Gráfico de línea de casos en el tiempo
st.header('Gráfico de casos en el tiempo:')
# Contar los casos por fecha
cases_by_date = filtered_df['FECHA_RESULTADO'].value_counts().sort_index()
# Generar el gráfico de línea
plt.figure(figsize=(10, 6))
sns.lineplot(data=cases_by_date)
plt.xlabel('Fecha')
plt.ylabel('Casos')
plt.title('Casos de COVID-19 por fecha')
plt.xticks(rotation=45)
st.pyplot()
#
st.markdown("# ")
# Gráfico circular de métodos de laboratorio
st.header('Gráfico circular de métodos de laboratorio:')
# Contar los métodos de laboratorio y generar el gráfico circular
lab_methods = filtered_df['METODODX'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(lab_methods, labels=lab_methods.index, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Métodos de laboratorio')
st.pyplot()
#
st.markdown("# ")
# Estadísticas sobre los datos filtrados
st.header("Otras estadísticas:")
# Calcular las estadísticas
promedio_edad = np.mean(filtered_df["EDAD"])
porcentaje_mujeres = np.mean(filtered_df["SEXO"] == "F") * 100
# Crear la figura para el gráfico de edad (histograma)
fig1, ax1 = plt.subplots(figsize=(8, 6))
ax1.hist(filtered_df["EDAD"], bins=20, edgecolor='black', color='steelblue')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.title('Distribución de Edades')
if isinstance(promedio_edad,int):
    plt.figtext(0.1,0,"Edad promedio: "+str(round(promedio_edad))+" años")
st.pyplot(fig1)
#
st.markdown("# ")
# Crear la figura para el gráfico de género (gráfico circular)
fig2, ax2 = plt.subplots(figsize=(6, 4))
if isinstance(porcentaje_mujeres,int):
    ax2.pie([porcentaje_mujeres, 100-porcentaje_mujeres], labels=['Mujeres', 'Hombres'], autopct='%1.1f%%', startangle=180)
plt.axis('equal')
plt.title('Distribución de Género')
st.pyplot(fig2)
# Espacios
st.markdown("# ")
st.markdown("# ")
st.markdown("# ")
st.markdown("# ")
st.markdown("# ")
st.markdown("# ")
# Miembros del equipo
st.markdown("### Equipo de trabajo:")
st.markdown("- Chirinos Paredes, Jorge")
st.markdown("- Pacsi Inga, Saransh")
st.markdown("- Pacheco Jeri, Sharon Gless")
st.markdown("- Manyahuillca, Borda Zully")