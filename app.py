from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
import datetime
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # si necesitas modo headless
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu') # Add this line to disable GPU
chrome_options.add_argument('--user-data-dir=/tmp/user-data') # Add this line to use a temporary user data directory
chrome_options.add_argument('--data-path=/tmp/data-path') # Add this line to use a temporary data path
chrome_options.add_argument('--homedir=/tmp') # Add this line to use a temporary homedir

#Usar Service correctamente
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


# URL de la página
url = "https://consultaprocesos.ramajudicial.gov.co/Procesos/NombreRazonSocial"

# Ir a la página
driver.get(url)

# Esperar a que el campo de nombre esté presente
wait = WebDriverWait(driver, 30)

# --- Generar nombre con fecha y hora actual ---
fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")

# --- Ruta final del archivo ---
screenshot = "screenshot"  # Define the directory for screenshots
os.makedirs(screenshot, exist_ok=True)  # Create directory if it doesn't exist

#wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.v-input--selection-controls__ripple.primary--text"))).click()
print("ULTIMOS 30 DIAS")
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.container.pa-0.ma-0.container--fluid > div > div.row.align-center.justify-center"))).click()
driver.save_screenshot(f"screenshot/Fecha_Ultima_actuacion_{fecha_hora}.png")
wait.until(EC.presence_of_element_located((By.XPATH, "//main[@id='mainContent']/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/input"))).click()
driver.save_screenshot("debug2.png")
wait.until(EC.presence_of_element_located((By.XPATH, "//main[@id='mainContent']/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/input"))).send_keys("N")
wait.until(EC.presence_of_element_located((By.XPATH, "//main[@id='mainContent']/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/input"))).send_keys(Keys.ENTER)
driver.save_screenshot("debug3.png")
time.sleep(1.5)
# --- INGRESAR NOMBRE ---
wait.until(EC.presence_of_element_located((By.XPATH, "//main[@id='mainContent']/div/div/div/div/div/div[2]/div/div[3]/div/div/div/input"))).click()
wait.until(EC.presence_of_element_located((By.XPATH, "//main[@id='mainContent']/div/div/div/div/div/div[2]/div/div[3]/div/div/div/input"))).clear()
wait.until(EC.presence_of_element_located((By.XPATH, "//main[@id='mainContent']/div/div/div/div/div/div[2]/div/div[3]/div/div/div/input"))).send_keys("JUAN MAURICIO CUERVO")
for i in range(2):
    driver.switch_to.active_element.send_keys(Keys.TAB)
    time.sleep(1.5)  # Pausa opcional entre TABs
driver.save_screenshot("debug4.png")

# Presionar TAB varias veces (por ejemplo, 5 veces)
for i in range(2):
    driver.switch_to.active_element.send_keys(Keys.TAB)
    time.sleep(1.5)  # Pausa opcional entre TABs


wait.until(EC.presence_of_element_located((By.XPATH, "//main[@id='mainContent']/div/div/div/div/div/div[2]/div/div[5]/button/span"))).click()
driver.save_screenshot("debug5.png")
time.sleep(1.5)
time.sleep(2.5)
time.sleep(3.5)
print("HISTORICO #1")
print("HISTORICO #1.1",driver.save_screenshot("screenshot/Fecha_Ultima_actuacion.png"))
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div > button.blue--text.v-btn.v-btn--text.theme--light.v-size--default"))).click()
time.sleep(3.5)
time.sleep(3.5)
print("HISTORICO #2")
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "td.text-start"))).screenshot("prueba.png")
time.sleep(3.5)
print("HISTORICO #3")
time.sleep(3.5)
# Presionar TAB varias veces (por ejemplo, 5 veces)
for i in range(1):
    driver.switch_to.active_element.send_keys(Keys.TAB)
    time.sleep(1.5)  # Pausa opcional entre TABs


print("HISTORICO #4",driver.save_screenshot("Ultima_actuacion.png"))
