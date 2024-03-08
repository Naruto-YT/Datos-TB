import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel
file_path = "C:/Users/50763/Downloads/BASE DE DATOS PARA PRUEBA.xlsx"
df = pd.read_excel(file_path)

# Agrupar por autor y sumar la cantidad total de comentarios
author_comments_total = df.groupby('Autor')['comments'].sum()

# Seleccionar los 10 autores con más comentarios
top_10_authors = author_comments_total.nlargest(10)

# Filtrar el dataframe para incluir solo los datos de los 10 autores con más comentarios
df_top_authors = df[df['Autor'].isin(top_10_authors.index)]

# Agrupar por autor y sumar la cantidad total de comentarios nuevamente
author_comments_total = df_top_authors.groupby('Autor')['comments'].sum()

# Crear el gráfico lineal
plt.figure(figsize=(10, 6))
plt.plot(author_comments_total, marker='o', linestyle='-')
plt.title('Total de Comentarios por Autor (Top 10 autores)')
plt.xlabel('Autor')
plt.ylabel('Total de Comentarios')
plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para una mejor legibilidad
plt.grid(True)  # Agregar rejilla al gráfico

# Mostrar el gráfico lineal
plt.tight_layout()
plt.show()
