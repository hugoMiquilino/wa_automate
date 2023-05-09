import urllib
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

contatos_df = pd.read_excel('Enviar.xlsx')

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 60)  # espera até 60 segundos
side_panel = wait.until(EC.presence_of_element_located((By.ID, "side")))

# já estamos com o login feito no whatsapp web
for i, mensagem in enumerate(contatos_df['Nome']):
    pessoa = contatos_df.loc[i, "Nome"]
    numero = contatos_df.loc[i, "Numero"]
    texto = urllib.parse.quote(f"Oi {pessoa}! Compra comigo! s2s2")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    driver.get(link)
    side_panel
    driver.find_element(
        By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)
