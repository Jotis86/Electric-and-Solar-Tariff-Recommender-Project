import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página web
url = "https://www.naturgy.es/hogar/luz"

# Realizar la solicitud HTTP
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar las filas de la tabla
filas = soup.select('.scroll-tabla .tabla-comp .fila-c')

# Extraer los datos de la tabla
columnas = ["Por uso de Luz", "Plana Luz", "Noche Luz"]
datos = {columna: [] for columna in columnas}

for fila in filas:
    celdas = fila.find_all('p')
    for i, celda in enumerate(celdas):
        if i == 0:
            continue  # Saltar la primera celda que es el título de la fila
        datos[columnas[i-1]].append(celda.text.strip())

# Asegurarse de que todas las listas en el diccionario tengan la misma longitud
max_length = max(len(lista) for lista in datos.values())
for lista in datos.values():
    while len(lista) < max_length:
        lista.append("No encontrado")

# Crear un DataFrame de pandas y guardar los resultados en un CSV
df = pd.DataFrame(datos)
df.to_csv("resultados_tarifas_naturgy.csv", index=False)

print("Datos guardados en resultados_tarifas_naturgy.csv")