from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import datetime
import pandas as pd

# --- CONFIGURACIÓN HEADLESS CHROME ---
chrome_options = Options()

# --- REEMPLAZAR CON RUTA ABSOLUTA DEL CHROMEDRIVER ---
service = Service("/content/projects/drivers/chromedriver")  # <-- Cambia esta ruta a la ruta absoluta de tu chromedriver

# --- INICIAR NAVEGADOR ---
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 20)

# --- URL DE CONSULTA ---
url = "https://consultaprocesos.ramajudicial.gov.co/Procesos/NombreRazonSocial"
driver.get(url)

# Presionar TAB varias veces (por ejemplo, 17 veces)
for i in range(17):
    driver.switch_to.active_element.send_keys(Keys.TAB)
    time.sleep(1.5)  # Pausa opcional entre TABs

driver.switch_to.active_element.send_keys("N")
time.sleep(0.5)
driver.switch_to.active_element.send_keys(Keys.ENTER)
time.sleep(1.5)
driver.switch_to.active_element.send_keys(Keys.ENTER)
time.sleep(1.5)

# --- INGRESAR NOMBRE ---
wait.until(EC.presence_of_element_located((By.ID, "input-78"))).send_keys("JUAN MAURICIO CUERVO")

# Presionar TAB varias veces (por ejemplo, 6 veces)
for i in range(6):
    driver.switch_to.active_element.send_keys(Keys.TAB)
    time.sleep(1.5)

driver.switch_to.active_element.send_keys(Keys.ENTER)
time.sleep(1.5)
time.sleep(2.5)
time.sleep(3.5)

print("HISTORICO #1")
print("HISTORICO #1.1", driver.save_screenshot("Fecha_Ultima_actuacion.png"))
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div > button.blue--text.v-btn.v-btn--text.theme--light.v-size--default"))).click()
time.sleep(3.5)
time.sleep(3.5)

print("HISTORICO #2")
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "td.text-start"))).screenshot("prueba.png")
time.sleep(3.5)

print("HISTORICO #3")
time.sleep(3.5)

for i in range(1):
    driver.switch_to.active_element.send_keys(Keys.TAB)
    time.sleep(1.5)

print("HISTORICO #4", driver.save_screenshot("Ultima_actuacion.png"))

