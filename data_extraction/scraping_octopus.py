import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página web
url = "https://octopusenergy.es/precios"

# Realizar la solicitud HTTP
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar las tarjetas de tarifas
tarjetas = soup.find_all('div', {'data-testid': 'tariff-card'})

# Extraer los datos de cada tarjeta
datos = []
for tarjeta in tarjetas:
    titulo = tarjeta.find('h3').text.strip() if tarjeta.find('h3') else "No encontrado"
    descripcion = tarjeta.find('p', class_='sc-192m2ep-0 jZCOHh').text.strip() if tarjeta.find('p', class_='sc-192m2ep-0 jZCOHh') else "No encontrado"
    
    # Extraer los precios de energía consumida
    energia_punta = "No encontrado"
    energia_llano = "No encontrado"
    energia_valle = "No encontrado"
    energia_labels = tarjeta.find_all('p', class_='sc-192m2ep-0 jZCOHh')
    energia_values = tarjeta.find_all('h5', class_='sc-192m2ep-0 bUWhfa')
    
    for label, value in zip(energia_labels, energia_values):
        if "Punta" in label.text and "€/kWh" in value.text:
            energia_punta = value.text.strip()
        elif "Llano" in label.text and "€/kWh" in value.text:
            energia_llano = value.text.strip()
        elif "Valle" in label.text and "€/kWh" in value.text:
            energia_valle = value.text.strip()
    
    # Extraer los precios de potencia
    potencia_punta = "No encontrado"
    potencia_valle = "No encontrado"
    potencia_divs = tarjeta.find_all('div', class_='sc-56k6h2-0 leiIyU')
    
    for div in potencia_divs:
        label = div.find('p', class_='sc-192m2ep-0 jZCOHh')
        value = div.find('h5', class_='sc-192m2ep-0 bUWhfa')
        if label and value:
            if "Punta" in label.text:
                potencia_punta = value.text.strip()
            elif "Valle" in label.text:
                potencia_valle = value.text.strip()
    
    datos.append([titulo, descripcion, energia_punta, energia_llano, energia_valle, potencia_punta, potencia_valle])

# Crear un DataFrame de pandas y guardar los resultados en un CSV
columnas = ["Título", "Descripción", "Energía Punta", "Energía Llano", "Energía Valle", "Potencia Punta", "Potencia Valle"]
df = pd.DataFrame(datos, columns=columnas)
df.to_csv("resultados_tarifas_octopus.csv", index=False)

print("Datos guardados en resultados_tarifas_octopus.csv")