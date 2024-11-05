from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# URL de la página web
url = "https://www.repsol.es/particulares/hogar/luz-y-gas/tarifas/tarifa-ahorro-plus/"

# Configurar Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Ejecutar en modo headless (sin interfaz gráfica)
driver = webdriver.Chrome(options=options)

# Navegar a la página web
driver.get(url)

# Extraer los datos específicos
titulo = "Tarifa Ahorro Plus"
descripcion = "Precio de la energía y término fijo"

# Extraer el precio de la energía
precio_energia_element = driver.find_element(By.CSS_SELECTOR, '.tax-left .rp-number-04')
precio_energia = precio_energia_element.text.strip() if precio_energia_element else "No encontrado"

# Extraer los precios de término fijo (potencia)
precio_punta = "No encontrado"
precio_valle = "No encontrado"
potencia_divs = driver.find_elements(By.CSS_SELECTOR, '.tax-right .element')

for div in potencia_divs:
    label = div.find_element(By.CSS_SELECTOR, '.main')
    value = div.find_element(By.CSS_SELECTOR, '.rp-number-04')
    if label and value:
        if "Hora punta" in label.text:
            precio_punta = value.text.strip()
        elif "Hora valle" in label.text:
            precio_valle = value.text.strip()

# Cerrar el navegador
driver.quit()

# Crear un DataFrame de pandas y guardar los resultados en un CSV
datos = [[titulo, descripcion, precio_energia, precio_punta, precio_valle]]
columnas = ["Título", "Descripción", "Precio Energía", "Precio Punta", "Precio Valle"]
df = pd.DataFrame(datos, columns=columnas)
df.to_csv("resultados_tarifas_repsol_2.csv", index=False)

print("Datos guardados en resultados_tarifas_repsol_2.csv")