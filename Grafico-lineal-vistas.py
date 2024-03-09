import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel
file_path = "C:/Users/50763/Downloads/BASE DE DATOS PARA PRUEBA.xlsx"
df = pd.read_excel(file_path)

# Agrupar por autor y sumar la cantidad total de vistas
author_views_total = df.groupby('Autor')['views'].sum()

# Seleccionar los 10 autores con más vistas
top_10_authors = author_views_total.nlargest(10)

# Filtrar el dataframe para incluir solo los datos de los 10 autores con más vistas
df_top_authors = df[df['Autor'].isin(top_10_authors.index)]

# Agrupar por autor y sumar la cantidad total de vistas nuevamente
author_views_total = df_top_authors.groupby('Autor')['views'].sum()

# Crear el gráfico lineal
plt.figure(figsize=(10, 6))
plt.plot(author_views_total, marker='o', linestyle='-')
plt.title('Total de Vistas por Autor (Top 10 autores)')
plt.xlabel('Autor')
plt.ylabel('Total de Vistas')
plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para una mejor legibilidad
plt.grid(True)  # Agregar rejilla al gráfico

# Mostrar el gráfico lineal
plt.tight_layout()
plt.show()
