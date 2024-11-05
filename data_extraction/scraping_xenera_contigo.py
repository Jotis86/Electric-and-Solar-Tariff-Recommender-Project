from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Paso 1: Configurar Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Ejecutar en modo headless (sin interfaz gráfica)
driver = webdriver.Chrome(options=options)

# Paso 2: Obtener el contenido de la página web
url = "https://xenera.com/esp/tarifas/luz/contigo"
driver.get(url)

# Esperar a que el contenido dinámico se cargue
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.grid.grid-cols-2.gap-x-10.xl\\:pb-10"))
)

# Obtener el HTML de la página
html = driver.page_source
driver.quit()

# Paso 3: Analizar el HTML
soup = BeautifulSoup(html, 'html.parser')

# Paso 4: Extraer la información específica
# Buscar los elementos de energía basados en el texto contenido
energia_elements = soup.select("div.flex.flex-col.sm\\:flex-row.items-center.justify-center.sm\\:justify-between.sm\\:h-1\\/4.md\\:h-2\\/5.border-2.border-primary-light.rounded-t-xl.overflow-hidden ul li")
potencia_element = soup.select_one("div.flex.flex-col.sm\\:flex-row.items-center.justify-center.sm\\:justify-between.sm\\:h-1\\/4.md\\:h-2\\/5.border-t.border-t-gray-100.border-2.border-primary-light ul li")
coste_gestion_element = soup.select_one("div.flex.flex-col.sm\\:flex-row.items-center.justify-center.sm\\:justify-between.sm\\:h-1\\/6.xl\\:h-1\\/5.border-t.border-t-gray-100.border-2.border-primary-light p.font-bold")

# Verificar que los elementos existen antes de acceder a su texto
energia_valle = energia_elements[0].text.strip() if len(energia_elements) > 0 else "No encontrado"
energia_llano = energia_elements[1].text.strip() if len(energia_elements) > 1 else "No encontrado"
energia_punta = energia_elements[2].text.strip() if len(energia_elements) > 2 else "No encontrado"
potencia = potencia_element.text.strip() if potencia_element else "No encontrado"
coste_gestion = coste_gestion_element.text.strip() if coste_gestion_element else "No encontrado"

# Paso 5: Crear un DataFrame de pandas y guardar los resultados en un CSV
data = {
    "Energía Valle": [energia_valle],
    "Energía Llano": [energia_llano],
    "Energía Punta": [energia_punta],
    "Potencia": [potencia],
    "Coste de gestión": [coste_gestion]
}

df = pd.DataFrame(data)
df.to_csv("resultados_tarifas_xenera_contigo.csv", index=False)

print("Datos guardados en resultados_tarifas_xenera_contigo.csv")