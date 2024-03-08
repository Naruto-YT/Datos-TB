import pandas as pd
import plotly.graph_objects as go

# Cargar el archivo Excel
file_path = "C:/Users/50763/Downloads/BASE DE DATOS PARA PRUEBA.xlsx"
df = pd.read_excel(file_path)

# Contar la cantidad de veces que aparece cada país
country_counts = df['País'].value_counts()

# Crear un dataframe para mostrar los países enumerados junto con su conteo
df_country_counts = pd.DataFrame({'País': country_counts.index, 'Cantidad': country_counts.values})

# Ordenar el dataframe por la cantidad de manera descendente
df_country_counts = df_country_counts.sort_values(by='Cantidad', ascending=False)

# Enumerar los países
df_country_counts['Ranking'] = range(1, len(df_country_counts) + 1)

# Crear la tabla interactiva
fig = go.Figure(data=[go.Table(
    header=dict(values=['Ranking', 'País', 'Cantidad']),
    cells=dict(values=[df_country_counts['Ranking'], df_country_counts['País'], df_country_counts['Cantidad']])
)])

# Agregar título a la tabla
fig.update_layout(title='Distribución de Países por Cantidad')

# Mostrar la tabla interactiva
fig.show()

# Guardar la tabla como una imagen
fig.write_image("tabla_paises.png")
