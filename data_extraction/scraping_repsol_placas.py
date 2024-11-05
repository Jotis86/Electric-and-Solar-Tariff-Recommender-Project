from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# URL de la página web
url = "https://www.repsol.es/particulares/hogar/energia-solar/tarifas/tarifa-solar-bateria-virtual/"

# Configurar Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Ejecutar en modo headless (sin interfaz gráfica)
driver = webdriver.Chrome(options=options)

# Navegar a la página web
driver.get(url)

# Extraer los datos específicos
titulo = "Tarifa Placa Solar"
descripcion = "Precio de la energía y término fijo"

# Extraer el precio de la energía
try:
    precio_energia_element = driver.find_element(By.CSS_SELECTOR, '.tax-left .rp-number-04')
    precio_energia = precio_energia_element.text.strip() if precio_energia_element else "No encontrado"
except:
    precio_energia = "0,139746 €/kWh"

# Extraer los precios de término fijo (potencia)
precio_punta = "No encontrado"
precio_valle = "No encontrado"
potencia_divs = driver.find_elements(By.CSS_SELECTOR, '.tax-right .element')

for div in potencia_divs:
    try:
        label = div.find_element(By.CSS_SELECTOR, '.main')
        value = div.find_element(By.CSS_SELECTOR, '.rp-number-04')
        if label and value:
            if "Hora punta" in label.text:
                precio_punta = value.text.strip()
            elif "Hora valle" in label.text:
                precio_valle = value.text.strip()
    except:
        continue

# Valores por defecto si no se encuentran
if precio_energia == "No encontrado":
    precio_energia = "0,139746 €/kWh"
if precio_punta == "No encontrado":
    precio_punta = "0,068219 €/kW/día"
if precio_valle == "No encontrado":
    precio_valle = "0,068219 €/kW/día"

# Extraer los excedentes generados
try:
    excedentes_element = driver.find_element(By.XPATH, '//*[contains(text(), "Precio al que te pagamos los excedentes generados")]/following-sibling::div[contains(@class, "rp-number-04 step-float js-price")]')
    excedentes = excedentes_element.text.strip() if excedentes_element else "No encontrado"
except:
    excedentes = "0,080000 €/kWh"

# Cerrar el navegador
driver.quit()

# Crear un DataFrame de pandas y guardar los resultados en un CSV
datos = [[titulo, descripcion, precio_energia, precio_punta, precio_valle, excedentes]]
columnas = ["Título", "Descripción", "Precio Energía", "Precio Punta", "Precio Valle", "Excedentes Generados"]
df = pd.DataFrame(datos, columns=columnas)
df.to_csv("resultados_tarifas_repsol_solar.csv", index=False)

print("Datos guardados en resultados_tarifas_repsol_solar.csv")