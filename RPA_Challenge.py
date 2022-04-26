from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import json


options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('--start-maximized')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-gpu')
options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-notifications')
driver = webdriver.Chrome(options=options, executable_path=r'C:\chromedriver.exe')
actions = ActionChains(driver)
options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")

url = "https://www.rpachallenge.com/?lang=EN"


def acesso():
    driver.get(url)
    driver.maximize_window()


acesso()
# converta csv para json
with open('caminho do json', 'r', encoding='utf-8') as file:
    data = json.load(file)


class enviar_dados():
    def iniciar(self):
        self.acessar_variaveis()
        self.inserir_variaveis()
        self.acessar_proxima_pagina()

    def acessar_variaveis(self):
        self.primeiro_nome = data[linha]['First Name']
        self.ultimo_nome = data[linha]['Last Name ']
        self.nome_companhia = data[linha]['Company Name']
        self.seguimento_companhia = data[linha]['Role in Company']
        self.endereco = data[linha]['Address']
        self.email = data[linha]['Email']
        self.numero_telefone = data[linha]['Phone Number']

    def inserir_variaveis(self):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@ng-reflect-dictionary-value="Role in Company"]/div/input'))).send_keys(self.seguimento_companhia)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@ng-reflect-dictionary-value="Email"]/div/input'))).send_keys(self.email)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@ng-reflect-dictionary-value="First Name"]/div/input'))).send_keys(self.primeiro_nome)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@ng-reflect-dictionary-value="Company Name"]/div/input'))).send_keys(self.nome_companhia)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@ng-reflect-dictionary-value="Phone Number"]/div/input'))).send_keys(self.numero_telefone)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@ng-reflect-dictionary-value="Address"]/div/input'))).send_keys(self.endereco)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@ng-reflect-dictionary-value="Last Name"]/div/input'))).send_keys(self.ultimo_nome)

    def acessar_proxima_pagina(self):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@value="Submit"]'))).click()


time.sleep(3)


def comecar_desafio():
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Start"]'))).click()


comecar_desafio()
start = enviar_dados()
for linha in range(0, len(data)):
    start.iniciar()
