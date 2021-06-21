from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

class Defaults:
    user_name = 'user'
    user_password = 'password'
    url_login = 'https://lalalalalalala.com.br'
    download_path = '/caminho_da_pasta_de_download'

options = Options()

#Modifica o diretório de download
prefs = {'download.default_directory': Defaults.download_path}
options.add_experimental_option('prefs', prefs)

#Faz o Chrome iniciar sem abrir janela
options.add_argument("--headless") # Runs Chrome in headless mode.

#Desabilita extensões
options.add_argument("--disable-extensions")

#Passa as options para o driver e diz a pasta do executável
#Será preciso baixar o executável para Windows de acordo com a versão do Chrome que está rodando
# https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome(options=options, executable_path='/usr/local/bin/chromedriver')

#Passa a url para o driver
driver.get(Defaults.url_login)

#Encontrar os campos de usuário e senha e passa as credenciais de acesso
username = driver.find_element_by_id("user-name")
password = driver.find_element_by_id("user-password")
username.send_keys(Defaults.user_name)
password.send_keys(Defaults.user_password)

#Encontra o botão de entrar e clica, espera 15 segundos para carregar a página
#Pode alterar esse tempo se for muito
enter_button = driver.find_element_by_class_name("accessAdvanceButton")
enter_button.click()
time.sleep(15)

#Encontra o botão de clientes parceiros e clica nele
button_parceiros = driver.find_element_by_id("/vip")
button_parceiros.click()
time.sleep(10)

#Encontra o botão para expandir a barra lateral e clica nele
button_parceiros = driver.find_element_by_class_name("subSidebarButton")
button_parceiros.click()
time.sleep(5)

#Encontra o botão de baixar csv e clica nele
button_csv = driver.find_element_by_class_name("csvButton")
button_csv.click()
