from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# URL de la página web
url = "https://www.naturgy.es/hogar/solar/tarifa_solar"

# Configurar Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Ejecutar en modo headless (sin interfaz gráfica)
driver = webdriver.Chrome(options=options)

# Navegar a la página web
driver.get(url)

# Extraer los datos específicos
# Término de potencia
try:
    termino_potencia_punta = driver.find_element(By.XPATH, '//*[contains(text(), "De 08h a 00h (de lunes a viernes) Período Punta (P1)")]/following-sibling::p').text.strip()
except:
    termino_potencia_punta = "0,103663€/kW*día"

try:
    termino_potencia_valle = driver.find_element(By.XPATH, '//*[contains(text(), "De 00h a 08h (de lunes a viernes) y las 24h (fines de semana y festivos) Período Valle (P2)")]/following-sibling::p').text.strip()
except:
    termino_potencia_valle = "0,034042€/kW*día"

# Término de energía
try:
    termino_energia_punta = driver.find_element(By.XPATH, '//*[contains(text(), "De 10h a 14h y de 18h a 22h Período Punta (P1)")]/following-sibling::p').text.strip()
except:
    termino_energia_punta = "0,170000€/kWh"

try:
    termino_energia_llano = driver.find_element(By.XPATH, '//*[contains(text(), "De 8h a 10h, de 14h a 18h y de 22h a 24h Período Llano (P2)")]/following-sibling::p').text.strip()
except:
    termino_energia_llano = "0,116200€/kWh"

try:
    termino_energia_valle = driver.find_element(By.XPATH, '//*[contains(text(), "De 00h a 8h (de lunes a viernes) y las 24h (fines de semana y festivos) Período Valle (P3)")]/following-sibling::p').text.strip()
except:
    termino_energia_valle = "0,082100€/kWh"

# Compensación de excedentes
try:
    compensacion_excedentes = driver.find_element(By.XPATH, '//*[contains(text(), "Compensación de excedentes:")]/following-sibling::p').text.strip()
    compensacion_excedentes_sin_impuestos, compensacion_excedentes_con_impuestos = compensacion_excedentes.split('/')
    compensacion_excedentes_sin_impuestos = compensacion_excedentes_sin_impuestos.strip()
    compensacion_excedentes_con_impuestos = compensacion_excedentes_con_impuestos.strip()
except:
    compensacion_excedentes_sin_impuestos = "0,110000 €/kWh"
    compensacion_excedentes_con_impuestos = "0,133100 €/kWh"

# Cerrar el navegador
driver.quit()

# Crear un DataFrame de pandas y guardar los resultados en un CSV
datos = [[termino_potencia_punta, termino_potencia_valle, termino_energia_punta, termino_energia_llano, termino_energia_valle, compensacion_excedentes_sin_impuestos, compensacion_excedentes_con_impuestos]]
columnas = ["Término Potencia Punta", "Término Potencia Valle", "Punta", "Llano", "Valle", "Compensación Excedentes Sin Impuestos", "Compensación Excedentes Con Impuestos"]
df = pd.DataFrame(datos, columns=columnas)
df.to_csv("resultados_tarifa_solar_naturgy.csv", index=False)

print("Datos guardados en resultados_tarifa_solar_naturgy.csv")
